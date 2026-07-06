# Phase 1 pinned inputs — panel selection, denominators, incidence, controls

`v0 · 2026-07-06 · workstream E · INPUTS to docs/phase1-preregistration.md — committed after docs/g1-band.md, before any Phase 1 computation; corrections MAY be logged here, the pre-registration's rules MAY NOT change`

## 1. Route-selection input (owner action — blocks the route list, not the freeze)

- **File:** BTS T-100 Domestic Segment (All Carriers), calendar year 2024,
  scheduled services; fields: ORIGIN, DEST, UNIQUE_CARRIER, PASSENGERS,
  DISTANCE. Download via TranStats on an unblocked connection.
- **SHA-256:** `PENDING-OWNER-PULL` (this line is replaced, with a log entry,
  when the owner commits the hash; the route list is computed only after).
- **Operating→marketing rollup (pinned):** wholly-owned or exclusive regionals
  roll to their mainline brand — Envoy/PSA/Piedmont → AA; Endeavor → DL;
  Horizon → AS. Multi-partner regionals (SkyWest, Republic, Mesa, GoJet) are
  NOT rolled up (attribution is itinerary-dependent and unknowable from T-100)
  — a disclosed limitation, mitigated by the wave-0 schedule check
  (additions-only; pre-registration §1).
- **DB1C/OD40 product-name verification (owner, unblocked connection):** the
  spec records DB1C/OD40 as the post-July-2025 successor to DB1B (monthly, 40%
  sample). Byte-verify the official product name and granularity on bts.gov
  before any methods text ships and before the first denominator pull. Due:
  August 2026.

## 2. Blackout windows (frozen)

Thanksgiving week (Mon–Sun containing the 4th Thursday of November);
**Dec 18 – Jan 4**; **Jul 1 – 7**. Iterate-forward rule and the
December-prices-mid-January consequence per pre-registration §2.

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
route per distance band → 15 routes / ≈ 37 cells; never below any carrier's
2-route minimum. Fires before wave 1 if wave 0 exceeds 8 h, or after two
consecutive over-8h waves.

## 6. Incidence primaries and grids (provenance per data/incidence-proxies.md)

| Profile | Primary | Grid / bounds | Tag |
|---|---|---|---|
| AIR-P1-CARRYON | none defensible | **[0%, 100%]**, structural ceiling ~70–85% as labeled upper bound | `gap/structural-ceiling` |
| AIR-P2-PERSONALITEM | complement bound | [0%, 100%] | derived |
| AIR-P3-ONEBAG | fee-payer ~16–19% of enplanements | check-rate ~34–39% shown alongside; grid [10%, 45%] | `administrative-ratio/usable` |
| AIR-P4-TWOBAG | bags-per-checker 1.4–1.6 derivation | fallback [0%, 100%] if ruled below the §8 bar | `administrative-ratio-derived/usable-with-assumption` |
| STR (Netflix / Disney+ / Hulu ad-free) | 55% / 63% / [40%, 70%] ad-FREE complements of the ad-tier shares | bounds as tagged in the register | Comscore / company / `envelope/sanity` |
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

## Amendment log

- (none yet)
