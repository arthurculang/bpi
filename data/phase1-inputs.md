# Phase 1 pinned inputs — panel selection, denominators, incidence, controls

`v0 · 2026-07-06 · workstream E · INPUTS to docs/phase1-preregistration.md — committed after docs/g1-band.md, before any Phase 1 computation; corrections MAY be logged here, the pre-registration's rules MAY NOT change`

## 1. Route-selection input (owner action — blocks the route list, not the freeze)

- **File (exact pull spec — the hash plus these parameters make the input
  unique and checkable):** BTS T-100 Domestic Segment (All Carriers) via
  TranStats, **all 12 months of calendar 2024 in one download**, fields
  ORIGIN, DEST, UNIQUE_CARRIER, PASSENGERS, DISTANCE, CLASS; hash the CSV
  **exactly as downloaded, no edits**. `select_routes.py` validates the header
  and excludes CLASS ≠ F rows itself (and fails loudly on pax-positive rows
  with blank distance), so a wrong pull cannot silently produce a panel. The
  log entry recording the hash must also record: download URL, date, row
  count, and column list.
- **SHA-256:** `PENDING-OWNER-PULL` (this line is replaced, with a log entry,
  when the owner commits the hash; the route list is computed only after).
- **Operating→marketing rollup (pinned; must match the script's ROLLUP dict
  exactly):** Envoy/PSA/Piedmont (MQ/OH/PT) → AA; Endeavor (9E) → DL; Horizon
  (QX) → AS; **Hawaiian (HA) → AS** (post-merger convention, logged).
  Multi-partner regionals (SkyWest, Republic, Mesa, GoJet) are NOT rolled up
  (attribution is itinerary-dependent and unknowable from T-100) — a disclosed
  limitation, mitigated by the wave-0 schedule check (additions-only,
  exhaustive over panel-route × listed-carrier pairs, evidence-registered;
  pre-registration §1).
- **DB1C/OD40 product-name verification (owner, unblocked connection):** the
  spec records DB1C/OD40 as the post-July-2025 successor to DB1B (monthly, 40%
  sample). Byte-verify the official product name and granularity on bts.gov
  before any methods text ships and before the first denominator pull. Due:
  August 2026.

## 2. Blackout windows (frozen; inclusive of both endpoints)

Thanksgiving week (Mon–Sun containing the 4th Thursday of November);
**Dec 18 – Jan 4**; **Jul 1 – 7**. Iterate-forward rule and the
December-prices-early-to-mid-January consequence per pre-registration §2
(worked traces there: Dec 2026 wave → depart Jan 5 / return Jan 12; Dec 2027
wave → depart Jan 11 / return Jan 18).

## 3. Fare-family crosswalk (frozen)

UA Basic Economy / Economy · AA Basic / Main Cabin · DL Basic / Main ·
WN Basic / Choice (Choice Extra = exempt two-free-bag family, conditioning
only) · AS Saver / Main · B6 Blue Basic / Blue · NK Go (single cabin,
`pair=not-applicable`) · F9 Basic / Economy-bundle. Renames are
label-reshuffle non-events unless the attribute vector changes.

## 4. Missing-code taxonomy (frozen)

MISS/BLOCKED · MISS/SOLDOUT · MISS/NO-BASIC (data, not a miss) ·
MISS/SITE-ERR · MISS/PAIR-BROKEN · MISS/SKIPPED. Ladders and allowances per
pre-registration §7.

## 5. De-scope order (frozen)

(1) shrink the rotating audit subsample; (2) drop the 6th (lowest-ranked)
route per distance band → 15 routes / ≈ 37 cells — unless dropping a band's
lowest-ranked route would push a carrier below its 2-route minimum, in which
case drop the next-lowest-ranked route in that band that does not; if none
qualifies, that band keeps 6 (deterministic branch). Fires before wave 1 if
the **committed wave-0 wall-clock total** (Step-0 start → Step-6 end, logged
in the wave-0 capture JSON) exceeds **9.0 h**, or after two consecutive waves
whose committed totals exceed 9.0 h.

## 6. Incidence primaries and grids (provenance per data/incidence-proxies.md)

