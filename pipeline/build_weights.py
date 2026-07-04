#!/usr/bin/env python3
"""Build bottom-two-quintile CE weights (workstream C).

Source: a maintained GitHub mirror of BLS Consumer Expenditure flat-file data
(github.com/mtkonczal/Blog-Posts-Presentations-and-Testimony), whose values were
cross-verified against the BLS 2024 news release (USDL-25-1586: Q1 total
$35,046, Q2 $50,054 — exact match) and against a second independent mirror of
raw BLS API responses. Major categories only through 2024; detail items
(cellular 270102, internet 690114, cable 270310, airfare 530110, out-of-town
lodging 210210, fees & admissions) require the BLS API / Table 1101 XLSX from
an unblocked connection — August task, plan §9 item 7.

Output: data/cex-b40-quintiles.csv
  item_code, item, q1_2023, q1_2024, q2_2023, q2_2024, q1_2024_share, q2_2024_share

Verification built in: fails loudly if TOTALEXP anchors drift from the
published release values, or if top-level categories stop summing to the total
(residual closure for the coverage map's "all other" row).
"""

import csv
import io
import sys
import urllib.request
from pathlib import Path

SRC = ("https://raw.githubusercontent.com/mtkonczal/"
       "Blog-Posts-Presentations-and-Testimony/main/"
       "blogs_2026/01_cex_food_consumption/data/cex_data.csv")
OUT = Path(__file__).resolve().parent.parent / "data" / "cex-b40-quintiles.csv"

ANCHORS = {("q1", "2024"): 35046.0, ("q2", "2024"): 50054.0}  # USDL-25-1586
QUINTILE = {"02": "q1", "03": "q2"}
YEARS = ("2023", "2024")
TOP_LEVEL = ["FOODTOTL", "ALCBEVG", "HOUSING", "APPAREL", "TRANS", "HEALTH",
             "ENTRTAIN", "PERSCARE", "READING", "EDUCATN", "TOBACCO", "MISC",
             "CASHCONT", "INSPENSN"]
ORDER = ["TOTALEXP", "FOODTOTL", "FOODHOME", "FOODAWAY", "HOUSING", "OWNDWELL",
         "RNTDWELL", "OTHLODGE", "HEALTH", "HLTHINSR", "MEDSERVS", "DRUGS",
         "TRANS", "VEHPURCH", "470111", "500110", "VEHOTHXP", "PUBTRANS",
         "ENTRTAIN", "APPAREL", "PERSCARE", "EDUCATN", "READING", "ALCBEVG",
         "TOBACCO", "MISC", "CASHCONT", "INSPENSN", "INCBEFTX"]


def main():
    raw = urllib.request.urlopen(SRC, timeout=60).read().decode()
    rows = list(csv.DictReader(io.StringIO(raw)))
    data = {}
    for r in rows:
        if r["year"] in YEARS and "quintile" in r.get("characteristics_text", "").lower():
            c = QUINTILE.get(r["characteristics_code"])
            if not c:
                continue
            d = data.setdefault(r["item_code"], {"title": r["series_title"].split(" by ")[0]})
            d[f"{c}_{r['year']}"] = float(r["value"])

    for (c, y), expect in ANCHORS.items():
        got = data["TOTALEXP"][f"{c}_{y}"]
        assert got == expect, f"anchor drift: TOTALEXP {c} {y} = {got}, expected {expect}"
    for c in ("q1", "q2"):
        s = sum(data[k][f"{c}_2024"] for k in TOP_LEVEL)
        assert abs(s - data["TOTALEXP"][f"{c}_2024"]) <= 2, f"residual closure failed for {c}: {s}"

    tot = {c: data["TOTALEXP"][f"{c}_2024"] for c in ("q1", "q2")}
    with OUT.open("w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["item_code", "item", "q1_2023", "q1_2024", "q2_2023", "q2_2024",
                    "q1_2024_share", "q2_2024_share"])
        for k in ORDER:
            if k not in data:
                print(f"missing item: {k}", file=sys.stderr)
                continue
            d = data[k]
            share = (lambda c: round(d[f"{c}_2024"] / tot[c] * 100, 2)
                     if f"{c}_2024" in d and k != "INCBEFTX" else "")
            w.writerow([k, d["title"], d.get("q1_2023", ""), d.get("q1_2024", ""),
                        d.get("q2_2023", ""), d.get("q2_2024", ""), share("q1"), share("q2")])
    print(f"wrote {OUT} (anchors verified, residual closed)")


if __name__ == "__main__":
    main()
