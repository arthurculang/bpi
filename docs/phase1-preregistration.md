# Phase 1 pre-registration — air-travel route panel, collection grid, controls

`v0 · 2026-07-06 · workstreams B/E · the codebook-§13 route-panel freeze, unlocked by the G0 pass (2026-07-04) · AWAITING owner sign-off (§14); freezes publicly with the Phase 0 note (Oct 2026)`

This document pre-registers the Phase 1 live-collection design: the air-travel
route panel and booking grid, the monthly paired-quote protocol, the streaming
sidecar, the grocery and banking controls, the Q1 2027 archival-denominator
exhibit, and the G1 evaluation protocol. It operationalizes Spec v00.02.00 and
codebook v0; where anything here conflicts with those, they govern and the
conflict is a logged erratum. Posture, restated because every artifact must:
the measure is an **upper bound published only as a spread** over matching CPI
series; negative and zero prints are features; every public number carries a
provenance tag; this is a **census of posted menus**, not a sample — no
standard errors are claimed anywhere in Phase 1.

Companion binding files: `docs/g1-band.md` (pass criteria — committed before
this document; numeric limits live there and only there),
`data/phase1-inputs.md` (pinned inputs), `pipeline/select_routes.py` (the
panel-selection formula as executable code).

---

## 1. Route panel (formula, not a list)

**Ranking source and vintage.** BTS **T-100 Domestic Segment (All Carriers),
calendar year 2024** — the codebook §13 wording ("top-N T-100 routes") honored
literally, and the last complete year untouched by the Oct–Nov 2025 federal
data disruptions (plan P11). DB1B/DB1C is used only for its sanctioned
purposes — route weights and unit-value context per spec §8, and scalar
archival denominators per the plan-§4 pre-registered convention — never for
ranking and never as the price concept. The segment-vs-
market unit tension is dissolved by construction, not amended away: **all
quotes are nonstop itineraries**, so T-100 segment ≈ O&D market on every panel
route.

**Freeze ordering (the G0 pattern).** (1) `pipeline/select_routes.py` is
committed with this document — the formula freezes first. (2) The owner
downloads the 2024 T-100 file on an unblocked connection and commits its
SHA-256 to `data/phase1-inputs.md`. (3) The route list is computed by running
the script on the hashed file, and committed as the script's output. The route
list is an **output of the freeze**, not an input to it; G1 test GD re-executes
the script on the hashed input and must reproduce the identical panel.

**Selection rule (deterministic; full definition in `select_routes.py`).**
Route unit = undirected nonstop airport pair, both directions summed, all
carriers; selection statistic = 2024 T-100 segment passengers (scheduled
services); tie-break alphabetical on concatenated airport codes. **N = 18
routes**, stratified 6 per great-circle distance band (SHORT ≤ 750 mi;
MEDIUM > 750 and ≤ 1,500 mi; LONG > 1,500 mi — the boundaries as the
executable formula applies them, so no distance is unassigned). Algorithm: (i) top-3 pairs per band
unconditionally; (ii) walk national rank order, adding a pair to its unfilled
band iff it strictly reduces the total constraint deficit (units missing, as
defined in the script — unit-counting is what lets a carrier's first
qualifying route count as progress toward its 2-route minimum); (iii) fill
remaining band slots in pure rank order; (iv) if constraints remain unmet at
full bands, relax in the fixed order hub-span → carrier-coverage, each
relaxation logged in the script's audit output. Hub-span constraint: each band contains ≥ 1
hub-dominated route (top-carrier share ≥ 60%) and ≥ 1 competitive route
(≤ 40%), shares computed from the same hashed file.

**Carrier rule.** Frozen 8-carrier list: AA, DL, UA, WN, AS (incl. Hawaiian
post-merger — logged convention), B6, NK, F9 — the eight largest US marketing
carriers, all with standing `targets.tsv` fee pages; six of the eight carry
verified 2025–26 ledger events (NK and F9 have none yet — they are in the
panel for menu coverage, not because of past events). Cell rule:
carrier c is quoted on route r iff its 2024 segment share on r ≥ 5%, computed
after the pinned operating→marketing rollup for wholly-owned regionals
(`data/phase1-inputs.md`; multi-partner regionals are not rolled up — a
disclosed limitation). Each listed carrier must qualify on ≥ 2 panel routes
(a selection constraint). **Wave-0 schedule check (additions only; protocol
pinned):** at wave 0, for every (panel route × listed carrier) pair that is
not already a cell, the owner checks the carrier's own site for nonstop
service on the wave-0 grid dates — a one-time, exhaustive sweep of all such
pairs, not a discretionary sample. Any nonstop found → the cell is **added**,
logged `cell-added-schedule-check` in `data/phase1-inputs.md`'s amendment log,
with the search-results page saved and registered via `capture.py --manual` as
the evidence. Cells are never removed by the check — additions expand the
census, removals would be discretion — and G1 test GD verifies the operating
cell list as script output ∪ these logged additions. Expected panel size ≈
**45 carrier-route cells**; the script's actual output governs and the wave
prompts are sized to it.

**Southwest exception.** WN is owner-manual, carrier-direct capture only
(Kiwi.com permanent injunction, 2021; WS-G counsel rule; WN absent from most
metasearch). WN cells are capped at the **top 4 panel routes by 2024 WN
segment passengers** (ranked within the selected panel — the formula's
implementation; deterministic; excluded WN cells logged). WN's fee-schedule
series is fully covered by its own posted fee pages regardless.