| Profile | Primary | Grid / bounds | Tag |
|---|---|---|---|
| AIR-P1-CARRYON | none defensible | **[0%, 100%]**, structural ceiling ~70–85% as labeled upper bound | `gap/structural-ceiling` |
| AIR-P2-PERSONALITEM | complement bound | [0%, 100%] | derived |
| AIR-P3-ONEBAG | fee-payer ~16–19% of enplanements | check-rate ~34–39% shown alongside; grid [10%, 45%] | `administrative-ratio/usable` |
| AIR-P4-TWOBAG | bags-per-checker 1.4–1.6 derivation | fallback [0%, 100%] if ruled below the §8 bar | `administrative-ratio-derived/usable-with-assumption` |
| STR (Netflix / Disney+ / Hulu ad-free) | 55% / 63% / **[0%, 100%]** ad-FREE complements (Hulu has no seller-specific usable source — register rule 1 applies; the Antenna market-wide envelope is context only) | bounds as tagged in the register | Comscore / company / `gap→[0,100]` |
| BNK-P1 | n/a (sign-only control) | — | `administrative/usable` |

Pre-collection selection discipline: primaries above were chosen before any
Phase 1 result exists (this commit). Changes = logged amendments.

## 7. Archival-denominator convention (Q1 2027 exhibit)

Per event: route-average one-way base fare for the event carrier on the panel
routes, from the O&D product covering the **last full quarter preceding the
effective date**; per-event single-product rule (no DB1B/DB1C splice inside
any event window; product printed as a column). Sensitivity grid: denominator
∈ {pre-event quarter, same-quarter-prior-year, carrier-route vs panel-pooled}
× fare-anchor grid {$250, $300, $325, $350, $400} × incidence {primary, bounds}
× DB1B/DB1C cross-product check where windows overlap. All cells shown;
out-of-band corners disclosed, never hidden.

**Gap composition (mirror of pre-registration §11; MAY NOT change after
sign-off):** published per-event object = incidence-weighted event
contribution EC = incidence × (Δfee/segment × profile segments) ÷ (2 ×
route-average one-way fare), a Gap **over the matched-carrier scalar-fare
comparator** (G0's G_air object) — never inserted into codebook §9's
Σw[ρ − π^CPI]; comparator labeled on every exhibit row. Where CPI's quote spec
captures the attribute (first bag ~80% of designated quotes), publish EC-gross
AND predicted residual Gap = EC-gross × (1 − capture share), capture share
sourced. Worked number pinned by `engine/test_phase1.py`: $10/segment × 2 ÷
$650 = +3.08%; × 17% incidence = +0.52pp gross; × (1 − 0.80) = +0.10pp
predicted residual. No composite before G3.

## 8. Grocery control inputs

Basket categories (frozen; UPCs + net quantities + the single ZIP freeze at
the December 2026 Ledger freeze, logged here): cereal, chips, paper towels,
bath tissue, ground coffee, ice cream, orange juice, laundry detergent, candy
multipack, granola bars, dish soap, cookies. Retailers: walmart.com,
target.com. List price only; member prices recorded as conditioning, never
headline.

## 9. Banking control inputs

Seller-list formula: top-5 US retail depositories by domestic deposits, **FDIC
Summary of Deposits, June 2025 vintage** — file pulled and SHA-256-committed by
the owner before the archival computation (due ~September 2026). Expected
output: Chase, Bank of America, Wells Fargo, Citi, U.S. Bank; the formula's
output is binding. Series: 2019 → latest posted overdraft + monthly
maintenance fees, banks' own schedules (Wayback legitimate), CFPB Data
Spotlight corroboration.

## 10. December-wave conventions (frozen)

- The annual December-to-December link **computes after the following January
  wave completes** (the schedule-posted confirmation window, pre-registration
  §4).
- ULCC (NK/F9/B6) December observation of record = **median of three same-day
  sessions** per cell.
- Every link-entering paired quote in the December wave gets an owner
  manual save registered via `capture.py --manual` (archival grade).
- Backup capture window: the second Tuesday of December.

## Amendment log

- 2026-07-06 (pre-sign-off, adversarial review of the draft package): pull
  spec tightened (12-month single download, CLASS field, as-downloaded hash,
  URL/date/row-count/column-list logging); HA → AS added to the pinned rollup
  (was in the script's ROLLUP, omitted here); blackout endpoints declared
  inclusive with worked traces; de-scope trigger re-anchored to the committed
  wave-0 wall-clock vs 9.0 h with a deterministic tie-branch; Hulu incidence
  corrected to [0%, 100%] per register rule 1; the archival Gap composition
  mirrored into §7; §10 December conventions added.
