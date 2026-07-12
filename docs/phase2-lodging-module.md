# Phase 2 lodging module — attribute dictionary, fixed property panel, and the post-FTC compression falsification test

`v0 · 2026-07-12 · workstreams D/E (sector module; the compression test is a WS-E falsification deliverable, plan §3; collection hooks in B; counsel scope in G) · STATUS: DRAFT — design only, nothing in this document is frozen; the binding freeze is the Phase 2 pre-registration + a dedicated band file (§8), committed band-first before any collection enters a published link or any test verdict is computed. No numeric pass-band limit appears anywhere in this document, by rule.`

This document is the executable design for the third and smallest Phase 2
module: **lodging on out-of-town trips** — Q1 $166/yr (0.5%), Q2 $338/yr
(0.7%) of bottom-two-quintile budgets (plan §1, 2023 vintage; B40 restated
$274/yr under the flagged 2023-share convention,
`data/coverage-restatement-2026-07-12.md`), against the comparator stratum's
byte-grade **0.589% true-B40 CPI-basket weight**
(`data/captures/b40-weights-joined-2026-07-12.json`; **CPI-U 1.049% /
CPI-W 0.661%**, `data/captures/cpi-relative-importance-2026-07-12.json`,
byte-grade — the tier map is cited for the R-active classification and the
fee-menu rationale only, never for a weight: its lodging figure sits in a
declared-mock B40 column). The module is deliberately not a coverage
workhorse. It exists for one reason, pre-committed in three binding places
(spec data table: *"treat May 12, 2025 as a structural break; falsifiable
prediction: the lodging seam should compress post-rule — publish the
test"*; plan §4 Phase 2: *"lodging (post-FTC compression test as a
falsification exhibit)"*; plan §7: *"lodging Gap compresses after May 12,
2025 (if the seam is real, the FTC rule should shrink it — a prediction
that can fail in public)"*): **it is the project's falsification
instrument.** The FTC's all-in pricing rule (16 CFR 464, effective
**2025-05-12**; spec §"prior-art" row — the rule is *data infrastructure*:
all-in lodging/ticket prices observable since 5/12/25) forced resort and
junk fees into displayed lodging prices. If the project's seam —
drip-priced mandatory fees opening a wedge between advertised prices and
the cost of the experience as purchased — is real, forced posting should
close it here, in public, on a schedule the project did not choose. If the
wedge does not close, the seam story weakens, and the release prints that.

Posture, restated because every artifact must: the measure is an **upper
bound published only as a spread** over the matching CPI series; it makes no
"true inflation" claim, in this document or anywhere; negative and zero
prints are features — this module's *headline prediction is its own
near-null*, the Southwest-honesty pattern made structural; every public
number carries a provenance tag; the panel is a **census of posted menus at
named properties**, not a sample — no standard errors are claimed anywhere
in this module. Single-operator dependency is structural and disclosed (§7).

Companion binding files **at freeze, none of which exists yet** (§8 fixes the
ordering): `docs/phase2-lodging-band.md` (pass criteria — committed first;
**the compression test's pass/fail limits live there and only there**, the
first-existence rule), the Phase 2 pre-registration (frozen successor of this
draft, shared with the rent and wireless modules or module-dedicated —
open item 2), `pipeline/select_lodging_panel.py` (the panel formula as
executable code), `data/phase2-lodging-inputs.md` (pinned inputs, including
the airport→CBSA crosswalk and the seam-concentration market list, §2.2).
Companion files that exist: `docs/codebook-v0.md` (§2 equivalence, §4
triggers, §5 route hierarchy, §6 link years, §7 re-freeze, §8 incidence),
`pipeline/targets.tsv` (whose lodging/rental comment block already says the
fixed unit sample is pending), and the sibling modules
`docs/phase2-rent-module.md` / `docs/phase2-wireless-module.md`, whose
conventions this document inherits by name rather than re-deriving.

---

## 0. What this module measures, and what it deliberately does not

**Facts the design rests on (spec + plan, verified there; rule-mechanics
details flagged).** The FTC rule effective 2025-05-12 requires businesses
offering live-event tickets and short-term lodging to display a total price
inclusive of all mandatory fees; the spec's own characterization is that
all-in lodging prices are *observable going forward* while the backward
series is *broken* — pre-rule displayed prices excluded mandatory
resort/destination fees at many sellers, and no archive reconstructs the
posted-total series across the break. Rule mechanics beyond that sentence —
the treatment of government taxes, the itemization-before-payment
requirement, whether OTA and metasearch displays are directly covered —
are stated in this document from training knowledge and are
**[owner-verify: read 16 CFR 464 as published; the design's LDG-A1 boundary
must quote the rule's own total-price definition at freeze — the
W_covered/W_boundary split (§3.2) keys on that quoted definition]**. The
named fees themselves did not disappear: a resort/destination/amenity fee
persists as a line item *inside* the displayed total, which is exactly what
makes the module's event grammar workable post-rule.

**The target concept.** The module prices, per panel property (§2) and
frozen room configuration, the **all-in replication cost of one frozen
room-night**, built from three named components the decomposition (§4.3)
keeps separate because they mean different things: (i) the displayed total
for the frozen room and stay grid; (ii) any **seller-mandatory** charge
posted or revealed *outside* the displayed total (a rule-boundary leak,
LD-4 — the compression test's object); and (iii) the **profile-activated
named fees** a profile's attribute vector adds (parking for the car
profile — optional on the seller's menu, required by the profile, and
therefore never called "mandatory" in this document). It publishes the
12-month December-to-December relative of that cost **only as a spread**
over the CPI **"Other lodging away from home including hotels and motels"**
stratum relative (§4), decomposed so the three components cannot masquerade
as one another.

**"Mandatory," defined — the load-bearing term, defined the way the rent
module defines its stack (rent §1, adapted) rather than left to wave-day
judgment, because mandatory-vs-optional is exactly what sellers game
post-rule (conditionally waived fees, "resort credits" netted against a
fee, online-booking-only fees):** a charge is **seller-mandatory** iff it
is required of every guest, at every posted rate, to acquire the frozen
room-night at the stay grid, as posted or as revealed in the quote flow;
the evidence of the boundary is the itemization page plus the property's
own fee page where one exists. Edge cases are ruled at that boundary at
ingestion, verbatim-recorded either way. Optional add-ons are menu context
— never in T_mand (§3.2), and in C only where a profile's attribute vector
activates them as component (iii). Throughout this document "mandatory,"
applied to a charge, means seller-mandatory and nothing else.

**What routes to the Exclusion Register instead of the index:** unpriced
degradation — housekeeping-frequency cuts (already named on the public
Register page), amenity closures and hour reductions inside an unchanged
resort fee (a standing exhibit: the fee's own stated justification is the
amenity bundle, so a fee that persists while the pool closes is counted,
loudly, even though no menu path prices it), shuttle discontinuations,
early check-in where no posted price exists. **Out of scope entirely:**
government occupancy taxes (not a seller menu item; recorded separately,
never in C); loyalty-member, AAA/AARP, and mobile-app rates (conditioning
under the cash-menu rule, codebook §2.3 — the T-Mobile AutoPay lesson;
headline = unconditioned posted rate); short-term-rental platforms (Airbnb/
Vrbo) in v1 — different seller grammar, a disclosed coverage limitation and
a v2 candidate, not a hidden one; and **sellers with no bookable direct
channel** (phone-only or walk-in-only budget properties — plausibly a
segment where B40 stays concentrate) fall outside the §2.2 qualification, a
disclosed coverage exclusion of the same kind, restated with the comparator
(§4.2).

---

## 1. Attribute dictionary v1 — lodging (draft-for-freeze; codebook §3 style)

Binding once frozen (§8); ex ante; no attribute may be added retroactively
to an already-frozen base (codebook §1). Kept deliberately short: this
module is a falsification instrument, and every attribute below either
carries the test or is a named fee the tier map already documents as
contractible (tier-map row: resort/destination fees, parking, breakfast
inclusion, cancellation-tier deltas).

