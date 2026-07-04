# Phase 0 input file — 2008–09 checked-bag unbundling chronology

`v0 · 2026-07-04 · workstream E · INPUTS ONLY — the G0 band was committed first (repo commit 57581d6); per the band's rules these inputs MAY be corrected with logging, the band MAY NOT`
`Sourcing: contemporaneous press triangulated via search snippets (most primary pages 403-block automated fetch); tie-breaker source for all fee dates = Brueckner–Lee–Picard–Singer (2015) Table 1 (ATPCO data) — pull from an unblocked connection before computation`

## Designated negative-print episode (fixed now, per G0 test 4)

**US Airways in-flight beverage unbundling and repeal.** Charged $2 for
soda/water ($1 coffee/tea) from **2008-08-01** — the only US carrier to do so;
announced repeal **2009-02-23**; free beverages resumed **2009-03-01** (NPR;
Cranky Flier). A dated restoration-of-inclusion inside the study window: the
method must print **≤ 0%** on this event. (Bag fees at US Airways were unchanged
by the repeal — the test isolates the beverage attribute.)

## Second-bag fee wave ($25 one-way, domestic nonrefundable economy)

| Carrier | Announced | Effective | Confidence |
|---|---|---|---|
| United | 2008-02-04 | purchase ≥ 2008-02-04, travel ≥ 2008-05-05 | high |
| US Airways | — | purchase ≥ 2008-02-26 | high |
| Continental | — | purchase ≥ 2008-04-05, travel ≥ 2008-05-05 | high |
| Delta | — | travel ≥ 2008-05-01 ($25); **raised $25→$50 announced ~2008-07-31, purchase ≥ that Thu / travel ≥ 2008-08-05** | high |
| Northwest | — | travel ≥ 2008-05-05 | high |
| Frontier | 2008-05 | purchase ≥ 2008-06-10 | medium |
| JetBlue | — | introduced 2008 (10-K-confirmed); **amount disputed: AP says $15, not $20/$25** | **low — pull mediaroom 06-30-2008 release + 10-K** |
| American | — | pre-dated its first-bag fee ($25) | medium |

## First-bag fee wave ($15 one-way at introduction)

| Carrier | Announced | Effective | Confidence |
|---|---|---|---|
| American (led) | 2008-05-21 | tickets ≥ 2008-06-15 | high |
| US Airways | ~2008-06-12 (recall) | 2008-07-09 | high (effective), low (announce) |
| United | 2008-06-12 | purchase ≥ 2008-06-13, travel ≥ 2008-08-18 | high |
| Northwest | 2008-07-09 | sold ≥ 2008-07-10, travel ≥ 2008-08-28 | high |
| Continental | 2008-09-05 | travel ≥ 2008-10-07 | high |
| Delta (last legacy) | 2008-11-05 | travel ≥ 2008-12-05 (grandfathering: pre-11/05 tickets kept free first bag, paid $50 second) | high |
| Alaska | 2009-04-23 | 2009-07-07 (purchase ≥ 2009-05-01); paired with 25-minute bag guarantee (2,500 miles / $25 voucher) — a *compensated* unbundling, flag in equivalence review | high |
| Frontier | via AirFairs fare families **effective 2008-12-18** (corrected from ~2008-09); lowest "Economy" tier excluded free bags, "Classic" (~$20 more) included two | date medium; **first-bag $ amount unverified** (believed $15) — Brueckner Table 1 |

**Non-chargers (the still-bundled menu for cheapest-replication pricing):**
Southwest — first two bags free throughout ("Bags Fly Free" campaign, ad spend
+20% to $112.6M in H1 2009; consider-first share 28%→35% 3Q09→2Q10).
JetBlue — first bag free until 2015-06-30.
*Codebook note: under the same-seller headline (H), WN/B6 menus do NOT restore a
legacy carrier's experience; they enter only the cross-seller sensitivity (S).*

## 2009 increase wave

UA, DL, CO, US raised airport-paid fees +$5 to **$20 first / $30 second**
(keeping $15/$25 online) during H1 2009; United led the online/airport split
(exact date still unverified — indirectly supported for Jan 2009 by a United
online-prepay discount running through 2009-01-31). American announced
**2009-07-24** a flat $20/$30 with no online discount, **effective tickets
bought on/after 2009-08-14** (AP-confirmed). By Dec 2009 the modal first-bag
price: $20 airport / $15 online.

## Anchors for the computation

- **Base fares (BTS annual average domestic itinerary):** 2008 = $346 (verified),
  2009 ≈ $310 (verified); 2007 = **$325 (triangulation-confirmed:** Q2-2008 $352
  was "an 8.3% increase from the $325 average in 2007", 352/1.083 = 325.0 —
  CNN/NPR citing BTS; still needs a byte-level pull for exact cents).
