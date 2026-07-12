#!/usr/bin/env python3
"""Coverage restatement — B40 restoration-priced share of the CE consumption
basket (RX-100 near-term win #1; plan §9 item 7 detail refresh).

Inputs (all committed):
  - the verified CE mirror (majors, 2024, quintile means) — same source
    build_weights.py asserts;
  - data/captures/fred-cex-quintiles-2026-07-12.json (detail cells, 2024,
    browser-agent-extraction provenance);
  - the plan §1 coverage map's 2023-vintage detail cells (airline fares,
    lodging-on-out-of-town-trips) as DETAIL-SHARE anchors: 2023 detail ÷ 2023
    parent, applied to the 2024 parent — a documented convention, flagged on
    every use, replaced when the owner registers CE Table 1101 2024.

Denominator: CE CONSUMPTION scope = average annual expenditures minus personal
insurance & pensions minus cash contributions (the CE lines outside the CPI
consumption basket). Owned-dwelling spending stays in the denominator at its
CE value — the full OER-weight treatment needs the R-CPI-I relative-importance
vintage (owner XLSX task) and is out of scope here, stated not hidden.

Run:  python3 pipeline/restate_coverage.py
Asserts the published anchors; prints the restatement table.
"""

import csv
import json
import sys
import urllib.request
from pathlib import Path

MIRROR = ("https://raw.githubusercontent.com/mtkonczal/"
          "Blog-Posts-Presentations-and-Testimony/main/"
          "blogs_2026/01_cex_food_consumption/data/cex_data.csv")
CAPTURE = Path(__file__).resolve().parent.parent / "data/captures/fred-cex-quintiles-2026-07-12.json"

# Plan §1 coverage-map 2023-vintage detail cells (committed, byte-verified era)
AIR_2023 = {"q1": 167.0, "q2": 274.0}
LODGING_OOT_2023 = {"q1": 166.0, "q2": 338.0}


def mirror_majors():
    with urllib.request.urlopen(MIRROR, timeout=60) as r:
        rows = list(csv.DictReader(r.read().decode().splitlines()))
    out = {}
    for r in rows:
        if (r["year"] == "2024" and r["demographics_code"] == "LB01"
                and r["characteristics_code"] in ("02", "03")):
            q = "q1" if r["characteristics_code"] == "02" else "q2"
            out.setdefault(r["item_text"], {})[q] = float(r["value"])
    return out


def main():
    majors = mirror_majors()
    cap = {s["concept"]: s for s in json.loads(CAPTURE.read_text())["series"]}

    # anchor assertions (fail loudly on a drifting mirror)
    assert majors["Average annual expenditures"]["q1"] == 35046.0, majors["Average annual expenditures"]
    assert majors["Rented dwellings"]["q1"] == 5781.0

    b40 = {}
    for name, v in majors.items():
        b40[name] = (v["q1"] + v["q2"]) / 2

    total = b40["Average annual expenditures"]
    outside = b40["Personal insurance and pensions"] + b40["Cash contributions"]
    consumption = total - outside

    # detail cells, 2024 (capture) and detail-share conventions (flagged)
    cell = lambda c: (cap[c]["q1_2024"] + cap[c]["q2_2024"]) / 2
    cell23 = lambda c: (cap[c]["q1_2023"] + cap[c]["q2_2023"]) / 2
    cellular = cell("Cellular phone service")
    resphone = cell("Residential phone/VOIP/phone cards")
    pubtrans24 = cell("Public and other transportation (parent of airline fares)")
    pubtrans23 = cell23("Public and other transportation (parent of airline fares)")
    air_share23 = ((AIR_2023["q1"] + AIR_2023["q2"]) / 2) / pubtrans23
    airline24 = air_share23 * pubtrans24                      # CONVENTION-flagged
    othlodge24 = cell("Other lodging (parent of out-of-town trips)")
    othlodge23 = cell23("Other lodging (parent of out-of-town trips)")
    oot_share23 = ((LODGING_OOT_2023["q1"] + LODGING_OOT_2023["q2"]) / 2) / othlodge23
    lodging24 = oot_share23 * othlodge24                      # CONVENTION-flagged
    tvaudio = cell("Audio and visual equipment and services (parent of pay-TV/streaming)")

    rent = b40["Rented dwellings"]
    # Restoration-priced set (R-active + Phase-2 entrants), pay-TV/streaming and
    # internet detail NOT published at quintile level -> interval [0, TVAUDIO]
    r_low = rent + cellular + resphone + airline24 + lodging24
    r_high = r_low + tvaudio
    fees = cell("Fees and admissions")                        # R-queued (Phase 3)

    print("B40 = pooled Q1/Q2 means, CE 2024 (mirror majors + FRED capture details)")
    print(f"CE total avg annual expenditures:        ${total:,.0f}")
    print(f"  - personal insurance & pensions + cash contributions: ${outside:,.0f}")
    print(f"CE CONSUMPTION scope (denominator):      ${consumption:,.0f}")
    print()
    print(f"Rented dwellings:                        ${rent:,.0f}")
    print(f"Cellular + residential phone:            ${cellular + resphone:,.0f}")
    print(f"Airline fares (2023-share convention):   ${airline24:,.0f}")
    print(f"Lodging out-of-town (2023-share conv.):  ${lodging24:,.0f}")
    print(f"Pay-TV/streaming+equipment parent (interval top): ${tvaudio:,.0f}")
    print(f"Fees & admissions (R-queued):            ${fees:,.0f}")
    print()
    lo, hi = r_low / consumption, r_high / consumption
    lo_t, hi_t = r_low / total, r_high / total
    print(f"RESTORATION-PRICED share of CONSUMPTION scope: {lo*100:.1f}% - {hi*100:.1f}%")
    print(f"  (same set over CE TOTAL outlays:             {lo_t*100:.1f}% - {hi_t*100:.1f}%)")
    print(f"  + R-queued fees&admissions adds:             {fees/consumption*100:.1f}pp")
    print(f"Renter shares (capture): Q1 57%, Q2 42% -> B40 renters ~= 49.5%")
    return {"consumption": consumption, "lo": lo, "hi": hi}


if __name__ == "__main__":
    main()