**Channel harmonization.** All headline (H) quotes are carrier-direct on the
carrier's own site, logged out, US point of sale, cash menu (codebook §2.3).
**Metasearch is banned for both H and S**: S is the cross-carrier minimum over
the same carrier-direct captures per route, so H − S is a clean brand-switching
coping margin. A Google Flights cross-check price is recorded as a
non-evidentiary sanity field, excluded from H and S.

**Expected example routes** (labeled EXPECTED/ILLUSTRATIVE — the script output
overrides mechanically): LAX–LAS, ATL–MCO, LGA–ORD (short); DEN–ORD, FLL–LGA,
MCO–PHL (medium); JFK–LAX, ORD–SEA, LAS–EWR (long).

## 2. Booking grid

- **Wave day:** first Tuesday of each month (federal holiday → capture shifts
  to the next business day, flagged `grid_shift=holiday-waveday`; **the
  itinerary dates stay anchored to the scheduled first-Tuesday date**, so a
  shifted capture day never moves the travel window); all air cells captured
  12:00–20:00 owner local time. **Wave 1 = Tuesday 2026-10-06** (plan §9 item
  13). Wave 0 = September 2026 unpublished dry run (§6).
- **Itinerary (one per cell):** round trip, 1 adult, nonstop only, depart the
  Tuesday **21 days** after wave day, return the Tuesday **28 days** after
  (7 nights) — codebook §2.3's at-booking / prepaid-online / 3-week-advance
  convention, deliberately parallel to CPI's fixed trip specification so the
  spread is concept-clean.
- **Blackout rule.** Frozen windows, **inclusive of both endpoints**: Mon–Sun
  of Thanksgiving week; **Dec 18 – Jan 4**; **Jul 1 – 7**. If the departure or
  return Tuesday falls inside a window, iterate forward to the next Tuesday
  pair falling **wholly outside all windows**, flag `grid_shift=holiday`.
  Standing consequence, stated so no reader mistakes it: **the December link
  wave prices early-to-mid-January travel every year** (e.g., wave day Tue
  Dec 1, 2026 → depart Jan 5 / return Jan 12; wave day Tue Dec 7, 2027 →
  depart Jan 11 / return Jan 18). This is acceptable and disclosed for two
  reasons, each doing its own work: fee-schedule and tier-structure **events**
  enter the link by effective date regardless of travel dates; and the
  fare-level component of the in-sample link (regime (ii), §11) compares
  December waves that both price the same relative travel window under this
  same rule, so the January-travel offset is common to numerator and
  denominator rather than a distortion of either.
- B6/ULCC peak-calendar fee dates are captured and flagged, never dodged
  (codebook §2.3).
- **Per-cell capture:** the two lowest fare families (lowest Basic-family and
  lowest Main-family fare, same flight) + the at-booking ancillary vector:
  carry-on where sold; first/second checked bag **conditional on fare class**
  (the AA Basic +$5 precedent) and **by purchase point** — the prepaid-online
  variant enters the min, airport/gate variants are recorded (this resolves the
  $45-vs-$50 first-bag ambiguity by rule); cheapest advance standard seat
  (outbound); same-day-change terms verbatim.
- **Annual-link convention.** The December-to-December link is measured from
  December-wave menus; fee-schedule events enter by effective date per codebook
  §6 (Southwest bags → 2025 link; April-2026 wave, AA Basic surcharge, Netflix
  March-2026 step → 2026 link — unchanged). The 11 non-December waves supply
  T1 evidence, event detection, the transient screen, and descriptive
  dispersion; **they are never chained** (spec §2.5).

## 3. Profiles

Air profiles P1–P4 partition base-period buyers; shares are jointly bounded and
sum to 100%. Incidence primaries and grids are pinned in
`data/phase1-inputs.md`; provenance tags per `data/incidence-proxies.md`.

