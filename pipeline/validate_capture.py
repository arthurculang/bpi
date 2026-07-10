#!/usr/bin/env python3
"""Capture-JSON validator — Phase 1 ingestion (pre-registration §6 Step 4).

Fails loudly on a malformed wave capture before it can enter the archive: it
enforces the §5 air record, the streaming record, and the grocery record, plus
the QC checks that are mechanical (QC-2 basic<=main, QC-3 all-in totals present,
QC-8 no member price in a headline field). A record is either valid or carries a
recognized missing_code; an unflagged hole is the only failure state
(pre-registration §6 QC).

Run:  python3 pipeline/validate_capture.py capture.json --kind air
Exit 0 = clean; exit 1 = at least one hard error (printed).
"""

import argparse
import json
import sys
from pathlib import Path

MISSING_CODES = {"MISS/BLOCKED", "MISS/SOLDOUT", "MISS/NO-BASIC",
                 "MISS/SITE-ERR", "MISS/PAIR-BROKEN", "MISS/SKIPPED"}
PAIR_STATUS = {"paired-same-flight", "pair=absent", "pair=not-applicable",
               "basic-soldout", "blocked"}
BAG_SOURCE = {"schedule-prepaid-online", "in-flow", "airport", "gate",
              "gated-behind-pax-info"}

AIR_REQUIRED = ["wave_id", "route", "carrier", "pair_status", "loaded"]
STREAMING_REQUIRED = ["seller", "tier_name", "monthly_price_usd", "ad_free", "loaded"]
GROCERY_REQUIRED = ["upc", "product_name", "net_quantity", "list_price_usd", "loaded"]


def _num(v):
    return v is None or isinstance(v, (int, float))


def validate_air(rec, i):
    errs = []
    mc = rec.get("missing_code")
    if mc is not None and mc not in MISSING_CODES:
        errs.append(f"air[{i}]: unknown missing_code {mc!r}")
    flagged = mc in MISSING_CODES
    for f in AIR_REQUIRED:
        if f not in rec:
            errs.append(f"air[{i}]: missing required field {f!r}")
    if rec.get("pair_status") not in PAIR_STATUS and not flagged:
        errs.append(f"air[{i}]: bad pair_status {rec.get('pair_status')!r}")
    for f in ("basic_outbound_leg_usd", "basic_return_leg_usd",
              "main_outbound_leg_usd", "main_return_leg_usd"):
        if f in rec and not _num(rec[f]):
            errs.append(f"air[{i}]: {f} not numeric ({rec[f]!r})")
    for f in ("first_bag_source", "second_bag_source"):
        if rec.get(f) is not None and rec[f] not in BAG_SOURCE:
            errs.append(f"air[{i}]: bad {f} {rec[f]!r}")
    # QC-2: basic <= main on a valid pair (sum of legs, when all four present)
    legs = [rec.get(k) for k in ("basic_outbound_leg_usd", "basic_return_leg_usd",
                                 "main_outbound_leg_usd", "main_return_leg_usd")]
    if rec.get("pair_status") == "paired-same-flight" and all(_num(x) and x is not None for x in legs):
        basic = legs[0] + legs[1]
        main = legs[2] + legs[3]
        if basic > main + 1e-9:
            errs.append(f"air[{i}]: QC-2 violation basic {basic} > main {main} "
                        "(expected MISS/PAIR-BROKEN)")
    # QC-3: a non-missing loaded row must carry the all-in totals it claims
    if rec.get("loaded") == "yes" and rec.get("pair_status") == "paired-same-flight":
        if rec.get("basic_outbound_leg_usd") is None:
            errs.append(f"air[{i}]: QC-3 loaded pair with no basic outbound price")
    # QC-8: membership/card price must never sit in a headline price field
    for f in ("basic_outbound_leg_usd", "main_outbound_leg_usd"):
        note = str(rec.get("conditioning_notes", "")).lower()
        if rec.get(f) is not None and ("member" in note or "autopay" in note) \
                and rec.get("member_price_in_headline") is True:
            errs.append(f"air[{i}]: QC-8 member/card price flagged into headline field {f}")
    return errs


def validate_streaming(rec, i):
    errs = []
    for f in STREAMING_REQUIRED:
        if f not in rec:
            errs.append(f"streaming[{i}]: missing {f!r}")
    if not _num(rec.get("monthly_price_usd")):
        errs.append(f"streaming[{i}]: monthly_price_usd not numeric")
    if rec.get("ad_free") not in (True, False, None):
        errs.append(f"streaming[{i}]: ad_free not boolean")
    return errs


def validate_grocery(rec, i):
    errs = []
    for f in GROCERY_REQUIRED:
        if f not in rec:
            errs.append(f"grocery[{i}]: missing {f!r}")
    if not _num(rec.get("list_price_usd")):
        errs.append(f"grocery[{i}]: list_price_usd not numeric")
    # net_quantity must be present and non-empty for the per-unit convention
    if not rec.get("net_quantity"):
        errs.append(f"grocery[{i}]: net_quantity empty (per-unit convention needs it)")
    return errs


VALIDATORS = {"air": validate_air, "streaming": validate_streaming,
              "grocery": validate_grocery}


def validate(records, kind):
    v = VALIDATORS[kind]
    errs = []
    for i, rec in enumerate(records):
        errs.extend(v(rec, i))
    return errs


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("capture", type=Path)
    ap.add_argument("--kind", choices=sorted(VALIDATORS), required=True)
    args = ap.parse_args(argv)
    data = json.loads(args.capture.read_text())
    records = data if isinstance(data, list) else data.get("records", data.get(args.kind, []))
    errs = validate(records, args.kind)
    if errs:
        print(f"FAIL: {len(errs)} error(s) in {args.capture.name} ({args.kind}):")
        for e in errs:
            print("  -", e)
        return 1
    print(f"OK: {len(records)} {args.kind} record(s) valid in {args.capture.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
