#!/usr/bin/env python3
"""Phase 1 route-panel selection — the frozen formula (pre-registration §1).

This script IS the panel definition: it is committed before the input data
(docs/phase1-preregistration.md §14 freeze ordering), the owner then commits
the SHA-256 of the 2024 T-100 Domestic Segment file to data/phase1-inputs.md,
and the route list is the script's output on that file. G1 test GD re-executes
this script on the hashed input and must reproduce the identical panel.

Input CSV columns (TranStats T-100 Domestic Segment, CY2024, scheduled):
    ORIGIN, DEST, UNIQUE_CARRIER, PASSENGERS, DISTANCE

Run:
    python3 pipeline/select_routes.py T100_2024.csv --out panel.json

Deterministic by construction: no randomness, no dates, fixed tie-breaks.
Zero discretion: every constraint decision is written to the audit log.
"""

import argparse
import csv
import hashlib
import json
import sys
from collections import defaultdict
from pathlib import Path

# --- Frozen parameters (pre-registration §1; MAY NOT change after sign-off) --
N_ROUTES = 18
PER_BAND = 6
BANDS = (("SHORT", 0.0, 750.0), ("MEDIUM", 750.0, 1500.0), ("LONG", 1500.0, float("inf")))
CARRIERS = ("AA", "DL", "UA", "WN", "AS", "B6", "NK", "F9")   # frozen 8-carrier list
ROLLUP = {"MQ": "AA", "OH": "AA", "PT": "AA",                  # wholly-owned regionals
          "9E": "DL", "QX": "AS",
          "HA": "AS"}                                          # Hawaiian post-merger convention
CELL_SHARE = 0.05          # carrier quoted on a route iff rolled share >= 5%
HUB_DOMINATED = 0.60       # top-carrier share >= 60%
COMPETITIVE = 0.40         # top-carrier share <= 40%
MIN_ROUTES_PER_CARRIER = 2
WN_MANUAL_CAP = 4          # WN cells capped at its top-4 panel routes (owner-manual)


def _band(distance):
    for name, lo, hi in BANDS:
        if lo < distance <= hi or (lo == 0.0 and distance <= hi):
            return name
    return "LONG"


def load_routes(csv_path):
    """Aggregate directional carrier rows into undirected route records."""
    pax = defaultdict(float)                    # pair -> total passengers
    carrier_pax = defaultdict(lambda: defaultdict(float))
    dist_wsum = defaultdict(float)              # passenger-weighted distance sum
    with open(csv_path, newline="") as f:
        for row in csv.DictReader(f):
            p = float(row["PASSENGERS"] or 0)
            if p <= 0:
                continue
            pair = tuple(sorted((row["ORIGIN"].strip(), row["DEST"].strip())))
            c = row["UNIQUE_CARRIER"].strip()
            c = ROLLUP.get(c, c)
            pax[pair] += p
            carrier_pax[pair][c] += p
            dist_wsum[pair] += p * float(row["DISTANCE"] or 0)
    routes = []
    for pair, total in pax.items():
        shares = {c: v / total for c, v in carrier_pax[pair].items()}
        top_share = max(shares.values())
        distance = dist_wsum[pair] / total
        routes.append({
            "route": "-".join(pair),
            "pax": total,
            "distance": round(distance, 1),
            "band": _band(distance),
            "shares": {c: round(s, 4) for c, s in sorted(shares.items())},
            "top_share": round(top_share, 4),
            "hub_dominated": top_share >= HUB_DOMINATED,
            "competitive": top_share <= COMPETITIVE,
            "cells": sorted(c for c in CARRIERS if shares.get(c, 0.0) >= CELL_SHARE),
            "wn_pax": carrier_pax[pair].get("WN", 0.0),
        })
    # National rank order: passengers desc, tie-break alphabetical on the pair.
    routes.sort(key=lambda r: (-r["pax"], r["route"]))
    for i, r in enumerate(routes):
        r["rank"] = i + 1
    return routes


def _unmet(selected):
    """List unmet constraints for the current selection (order = relaxation order)."""
    unmet = []
    by_band = defaultdict(list)
    for r in selected:
        by_band[r["band"]].append(r)
    for name, _, _ in BANDS:                                   # hub-span first
        if not any(r["hub_dominated"] for r in by_band[name]):
            unmet.append(f"hub-span:{name}:hub-dominated")
        if not any(r["competitive"] for r in by_band[name]):
            unmet.append(f"hub-span:{name}:competitive")
    counts = defaultdict(int)
    for r in selected:
        for c in r["cells"]:
            counts[c] += 1
    for c in CARRIERS:                                         # carrier-coverage second
        if counts[c] < MIN_ROUTES_PER_CARRIER:
            unmet.append(f"carrier-coverage:{c}:{counts[c]}/{MIN_ROUTES_PER_CARRIER}")
    return unmet


