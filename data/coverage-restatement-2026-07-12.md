# Coverage restatement — B40 restoration-priced share, CE 2024 detail refresh

`v0 · 2026-07-12 · workstream C (plan §9 item 7; RX-100 near-term win #1) · computed by pipeline/restate_coverage.py (executable; asserts the published anchors) from the verified CE mirror (majors, 2024) + data/captures/fred-cex-quintiles-2026-07-12.json (details, browser-agent-extraction provenance)`

## Results (B40 = pooled Q1/Q2 means, CE 2024)

| Quantity | Value |
|---|---|
| CE total average annual expenditures (B40) | $42,550 |
| − personal insurance & pensions + cash contributions | $2,810 (6.6%) |
| **CE consumption scope (denominator)** | **$39,740** |
| Rented dwellings | $6,003 |
| Cellular + residential phone | $1,018 |
| Airline fares (2023-share convention, flagged) | $230 |
| Lodging out-of-town (2023-share convention, flagged) | $274 |
| Pay-TV/streaming parent, interval top (detail not published at quintile level) | $704 |
| **Restoration-priced share of consumption scope** (rent + wireless + air + lodging + streaming interval) | **18.9% – 20.7%** |
| Same set over CE total outlays | 17.7% – 19.3% |
| R-queued fees & admissions adds | +0.7pp |
| Renter shares (2024, captured) | **Q1 57% / Q2 42%** (B40 ≈ 49.5%) |

## The finding this corrects — logged, not buried

The RX-100 concept and proposal hypothesized that restating coverage in
CPI-consumption-basket space would lift the ~26% figure to **~30–35%**,
because CE total outlays include ~11% pensions/insurance outside the CPI
basket. **The real B40 data corrects this downward: bottom-40 households put
only 6.6% into pensions/insurance and cash contributions, so the scope
restatement buys ≈1.2pp, not 4–9pp.** The hypothesis was calibrated on
all-consumer-unit shares; B40 shares are structurally different exactly
because these households have little slack income. Both RX-100 documents are
amended to the computed range this same day. The measure corrects its own
optimistic hypotheses in public — that is the posture working as designed.

What remains genuinely open: the CE-consumption-scope share is still not the
CPI-*weight* share. CPI replaces owner out-of-pocket housing with owners'
equivalent rent, and the B40 renter-majority (57%/42%) interacts with that
through the R-CPI-I weight recipe — resolving it needs the R-CPI-I
relative-importance vintage (owner XLSX registration task, queued). Until
then, ~19–21% of consumption-scope spending is the honest, computed,
provenance-tagged coverage claim at the Phase-2 composition.

## Availability findings (from the 2026-07-12 pull; they matter for the concordance)

Published CE quintile series do **not** exist below these parents: airline
fares (parent: public & other transportation), pay-TV/streaming and internet
(parent: audio & visual equipment and services), trash collection (parent:
water & other public services). Detail allocation therefore uses either the
2023-share convention (flagged per cell) or intervals — never a bare point.
R-CPI-I is XLSX-only (no HTML table); CE Table 1101 2024 XLSX identified
(`cu-income-quintiles-before-taxes-2024.xlsx`) — both queued for owner
`--manual` registration as the byte-grade evidence behind this file.

## CPI-weight space (added same day, on the completed relative-importance capture)

With the full Dec-2024 CPI relative-importance table captured
(`data/captures/cpi-relative-importance-2026-07-12.json`, 293 items, majors
close to 100.000 exactly), the same questions computed in **real CPI-weight
space** (`pipeline/restate_coverage.py --cpi`):

| Quantity | CPI-U | CPI-W |
|---|---|---|
| Phase-2 restoration-priced composition (rent + wireless + res-phone + internet + pay-TV/streaming + air + hotels/motels) | **12.49%** | **15.28%** |
| + R-queued Admissions | +0.74 | +0.53 |
| Tier R (tier-map join, 173/187 strata matched, 95.97% of basket) | **17.8%** | — |
| Tier A | **24.3%** | — |
| Tier B | **53.8%** | — |
| Owners' equivalent rent (largest Tier-B stratum) | **26.28%** | 21.58% |
| Rent of primary residence | 7.50% | 10.44% |

Readings: (1) under average-household CPI-U weights the corridor's Tier B is
the majority of the basket — OER alone is a quarter of it — so the corridor's
width under CPI-U weighting is structurally wide; (2) CPI-W (a
wage-earner-household population, the closest published proxy toward B40
weighting) moves rent +2.9pp and OER −4.7pp, showing the direction the
R-CPI-I bottom-quintile vintage will pull — renters are 57%/42% of B40 —
without yet licensing a B40 number; (3) the 14 unmatched tier-map rows are
name variants already ✓verify-flagged (e.g. "Toys, games, hobbies…" vs the
published "Toys") — they resolve at the owner's byte-verification pass.

## Byte-verification (same day — owner registered both XLSX files)

`data/captures/ce-table1101-quintiles-2024.xlsx` (sha256 05640c17…) and
`data/captures/r-cpi-i-series-dec2005-dec2024.xlsx` (sha256 978de8ca…) are now
in-repo with hashes in `data/captures/xlsx-registration-2026-07-12.json`.
**Every value this file used from the mirror and the FRED capture matches
Table 1101 exactly** — the chain is byte-grade end to end. Two findings:

- Table 1101's hierarchy bottoms out at "Cellular phone service" / "Other
  lodging" — **no airline/cable/internet/trash detail exists there either**,
  so the 2023-share conventions stand permanently unless a BLS-API detail pull
  supplies UCC-level quintile cells.
- R-CPI-I Dec–Dec changes by quintile now byte-grade
  (`data/captures/r-cpi-i-decdec-2026-07-12.json`): cumulative Dec 2005 – Dec
  2024, Q1 +65.6% vs Q5 +57.5% — a **+8.1pp** bottom-vs-top gap (≈0.43pp/yr;
  the spec's Seam-2 cites ≈0.28pp/yr — same order, different figure; flag for
  the spec's next revision to reconcile window/derivation). 2024 alone:
  Q1 +3.02% vs Q5 +2.90%. This series is the weighting-effect exhibit's
  validation anchor. The R-CPI-I *relative-importance* XLSX (the B40 weight
  vintage, a separate file, Dec 2005–Dec 2023) remains the one outstanding
  owner pull.

## Changelog

- v0 (2026-07-12) — first computation; supersedes the mock 30–35% hypothesis
  in the RX-100 docs (amended same day) and refreshes plan §9 item 7 detail
  cells (2024 vintage, quintile level, with availability findings).