| ID | Attribute vector (codebook §2/§3 language) | Incidence source / tag |
|---|---|---|
| AIR-P1-CARRYON (flagship) | RT nonstop; 1 full-size carry-on **in cabin, no gate surrender**; personal item; 0 checked; no paid seat. Where a carrier strips the carry-on from its cheapest family (UA standing event), restoration is priced **only** via the same-flight tier spread, published **[0, gap]** with the point at the gap, superset-flagged. The gate-check path is excluded as a **wrong-attribute path regardless of price** (pre-registered attribute-level exclusion; closes the spec §4.1 S1 ambiguity). | **GAP** (`gap/structural-ceiling`): the [0%, 100%] utilization interval, with the labeled ~70–85% bin-capacity structural ceiling as an upper bound. The spec §4.1 assumption shares (55/30/15) appear **nowhere** in Phase 1. |
| AIR-P2-PERSONALITEM | RT nonstop; personal item only. The dominance profile: genuine decreases print here when a cheaper option weakly dominates (S2), while P1 prints 0. | Complement bound of P1; [0%, 100%]. The release cites G0's exactly-0.0000% zero-bag event contribution as the built-in avoidability control. |
| AIR-P3-ONEBAG | RT nonstop; carry-on + 1 checked bag (≤ standard size/weight; ≥10% threshold changes are separate attribute events); **named-fee route** (prepaid-online, fare-class-conditional). This is the **Southwest honesty-exhibit profile**: predicted Gap SMALL, because CPI's airfare quote includes the first checked bag on ~80% of designated quotes. A prediction-met print is a headline, never designed away. | `administrative-ratio/usable`: fee-payer ~16–19% of enplanements (BTS Sch. P-1.2 acct 3906.2 ÷ enplanements, blended-fee divisor stated); the ~34–39% check-rate shown alongside. Enplanement reconstructions replaced with official BTS prints before publication (owner task). |
| AIR-P4-TWOBAG | RT nonstop; carry-on + 2 checked; named-fee route. | `administrative-ratio-derived/usable-with-assumption`: bags-per-checker 1.4–1.6 derivation published; pre-registered fallback to [0%, 100%] if the discussant rules it below the codebook §8 bar. |
| AIR-ATTR (seat, same-day change) | Not standalone profiles in v1. Both dictionary attributes are recorded in every fare family's base vector at the Dec-2026 Ledger freeze and **priced every wave**, so T1 evidence exists the day any carrier strips them. | Seat: Senate PSI exhibits ($12.4B, 2018–23; DOT data cannot separate seat-fee revenue — Appendix A). Else [0%, 100%] if triggered. |
| STR-P1/P2/P3 | Cheapest ad-free plan — Netflix / Disney+ / Hulu; posted national monthly rate, no promo, no bundle; Netflix extra-member slot as a standing named-fee line item. | Netflix ~45% ad-tier households (Comscore, stock; household-vs-billing caveat); Disney+ 37% company Aug-2024 (Ampere 14% / survey ~20% as bounds); Hulu: **no seller-specific usable source — [0%, 100%] per the register's rule 1** (the Antenna market-wide 46% envelope is context only, `envelope/sanity`; a seller-specific usable figure upgrades it via a logged amendment). |
| BNK-P1-CHECKING-OD | Checking account + 1 overdraft incident at the posted standard fee + posted monthly maintenance fee; cash menu, no relationship pricing. | CFPB Data Spotlight 2024-04 (overdraft/NSF revenue −>50% 2019→2023, other fees flat) — `administrative/usable`. |
| GRO-P1-PERUNIT-BASKET | Fixed 12-item national-brand basket, frozen at UPC + net quantity (basket categories in §9; UPCs freeze at the Dec-2026 Ledger freeze); **divisible-good per-unit convention** (codebook §3): replication cost = current unit price × frozen base quantity. ≥10% size changes are also logged as attribute events. | n/a — CPI-priced null control; **monitored coverage only**, never restoration coverage. |

## 4. Paired-quote protocol

**Identification core.** The paired same-flight, same-session Basic/Main quote
identifies the tier gap g with route/date/demand scalar volatility differenced
out **to the extent the shock is common to both families on the flight** —
additively common components cancel in a same-flight, same-session contrast;
family-specific pricing shocks do not, which is why the gap is published as a
December-wave reading with the 11 other waves' dispersion shown alongside,
never dressed in census language it hasn't earned. Trigger rule T3's "net of
pure scalar moves" is operationalized
**with no deflator and no estimated decomposition**:

- **Named-fee events** are measured from posted fee schedules dated by
  effective date, with the base fare held fixed at the pre-registered
  denominator. Same-seller fare drift never enters the numerator — it flows
  through the CPI side of the Gap. (The retro harness's matched-fare netting
  was correct for a *retrospective with a known fare path*; for live
  fee-schedule events the fixed-denominator construction replaces it — netting
  live fare drift against the event would double-count scalar moves already on
  CPI's side of the spread.)
- **Tier-gap attributes** publish as [0, g] with the point at g,
  superset-flagged; a named fee caps the line item wherever both routes exist
  (codebook §5).

**Per cell:** (a) carrier-direct, logged-out search; (b) the grid itinerary;
(c) **pairing rule (sequential, leg-by-leg — executable on real round-trip
flows, which price per leg):** on the outbound results display, select the
nonstop with the lowest displayed Basic-family leg price, tie-break earliest
departure, and record BOTH families' displayed leg prices for that same flight
from that same display; then, on the return results display **as presented
after that outbound selection** (family combinability is conditional on the
outbound, so the return rule is deliberately sequential, not independent),
select the return nonstop by the same rule and record both families' displayed
leg prices the same way. Displayed leg prices are all-in under 14 CFR 399.84
and are recorded **verbatim, per leg**; the round-trip totals and the tier gap
(gap = Σ leg gaps) are computed **at ingestion, never by the agent**. Where a
site also displays a running trip total, it is recorded as a cross-check
field. If no Basic family is sold, record the single family per leg and flag
`pair=absent` (a menu fact, not a failure). (d) **in-flow ancillary step** for
NK/F9/B6 (WN manual): advance only to the bag/seat add-on page, record
at-booking prices, **abort before any passenger-details or payment field**.
AA/DL/UA/AS bag fees come from fee-schedule pages, verified by a rotating
**2-cell in-flow audit subsample** per wave — **rotation deterministic**: the
legacy cells ordered lexicographically by (carrier, route); wave w audits the
cells at positions (2w) mod N and (2w+1) mod N in that order. The wave
worksheet computes it; no per-wave discretion.

**Safety-rail carve-out (stated, never silent).** The frozen wave prompts
(`pipeline/wave-prompts.md`) explicitly permit: entering routes/dates into
public fare-search forms, clicking Search, selecting a flight, and opening
seat-map/bag displays. They forbid: login, credentials, any name/email/payment
entry, fare holds, and any purchase/reserve action — hard stop at the
passenger-information page. Blocked or sign-walled cells record
`loaded=blocked` and fall to the owner-manual path. WS-G counsel reviews the
carve-out and the WN manual protocol before the October go-live.

**Provenance ladder.** (1) `capture.py` static fee/policy pages, same day =
raw HTML + SHA-256 manifest, full archival weight. (2) Owner manual
Save-Page-As registered via `capture.py --manual` = full archival weight —
covers all WN cells, the rotating 2-cell audit, and **every link-entering
paired quote in the December wave** (+~1.5 h, December only), with full-page
saves of both the fare-selection and ancillary-disclosure pages for December
and audit cells. (3) Chrome-agent extractions = content-grade,
`browser-agent-extraction` tag, authoritative timestamp = git commit of the
ingested JSON. G1-GD's independent rerun of the flagship December gap statistic
therefore rests on hashed artifacts, not agent text.

**Whole-menu census obligation.** A carrier-route cell is not complete until
**every dictionary attribute** has either a recorded price/path or an explicit
no-priced-path entry feeding the Exclusion Register. "You only collected fee
increases" is false by construction: decreases and eliminations flow through
the identical diff (codebook §4 symmetry).

**Anti-promotion rule (split by price type; symmetric by construction).**
- **Schedule-posted fees** (AA/DL/UA/AS/WN named fees; the B6 schedule incl.
  its peak calendar): a single-wave level change of **either sign** without
  carrier documentation is logged pending-confirmation — dips as
  `suspected-promotion`, spikes as `suspected-error` — and held, not entered.
  The carrier's own hash-captured fee-schedule or contract-of-carriage page in
  that wave's static capture **counts as the corroborating document** (a
  genuine quiet decrease lands on the posted schedule; a session-only
  promotion does not — this is what keeps the rule symmetric rather than a
  one-way filter against decreases). **The annual link computes after the
  following January wave completes**, so a December-effective change gets its
  confirmation wave and still enters the link its effective date assigns it to
  (codebook §6); a level later disconfirmed as transient triggers a logged
  re-statement under the pre-committed correction protocol, never a silent
  edit.
