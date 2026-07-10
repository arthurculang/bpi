#!/usr/bin/env python3
"""Wave worksheet generator — Phase 1 collection (pre-registration §6 Step 0).

Given the frozen panel (select_routes.py output) and a wave date, emits the
operator's worksheet for one monthly wave: every carrier-route cell with its
band, the blackout-iterated travel dates, the Southwest manual list, and the
deterministic 2-cell in-flow audit rotation. No discretion: the same panel +
wave date always yields the same worksheet.

Run:  python3 pipeline/build_worksheet.py panel.json 2026-10-06 --out wave.json

Conventions (frozen in docs/phase1-preregistration.md §2/§4 and
data/phase1-inputs.md §2/§5):
  - Itinerary: depart wave+21 days, return wave+28 days (Tuesday/Tuesday, 7 nights).
  - Blackout windows, endpoint-inclusive: Thanksgiving week (Mon-Sun containing
    the 4th Thursday of November); Dec 18 - Jan 4; Jul 1 - 7. If depart or return
    lands in a window, advance the pair by whole weeks until both fall wholly
    outside all windows (flag grid_shift=holiday).
  - Wave 1 = 2026-10-06; the wave number drives the audit rotation.
  - Audit: legacy cells (AA/DL/UA/AS) ordered by (carrier, route); wave w audits
    positions (2w) mod N and (2w+1) mod N.
"""

import argparse
import datetime as dt
import json
from pathlib import Path

WAVE1 = dt.date(2026, 10, 6)          # pre-registration §2
DEPART_OFFSET = 21                     # days after wave day
RETURN_OFFSET = 28
LEGACY = ("AA", "DL", "UA", "AS")      # fee-schedule carriers, audited in-flow
WN = "WN"                              # owner-manual


def fourth_thursday_november(year):
    d = dt.date(year, 11, 1)
    # weekday(): Mon=0 .. Thu=3
    first_thu = 1 + (3 - d.weekday()) % 7
    return dt.date(year, 11, first_thu + 21)


def in_blackout(d):
    """Endpoint-inclusive per data/phase1-inputs.md §2."""
    if d.month == 7 and 1 <= d.day <= 7:
        return True
    if (d.month == 12 and d.day >= 18) or (d.month == 1 and d.day <= 4):
        return True
    thu = fourth_thursday_november(d.year)
    if (thu - dt.timedelta(days=3)) <= d <= (thu + dt.timedelta(days=3)):
        return True
    return False


def grid_dates(wave_day):
    """Return (depart, return, shifted) applying the iterate-forward rule."""
    depart = wave_day + dt.timedelta(days=DEPART_OFFSET)
    ret = wave_day + dt.timedelta(days=RETURN_OFFSET)
    shifted = False
    # advance by whole weeks until BOTH endpoints clear every window
    guard = 0
    while in_blackout(depart) or in_blackout(ret):
        depart += dt.timedelta(days=7)
        ret += dt.timedelta(days=7)
        shifted = True
        guard += 1
        if guard > 12:
            raise RuntimeError("blackout iteration failed to converge — check windows")
    return depart, ret, shifted


def wave_number(wave_day):
    """Wave 1 = 2026-10-06; subsequent first-Tuesdays increment by one."""
    return (wave_day.year - WAVE1.year) * 12 + (wave_day.month - WAVE1.month) + 1


def build(panel, wave_day):
    cells = []
    for r in panel["panel"]:
        for c in r["cells"]:
            cells.append({"route": r["route"], "carrier": c, "band": r["band"]})
    cells.sort(key=lambda x: (x["carrier"], x["route"]))

    depart, ret, shifted = grid_dates(wave_day)
    wnum = wave_number(wave_day)

    # deterministic audit rotation over legacy cells
    legacy_cells = [x for x in cells if x["carrier"] in LEGACY]
    audit = []
    if legacy_cells:
        n = len(legacy_cells)
        for k in (2 * wnum, 2 * wnum + 1):
            audit.append(legacy_cells[k % n])

    wn_manual = list(panel.get("wn_manual_routes", []))
    return {
        "wave_id": f"wave-{wnum:02d}-{wave_day.isoformat()}",
        "wave_number": wnum,
        "wave_day": wave_day.isoformat(),
        "depart_date": depart.isoformat(),
        "return_date": ret.isoformat(),
        "grid_shift": "holiday" if shifted else "",
        "agent_cells": [x for x in cells if x["carrier"] != WN],
        "wn_manual_routes": wn_manual,
        "audit_cells": audit,
        "n_agent_cells": sum(1 for x in cells if x["carrier"] != WN),
        "december_link_wave": wave_day.month == 12,
    }


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("panel", type=Path)
    ap.add_argument("wave_day", help="ISO date of the wave (a first Tuesday)")
    ap.add_argument("--out", type=Path, default=None)
    args = ap.parse_args(argv)
    panel = json.loads(args.panel.read_text())
    wave_day = dt.date.fromisoformat(args.wave_day)
    ws = build(panel, wave_day)
    text = json.dumps(ws, indent=2)
    if args.out:
        args.out.write_text(text + "\n")
        print(f"worksheet written: {args.out} "
              f"({ws['n_agent_cells']} agent cells, "
              f"{len(ws['wn_manual_routes'])} WN manual, "
              f"depart {ws['depart_date']}{' [shifted]' if ws['grid_shift'] else ''})")
    else:
        print(text)
    return ws


if __name__ == "__main__":
    main()