| ID | Attribute | Definition (equivalence, codebook §2 register) | Priced route in v1 |
|---|---|---|---|
| LDG-A1 | **Displayed-total-price entitlement** | Acquisition of the frozen room-night at a first-displayed price that includes every seller-mandatory charge (the post-2025-05-12 entitlement, created by the rule and therefore frozen into every base from the December 2026 base onward). Degradation event = any seller-mandatory charge posted or revealed outside the displayed total (LD-4: a rule-boundary leak). This attribute IS the compression test's event grammar. | Named fee (net ΔT_mand per LD-4's mirror), verbatim-recorded |
| LDG-A2 | Resort / destination / amenity fee (in-display line item) | The named mandatory fee as itemized, amount + name verbatim, recorded every wave **even while inside the displayed total** — in-display movement is composition, not an event (LD-1), but its persistence, amount, and the amenity bundle it claims to fund are findings and feed the Register cross-check. | Recorded; enters C via the displayed total |
| LDG-A3 | Parking (one vehicle, overnight, on-site) | One on-site overnight parking entitlement at the base's basis. **Ruled ex ante against the codebook §2.1 surrender precedent rather than around it:** the frozen entitlement is overnight on-site vehicle *storage with the vehicle available at departure* — access-on-demand mid-stay is not part of the frozen entitlement — so valet-only replacement of a base self-park entitlement weakly dominates and is admissible, key surrender notwithstanding. That is the opposite call from the gate-checked-bag rule (where surrender of possession defeats equivalence for a bag needed *in transit*), and the distinction is stated here as a design ruling so no wave decides it ad hoc. Off-site lots do not restore an on-site entitlement — wrong attribute regardless of price. Active in LDG-P2 only; a profile-activated named fee (§0 component iii), never "mandatory." | Named fee; else tier spread [0, gap], superset-flagged |
| LDG-A4 | Early check-in / late checkout | Recorded attributes; priced only where a named fee or posted option exists. **Expected-MISS at most properties most waves** (typically unposted, day-of, discretionary) — recorded, Register-routed where unpriced, stated now so the MISS pattern is a design fact, not a surprise. | Named fee where posted; else Register |
| LDG-A5 | Breakfast included | Documented base inclusion (T1 from the frozen snapshot) of breakfast in the frozen rate. Loss prices via the named breakfast add-on where posted, else the rate-class-with-breakfast tier spread [0, gap], superset-flagged; else Register. | Named fee / tier spread |
| LDG-A6 | Cancellation class | The frozen rate's cancellation basis (free-cancellation-by-date vs prepaid/nonrefundable — the tier map's "cancellation-tier delta"). Replication must weakly dominate: a refundable rate restores a frozen refundable entitlement; a prepaid rate does not, whatever it costs. The refundable–prepaid spread is the tier delta where the frozen class disappears. | Tier spread [0, gap], superset-flagged |
| LDG-A7 | In-room wifi | Included connectivity without a separate mandatory line item (historically the resort fee's flagship justification). A new standalone mandatory wifi fee is an unbundling event; the named fee prices it. | Named fee |

**Worked rulings (binding at freeze, decided now so no wave decides them ad hoc):**

- **LD-1 (in-display composition non-event — the RD-2 analog).** A resort
  fee raised inside a constant all-in displayed total (room rate down, fee
  up) is a **non-event** (codebook §4 relabeling at constant all-in
  replication cost): ρ moves ≈ 0 even as both components move. The rule
  itself is expected to force fee-folding at some sellers, and the module
  must print ≈ 0 on a pure folding — test GL-D (§8) proves the module
  passes its own non-event rule; the tolerance lives in the band file.
- **LD-2 (channel and seller-identity ruling — one test, stated once).**
  **The seller is the named property.** The brand booking engine is that
  property's *posting channel*, not a seller in its own right; codebook
  §2.2's billing-unified brand-family rule is **not invoked** — franchised
  lodging is not billing-unified (the merchant on a brand.com booking is
  typically the individual property), so no brand-family clause is granted
  and cross-property replication within a brand family is out, full stop.
  **The posted menu of record is the direct channel** — the property's own
  page on its brand booking engine: same-seller replication means buying
  from the seller, and the direct channel is the seller's own posting.
  Merchant-of-record variation in the payment flow (an "Expedia
  Collect"-style booking makes the OTA the merchant) does not move the menu
  of record: the ruling keys on *whose posting it is*, not on who processes
  payment. OTA displays (Expedia, Booking.com) are a *different seller's
  presentation of the same inventory*: recorded as corroboration, conflict
  detection, and compression-test context (whether the rule binds OTA
  displays directly is a rule-boundary question [owner-verify]), **never
  H**. Asymmetries disclosed now: the pre-period archival evidence (§3) is
  mostly OTA-side, so the pre/post exhibit compares OTA-display wedges
  pre-rule against both channels post-rule, with the channel printed on
  every exhibit row — the rent module's §3.4 form-confound pattern,
  transplanted — and the property-composition confound is disclosed
  alongside it (§3.3).
- **LD-3 (conditioning).** Member/loyalty rates, AAA/AARP, mobile-app and
  package rates are conditioning, recorded and never headline (cash-menu
  rule). Promotional strikethrough rates follow the RD-3 pattern: face
  posted rate is the H series.
- **LD-4 (boundary leak — with its observability boundary and its
  non-event mirror, both stated now).** A seller-mandatory charge posted or
  revealed outside the first-displayed total (a mandatory "service
  charge," an energy surcharge, a newly mandatory amenity charge) is an
  **LDG-A1 degradation event**: named-fee priced, ledger-drafted with
  T1/T2/T3 checks, **and a compression-test exhibit row in its own right**
  — leaks are the mechanism by which the seam would relocate rather than
  close (§3.3, outcome iii). **The mirror (the LD-1 analog, so no double
  counting):** C already includes outside-display seller-mandatory charges
  by definition (§0), so a fee *relocating* outside the display at constant
  T_mand fails trigger T3 (replication cost unchanged) and prints ρ ≈ 0 —
  a wedge/exhibit fact, not an index event; a leak is an index event only
  insofar as ΔT_mand > 0, and the priced amount is the **net change in
  T_mand, never the leaked line item gross**. **Observability boundary
  (disclosed, because a falsification instrument may not carry an
  undisclosed blind spot on its own failure state):** leaks observable
  in-protocol are those visible between the first display and the itemized
  pre-payment total, plus grade-1 fee-policy-page disclosures; charges
  collected at the desk or revealed after the payment step are **outside
  the instrument** — the agent never books, pays, or stays (§2.3 rails).
  Desk-collected and post-payment charges route to the
  enforcement-record/press watch and the Exclusion Register, with
  third-party documentation as the correction path (the rent module's
  A-R-style completeness vocabulary); a small owner-stay realized-side
  audit is a pre-registration decision item (§9 item 11, WS-H budget
  line). §3.3–§3.4 condition the test's leak clauses on this observable
  surface.
- **LD-5 (the wedge is within-quote; the link is on the grid).** The
  compression statistic W (§3.2) is computed *within* a single quote —
  displayed vs itemized-total for the same room, date, seller — so it is
  robust to the stay-date grid by construction. The December-to-December
  link, by contrast, uses the fixed grid (§2.3) on both sides, exactly as
  the air panel prices a fixed travel window.
- **LD-6 (flag change / rebrand).** A property changing brand family or
  leaving its booking engine is an identity/posting-channel break **at the
  same property**: MISS/FLAG-CHANGE, logged structural break, never a
  silent splice; base re-freezes at the next December (spec §9.2).

### 1.2 Profiles (partition of in-scope hotel-staying trips)

| ID | Attribute vector | Incidence source / tag (details §5) |
|---|---|---|
| LDG-P1-NOCAR (flagship) | One frozen room-night at the panel property: LDG-A1, A2, A4–A7 active; **A3 inactive** (parking is exactly what P2 adds). Replication cost = displayed total (frozen room, frozen cancellation class, stay grid) + any LD-4 leaked seller-mandatory charge. | (1 − c) |
| LDG-P2-CAR | P1 + one on-site overnight parking entitlement (LDG-A3 active — a profile-activated named fee, §0 component iii, not a seller-mandatory charge). | c = car-on-trip share among hotel stays — [owner-verify: NHTS long-distance / CE trip detail]; **[0%, 100%]** until a usable source lands (codebook §8 rule) |

Exact partition: P1 = (1 − c), P2 = c; shares sum to 100% of in-scope
hotel-staying trips by construction and are the Young-mean aggregation
weights (codebook §9). The P0 phantom-loss control is inherited: a base
stay that never included breakfast or parking prints 0 on those line items.
Hotel-stay incidence among B40 households (h) is **not** a profile
parameter; it is the module's coverage disclosure (§5).

---

## 2. The fixed property panel

### 2.1 Unit of observation

Per panel property, freeze: the seller (the named property, LD-2), one
**frozen room configuration** — the cheapest 2-adult **standard** room type
by lowest displayed total at the §2.2 freeze snapshot (**standard, pinned
by keyword exclusion:** room types whose posted names carry
suite/apartment/villa/townhouse labels or an accessible designation are
excluded from the walk, each exclusion logged; tie-break: smaller listed
occupancy, then alphabetical room-type name), its cancellation class
(LDG-A6) as posted for that cheapest rate, and the attribute vector (§1).
Replication each wave = the cheapest currently offered rate for that room
type **weakly dominating on LDG-A6**, at the stay grid (§2.3), on the
direct channel (LD-2), plus named fees per profile. Room-type churn is
handled by MISS/RECONFIG, not by walking up the menu.

### 2.2 Selection formula (deterministic; full definition in `pipeline/select_lodging_panel.py` at freeze)

**Freeze ordering (the G0 pattern, copied from the rent module §2.2
verbatim in structure):** band file → pre-freeze parser round-trip on the
pilot snapshot → pre-registration + `select_lodging_panel.py` (formula
before inputs) → hashed inputs committed to
`data/phase2-lodging-inputs.md` → market list = script output → hashed
freeze-wave snapshot (owner machine; the proxy blocks every booking host)
→ panel list = script output. Markets and properties are **outputs of the
freeze, never inputs to it**; test GL-C (§8) re-executes both steps.

**Markets, M = 4.** Proposed ranking instrument, stated with its
alternative because the choice is a reviewer question (open item 3):
**reuse the Phase 1 T-100 pull** (`data/phase1-inputs.md` §1 — the pull
spec is pinned; **its SHA-256 line still reads PENDING-OWNER-PULL**, so
this module's market list blocks on the same Phase 1 owner pull, stated
rather than implied — still zero *new* owner pulls). The CSV is
airport-level (ORIGIN/DEST/PASSENGERS; no CBSA field), so the aggregation
rule is pinned here, not left to judgment: **market = CBSA; a DEST airport
maps to its CBSA via a hashed airport→CBSA crosswalk file committed to
`data/phase2-lodging-inputs.md` (a new pinned *input file*, disclosed as
such — committed, not pulled); a CBSA's ranking statistic = the sum of 2024
domestic PASSENGERS over all rows whose DEST is listed for that CBSA in
the crosswalk**; rank descending, select the top-3, tie-break alphabetical
on CBSA title. **Seam-concentration constraint (the
disclosure-jurisdiction analog):** the panel must contain ≥1 market from a
resort-fee-intensive list — **proposed now as {Las Vegas, Orlando, Miami},
a labeled convention chosen for the geography of the state-AG enforcement
actions and the rulemaking record [owner-verify: resort-fee
market-prevalence evidence, e.g. the FTC docket, cited at freeze], and
committed hashed in `data/phase2-lodging-inputs.md` at freeze rather than
carried as an adjective** — the market where the tested fee concentrates
is where the test has power — filled by the highest-ranked list member if
the top-3 walk has not produced one, logged in the script's audit output;
else the 4th slot fills in pure rank order. **Labeled convention, not a
representativeness claim, with both confounds stated:** (i) air-derived
destinations under-represent drive-trip lodging, which is plausibly where
B40 stays concentrate; (ii) **T-100 segment PASSENGERS by DEST counts
onboard segment arrivals including connecting passengers who never leave
the airport**, so hub CBSAs over-rank relative to visitor volume —
precisely wrong for a lodging ranking, and the reason spec §8's O&D
products (DB1C/OD-40) are the named candidate for the alternative: a
dedicated hashed lodging-market input costs one more owner pull and is the
open item.

**Segments (2 per market), deterministic from the freeze snapshot alone —
no external chain-scale classification. Selection statistics are computed
on the pinned aggregation surface's property pages (a selection-only
labeled convention, distinct from LD-2's menu of record; whether fee line
items are visible at that surface's property-page level is a required
field of the §8.2 pilot parser round-trip):**
- **SEG-BUDGET** — the 2 qualifying properties cheapest by displayed total
  at the freeze snapshot (the B40-relevant price point).
- **SEG-FEE** — the 2 qualifying properties with the largest posted
  resort/destination/amenity fee line item at the freeze snapshot (the
  seam-concentrated segment; where no property in walk range posts such a
  fee, the cell ships smaller, disclosed — a market with no resort fees is
  a finding).
- **Dedup rule (one property, one slot):** a property qualifying for both
  segments fills **SEG-FEE**; SEG-BUDGET takes the next-cheapest
  qualifying property — the panel is 16 *distinct* properties, never 15
  with a double-counted seller.

**Qualification:** brand-affiliated or otherwise standing seller with a
bookable direct channel (a re-observable posted menu — the same standing-
seller discipline that excludes one-off rental listings; the resulting
exclusion of phone-only sellers is disclosed in §0 and §4.2), ≥1 offered
rate for a 2-adult standard room (§2.1 keyword rule) at the
freeze-snapshot grid date. **Candidate set and walk:** per market, a
committed search-URL list on one pinned aggregation surface (logged-out,
US access, filters = the market geography; surface pinned at freeze after
the pilot proves it parses), pages 1..P_max; property pages open in
**SHA-256-of-canonical-URL ascending walk order** (the rent module's
arbitrary-but-deterministic labeled convention), and the manifest records
exactly the pages the walk touched. **The freeze-snapshot walk runs one
grid-date quote flow per candidate property** — the segment statistics
(displayed total; largest fee line item) exist only inside a quote flow,
so the flows are part of the formula, priced in §7's one-time section.
**Panel = 4 markets × (2 + 2) = 16 properties** — inside the 12–20
envelope this module targets; K, M, and P_max are provisional until the
pilot commits a measured per-quote basis (§7), and any post-freeze
shrinkage follows the pre-registered de-scope order (§7), never
improvisation.

**Succession rule:** a property dead ≥3 consecutive waves stays MISS/CLOSED
through December; replacement only at the December re-freeze from the
original frozen walk order, logged. Mid-year replacement is banned — churn
is a finding.

### 2.3 Capture protocol and cadence

- **Wave day:** shared with the standing runbook — first Tuesday of each
  month (holiday shift rule inherited). **Stay grid (pinned):** check-in =
  the **third Friday after wave day**, 1 night, 1 room, 2 adults — the
  ~3-week-advance purchase point, the codebook §2.3 airlines analog,
  stated as a labeled convention. Blackout windows are the Phase 1 frozen
  set (Thanksgiving week; Dec 18–Jan 4; Jul 1–7), iterate-forward
  Friday-by-Friday. **Worked date traces:** wave Tue 2026-10-06 → Fridays
  Oct 9/16/23 → check-in **2026-10-23**; wave Tue 2026-12-01 → third
  Friday 2026-12-18 → blackout → Dec 25 ✗, Jan 1 ✗ → check-in
  **2027-01-08** (the December-prices-January consequence, exactly as the
  air panel's §2 traces). Per LD-5 the wedge statistic is grid-robust; the
  grid discipline exists for the link.
- **December sessions (ruled, the phase1 §10 pattern adopted rather than
  deviated from — and the deviation question answered rather than left
  silent, the rent §2.3 discipline):** hotel booking-engine rates are
  session-priced dynamic quotes (A/B tests, demand repricing) — the
  ULCC-ancillary case, not the rent module's posted per-unit list price,
  so rent's one-session argument does not transfer here. **December
  direct-channel observation of record = median of three same-day sessions
  per property**, priced in §7; non-December waves stay single-session
  (they never chain).
- **Quote flow fields per property-wave (verbatim-never-computed):**
  wave_id; capture timestamp; channel + provenance grade + manifest/commit
  ref; market; segment; canonical_url + url_sha256 (walk key); seller;
  brand family of record (identity-break tracking, LD-6); frozen room
  type; **D_first** — the price first displayed for the frozen room at the
  results/selection step, verbatim; **T_display** — the displayed total at
  the rule's total-price point; **T_itemized** — the itemized pre-payment
  total, with every line item name + amount verbatim (room, each mandatory
  fee, government taxes separately); cancellation class of the priced rate
  (LDG-A6); resort/destination fee line (LDG-A2); parking basis + price
  (LDG-A3); breakfast basis (LDG-A5); early/late options where posted
  (LDG-A4); wifi basis (LDG-A7); conditioning offers seen (member rate
  etc., LD-3, labeled); promo/strikethrough flag; loaded status; missing
  code; no-priced-path entries (→ Register feed); page title + URL;
  saved-file sha256 where manual; notes. All arithmetic — W and its
  W_covered/W_boundary split (§3.2), C, diffs — happens **at ingestion**
  (`pipeline/validate_capture.py` gains a lodging record schema), never in
  the agent.
- **Safety rails (the lodging wave prompt; frozen text lands in
  `pipeline/wave-prompts.md` at the pre-registration).** The agent MAY:
  open property and booking-engine pages, select the frozen room and grid
  dates, proceed **at most to the first page that displays the itemized
  total**. It may NOT: log in, enter any personal or payment detail,
  create an account, hold or complete any booking — hard stop at any
  identity, contact, or card field. (The detection boundary this rail
  creates for LD-4 leaks is disclosed there and conditioned on in
  §3.3–§3.4.) Blocked pages record `loaded=blocked` and fall to the
  owner-manual path. **Prompt letter: the rent and wireless drafts both
  claimed "Prompt D" — a naming collision logged here (open item 8); this
  module's prompt is provisionally "Prompt E (lodging)" and the
  pre-registration assigns final letters.** WS-G counsel review explicitly
  covers automated capture of brand booking engines and OTAs (ToS exposure
  — the rent module's platform precedent; hence G in this document's
  stamp).
- **Channel sweeps:** direct channel monthly (the menu of record, LD-2);
  one pinned OTA captured **semiannually (June + December)** as
  corroboration and rule-coverage context. Cross-channel disagreement in a
  mandatory fee's presence or amount → `fee-conflict` flag, held to the
  next dual-channel wave, resolved against the property's own posted fee
  page where one exists (`pipeline/targets.tsv` rows at freeze).
  **December disposition ruled ex ante (the link cannot wait five months
  for June):** the direct channel's reading enters the link — it is the
  menu of record per LD-2 — with the `fee-conflict` flag carried into the
  link row as disclosure (the rent module's December cross-platform
  pattern); the June wave's resolution amends the exhibit, never the link.
  Symmetric by construction.
- **Anti-promotion rule (split by price type, the phase1 §4 pattern):**
  *fee-schedule items* (resort fee, parking, wifi) — a single-wave level
  change of either sign without a corroborating posted document is held
  pending confirmation (two consecutive readings, or the same wave's
  hash-captured fee page); the annual link computes after the following
  January wave, so December-effective changes get their confirmation wave.
  *Room rates* are dynamic prices — they ARE the menu, like ULCC
  ancillaries — so no multi-wave screen applies; promos record per LD-3.

**Provenance ladder (grades identical to phase1 §4):** (1) `capture.py`
static pages = raw HTML + SHA-256 manifest, full archival weight —
**reserved for property/brand fee-policy and resort-fee disclosure pages**
(rows added to `targets.tsv` at freeze; booking engines are JS
applications and are not grade-1 targets, the rent-module ruling copied).
(2) Owner manual Save-Page-As registered via `capture.py --manual` = full
archival weight — **every link-entering December observation (all 16
panel quotes' itemization pages, priced in §7)** plus a rotating audit
subsample. (3) Chrome-agent extraction = content-grade. The December link
and every compression-exhibit W that enters the pre/post comparison rest
on hashed artifacts, not agent text.

### 2.4 Missingness (lodging MISS codes)

**MISS/SOLD-OUT** (no offered rate for the frozen room at the grid date —
the fee schedule is still captured; the rate field stays empty; no
imputation, stale quotes never enter a link), **MISS/CLOSED** (property
gone from the direct channel), **MISS/RECONFIG** (frozen room type no
longer offered — a menu-removal fact, ledger/Register-drafted),
**MISS/FLAG-CHANGE** (LD-6), **MISS/SITE-ERR, MISS/BLOCKED, MISS/SKIPPED.**

1. A missing monthly observation flags and stays empty. Up to 2 whole
   non-December waves per year may be missed (flagged) with zero effect on
   the published link; December is mandatory.
2. **December miss ladder:** retry within Dec 1–15 (the backup capture
   window) → for MISS/SOLD-OUT with a posted fee schedule, the fee
   components enter and the rate component is excluded with in-stratum
   reallocation → full Exclusion for the link. **The rent ladder's
   ±15-day `link-substitute` rung is not copied, because it is
   unreachable:** waves are monthly (first Tuesday), so the nearest waves
   sit ~4–5 weeks from the December wave day and no wave can ever be
   "within ±15 days" — the rung is dead code in rent §2.4 too, logged as a
   sibling correction (open item 12). Widening the rate window to reach
   the January wave was considered and rejected: lodging rates are
   seasonal, and a January-for-December substitution imports the gradient
   into the link (the rent module's own narrowed-window argument). The
   **fee-schedule components** keep the ±45-day window (schedule-posted,
   not seasonal). Never reservation-price imputation.
3. **Base re-freeze:** annually at the December wave from the Ledger's
   attribute records (codebook §7): no superset ratchet (a valet upgrade
   priced under LDG-A3's route does not enter the next base), no
   forgiveness drift (a leaked mandatory fee stays priced until the
   December re-freeze closes its link).

---

## 3. The compression test (the module's centerpiece)

### 3.1 The prediction, restated precisely

The seam claim: drip-priced mandatory fees open a wedge between the price a
household sees first and the cost of the experience as actually purchased.
16 CFR 464 forced the mandatory-fee stack into the first-displayed lodging
price on 2025-05-12. **If the seam is real, the displayed-vs-all-in wedge
in lodging should be small after that date and should have been materially
larger before it** — and the module's own forward Gap should carry a ≈ 0
leak row (§4.3 row 2) while displays comply. The prediction was committed
in the spec and plan before this module was designed; it can fail in
public; the release prints it either way.

**Honest operationalization of the plan's sentence (logged, open item 7).**
The plan's shorthand — "the lodging Gap compresses after May 12, 2025" —
cannot be tested as a within-series comparison of this module's Gap: no
pre-rule ρ series exists (the spec's own row: *exists going forward; broken
series backward*), the panel freezes in 2026, and spec §9.2 bans
backfilling across a dated observability break. The test therefore has two
arms plus a forward null, defined on the **wedge statistic** (§3.2), and
the compression claim is a claim about the wedge across the 2025-05-12
break — never a spliced Gap series.

### 3.2 The wedge statistic — and its split at the rule's own boundary

Per quote j (one property × wave × channel): with **D_first** the price
first displayed for the frozen room at the results/selection step and
**T_mand** the itemized total of room plus **all seller-mandatory charges**
for the stay (§0's definition: required of every guest, at every posted
rate, to acquire the frozen room-night; government taxes excluded and
recorded separately; profile-activated fees such as parking never in
T_mand),

> **W_j = (T_mand − D_first) / T_mand.**

W ≈ 0 is what rule compliance looks like; W > 0 measures mandatory money
outside the first-displayed price — the seam, per quote, in one number.
**At ingestion (never in the agent), W splits at the rule's own coverage
boundary into two components keyed to the quoted total-price definition
(the LDG-A1 [owner-verify at freeze] boundary, §0):**

> **W_j = W_covered,j + W_boundary,j** — **W_covered** = mandatory money
> that 16 CFR 464's total-price definition requires inside the display
> (so W_covered > 0 is a noncompliant display, an enforcement fact);
> **W_boundary** = seller-mandatory money in charges outside the rule's
> definition but inside this module's replication concept (a rule-legal
> LD-4 leak, the seam's relocation channel).

The split is what makes §3.4's outcome states separable on observables
rather than by adjective. W is within-quote (LD-5): robust to date grid,
seasonality, and market mix by construction, which is what makes archival
single-page evidence usable in the pre-period arm — under the Arm P
estimator defined in §3.3, never assembled ad hoc at verdict time.

### 3.3 Arms, evidence, and what can and cannot be reconstructed

- **Arm F (forward, panel; from the first post-freeze wave — December
  2026 at the latest, earlier if the freeze lands earlier, logged in the
  pre-registration).** The panel is an output of the freeze (§8.2), so no
  panel W exists before it; W readings from the §8.7 preservation capture
  publish only as **labeled unfrozen exhibit context**, never as
  panel-census statistics. From the first post-freeze wave: W_j (with its
  W_covered/W_boundary split) for every panel quote, every wave, both
  channels where captured; plus the count and magnitude of LD-4
  boundary-leak events **on the observable surface (LD-4's disclosed
  boundary: display-level leaks and grade-1 fee-page disclosures;
  desk-collected and post-payment charges are out of instrument, routed
  per LD-4)**. Predictions: the panel W distribution sits ≈ 0 and stays
  there; observable leaks are rare, and each one prints as a named-fee
  event when it happens.
- **Arm P (pre-period, archival; exhibit-grade, never chained).** **The
  estimator, defined ex ante so Arm P cannot assemble itself at verdict
  time — the project bans that everywhere else:** an Arm P observation is
  **usable only if D_first and every mandatory-fee amount appear in the
  same archived capture (same domain, same capture date)**, normalized
  **per-night at the archived page's own quoted stay length** (per-stay
  fees ÷ nights; pages stating no stay length are unusable), and labeled
  per row as **observed-W** (both quantities read off the same quote flow
  — rare: JS booking engines archive unreliably, the grade-1 ruling's own
  point) or **reconstructed-W** (e.g., W ≈ fee/(rate + fee) from a fee
  disclosed in fine print on the same archived page) — a *different
  estimator from Arm F's observed within-quote W*, printed as such on
  every exhibit row, never pooled silently. **Evidence classes,
  pre-committed with the selection bias stated before any number:**
  enforcement and rulemaking exhibits exist *because* they document the
  largest pre-rule wedges, so a W_pre distribution built from them is
  upward-biased by construction and would make "W_post < W_pre" nearly
  automatic — a falsification instrument rigged toward pass. Therefore:
  **class 1** — archived pre-rule pages of the frozen panel properties
  themselves: the panel *selection* did not exist pre-rule, but the
  properties did, and once the panel freezes Arm P prioritizes their own
  2024–early-2025 archived OTA/property pages — same-property pre/post
  pairs neutralize the property-composition confound, which is otherwise
  disclosed alongside LD-2's channel confound. **Class 2** — archived
  pages of properties captured for reasons unrelated to fees (e.g.,
  systematic Wayback crawls of OTA result pages; Wayback is legitimate
  for HTML with the standing caveat that JS-heavy booking pages archive
  unreliably; each exhibit carries its own capture-quality note).
  **Class 3, context only, excluded from the W_pre distribution the
  verdict is computed on** — the 16 CFR 464 rulemaking record (the FTC's
  NPRM analysis and public comments carry documented pre-rule
  displayed-vs-total examples and fee-prevalence evidence [owner-verify
  docket contents on an unblocked connection]); state-AG resort-fee
  enforcement and settlement records [owner-verify case names, dates,
  exhibits]; and the FTC staff economics literature — **Sullivan (2017),
  the FTC resort-fee analysis, spec-verified (spec §7 and Sources)**. The
  rule's live-enforcement anchor is likewise spec-verified: the StubHub
  $10M settlement, 2026-04-09 (spec §8 regulatory row, verified
  2026-07-04). **What CANNOT be reconstructed, stated plainly:** a
  pre-rule replication-cost *series*; pre-rule first-displayed prices at
  scale; and pre-rule W at the panel properties is **unknowable until the
  panel freezes** — not unrecoverable in principle (an earlier wording of
  this draft said so and thereby foreclosed the strongest available
  design, the same-property pair; corrected). Arm P is a **distributional
  exhibit at recoverable properties, class- and channel-labeled (mostly
  OTA-side, LD-2's disclosed asymmetry)**, not a panel. **Pre-registered
  fallback:** if classes 1–2 yield too few usable observations (the
  usability floor is a band-file number), the exhibit ships forward-only
  with Arm P reported *unrecoverable* — the honest version of "broken
  series backward," printed rather than papered over.
- **The comparison:** W_post (Arm F, panel census) vs W_pre (Arm P,
  classes 1–2 only, archival, labeled). Prediction: **W_post < W_pre, and
  W_post ≈ 0.** Every numeric threshold — what counts as "≈ 0," what
  counts as compression, Arm P's usability floor — lives in
  `docs/phase2-lodging-band.md` and nowhere else; the *category*
  definitions (the W split, the outcome keying, the Arm P estimator and
  evidence classes) are pre-registration text, because a band file can
  set limits but cannot supply missing definitions.

### 3.4 Pass/fail semantics and what a failure means

Three outcome states, keyed to the W_covered/W_boundary split so they are
separable on observables — the test is designed so its failure modes are
distinguishable, not so it cannot fail:

1. **Displays comply and the wedge is closed** (W_post ≈ 0 within the
   band, both components; Arm P classes 1–2, where recoverable, show the
   pre-rule wedge was larger): the prediction is met. The module then
   predicts **its own near-null forward leak row** (§4.3 row 2) — a small
   lodging Gap where the rule works is a prediction met, not a
   disappointment (the Southwest-honesty machinery, made structural).
   Negative and zero prints are features.
2. **Noncompliant displays** — **W_covered > 0**: mandatory money the
   rule's own quoted total-price definition requires inside the display is
   observed outside it at panel sellers. Directly observable per quote and
   keyed to the quoted rule text, so this is a fact about enforcement, not
   about the seam — reported as such, with the rule-coverage question
   routed to the byte-verification queue. The seam claim is neither
   confirmed nor weakened; the test is *inconclusive on the mechanism* and
   says so.
3. **Compliant displays, persistent wedge** — **W_boundary stays
   materially positive** (mandatory money migrating into rule-legal
   categories outside the total-price definition but inside the
   replication concept), or LD-4 leaks are frequent and material **on the
   disclosed observable surface** (LD-4's boundary — the desk-collection
   blind spot is disclosed, not silently absorbed into a pass), or Arm P
   classes 1–2 show no pre/post difference where recoverable. **This is
   the failure state, and here is what it means, plainly: the project's
   seam mechanism — that forced posting closes the
   advertised-vs-experienced wedge — failed its cleanest available
   regulatory test.** The same mechanism underwrites the rent module's
   §3.4 disclosure-jurisdiction prediction and, at one remove, the
   project's premise that posted-menu replication cost captures something
   advertised prices miss. A failure here weakens that story everywhere,
   and the release states the cross-module consequence in those words.
   That is the point of a falsification exhibit: it is only evidence when
   it could have come out the other way.

Whether the compression test **gates** any Phase 2 publication or remains
a published exhibit alongside it is a reviewer question for the H1 2027
round (open item 4); the v1 default, per the plan's wording ("falsification
exhibit"), is exhibit-with-verdict, printed in full either way.

### 3.5 Pre-registered contingency: rescission or vacatur

The module rides on 16 CFR 464 remaining in force through the test window,
and the project's own spec records the precedent that fee rules die
(DOT's 2024 ancillary rule, vacated 2026-02-03 — spec §8 regulatory row,
verified). So the treatment is pre-registered now, not improvised at the
news cycle: **rescission, vacatur, or formal non-enforcement withdrawal of
the rule is a second dated observability break** (the 2025-05-12 pattern;
it joins the codebook's dated-break list, open item 9). Arm F truncates at
the break date and publishes as-of; a verdict not yet computed computes on
the truncated window and says so. Post-break, LDG-A1's display entitlement
is no longer rule-backed: display relocations at constant T_mand are
ρ-neutral wedge facts (LD-4's mirror already prices only ΔT_mand), the W
series continues as an exhibit — the wedge is observable with or without
the rule — and the release states that **the test ended by external
action, not by verdict**. A truncated test is not a passed one.

---

## 4. Link mechanics, comparator, decomposition

### 4.1 Links

December-to-December per codebook §6; an event belongs to the link year
containing its effective date; fee-schedule events enter by effective date
from posted documents; the rate component is measured December-wave to
December-wave on the frozen grid. The 11 non-December waves supply T1
evidence, event detection, the transient screen, the monthly W series —
**they are never chained** (spec §2.5). Frozen-panel baseline = the
**December 2026 wave (Tue 2026-12-01)**; first fully in-sample annual link
= **the 2027 link (Dec 2026 → Dec 2027)**, measured from the December 2027
wave and computed after the January 2028 confirmation wave. The
compression exhibit does not wait for a link: Arm F wave statistics
publish with the **H2 2027 Phase 2 release** (plan §4), clearly labeled as
wave-level census statistics, never annualized. **The Q1 2027 Phase 1
release contains no lodging number** — its scope is fixed by the signed
Phase 1 pre-registration (the wireless module's §3.5 discipline, copied).

### 4.2 Comparator

**CPI "Other lodging away from home including hotels and motels"** item
stratum, 12-month relative — the stratum name is repo-verified against the
byte-grade weights join (`data/captures/b40-weights-joined-2026-07-12.json`,
B40 weight 0.589%); [owner-verify exact series ID and publication
structure on an unblocked connection]. `vintage=` tagged; any comparator
window spanning October 2025 takes `bridge=oct2025` (codebook §6). **The
flag attaches to CPI windows, not to the wedge exhibit:** the
W_pre-vs-W_post comparison contains no CPI window and never takes the
flag; a Gap or CPI-relative context exhibit whose 12-month window actually
spans October 2025 does. **Composition disclosure (the rent module's §4.2
sentence pattern, owed here too):** the Gap differences a deliberately
fee-tilted panel (half of it SEG-FEE by design) in 4 air-derived markets,
qualified on having a bookable direct channel, against the national
hotels/motels stratum — a stated composition choice, not an oversight; the
mismatch loads into the spread and is disclosed as such on every release,
alongside §0's coverage exclusions (no short-term-rental platforms, no
phone-only sellers). **Comparator honesty, load-bearing and unresolved:**
how BLS collects the stratum and whether mandatory resort fees were inside
CPI's price definition before and after the rule is exactly the seam
question on the CPI side — [owner-verify BLS collection methodology for
lodging away from home before any release interprets the Gap's sign].
Until that verification lands, the release states the comparator's concept
as unverified-in-detail rather than asserting which side of the wedge CPI
was on.

### 4.3 Mandatory decomposition (every release; identity, not gesture)

("Mandatory" in this section's title means the decomposition is required
in every release — sibling parity with rent §4.3; applied to a charge, the
word means seller-mandatory, §0's definition, and nothing else.) Three
rows, matching §0's three components, **defined so the compression
prediction is computable in the release identity itself and a parking
reprice can never masquerade as a leak.** With C₍t−1₎ the base replication
cost (displayed total + outside-display seller-mandatory items +
profile-activated named fees, per profile):

> ρ − π = [ΔT_display ÷ C₍t−1₎ − (π − 1)] + [Δ(LD-4 leaked seller-mandatory) ÷ C₍t−1₎] + [Δ(profile-activated named fees) ÷ C₍t−1₎],

rows labeled with predicted CPI-capture status. Row 1: in-display fee
movement (LDG-A2) prints as a labeled composition memo line inside it,
never as a separate contribution (LD-1). **Row 2 alone carries the
compression prediction** — ≈ 0 under compliance (§3.4 outcome 1), and the
leak-frequency failure signal of outcome (iii) is readable in this row,
release by release. Row 3 (parking, breakfast add-on) is ordinary
named-fee restoration pricing with no compression claim attached.
**Worked numbers (executable — land with `engine/test_phase2_lodging.py`
at pre-registration, per the standing repo rule; two variants so the leak
row is proven non-degenerate):**

*Variant A (compliant, no leak).* Base displayed total $180 (room $150 +
in-display resort fee $30), parking $20 ⇒ C₍t−1₎ = $200 (P2). Current
displayed $189 (room $153 + resort $36), parking $25, no outside-display
seller-mandatory item ⇒ C_t = $214; ρ = 214/200 = **+7.0%**; π = +4.0% ⇒
row 1 = 9/200 − 4.0pp = **+0.5pp**; row 2 = 0/200 = **0.0pp** — the
compliance near-null, printed as its own row; row 3 = 5/200 = **+2.5pp**;
sum = **+3.0pp** = ρ − π exactly. P1 (no car): 189/180 = +5.0%, Gap
+1.0pp, rows 1–2 only.

*Variant B (leak).* Variant A plus a newly mandatory $6 "service charge"
revealed outside the displayed total (ΔT_mand = +6, an LD-4 event) ⇒
C_t = $220; ρ = 220/200 = **+10.0%**; row 1 = **+0.5pp**; row 2 = 6/200 =
**+3.0pp**; row 3 = **+2.5pp**; sum = **+6.0pp** = ρ − π exactly.

A fee elimination or a compliant folding prints ≈ 0 or negative in its
row, and the module's credibility rests on printing it.

**Exclusive partition (codebook §9):** when the stratum is
restoration-priced in a period it leaves the ordinary pool; the public
concordance maps the module to the CPI stratum. **Archival discipline:**
all Arm P output is archival-grade, exhibit-only, never spliced into a
live link — 2025-05-12 is a dated observability break (spec §9.2),
exactly parallel to Zillow Total Price 2025-07-15 in the rent module.

---

## 5. Incidence and weights (codebook §8; register rows to be added to `data/incidence-proxies.md`)

**Stratum weight.** Lodging on out-of-town trips: Q1 $166/yr (0.5%), Q2
$338/yr (0.7%) — plan §1, 2023 vintage, refreshed at the scheduled Table
1101 pull (Table 1101's hierarchy bottoms out at "Other lodging," so the
2023-share convention stands, flagged — coverage restatement §); B40
restated $274/yr. Comparator-stratum B40 CPI-basket weight **0.589%**
(byte-grade); parent "Lodging away from home" 0.725% B40; **CPI-U 1.049% /
CPI-W 0.661%** (`data/captures/cpi-relative-importance-2026-07-12.json`,
byte-grade — codebook §9's Gap computes with w^CPI-U, so this is the
anchor that must be right; the tier map's 0.50 is a declared-mock B40
share and is not cited for any weight).

| Quantity | Value | Provenance | Status |
|---|---|---|---|
| Hotel-stay incidence among B40 households, h (coverage disclosure) | no repo source | candidate: CE percent-reporting detail / NHTS long-distance travel — [owner-verify] | **GAP — [0%, 100%]** until a usable source lands |
| Car-on-trip share c (P2 partition parameter) | no repo source | candidate: NHTS long-distance mode split — [owner-verify] | **GAP — [0%, 100%]** |
| Resort-fee prevalence / typical amounts | measured by the panel itself (share of panel properties posting a mandatory resort/destination fee; amounts verbatim) | panel census statistic, labeled **panel-scope**, never national; FTC rulemaking-record figures as `envelope/sanity` [owner-verify] | usable within stated scope |

No assumption share appears anywhere in this module; where the register
says GAP, the release publishes the interval.

**Exclusion Register routings (restated as the census obligation):**
housekeeping-frequency cuts; amenity closures/hour cuts inside an
unchanged resort fee (the standing fee-persists-while-amenity-closes
exhibit); unpriced early check-in; shuttle discontinuations; desk-collected
and post-payment charges surfaced by third-party documentation (LD-4's
observability boundary). Counts + affected base expenditure, every wave —
a property-wave is complete only when every dictionary attribute has a
priced path or an explicit no-priced-path entry.

---

## 6. Wave runbook integration and QC

- **Step L0 (T−1, sandbox):** lodging worksheet appended to Step-0
  generation (`pipeline/build_worksheet.py` extension at freeze: property
  list, grid check-in date with blackout iteration, channel-sweep flag,
  manual-save rotation).
- **Step L1:** `capture.py --sector lodging` static targets — property/
  brand fee-policy pages only (grade-1 ladder).
- **Step L2:** Chrome-agent lodging prompt (16 direct-channel quote flows;
  content-grade; §2.3 rails), owner's browser — **December: three same-day
  sessions per property, median of record (§2.3)**.
- **Step L3 (June/December + rotation):** pinned-OTA sweep; December
  manual saves of all 16 itemization pages via `capture.py --manual`.
- **Step L4:** ingest to `data/captures/lodging-<YYYY-MM-DD>.json`;
  `validate_capture.py` lodging schema fails loudly; W (with its
  W_covered/W_boundary split) and C computed at ingestion only.
- **Step L5:** diff vs prior wave → LD-4 leak detection (net-ΔT_mand per
  the mirror), fee events with T1/T2/T3 checks, decreases identical
  (codebook §4 symmetry), Register drafts.

**QC rows:** QC-L1 completeness/missing codes; QC-L2 D_first, T_display,
T_itemized all verbatim with line items; QC-L3 W and its split computed at
ingestion and ≥0-sanity-checked (a negative W is a data error or a genuine
below-display sale — flagged, never clipped); QC-L4 fee diffs → event
workflow; QC-L5 manual saves have sha256; QC-L6 conditioning never in a
headline field; QC-L7 cancellation-class dominance respected; QC-L8
government taxes excluded from T_mand and recorded separately; QC-L9
profile-activated fees never coded seller-mandatory (the §0 boundary,
checked mechanically).

---

## 7. Honest hours and the single operator

Sizing basis, the rent module's discipline copied: the repo's only
measured per-cell number is phase1 §6's **8 min/cell**. At that basis the
16-property agent pass ≈ **2.1 h/wave**; a single-property quote flow
could be cheaper (~3.5 min ⇒ ≈ 0.9 h) **or dearer — a multi-step JS
checkout flow may well run slower than a static cell** — so the section
sizes at the measured number in both directions, and the pilot's committed
wall-clock figure governs whichever way it lands (the de-scope order fires
on the measured figure, never on the hope). Steps L0/L1/L4/L5 ≈ 30 min ⇒
**≈ 2.6 h per typical wave at basis**. **December, summed rather than
listed:** 3 sessions × 2.1 h = 6.3 h direct-channel passes (§2.3
median-of-three) + OTA sweep ≈ 2.1 h + 16 manual saves × ~3 min ≈ 0.8 h +
re-freeze ≈ 0.5 h + steps ≈ 0.5 h ⇒ **≈ 10.2 h in the December month at
basis** (June ≈ 4.7 h with its OTA sweep). **De-scope order (frozen at
pre-registration):** (1) drop the June OTA sweep (keep December); (2)
SEG-BUDGET 2→1 per market (12 properties); (3) M 4→3 keeping the
seam-concentration market unconditionally. **Stacked truth, summed rather
than listed:** Phase 1 ≈ 9.7 h/month + rent ≈ 7.4 + wireless ≈ 1.3–1.5 +
this module ≈ 2.6 at basis ⇒ **≈ 21 h in a typical month at the measured
basis, more in December** — the Phase 2 stack's feasibility is a
plan-level owner decision the rent module already flagged; this module's
contribution is smallest and its de-scope order is pre-registered.

**One-time build:** selection script + parser round-trip + prompt +
validator/worksheet extensions + targets rows ≈ **8–12 h**
(sandbox-buildable except captures). **The freeze-wave selection snapshot
is owner-machine capture and is priced, not elided:** one grid-date quote
flow per candidate property up to P_max (§2.2 — the segment statistics
require it), at the 8-min basis e.g. 10 candidates × 4 markets ≈
**5.3 h**, scaling linearly in the candidate yield — which is exactly why
P_max is chosen at freeze with this line in view. Arm P archival
reconstruction is a separate owner task, ≈ 4–6 h on an unblocked
connection (Wayback, docket, settlement exhibits), honestly uncertain
because recoverability is the question.

**Single-operator disclosure (structural, printed):** every capture runs
on the owner's machine — the sandbox proxy blocks every booking host, OTA,
and archive; sandbox work is formulas, validators, worksheets, tests. No
backup operator exists, and this document says so.

---

## 8. What freezes when (the G0/G1 pattern; this document freezes nothing)

1. **This document is a DRAFT design.** It binds nothing.
2. **Commit ordering at freeze (band first — never another order):**
   `docs/phase2-lodging-band.md` (pass criteria; **the first and only
   existence of every numeric limit for this module, including every
   compression-test threshold** — its header states its relation to plan
   gate G2 without borrowing the label, the g1-band precedent) →
   pre-freeze parser round-trip on the pilot snapshot (rendered-DOM
   artifacts — booking engines are JS applications; required fields
   include fee-line-item visibility on the aggregation surface, §2.2) →
   Phase 2 pre-registration (frozen dictionary §1, rulings LD-1–LD-6,
   profiles, grid, channel ruling, missingness, prompt text, the §3.2 W
   split and Arm P estimator/evidence classes, the §3.5 contingency) +
   `pipeline/select_lodging_panel.py` → `data/phase2-lodging-inputs.md`
   (hashed ranking input; airport→CBSA crosswalk; seam-concentration
   market list; search-URL lists; freeze-wave snapshot) → computed market
   and panel lists → collection enters links and the test verdict
   computes. Worked-example arithmetic (both §4.3 variants) lands with
   `engine/test_phase2_lodging.py` in the same commit.
3. **Band tests (named now, limits later):** **GL-A** external review —
   rides the scheduled H1 2027 review, no bypass; **GL-B** the compression
   test's pass/fail limits — the W_post band per component (W_covered and
   W_boundary), the W_pre-vs-W_post compression criterion, and Arm P's
   usability floor; the *category definitions* behind them (the split, the
   outcome keying, the estimator, the evidence classes) are
   pre-registration text, not band numbers (§3.2–§3.4); **GL-C**
   independent reproduction of markets, panel, every published relative
   and every published W from hashed inputs + code + codebook, disclosure
   parity; **GL-D** the in-display composition non-event test (LD-1), two
   arms per the rent module's GR-D precedent: a conditional arm firing
   only where a documented in-panel fee-folding event exists (else
   not-applicable, never silent-pass) and an unconditional executable arm
   (a worked folding example proving ρ ≈ 0 within the band tolerance).
4. **Deadline logic:** freeze complete before the **2026-12-01 wave** or
   the first fully in-sample link slips to the 2028 link — stated now.
5. **MAY / MAY-NOT after sign-off:** inputs (vintages, URLs, series IDs,
   fee amounts in evidence, docket citations) MAY be corrected with logged
   amendments; the dictionary and rulings LD-1–LD-6, the profile
   partition, the panel formula (M, K, P_max, segments, dedup rule, walk
   order, seam-concentration constraint, succession), the channel ruling,
   the grid, the missingness rules and December ladder, the wedge
   statistic's definition and its W_covered/W_boundary split, the Arm P
   estimator and evidence-class hierarchy, the three-outcome reporting
   structure of §3.4, the §3.5 contingency, the decomposition identity,
   the comparator, and the de-scope order MAY NOT change after sign-off; a
   post-hoc case for changing them is a logged design failure with a
   methods note.
6. **The pilot object (pinned):** the lodging pilot runs the draft formula
   on an unfrozen, labeled pilot snapshot (Sprint-0 preservation
   candidates); committed outputs are exactly two — the per-quote
   wall-clock number (§7) and the parser round-trip. Nothing selected in
   the pilot carries standing; the frozen panel selects from a later
   snapshot regardless.
7. **Preservation capture is exempt and urgent** (plan P3): an unfrozen
   lodging panel v0 (candidate properties' displayed totals + fee pages)
   should run on the owner's machine now — `targets.tsv`'s lodging comment
   block has said the fixed unit sample is pending since the codebook
   milestone, and every month of forward W baseline is cheap and
   unreconstructible. Its W readings publish only as labeled unfrozen
   exhibit context (§3.3 Arm F), never as panel-census statistics.

---

## 9. Open items

1. Owner: Sprint-0 lodging preservation capture (supplies the §8 pilot
   snapshot; the panel's most time-sensitive task).
2. Freeze packaging decision: one Phase 2 pre-registration covering
   rent + wireless + lodging, or per-module documents with a shared band
   commit ordering — decided when the freeze package assembles, logged.
3. Market-ranking instrument (reviewer question): reuse the Phase 1 T-100
   pull — whose **SHA-256 is still PENDING-OWNER-PULL**, so the lodging
   market list blocks on that same Phase 1 owner task; the airport→CBSA
   crosswalk is a new pinned input file (committed, not pulled) — vs a
   dedicated hashed lodging-market input, for which spec §8's O&D products
   (DB1C/OD-40) are the named candidate; the §2.2 hub-connection confound
   is the argument for the alternative, the drive-trip confound weighs on
   both. The §2.2 text is the reuse proposal; the pre-registration
   decides.
4. Whether the compression test gates any Phase 2 publication or remains a
   published exhibit-with-verdict (v1 default) — H1 2027 reviewer
   question; the band file records the answer.
5. Owner byte-verification queue (narrowed to genuinely unverified items —
   Sullivan (2017) and the StubHub 4/9/26 settlement are already
   spec-verified and cited from the repo): 16 CFR 464 text (total-price
   definition — the W_covered/W_boundary split keys on it;
   government-tax treatment; itemization-before-payment; OTA/metasearch
   coverage; lodging-specific enforcement since 2026-07-04); BLS
   collection methodology and price definition for the
   lodging-away-from-home stratum (load-bearing for the Gap's
   interpretation, §4.2) + exact series ID; the state-AG resort-fee
   settlement records and the FTC rulemaking docket's pre-rule display
   exhibits (Arm P class-3 context and the class-1/2 recoverability map);
   resort-fee market-prevalence evidence for the §2.2 seam-concentration
   list; NHTS/CE incidence pulls (§5).
6. Lodging pilot → committed wall-clock number + parser round-trip →
   frozen M/K/P_max and de-scope order.
7. Plan input correction (logged, the phase1 precedent): restate plan §7's
   "lodging Gap compresses after May 12, 2025" to the §3.1
   operationalization (wedge-statistic compression across the dated break
   + forward near-null prediction), so the binding text and the executable
   test say the same thing.
8. Prompt-letter collision: rent §2.3 and wireless §4.2 both name their
   new wave prompt "Prompt D" — assign final letters (this module
   provisionally "Prompt E") when `pipeline/wave-prompts.md` gains the
   Phase 2 prompts at pre-registration.
9. Codebook next-revision queue: fold the frozen lodging dictionary into
   codebook §3 per the Phase-2 dictionary mandate; **create the codebook's
   dated-observability-break list** at its next revision (Zillow Total
   Price 2025-07-15; FTC 16 CFR 464 2025-05-12; any §3.5 rescission date),
   coordinated with the rent module's codebook next-revision queue — no
   such list exists in the codebook today, so this item creates it rather
   than appending to it.
10. Ledger seeding decision: whether the rule's effective date itself
    enters `data/ledger-events.json` as a dated market-wide observability
    event (evidence-rich, but not a seller menu event under §4 triggers) —
    decided at pre-registration, defaulting to a dated break annotation
    rather than a ledger row.
11. Owner-stay realized-side audit (pre-registration decision item, LD-4's
    observability boundary): whether a small realized-side audit — one
    stay per market per year, receipt and folio registered via
    `capture.py --manual`, a WS-H budget line — ships in v1, or the
    display-only detection boundary stands disclosed with the
    enforcement-record watch as the sole realized-side instrument.
12. Sibling correction (logged, the phase1 precedent): rent §2.4's
    ±15-day December `link-substitute` rung is unreachable under monthly
    first-Tuesday waves (§2.4 here) — log the same correction against the
    rent module at its next version bump.

## Changelog

- v0 (2026-07-12) — first complete draft: attribute dictionary v1
  (LDG-A1–A7) with binding-at-freeze rulings LD-1–LD-6 and the P1/P2
  partition; 4-market × 2-segment × 2-property deterministic panel (16
  properties) with the seam-concentration constraint, URL-hash walk order,
  and the direct-channel-as-menu-of-record ruling; stay grid with worked
  blackout traces (Oct 2026 → check-in 2026-10-23; Dec 2026 → 2027-01-08);
  the compression test defined on the within-quote wedge statistic W with
  two arms plus a forward null, the CAN/CANNOT archival honesty statement,
  the three-outcome reporting structure separating enforcement failure
  from seam failure, and the stated cross-module consequence of a failed
  test; Dec–Dec link mechanics against the CPI hotels/motels stratum
  (B40 weight 0.589% byte-grade) with an executable worked decomposition;
  incidence register rows at [0%, 100%]; honest hours at the measured
  8-min basis; freeze mechanics with named band tests GL-A–GL-D and **no
  numeric pass limits anywhere in this file, including none for the
  compression test itself** — first-existence discipline, the G0/G1
  pattern copied exactly.
- v0 (2026-07-12, same-day pre-commit revision after adversarial review) —
  decomposition rebuilt as a three-row identity (displayed / LD-4 leaks /
  profile-activated fees) with two executable variants so a parking
  reprice can never masquerade as a leak; "seller-mandatory" defined (the
  rent-§1 pattern) and the word reserved; W split into
  W_covered/W_boundary at the rule's own total-price boundary so §3.4's
  outcomes 2 and 3 separate on observables; Arm F re-anchored to the first
  post-freeze wave (no panel exists at wave 0); Arm P given an ex-ante
  estimator (same-capture usability, per-night normalization,
  observed-vs-reconstructed labels) and a pre-committed evidence-class
  hierarchy with enforcement/docket material demoted to context-only
  (selection-on-outcome bias stated) and same-property pre/post pairs
  restored as the priority class; LD-2 rewritten to a single seller test
  (brand-family and merchant-of-record clauses removed, with reasons);
  LD-4 given its observability boundary, its constant-T_mand non-event
  mirror, and an owner-stay audit decision item; LDG-A3's valet ruling
  stated against the codebook §2.1 precedent instead of past it; §3.5
  rescission/vacatur contingency pre-registered (the DOT-vacatur
  precedent, spec-verified); market ranking made deterministic (hashed
  airport→CBSA crosswalk; PENDING-OWNER-PULL status stated; hub-connection
  confound disclosed next to the drive-trip one; seam list relabeled a
  proposed convention with an owner-verify tag); segment-statistic channel
  pinned, dedup rule and standard-room keyword exclusion added,
  freeze-snapshot quote flows named and priced; December median-of-three
  sessions adopted (phase1 §10 — the reasoned-deviation question answered,
  not skipped) and the December fee-conflict disposition ruled; the dead
  ±15-day ladder rung removed with the sibling correction logged (open
  item 12); CPI-U weight corrected 0.50% → 1.049% (CPI-W 0.661%) — the
  tier-map figure was a declared-mock B40 share, byte-grade JSON now
  cited; `bridge=oct2025` restated to CPI windows only; comparator
  composition disclosure and the no-direct-channel coverage exclusion
  added; Sullivan (2017) and StubHub 4/9/26 cited as spec-verified and
  open item 5 narrowed; hours summed honestly (≈ 10.2 h December, ≈ 21
  h/month stacked, freeze snapshot priced, the 3.5-min hypothesis allowed
  to run in both directions); workstream stamp gains G; open items 3/5/9
  corrected, 11–12 added.