- **Dynamic in-flow prices** (NK/F9/B6 ancillaries — the observation of
  record): no multi-wave screen applies, because dynamic prices ARE the menu.
  Instead the December observation of record is the **median of three
  same-day sessions** per ULCC cell in the December wave (fixed reconciliation
  rule, pre-registered; ~+30 min in December), which is what defuses a
  single-session A/B-test draw without operator judgment.

**Fare-family crosswalk (frozen; renames are label-reshuffle non-events unless
the attribute vector changes):** UA Basic Economy / Economy; AA Basic / Main
Cabin; DL Basic / Main; WN Basic / Choice (Choice Extra = the exempt
two-free-bag family, recorded as conditioning); AS Saver / Main; B6 Blue Basic /
Blue; NK Go (single cabin — `pair=not-applicable`, all attributes named-fee);
F9 Basic / Economy-bundle.

## 5. Fields recorded per quote

wave_id; capture_timestamp_utc; capture_channel (carrier-direct-agent |
carrier-direct-manual); provenance_grade (hash-archival | manual-registered |
browser-agent-extraction) + manifest_or_commit_ref; route; marketing_carrier;
outbound/return flight numbers (the pairing key); depart/return dates + times;
grid_shift_flag; peak_calendar_flag; fare_family_basic_name_verbatim;
fare_family_main_name_verbatim; fare-basis/brand codes if displayed;
basic_outbound_leg_usd; basic_return_leg_usd; main_outbound_leg_usd;
main_return_leg_usd (per-leg displayed all-in prices, verbatim, never rounded
— 14 CFR 399.84); displayed_trip_total_usd (cross-check field where a running
total is shown); total_fare_basic_rt_usd, total_fare_main_rt_usd and
tier_gap_rt_usd (all three computed at ingestion from the leg fields, never by
the agent); pair_status (paired-same-flight | pair=absent |
pair=not-applicable | basic-soldout | blocked);
carryon_price_at_booking_usd; first_bag_price_usd + source
(schedule-prepaid-online | in-flow | airport | gate | gated-behind-pax-info) +
fare_class_conditioning;
second_bag_price_usd + source + conditioning;
bag_size_weight_limits_verbatim (≥10% threshold-event detection);
cheapest_advance_standard_seat_outbound_usd; same_day_change_terms_verbatim;
membership_or_card_conditioning_notes (recorded, never in H);
google_flights_crosscheck_price (non-evidentiary); display_context_saved
(yes/no) + saved_file_sha256; promo_detected_flag + verbatim text; page_title +
url; loaded (yes | partial | blocked — blocked cells retained); missing_code
(§7); no_priced_path_entries (→ Exclusion Register feed); notes.

## 6. Monthly wave runbook and hours

- **Step 0 (T−1, sandbox):** auto-generated wave worksheet (routes × cells,
  travel dates with blackout iteration applied, WN manual list, deterministic
  audit rotation per §4) — owner review ~15 min. **Build note:** the worksheet
  generator and the Step-4 ingestion validator (schema + range checks for air,
  streaming, and grocery records — the record schemas are §5 and the Prompt
  B/C field lists) are sandbox deliverables **built and committed with wave-0
  prep (September 2026)**; wave 0 does not run without them.