- **Bag-fee revenue:** $464M (2007) → >$1.1B (2008) → **$2.7B (2009, confirmed:**
  BTS via CNN 2011, "$3.4B [2010] a 24% increase from $2.7 billion in 2009") →
  $3.4B (2010). Exact-to-the-thousand (~$2.74B) needs the BTS page.
- **Incidence response (GAO-10-785):** one carrier's checked baggage fell by
  half, another's bags/passenger fell 40%; DOT mishandled-bag rate 7.03 (2007)
  → 5.26 (2008) → 3.91 (2009) per 1,000. No published absolute pre-fee
  check-rate found — derive base-period incidence per `data/incidence-proxies.md`
  and document the assumption before the sector computation runs (G0 rule).

## Pinned conventions (committed BEFORE any computation — required by the codebook)

1. **Band tests 2–3 are computed as event contributions** — the profile's link
   relative NET of the matched-fare comparator (ρ − π_fare) — consistent with
   test 4's "event contribution" language and trigger rule T3 (pure scalar fare
   moves, e.g. the 2008 fuel spike, are not the event's doing). Test 1's
   measured line item is 2 × end-2009 first-bag fee as posted; the
   fee-minus-offset variant is reported alongside solely for the B2 comparison.
2. **Incidence (selected now, per codebook §8):** 2007 base-period share of
   passengers checking ≥1 bag — primary **45%** (midpoint implied by GAO-10-785's
   40–50% post-fee decline against the modern ~35–40% level), sensitivity grid
   **[35%, 55%]**. Gate evaluation reports the full grid; the primary value was
   chosen before any result existed (this commit).
3. **Purchase-point:** per codebook §2.3, prepaid-online rates are primary
   (end-2009: $15 online at UA/DL/CO/US); airport rates ($20; AA flat $20)
   reported as sensitivity.
4. **Fare anchors:** BTS average domestic itinerary fares; annual averages as
   primary pending byte-verification, anchor sensitivity grid **[$250, $400]**
   (the range the band itself contemplates). Q4/December-point anchors are a
   refinement to pull (open item 7) since links run Dec-to-Dec.
5. **Materiality:** open items 1–3 and 5–6 (Frontier, JetBlue, Delta second-bag
   step, 2009 split dates, 2009 revenue) do not enter the four band tests,
   which use the modal legacy schedule ($15 first bag end-2008; $15 online/$20
   airport end-2009) — they block full sector coverage in the Phase 0 note, not
   gate evaluation. Items 4 and 7 (fare anchors) are handled by the grid above.

## Open items (status after 2026-07-04 research pass; log every change)

1. Frontier first-bag **date fixed (AirFairs 2008-12-18)**; dollar amount still
   open (Brueckner Table 1 / Frontier Dec-2008 release via Wayback).
2. JetBlue second-bag: introduction confirmed, **amount still disputed** ($15 vs
   $20/$25); 2009 step open. Pull mediaroom 06-30-2008 + FY2008/09 10-Ks.
3. Delta $25→$50 second-bag step: **RESOLVED** (~2008-07-31 purchase / 2008-08-05
   travel). Owner spot-check the AP dateline for the exact Thursday.
4. 2007 average fare: **RESOLVED to $325** by triangulation (still wants a
   byte-level cents read from the official BTS table).
5. AA flat $20/$30 **effective date RESOLVED (2009-08-14)**; United's online/
   airport split announcement date still open (AP/Reuters archive ~Jan 2009).
6. 2009 bag-fee revenue: **RESOLVED to ~$2.7B**; exact figure wants the BTS page.
7. Q4/December-point BTS average fares for 2007–2009 — **still open** (links run
   Dec-to-Dec; the annual averages above carry the mid-2008 fuel spike).

**Gate status unchanged (still DRY RUN):** none of the above alter the four band
tests — items 1–3, 5–6 are non-material per pinned convention 5; item 4 confirms
a value ($325) already central on the tested anchor grid, so the dry run is not
re-run. Official G0 evaluation still waits only on item 7 (December-point fare
anchors) plus a byte-level read of the item-4 cents — both owner tasks on an
unblocked connection.

## Amendment log

- 2026-07-04 (research pass, workflow wx2gjc8p0): **material correction** —
  Frontier AirFairs launch moved from "~2008-09" to 2008-12-18 (ColoradoBiz;
  CBS 2008-12-19; FlyerTalk). Resolved: Delta second-bag $25→$50 (~2008-07-31);
  2007 fare $325; 2009 bag revenue ~$2.7B; AA flat-fee effective 2009-08-14.
  JetBlue amount flagged disputed (do not commit). No band-test inputs changed;
  the modal legacy schedule used by the harness ($15 first bag end-2008; $15
  online / $20 airport end-2009) is unaffected.