def _deficit(selected):
    """Total units of unmet constraint — the step-(ii) metric. Counting units
    (not items) is what lets a carrier's FIRST qualifying route count as
    progress toward its 2-route minimum; a count-of-items metric would skip
    it and defeat the constraint walk."""
    d = 0
    by_band = defaultdict(list)
    for r in selected:
        by_band[r["band"]].append(r)
    for name, _, _ in BANDS:
        d += 0 if any(r["hub_dominated"] for r in by_band[name]) else 1
        d += 0 if any(r["competitive"] for r in by_band[name]) else 1
    counts = defaultdict(int)
    for r in selected:
        for c in r["cells"]:
            counts[c] += 1
    for c in CARRIERS:
        d += max(0, MIN_ROUTES_PER_CARRIER - counts[c])
    return d


def select_panel(routes):
    """The frozen algorithm: (i) top-3 per band; (ii) constraint walk;
    (iii) rank fill; (iv) logged relaxation of whatever remains unmet."""
    audit = []
    selected, chosen = [], set()
    by_band = defaultdict(list)
    for r in routes:
        by_band[r["band"]].append(r)           # already in rank order

    # (i) top-3 per band, unconditional
    for name, _, _ in BANDS:
        for r in by_band[name][:3]:
            selected.append(r); chosen.add(r["route"])
            audit.append(f"step-i top-3 {name}: {r['route']} (rank {r['rank']})")

    # (ii) walk national rank order; add iff band unfilled AND strictly lower deficit
    def band_count(name):
        return sum(1 for r in selected if r["band"] == name)
    for r in routes:
        if len(selected) >= N_ROUTES:
            break
        if r["route"] in chosen or band_count(r["band"]) >= PER_BAND:
            continue
        before = _deficit(selected)
        after = _deficit(selected + [r])
        if after < before:
            selected.append(r); chosen.add(r["route"])
            audit.append(f"step-ii constraint walk: {r['route']} (rank {r['rank']}) "
                         f"deficit {before}->{after}")

    # (iii) fill remaining band slots in pure rank order
    for r in routes:
        if len(selected) >= N_ROUTES:
            break
        if r["route"] in chosen or band_count(r["band"]) >= PER_BAND:
            continue
        selected.append(r); chosen.add(r["route"])
        audit.append(f"step-iii rank fill: {r['route']} (rank {r['rank']})")

    # (iv) whatever is still unmet is relaxed, in _unmet()'s fixed order, logged
    for u in _unmet(selected):
        audit.append(f"step-iv RELAXED (constraint unmet at full bands): {u}")

    selected.sort(key=lambda r: (-r["pax"], r["route"]))

    # WN manual cap: keep WN cells only on WN's top-4 panel routes by WN pax
    wn_routes = sorted((r for r in selected if "WN" in r["cells"]),
                       key=lambda r: (-r["wn_pax"], r["route"]))
    for r in wn_routes[WN_MANUAL_CAP:]:
        r["cells"] = [c for c in r["cells"] if c != "WN"]
        audit.append(f"wn-cap: WN cell dropped on {r['route']} "
                     f"(rank {r['rank']}, wn_pax {int(r['wn_pax'])}) — logged, owner-manual budget")
    wn_manual = [r["route"] for r in wn_routes[:WN_MANUAL_CAP]]
    return selected, wn_manual, audit


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("csv", type=Path)
    ap.add_argument("--out", type=Path, default=None)
    args = ap.parse_args(argv)
    sha = hashlib.sha256(args.csv.read_bytes()).hexdigest()
    routes = load_routes(args.csv)
    panel, wn_manual, audit = select_panel(routes)
    result = {
        "_provenance": {
            "input_file": args.csv.name,
            "input_sha256": sha,
            "formula": "pipeline/select_routes.py (frozen, pre-registration §1)",
            "n_routes": N_ROUTES, "per_band": PER_BAND,
            "carriers": list(CARRIERS), "rollup": ROLLUP,
            "cell_share": CELL_SHARE, "hub_dominated": HUB_DOMINATED,
            "competitive": COMPETITIVE,
            "min_routes_per_carrier": MIN_ROUTES_PER_CARRIER,
            "wn_manual_cap": WN_MANUAL_CAP,
        },
        "panel": [{k: r[k] for k in ("route", "rank", "pax", "distance", "band",
                                     "top_share", "hub_dominated", "competitive",
                                     "cells")} for r in panel],
        "wn_manual_routes": wn_manual,
        "n_cells": sum(len(r["cells"]) for r in panel),
        "audit": audit,
    }
    text = json.dumps(result, indent=2)
    if args.out:
        args.out.write_text(text + "\n")
        print(f"panel written: {args.out} ({len(panel)} routes, {result['n_cells']} cells)")
    else:
        print(text)
    return result


if __name__ == "__main__":
    main()