- **Step 1:** `capture.py --sector air`, `--sector streaming` (+ `--sector
  banking` quarterly). Never run unfiltered (the needs-url pitfall). ~20 min
  incl. manifest inspection; failed urgent targets → documented `--manual`
  fallback.
- **Step 2:** Chrome-agent batch, three prompts (A: UA/AA/DL/AS ≈ 24 cells;
  B: NK/F9/B6 in-flow ≈ 17 cells; C: groceries ≈ 24 pages + streaming
  **fallback-only** — the streaming observation of record is Step 1's
  hash-grade `capture.py` snapshot, and Prompt C touches a streaming page only
  when Step 1 failed for it that wave, flagged), slug parity with
  `targets.tsv` enforced. **≈ 41 agent cells × 8 min ≈ 5.5 h** — the honest
  number, from the measured timing basis, stated rather than hoped down.
- **Step 3:** WN manual, 4 cells, Save-Page-As + `--manual` registration,
  ~45 min.
- **Step 4:** ingest to `data/captures/<topic>-<YYYY-MM-DD>.json` (`_capture`
  block: method, provenance_grade, gaps_and_follow_ups; git commit =
  authoritative timestamp); the schema/range validator fails loudly; ~30 min.
- **Step 5:** event triage — automated diff vs the prior wave (fees, crosswalk
  families, attribute vectors, bag size limits); any change drafts a ledger
  entry with T1/T2/T3 checks; decreases flow identically; unrestorable
  disappearances draft Exclusion Register entries; ~20 min.
- **Step 6:** snapshots + manifests to durable storage (snapshots gitignored;
  manifests are the hash-commitment record); ~5 min.
- **Mid-month:** one 60-min press watch (~15th); an effective-dated fee event
  triggers urgent capture within 7 days (the monthly static layer already
  guarantees ≤ 31-day detection).

**Honest totals, all steps counted:** air agent cells ~5.5 h + WN manual
~45 min + Prompt C ~40 min (grocery — running from the December 2026 wave,
since the basket's UPCs freeze at the December Ledger freeze, so the
October–November waves carry no grocery quotes; streaming only as a flagged
fallback) + the rotating audit's manual saves ~20 min + Steps 0/1/4/5/6
~1.5 h ≈ **8.4 h/wave at 18 routes from December 2026 (~7.8 h before the
grocery start); ~9.5 h/month with the press watch.** Above the
single-digit target's comfortable interior — which is exactly why: **wave 0
(September 2026) is an unpublished dry run** measuring per-cell timing and
validating prompts/QC/ingestion, and its wall-clock total (Step-0 start to
Step-6 end) is **logged in the wave-0 capture JSON and committed** — the
de-scope trigger reads that committed number, not operator recollection.
**De-scope order (pre-registered, fires BEFORE wave 1 if the committed wave-0
total exceeds 9.0 h; also fires after any two consecutive waves whose
committed totals exceed 9.0 h):** (1) shrink the audit subsample; (2) drop the
6th (lowest-ranked) route per band → 15 routes / ≈ 37 cells (~7 h/wave) —
**unless dropping a band's lowest-ranked route would push a carrier below its
2-route minimum, in which case drop the next-lowest-ranked route in that band
that does not; if none qualifies, that band keeps 6** (deterministic branch,
no judgment call). Shrinkage is pre-registered, not improvised.

**December extras (+3.5–4.5 h):** the link-wave manual-save upgrade; the
ULCC median-of-three-sessions capture (§4, ~30 min); the annual
Ledger re-freeze from attribute records (no superset ratchet, no forgiveness
drift — codebook §7); incidence refresh; the chained-vs-direct drift
diagnostic; the transient screen on the December min; concordance /
exclusive-partition update. A backup window is pre-scheduled for the second
Tuesday of December.

**QC checklist:** QC-1 cell completeness with missing codes; QC-2 Basic ≤ Main
on every valid pair (violation → MISS/PAIR-BROKEN, one re-check); QC-3 all-in
totals present (399.84); QC-4 fee diffs → event workflow; QC-5 every manual
save has sha256 + file; QC-6 B6 peak flag present; QC-7 rotating
one-carrier-per-month display-context capture (dates a DOT
fee-display-prominence break if the NPRM lands mid-panel); QC-8 no
membership/card price in any headline field; QC-9 whole-menu census satisfied
per cell. **A wave is complete when every check is green OR every red item
carries a missing code — an unflagged hole is the only failure state.**

## 7. Missingness and degradation rules

Codes: **MISS/BLOCKED, MISS/SOLDOUT, MISS/NO-BASIC** (data, not a miss),
**MISS/SITE-ERR, MISS/PAIR-BROKEN, MISS/SKIPPED.**

1. A missing monthly cell flags and stays empty — no imputation, no
   interpolation; stale displays carry `stale=n` and never enter a link.
2. **December-wave miss ladder:** retry within Dec 1–15 → nearest wave within
   ±45 days flagged `link-substitute` → named-fee cap where one exists →
   Exclusion Register for the link with in-stratum weight reallocation (never
   reservation-price imputation).
3. Up to **2 whole non-December waves per year** may be missed (flagged) with
   zero effect on the published link; December is mandatory, with the retry
   window and the pre-scheduled backup Tuesday.
4. A carrier blocked ≥ 3 consecutive waves triggers the **ATPCO/ARC licensing
   decision** (WS-G obtains quotes during Phase 1) and a collection-risk
   disclosure. A channel switch is a logged structural break, never a silent
   splice (spec §9.2). Static fallbacks stay live regardless: jetblue.com/legal/fees
   carries the named schedule + peak calendar; NK/F9 static pages evidence
   schedule structure for event detection (in-flow prices remain the
   observation of record); legacy fee pages still price P3/P4 named fees when
   only the tier gap and seat map are lost.

**Single-operator dependency is structural and disclosed:** every wave, the
December link, and all owner-machine pulls run through one person; the backup
window, the ±45-day ladder, and the 2-skippable-waves allowance are the only
hedges. There is no backup operator, and this pre-registration says so.

## 8. Streaming sidecar

Sellers frozen = Netflix, Disney+, Hulu (the standing `targets.tsv` set;
additions append-only). Streaming attribute dictionary v1 freezes with this
document: ad-free playback; out-of-household member slot; concurrent-stream /
resolution tier; posted national monthly price, no promo, no bundle.
Collection is fully archival, and **the `capture.py` hash-grade snapshot is
the observation of record**: the four standing pages each wave (~15 min inside
Step 1), plus Wayback timestamped URLs as third-party-attestable corroboration
(legitimate for streaming HTML; banned for airline JS pages). Prompt C's
streaming section is a flagged fallback for a failed Step-1 target only —
never a second, competing reading of the same menu.
Posted national prices make the **2025→2026 link exact**; the Netflix
March-2026 step is pre-assigned to the 2026 link (codebook §6). **Disney+
2025-10-21 step ruling (frozen):** it enters the 2025 link as a **scalar move
on an unchanged menu** (matched-model relative; P1 neutrality); the widened
ad-free-minus-ads spread updates the attribute-level tier-spread series without
double-counting; the 2022 launch event stays retrospective-exhibit-only. CPI
concordance: the cable/satellite/live-streaming stratum, with the `bridge=oct2025`
convention where a window spans October 2025.

## 9. Groceries control (the G1 null)

A 12-item national-brand basket in GAO-flagged downsizing-prone categories —
cereal, chips, paper towels, bath tissue, ground coffee, ice cream, orange
juice, laundry detergent, candy multipack, granola bars, dish soap, cookies —
frozen at UPC + net quantity at the December 2026 Ledger freeze; 2 retailers
(walmart.com, target.com), one pre-registered ZIP (a labeled convention, not a
representativeness claim); logged out; **list price only** — member prices
recorded as conditioning, never headline (the T-Mobile AutoPay lesson).
Pricing: the divisible-good per-unit convention (codebook §3).

**Conservative-tilt framing, stated up front:** the basket is deliberately
tilted toward documented downsizing-prone categories — biased *toward* finding
a gap — so a ≈ 0 print is affirmative evidence the method does not manufacture
inflation. Comparator: two-stage per the plan (CPI food-at-home per-unit series
available at print time; full R-CPI-SC reconciliation as an addendum when the
covering vintage ships). Live-window honesty: at Q1 2027 the panel spans
~3 months; the print labels the window length and shows the GAO archival
reconciliation — no annualization of a quarter-length window. **The numeric
pass band appears nowhere in this document — `docs/g1-band.md` is its first
and only existence.** Collection: 24 quotes/wave inside prompt C (~40 min),
**starting with the December 2026 wave** (no UPCs exist to quote before the
freeze); rotating 2-page full-save audit via `--manual`; targets rows added at
the December UPC freeze.

## 10. Banking control (the G1 negative)

**The test object is the archival series** (disclosed: no 2025/26-dated banking
ledger event exists): the 2019 → latest replication cost of BNK-P1 across the
**top-5 US retail depositories by domestic deposits, FDIC Summary of Deposits
June-2025 vintage, file hash-committed by the owner before computation**
(expected: Chase, Bank of America, Wells Fargo, Citi, U.S. Bank — the binding
list is the formula's output). Evidence: the banks' own posted fee schedules
(Wayback legitimate here) + the CFPB Data Spotlight. The documented
eliminations and reductions are named-fee decreases that enter through
codebook §4's symmetric event grammar, so the series is **expected** to print
negative — but GC is a real test, not a staged one: if maintenance-fee
increases at the top-5 outweigh the overdraft declines over the window, the
blend prints positive, GC fails, and that is reported (the gate is allowed to
bite here as everywhere). Forward
series: quarterly `capture.py` on the five banks' fee pages; a flat 2026 live
link printing 0.0 is a correct zero. Coverage arithmetic: excluded from both
coverage denominators (not a CEX line item; the nearest CE row is disclosed as
context only). Effort: ~8 h one-time archival build; ~1 h/quarter standing.

## 11. Q1 2027 archival-denominator exhibit

Bounded by plan P10 (versioned research note + DOI + public code + snapshot
archive under documented access rules; no composite before G3; no news-cycle
timing). Title block: **"archival-denominator exhibit,"** and the header
sentence: *"the panel's first fully in-sample annual air link is the 2027 link
(December 2026 → December 2027), measured from the December 2027 wave; the
panel attains 12 months of live coverage in October 2027."*

**(A) Air events (all `verified-preprint` in `data/ledger-events.json`):**

- **2025 link:** `air-southwest-202505` (first/second bag $35/$45 eff.
  2025-05-28; named fee, no superset flag) — printed WITH the Southwest honesty
  exhibit as a **prediction-met headline**: CPI's airfare quote includes the
  first checked bag on ~80% of designated quotes, so the predicted Gap on this
  event is small, and the exhibit says so before the number does.
- **2026 link:** `air-wave-202604` (UA 4/3 $45/$50; DL 4/8 $45/$55; AA 4/9
  $45/$55 prepaid, $50/$60 airport; AS/HA 4/10 $45/$55; B6 3/31 peak/off-peak
  $39–49/$59–69, priced date-matched); `air-american-202605` (Basic +$5/bag —
  the pure tiering observable, eff. 2026-05-18); `air-southwest-202604`
  (+$10/bag, 2026-04-09); `air-united-standing` (carry-on) as the
  superset-flagged interval [0, tier gap] with the point at the gap — the gap
  statistic is the **December-2026-wave passenger-weighted median of
  within-flight Basic/Main spreads**, weights = 2024 T-100 route passengers
  from the hash-committed selection file (carrier cells within a route
  weighted by rolled 2024 carrier-route passengers — no other vintage, no
  discretion; the panel's first in-sample quarter supplies the gap statistic
  only, never a denominator). Third-party spread surveys (e.g., NerdWallet)
  appear only as survey-grade context.

**Denominator convention (pinned in `data/phase1-inputs.md` BEFORE any exhibit
computation):** the elementary denominator per event = the route-average
one-way base fare for the event carrier on the panel routes, from the O&D
product covering the last full quarter preceding the effective date.
**Per-event single-product rule: no DB1B/DB1C splicing within any single
event's denominator window** — DB1B supplies windows through 2025Q2, DB1C/OD40
from July 2025; the product used prints as a column. DB1C limitations (Total
Amount excludes ancillaries; no Basic Economy identifier) print as publication
material — they are the documented reason primary quote collection exists.
**Sensitivity bands (pre-registered grid; all cells shown; out-of-band corners
disclosed — the G0 pattern):** denominator ∈ {pre-event quarter, same quarter
prior year, carrier-route vs panel-pooled} × the G0-style fare-anchor grid
($250–$400) × incidence ∈ {primary proxy, stated bounds} × a DB1B/DB1C
cross-product check where windows overlap. **T3 attribution:** event relative =
named fee at effective date ÷ the fixed archival denominator; same-seller fare
drift never enters the numerator.

**Archival-regime Gap composition (pinned; mirrored in
`data/phase1-inputs.md` §7; MAY NOT change after sign-off).** The published
per-event object is the **incidence-weighted event contribution**

> EC = incidence × (Δfee per segment × profile segments) ÷ (2 × route-average
> one-way base fare),

which is a Gap **over the matched-carrier scalar-fare comparator** — the same
object, same wording, as G0's G_air ("over the matched-fare comparator"). It
is **never inserted into codebook §9's Σw[ρ − π^CPI] as-is**: same-seller fare
drift is excluded from the RX-side numerator by construction, so subtracting a
full CPI airfare relative from it would be double-counting on one side and
nonsense on the other; every exhibit table labels its comparator on the row.
The CPI-side treatment is pre-registered per attribute component: where the
attribute sits inside CPI's airfare quote specification (the first checked bag
on ~80% of designated quotes), the exhibit publishes **both** EC-gross and the
**predicted residual Gap = EC-gross × (1 − CPI capture share)**, with the
capture share sourced and labeled — this is the Southwest honesty-exhibit
machinery generalized, and it is a prediction published before the comparison,
not a tuning knob. Worked number (executable — `engine/test_phase1.py`): Δfee
= $10/segment on a 2-segment round trip, denominator $325 one-way, incidence
17% ⇒ event relative for the checking profile = 20/650 = **+3.08%**, sector
contribution = **+0.52pp** gross, predicted residual Gap at an 80% capture
share = **+0.10pp**. No composite index is formed from these contributions
before Gate G3 (plan P10).

**Denominator handoff (all three regimes
pinned now):** (i) this archival convention; (ii) from the 2027 link (Dec 2026
→ Dec 2027, the first fully in-sample annual link) onward, each cell's t−1
December-wave posted all-in fare at the fixed booking point — for each
profile, the t−1 fare of the **fare family that prices the profile's
replication** (Main-family for carry-on profiles, cheapest family + named fees
for bag profiles), with t−1 named fees included in the profile's t−1
replication cost exactly as codebook §1 defines C(z; t−1); (iii) the first
in-sample release computes the link under BOTH conventions side-by-side as the
published splice diagnostic — expected direction stated now: the archival
convention's scalar denominators are route-average (all-family) fares, so it
mechanically prints **smaller** event relatives than the paired-panel
convention on cheapest-family-anchored profiles — after which the archival
convention retires.

**(B) Streaming:** the exact 2025→2026 link; the 2025-link Disney+ scalar step;
the 2022–2025 ladder as a caveated retrospective memo. **(C) Controls:** the
grocery null (print-time comparator; R-CPI-SC addendum pending) and the
banking series — expected negative on the documented fee declines (§10; GC is
a real test and is allowed to fail). **(D) Apparatus:** both
coverage numbers (restoration-priced ≈ 2%; monitored ≈ 12%; controls
segregated); the two-way Gap decomposition per sector + democratic-weight
sensitivity; the CPI-stratum concordance + exclusive-partition table; H and S
with the H − S coping margin; min-cost AND standalone-fee series per attribute;
Inclusion Ledger line items + the Exclusion Register (counts + affected base
expenditure); the standing reconciliation vs CPI-U / C-CPI-U / R-CPI-SC with
`vintage=` tags and `bridge=oct2025` flags; weights from the pinned Dec-2024
R-CPI-I recipe on published CE bottom-two-quintile tables (airfare-within-
public-transportation and streaming-within-entertainment sub-allocations
documented from the August Table 1101 pull; 2025-vintage shutdown footnotes);
Assumption Q verbatim; upper-bound language and the spec §12 limitations
abridged; the flat-average-fare concession (the claim is distributional and
experience-constant, never average-spend). The six-attacks-to-design-features
table ships as a standing methods appendix, citing G0's 0.0000% zero-bag
contribution as the built-in avoidability control.

## 12. G1 evaluation

The pass criteria — tests GA (discussant), GB (grocery null, two-stage),
GC (banking negative, sign-only), GD (independent rerun with disclosure
parity) — live in `docs/g1-band.md`, committed before this document. Failure
handling is fixed there: fix-inputs-then-rerun once; a second miss fails the
gate and a methods note publishes instead of the release.

## 13. Worked example (executable)

The paired-quote identification in one number, pinned by
`engine/test_phase1.py` (run: `python3 -m unittest discover engine`):

Base December wave: Basic $200 (no carry-on), Main $260 (carry-on included),
same flight — tier gap **$60**. Next December wave: Basic $240 (+20%), Main
$290 (+11.5%) — the tier gap **narrowed to $50**. For AIR-P1-CARRYON:
ρ = 290/260 = **+11.5%**, a scalar fare move that also sits in the CPI
comparator side of the Gap; the menu-structure component — the tier gap —
moved **down**, and the published attribute interval [0, g] tightens with
today's menu baseline (trigger rule T3; the interval is baselined on the
current wave's non-superset floor, never on base-period cost). A naive
fee-tracker reads "Basic +20%"; the paired design reads "menu structure
improved while fares rose" — the Gap over the matched CPI series, not the raw
relative, is the publication object.

## 14. Freeze and amendment mechanics (the G0 pattern, copied exactly)

1. **Commit ordering:** `docs/g1-band.md` first (its git hash is the timestamp
   of record) → this pre-registration + `pipeline/select_routes.py` →
   `data/phase1-inputs.md` (pinned inputs; the T-100 SHA-256 lands there on the
   owner's pull) → the computed route list → results. Band, then inputs, then
   results — never another order.
2. **MAY / MAY NOT after owner sign-off:** inputs (dates, amounts, vintages,
   URLs) MAY be corrected with every change logged in the amendment log below.
   The panel formula (`select_routes.py`), N and the stratification, the
   carrier list and cell rule, the booking grid and blackout windows, the
   profile definitions, the pairing rule, the denominator conventions, the
   archival-regime Gap composition, and the handoff, the anti-promotion and
   missingness rules, and the de-scope order MAY NOT change after sign-off;
   any post-hoc case for changing them is a logged design failure with a
   methods note, never a quiet re-draw.
3. This document freezes publicly with the Phase 0 note (October 2026);
   amendments are append-only thereafter; no retroactive convention change
   ever applies to a published link.
4. Owner sign-off gates collection: wave 0 may not run before the checkbox
   below is checked.

## Amendment log

- 2026-07-06 (pre-sign-off, from the adversarial review of the draft package —
  46 confirmed findings across 5 review lenses; no in-scope computation has
  run, so nothing could be tuned to a result). The load-bearing corrections:
  (1) all "October 2027 link" language restated to the 2027 link (Dec 2026 →
  Dec 2027, December-wave-measured) — no October link exists under codebook
  §6; (2) the archival-regime Gap composition pinned explicitly (§11): EC over
  the matched-carrier scalar-fare comparator, never inserted into codebook
  §9's Σw[ρ − π^CPI], with the predicted-residual-Gap machinery and an
  executable worked number; (3) the anti-promotion rule split by price type
  and made symmetric (schedule-posted: either-sign single-wave changes held
  pending confirmation, link computes after the January wave; dynamic in-flow:
  December = median of three same-day sessions); (4) the pairing rule
  rewritten sequential leg-by-leg with per-leg verbatim fields (round-trip
  flows price per leg; totals computed at ingestion); (5) hours restated with
  every step counted (~8.4 h/wave from Dec 2026), the de-scope trigger moved
  to a committed wave-0 wall-clock reading vs 9.0 h, and its tie-branch made
  deterministic; (6) wave-0 schedule-check protocol pinned (exhaustive,
  additions-only, evidence-registered, GD-verifiable); (7) streaming
  observation of record = the hash-grade capture.py snapshot, Prompt C
  fallback-only; (8) Hulu incidence to [0%,100%] per the register's rule 1;
  (9) blackout windows endpoint-inclusive with worked date traces; the
  identification-language, banking-expectation, carrier-list-justification,
  audit-rotation, band-boundary, and example-route corrections. Companion
  fixes landed in g1-band.md (its own log), phase1-inputs.md, the incidence
  register, select_routes.py (+6 tests), wave-prompts.md, capture.py, and the
  plan (v00.03.08).

## Sign-off

- [ ] Owner reviewed and accepted the Phase 1 pre-registration as-is —
      YYYY-MM-DD
