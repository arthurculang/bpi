# The Restoration Gap — Phase 0 note: the 2008–09 retrospective, the validated primitive, and the public pre-registration of Phase 1

`v0 · 2026-07-12 · workstream F · STATUS: DRAFT — publishes October 2026 on restorationgap.org and as the versioned pre-registration of record (plan P10: research note + DOI + public code + snapshot archive under documented access rules); every [owner-verify] tag below must be resolved on an unblocked connection before publication; DOI minting (Zenodo or SSRN) is an owner action at publication`

---

## Abstract

We introduce the Restoration Index (RX), a conditional replication-cost price
measure, and its published product, **the Restoration Gap**: the 12-month cost
change of replicating last year's purchased experience on today's menu, minus
the matching official CPI item-stratum change, in percentage points. The
measure freezes the attribute vector of what a bottom-40%-income household
actually bought — including formerly included features like a checked bag or
ad-free playback — and prices the cheapest same-seller bundle on today's menu
that weakly dominates it. RX is a Konüs **upper bound** on constant-experience
cost growth by construction; it is published only as a spread, never as a
rival index, and it makes no claim to measure "true inflation" — here or
anywhere.

Validation preceded collection. A numeric plausibility band for the 2008–09
US airline checked-bag unbundling — four tests, their numeric limits, the
profile definitions, and the comparator window — was committed to the
project's git repository **before the event chronology and incidence register
were committed, and before any computation ran** (§3.1 states exactly what
the commit graph proves, what it does not, and how to check the ordering
against server-side merge timestamps). The method then reproduced the
documented event inside every limit at the pre-committed primary evaluation
point (one sensitivity-grid corner prints above the sector ceiling and is
disclosed in §3.4): one-bag line item $30.00 (band [$18, $42]); one-bag
profile event contribution +9.22% (band [+4%, +14%]); incidence-weighted
sector gap +4.15pp (band [+1.0pp, +6.0pp]); a zero-bag profile at exactly
+0.0000%; and the pre-designated re-bundling episode printing −1.21%
(required ≤ 0).

This note is the public pre-registration of the Phase 1 live collection
(first wave 2026-10-06; first print target Q1 2027) and the freeze point of
codebook v0.

## 1. What this is — and what it is not

One paragraph, up front, because everything else depends on it. The
Restoration Index measures the change in the minimum cost of *replicating, on
today's menu, the consumption experience actually purchased in the base
period* — formally, a conditional replication-cost index in characteristics
space: the cost function of a Leontief-in-characteristics consumer (Lancaster
1966) anchored at the base-period attribute vector, minimized over the current
same-seller menu, which makes it a Pollak-style conditional index and a Konüs
**upper bound** on the constant-experience cost of living (spec v00.02.01,
§2.4 P4). Because it is an upper bound, it ships **only as a spread** — the
Restoration Gap — over the matching CPI item-stratum series, reconciled
against them in every release. It is **not** a cost-of-living index; **not** a
claim that headline CPI is wrong (it targets a different concept: reproduction
cost, not compensated cost); **not** an all-items index (covered sectors only,
with the coverage share published every release — at the Phase 2 composition,
≈ 17.7% of the true-B40 CPI-weight basket (17.68%, the closed byte-grade
weights chain), equivalently 18.9–20.7% of CE consumption-scope spending —
both computed, denominator-labeled, and provenance-tagged in
`data/coverage-restatement-2026-07-12.md`); and **not**
a "true inflation" measure — no artifact of this project makes that claim,
and the full limitations section (§7 below, carried in every release) leads
with it. The profession's consensus that CPI *overstates* cost-of-living
growth and this measure are answers to different questions and can both be
right. Negative and zero prints are features of the design, not failures of
it — this note contains both.

## 2. The method in brief

The formal statement lives in the spec (v00.02.01 §2; errata to v00.02.00,
2026-07-12) and the binding operating rules in codebook v0, which freezes
publicly with this note. The load-bearing pieces, briefly:

- **Replication cost.** C(z; t) = the minimum posted cost of any same-seller
  bundle on today's menu M_t that weakly dominates the frozen base-period
  attribute vector z, attribute-by-attribute. No attribute substitution
  (Leontief in characteristics); free *procurement* substitution
  (re-bundling, à-la-carte reassembly). The headline is same-seller (H); a
  cross-seller minimum (S) publishes as a sensitivity, and the H − S spread
  itself measures how much coping relies on brand switching.
- **Menu-expansion monotonicity (spec P2).** Adding a product without
  changing existing ones can never *raise* RX. A new cheap tier beside an
  unchanged incumbent prints exactly 0% for the profiles it does not
  dominate — menu expansion is not inflation, and an index that prints
  positive on it measures resentment, not prices. Where the new option weakly
  dominates a profile's frozen experience at lower cost, the index prints a
  genuine **decrease**. Symmetry (P3) is mandatory: re-bundling, fee
  elimination, and cheaper restoring paths must print negative.
- **Trigger rules (codebook §4).** A restoration event exists iff all three
  hold: **T1** — the attribute was in the modal purchased configuration at
  t−1, with documentary evidence; **T2** — a priced path to it exists on
  today's menu (named fee, à-la-carte item, or tier delta); **T3** —
  replication cost actually rose, attributable to the menu change, not to a
  pure scalar price move (which flows through as ordinary price change). If
  T2 fails — the attribute is unrestorable at any price — the item exits to
  the public Exclusion Register with its affected base expenditure counted.
  **No reservation-price imputation, ever** (codebook §4) — **and no hedonic
  imputation anywhere in the design** (spec §3.2 and decision 8).
- **Route hierarchy (codebook §5).** Restoration routes rank
  lexicographically: (1) named fee — the cleanest identification, and a cap
  on the line item wherever it exists; (2) à-la-carte reassembly; (3) tier
  upgrade, published as a flagged interval [0, tier gap] with the point at
  the gap, because the upgrade buys extras (superset conservatism, spec P6 —
  the bias runs *against* the thesis).
- **Discipline.** Annual December-to-December links only; the 12-month
  relative is the headline and the cumulated chain is a caveated memo item
  (no monthly chaining with a min operator — textbook chain-drift bait).
  Base experiences re-freeze annually from the Ledger's attribute records,
  so superset extras never ratchet into next year's base and degraded
  defaults never silently become the entitlement. Incidence weighting uses
  base-period utilization shares with a provenance tag on every figure;
  where no source meets the bar, the release publishes the **[0%, 100%]
  utilization interval** — never a bare point, never an assumption share.

## 3. The centerpiece: a band committed before its inputs

The standard failure mode for an advocacy-adjacent price measure is to fit
its method to the result it wanted. Phase 0 was designed to make that
impossible in the one place it could be tested: a documented historical
event — the 2008–09 US airline checked-bag unbundling — with fixed,
already-published external benchmarks the method could be checked against.

### 3.1 The commit ordering is the argument — stated exactly

The plausibility band (`docs/g0-plausibility-band.md`) — four numeric tests,
their limits, the profile definitions, and the comparator window — was
committed and owner-signed **before the retrospective's event chronology and
incidence register were committed, and before any computation ran**. The
ordering, concretely (times are UTC commit timestamps; the artifacts'
2026-07-04 date is the owner-local evaluation date — commit `9662e0c` lands
at 2026-07-04 21:54 US Pacific) [owner-verify: confirm the local-time
convention and that these hashes resolve in the public repository's history
at publication]:

| Commit | Time (2026, UTC) | What it fixed |
|---|---|---|
| `57581d6` | Jul 4, 19:53 | **The band**: four tests, numeric limits, profiles, comparator window — owner-signed the same day, accepted as-is |
| `5320008` | Jul 4, 20:08 | **The inputs are first committed**: the 2008–09 fee chronology and incidence register — 15 minutes *after* the band that judges them |
| `da8f599` | Jul 4, 22:44 | **Conventions pinned before computation**: event-contribution definition, primary incidence 45% with its [35%, 55%] grid, purchase-point rule, anchor grid |
| `295eb0f` | Jul 4, 22:47 | The retrospective harness (`engine/retro_2008.py`) and its dry run |
| `9662e0c` | Jul 5, 04:54 | **Official G0 PASS** on byte-verified BTS fare anchors (2026-07-04, owner-local) |

Two honesty notes on that table, because the point of this section is to
pre-empt rebuttals, not invite them. First, these commits fall within a
single working session. A commit timestamp shows when content was
*committed*, not when it was researched — nobody compiles a multi-carrier fee
chronology in 15 minutes or writes a harness in the 3 minutes between the
conventions commit and the dry run. The protection pre-commitment provides is
exactly and only this: the numeric limits, the four tests, the profiles, and
the comparator window were fixed and owner-signed **before any result was
seen**, so nothing could be tuned to a result. Second, the claim is *not*
that the author was ignorant of public facts before the band was drawn — the
opposite. The external benchmarks B1/B2 and the well-known fee facts were
deliberately **in** the band file, because the band was built from them; a
plan revision committed an hour before the band (`a52e85c`, 18:52 UTC)
already cites the PPI correction and the Brueckner wedge, and we say so here
rather than let a diff of our own history say it for us. Pre-commitment
proves the limits could not be tuned to results; it does not prove, and does
not need, ignorance of a documented public event.

Author timestamps in a git history are claims; server-side events are
evidence. The band and the inputs reached GitHub in the pull request merged
as `9f5ff43` (2026-07-04, 22:42 UTC) — *before the official result commit
existed*; the G0 result arrived in the later merge `726ca9c` (2026-07-05,
05:05 UTC). Server-side merge timestamps are not author-editable, so the
band-before-result ordering is externally anchored; the finer
band-before-inputs ordering within the first merge rests on author
timestamps, and we say so. The build-in-the-open posture was adopted the
same evening (`09f5d54`, 22:33 UTC) and the site went live 2026-07-06
[owner-verify: state the exact date the repository became public, alongside
the hash-reachability check].

Under the band's own binding rules, inputs (dates, amounts) MAY be corrected
with every change logged; the numeric limits, the four tests, the profiles,
and the comparator window MAY NOT change — any post-hoc case for revising
them is, by definition, a gate failure with a methods note, not a re-draw.
One material input correction was in fact logged after computation
(Frontier's fare-family launch date moved from ~2008-09 to 2008-12-18); it
touched no band-test input, and the amendment log in
`data/retro-2008-inputs.md` shows it. The claim a skeptic should attack is
stated exactly: the band's limits were fixed before the inputs were committed
and before any result existed — and the evidence is the commit graph plus the
server-side merges, not our say-so.

### 3.2 The event being reproduced

The chronology (full sourcing in `data/retro-2008-inputs.md`; tie-breaker
source for fee dates: Brueckner–Lee–Picard–Singer 2015, Table 1
[owner-verify: pull Table 1 on an unblocked connection]): legacy carriers
introduced **second-bag** fees ($25 one-way) between February and May 2008;
American led the **first-bag** fee ($15 one-way) on 2008-05-21 for tickets
on/after 2008-06-15, followed by US Airways, United, Northwest, Continental,
and finally Delta (tickets from 2008-11-05, travel from 2008-12-05). In H1
2009 the fee schedule stepped up to the $20-airport / $15-online modal
first-bag price. Southwest kept the first two bags free throughout ("Bags Fly
Free"); JetBlue kept the first bag free (it introduced a second-bag fee
during 2008 — amount disputed in the inputs file, non-material to the band
tests) — and under the same-seller headline rule their menus do **not**
restore a legacy carrier's experience; they enter only the cross-seller
sensitivity.

The band also required a **designated negative-print episode, selected in the
inputs file before computation**: US Airways charged $2 for in-flight
soda/water ($1 coffee/tea) from 2008-08-01 — the only US carrier to do so —
announced repeal on 2009-02-23, and resumed free beverages on 2009-03-01. A
dated restoration-of-inclusion inside the study window: the method must print
≤ 0% on it, or the symmetry claim is decorative.

### 3.3 The result

Evaluated at the pre-committed primary point — the byte-verified BTS annual
average domestic itinerary fare anchor (2007 **$325.26** → 2008 **$346.38**,
current dollars, +6.49% matched-fare) at the primary incidence of 45%
(pinned before any result existed) — the official gate evaluation
(`data/retro-g0-result-2026-07-04.md`):

| Band test | Value | Pre-committed band | In band |
|---|---|---|---|
| Band 1 — one-bag round-trip line item (online) | **$30.00** | [$18, $42] | yes |
| Band 2 — one-bag profile event contribution | **+9.22%** | [+4%, +14%] | yes |
| Band 3 — incidence-weighted sector gap | **+4.15pp** | [+1.0pp, +6.0pp] | yes |
| Band 4a — zero-bag profile event contribution | **+0.0000%** | = 0 | yes |
| Band 4b — designated negative print (US Airways beverage repeal) | **−1.21%** | ≤ 0 | yes |

(The result file labels these tests T1–T4b; they are relabeled here because
§2 already uses T1–T3 for the codebook's trigger rules — the same collision
gate G1's tests were named GA–GD to avoid.)

Two of these five numbers are the ones to sit with. The zero-bag profile
prints **exactly zero** — not approximately, exactly, because menu-expansion
monotonicity is arithmetic, not judgment: no 2008–09 menu change raised the
replication cost of an experience that never included a checked bag. And the
beverage repeal prints **negative**, because the method's event grammar is
symmetric and the episode was designated in advance, where it could not be
selected to flatter the result. A measure that can only go up is
unfalsifiable advocacy; this one demonstrably goes to zero and below when the
world does.

### 3.4 The sensitivity grid, including the corner outside the band

The pinned conventions required the full incidence × anchor grid
([35%, 55%] × [$250, $400]) to be reported with the gate evaluated at the
primary. Of the grid's sector-gap cells, **one lies outside the band**:
incidence 55% × anchor $250 prints +6.60pp against the +6.0pp ceiling. It is
in the result file, labeled, at the corner the band's own rationale
anticipated (the upper edge as the incidence assumption is pushed above the
primary against the lowest fare anchor). It is sensitivity, not a gate
failure — the gate is the pre-committed primary — and it is shown, not
hidden. That practice is itself pre-registered forward: every future
sensitivity grid publishes all cells, out-of-band corners disclosed.

### 3.5 Reconciliation against benchmarks we do not control

Two external benchmarks were fixed in the band file, both published years
before this project existed:

- **B1 — the PPI correction.** BLS's own producer price program confronted
  this exact event and chose to correct for it: without the fee adjustment it
  adopted in March 2009, *"the PPI for scheduled passenger air transportation
  would have been 1.6 percent lower in December 2009"* (BLS, Beyond the
  Numbers vol. 1, 2012) [owner-verify: re-quote from the live BLS page]. Our
  +4.15pp sector gap exceeds 1.6% in the expected direction and for the
  stated reason: B1 is a realized, incidence-included average-revenue effect
  over *post-fee* fee-paying passengers, while RX weights by *base-period*
  (pre-fee) checked-bag incidence — which is the design intent, since the
  measure prices the experience people had, not the coping they settled
  into. The band's ceiling (+6.0pp) enforced "same order of magnitude as
  B1"; the print lands mid-band.
- **B2 — the fee-minus-offset wedge.** First-bag fees of $15–20 per segment
  against base-fare declines of roughly 3% (~$5) (Brueckner–Lee–Picard–Singer
  2015; Henrickson–Scott estimate ~$0.11 of offset per fee dollar) imply a
  net wedge of about $10–15 per bag-checking segment, ≈ $20–30 per round
  trip. Our measured line item is the posted fee ($30.00 round trip at
  end-2009 online rates, $40 at airport rates — both reported), with the
  fee-minus-offset variant computed alongside solely for this comparison; the
  band's [$18, $42] limits were constructed as 2×[$15, $20] adjusted by an
  offset in [$0, $12], so the benchmark disciplines the band rather than the
  reverse.

The retrospective is executable: `engine/retro_2008.py` recomputes every
number in this section from the inputs pinned in `data/retro-2008-inputs.md`
(mirrored as committed constants in the harness and cross-referenced in its
header), and the repo's test suite pins the worked examples
(`python3 -m unittest discover engine`).

## 4. What CPI already captures — the part we are required to say

The strongest one-line rebuttal to a project like this is "BLS already
handles that." Sometimes it does, and this measure is built to say so.

- **Shrinkflation is captured, contemporaneously.** CPI standardizes packaged
  goods to per-unit prices, so a 64→60 oz downsizing at constant sticker
  records as +6.7% per ounce the same month. BLS's own research series
  (R-CPI-SC) puts the residual at roughly 0.01pp/yr (R-CPI-SC covers
  food-at-home and selected strata, not all items), and GAO attributes
  ~0.06pp of the 34.5% CPI rise over 2019–24 to downsizing
  [owner-verify: re-confirm both figures against the live R-CPI-SC page and
  GAO-25-107451]. Accordingly, shrinkflation is **not** a motivation of this
  project — it is the **null-test channel**: the grocery Restoration Gap on
  pure downsizing should print ≈ 0, and Phase 1 carries a deliberately
  downsizing-tilted 12-item grocery basket as a control precisely so a ≈ 0
  print can demonstrate the method does not manufacture inflation.
- **The first checked bag is priced inside the CPI airfare quote on the ~80%
  of quotes designated to include one.** The CPI airline-fares specification
  includes taxes, fuel surcharges, airport/security fees, and the first
  checked bag on those designated quotes. What the factsheet says
  CPI does not track — verbatim: *"The CPI only tracks the price of the
  first piece of checked luggage. The price of carry-on bags and any
  additional checked luggage are not tracked"* [owner-verify: all BLS
  factsheet quotations in this note were triangulated via multiple
  independent search extractions because bls.gov blocks automated fetch;
  re-quote every one from the live pages before publication] — is the
  narrower, structural seam this measure actually targets: carry-on
  unbundling, seat-selection fees, second bags, and fare-class-conditional
  pricing sit outside the priced specification, so those transitions never
  enter.
- **The Southwest prediction — published before the comparison.** The
  sector's largest unbundling event in decades (Southwest ending "bags fly
  free," May 2025) is mostly *inside* CPI's quote specification: designated
  quotes reprice the first bag too. We therefore predict, in advance and in
  print, that **our own headline event prints a SMALL Gap** — the residual
  is the ~20% of undesignated quotes, second bags, and carve-out
  conditioning. If the first print manufactures a large Gap on Southwest,
  the measure is wrong, and this paragraph is the standard it fails against.
  A prediction that can fail in public is the point.

## 5. What this note freezes, what starts when, and what we have already corrected

### 5.1 Frozen as of this note

- **Codebook v0** (`docs/codebook-v0.md`) — the equivalence protocol, trigger
  rules, route hierarchy, link-year and comparator conventions, incidence
  discipline, and Assumption Q. From publication it is the public
  pre-registration: amendments are versioned and append-only, and no
  retroactive convention change ever applies to an already-published link.
- **The Phase 1 pre-registration** (`docs/phase1-preregistration.md`, signed
  2026-07-06) — the air-travel route panel as an **executable formula, not a
  list** (`pipeline/select_routes.py`: N = 18 nonstop routes, 6 per distance
  band, ranked on the 2024 BTS T-100 file whose SHA-256 commits to
  `data/phase1-inputs.md` at the owner's pull; the route list is an output
  of the freeze, not an input to it) [owner-verify: T-100 SHA-256 committed
  to `data/phase1-inputs.md` and the route list generated by
  `pipeline/select_routes.py` before publication]; the 8-carrier list and
  cell rule; the first-Tuesday booking grid with pre-committed blackout
  windows; experience profiles P1–P4 with pinned incidence sources (the
  carry-on profile ships with the honest [0%, 100%] utilization interval —
  no usable source exists, and we publish the interval rather than an
  assumption); the paired same-flight Basic/Main quote protocol; the
  streaming sidecar (Netflix, Disney+, Hulu); the grocery null and banking
  negative controls; the denominator conventions for the first print; the
  missingness taxonomy and the pre-registered de-scope order. After
  sign-off these MAY NOT change; input corrections are logged in the
  amendment log.
- **The G1 pass criteria** (`docs/g1-band.md`, committed 2026-07-06 —
  *before* any Phase 1 in-scope computation, the G0 pattern copied exactly).
  Four tests: **GA** — written sign-off from at least one sympathetic-methods
  reviewer AND at least one critical-prior reviewer, no bypass path (failed
  outreach slips the date, never bends the gate); **GB** — the grocery null,
  two-stage; **GC** — the banking negative control, sign-only; **GD** — an
  independent third-party rerun from the hash-committed archive and public
  code, with disclosure parity (blocked cells, Exclusion Register entries,
  and out-of-band corners must appear in the rerun exactly as published).
  Per standing rule, **the numeric pass limits live in the band file and
  only there** — they are deliberately not reproduced in this note. If a
  test cannot be passed, the release does not ship; a methods note ships
  instead.

Not frozen, stated so no reader over-credits us: the Phase 2 rental-housing
and wireless module designs are drafts that bind only through their own
dedicated pre-registrations and band files, and the RX-100 full-basket
corridor is a **proposal under external review, not adopted** — it sits
behind its own gate.

### 5.2 What starts when

- **Wave 0 — September 2026**: an unpublished dry run. Its wall-clock total
  is committed to the repository, and the pre-registered de-scope trigger
  reads that committed number, not operator recollection.
- **Wave 1 — Tuesday 2026-10-06**: live collection begins on the frozen
  panel.
- **First print — target Q1 2027**, gated on G1, labeled exactly what it is:
  an **archival-denominator exhibit** (the verified 2025- and 2026-link air
  events priced against pre-registered archival fare denominators), plus the
  **exact 2025→2026 streaming link** (posted national prices make it exact),
  plus **both controls** (the grocery reconciliation with its short live
  window disclosed and never annualized; the banking series, expected
  negative on the documented overdraft/NSF fee declines — and allowed to
  fail). The first print's own coverage numbers publish with it —
  **restoration-priced ≈ 2% of the B40 basket, monitored ≈ 12%, controls
  segregated** (pre-registration §11(D)); the ≈ 17.7% / 18.9–20.7% figures
  in §1 are the prospective Phase 2 composition, not the first print's. The
  panel's first fully in-sample annual link is the 2027 link (December 2026
  → December 2027, measured from the December 2027 wave). No composite
  index is formed before its own gate. One worked trace of the first
  print's arithmetic, executable in `engine/test_phase1.py`: a $10 per
  segment fee increase on a two-segment round trip against a $325 one-way
  archival denominator at 17% incidence prints an event relative of 20/650 =
  **+3.08%** for the bag-checking profile and **+0.52pp** gross at the
  sector — and, where CPI's quote specification already captures the
  attribute at an 80% share, a **predicted residual Gap of +0.10pp**,
  published as a prediction before the comparison, not fit after it.
- **Single-operator disclosure**, restated because every artifact must:
  every wave, the December link, and all owner-machine pulls run through one
  person. The backup capture window, the ±45-day substitution ladder, and
  the two-skippable-waves allowance are the only hedges; there is no backup
  operator, and this note says so.

### 5.3 The corrections trail to date — three of our own numbers, corrected downward, in public

We consider this the strongest exhibit in the packet, and we would rather
you hear it from us:

1. **Coverage.** We hypothesized that restating coverage in
   consumption-basket space would lift the ~26% figure to ~30–35%. Real
   bottom-40 data corrected this downward: B40 households put only 6.6% into
   pensions/insurance and cash contributions, so the scope restatement buys
   ≈1.2 percentage points, and the computed, provenance-tagged figure is
   **18.9–20.7% of CE consumption-scope spending** — which fell again, to
   **17.68% of the true-B40 CPI-weight basket**, when the R-CPI-I
   relative-importance vintage landed the same day and closed the weights
   chain byte-grade (`data/coverage-restatement-2026-07-12.md`, amended into
   both RX-100 documents the same day). The correction ran downward twice,
   and both steps are logged.
2. **Tier shares.** The corridor tier map's mock shares (R ≈ 29 / A ≈ 33 /
   B ≈ 40) corrected to **23 / 28 / 49** under registered true-B40 weights
   (in the full-basket RX-100 proposal, every CPI stratum is classed
   **R** = restoration-priced, **A** = auditable against posted per-unit
   prices, or **B** = bounded only — Tier B is the share that can only be
   bounded, not priced). Owners' equivalent rent alone is 24% of the B40
   basket and keeps Tier B near half. That is stated as the corridor's
   central design problem, not hidden in an appendix.
3. **A citation that disagreed with our own computation — flagged and
   reconciled the same day.** The spec's Seam-2 reweighting figure
   (≈ 0.28pp/yr, the R-CPI-I bottom-vs-top quintile gap) did not match our
   byte-grade computation from the registered R-CPI-I series (≈ 0.43pp/yr).
   The flag was raised 2026-07-12 in the coverage restatement file and
   resolved the same day in spec v00.02.01's errata: **two conventions, one
   series, not an error** — 0.28pp/yr is the geometric-annualized
   convention; ≈ 0.43pp/yr is the simple per-year convention of the same
   series (cumulative 7.67pp over 2006–2023; +8.1pp through Dec 2024), both
   now byte-verified against
   `data/captures/r-cpi-i-series-dec2005-dec2024.xlsx`. The spec cites both
   conventions with their labels, and the original discrepancy remains
   visible in the restatement file — a flag raised, run to ground, and
   closed in public is the correction protocol working, and a stronger
   exhibit than an open discrepancy.

Every correction is logged where it happened, with the original number still
visible. The measure corrects its own optimistic hypotheses in public; that
is the posture working as designed, and the pre-committed correction
protocol (logged restatements, never silent edits) carries it forward into
the live series.

## 6. The verified event gallery — evidence of the phenomenon, explicitly not index output

The Inclusion Ledger (`data/ledger-events.json`; live at
restorationgap.org/ledger.html) is seeded with events verified against
primary or multiple independent sources. The site's standing disclaimer
applies verbatim and is repeated here: *"The Restoration Gap is a research
measure in development. Numbers shown pre-launch are verified event data,
not index output. The measure is an upper bound on constant-experience cost
growth by design; it is published as a spread over official CPI series and
reconciled against them in every release."* These become index inputs at
first print; none has been run through the index yet. Fee amounts are
one-way, domestic US, standard (non-elite, non-cardholder) menus unless
noted [owner-verify: re-verify all fee amounts and streaming prices against
carrier/platform pages in the publication week].

| Sector | Event | Effective | Restoration route |
|---|---|---|---|
| Air | **Southwest ends "bags fly free"** (first two bags included since ~1971): $35 first / $45 second | 2025-05-28 | Named fee. The honesty-exhibit event: predicted SMALL Gap (§4) |
| Air | Southwest raises bag fees to $45/$55 amid the jet-fuel spike | 2026-04-09 | Named fee (+$10/bag on the 2025 line item) |
| Air | **Industry fee wave**: UA $45/$50 (4/3) · DL $45/$55 (4/8) · AA $45/$55 prepaid, $50/$60 airport (4/9) · AS/Hawaiian $45/$55 (4/10) · B6 peak/off-peak $39–49/$59–69, +$10 airport (3/31) | 2026-03/04 | Named fees; B6 priced date-matched to its peak calendar |
| Air | **American prices checked bags $5 higher in Basic Economy than Main Cabin** ($55/$65 online) — the first US fare-class-conditional price for an identical physical service [owner-verify: reconcile AA Main-cabin online fees between the 4/9 row ($45/$55 prepaid) and this row's implied $50/$60] | 2026-05-18 | Named fee, fare-class-conditional: a pure tiering observable |
| Air | **United domestic Basic Economy excludes the full-size carry-on** (personal item only); gate charge $75 | standing | Tier spread, superset-flagged interval [0, gap]; the $75 gate charge prices a *different* attribute (bag checked, not in cabin) and is excluded by the equivalence protocol regardless of price |
| Wireless | **T-Mobile force-migrates 8M+ lines** (Simple Choice/ONE/Magenta/legacy Sprint) to Experience tiers; ~1,100 plan codes retired, no opt-out; avg +$4/line | 2026-07-13 | Cheapest current-menu plan weakly dominating the frozen plan-feature vector — superset by construction, flagged; pre-migration menus and retired-plan feature vectors archived before the deadline [owner-verify: confirm the migration executed as announced] |
| Streaming | **Netflix retires Basic** (cheapest ad-free): closed 7/2023, removed 7/2024; cheapest ad-free $11.99 → $19.99 by 3/2026; plus the 2023 "extra member" slot ($7.99 at launch) — a formerly included capability, now a named line item | 2023–2026 | Tier spread (menu removal); named fee (extra member) |
| Streaming | **Disney+ launches the ad tier at the old ad-free price** ($7.99) while ad-free moves to $10.99; the ad-free-minus-ads spread widens $3 → $7 by late 2025 | 2022-12-08 | Tier spread; day-one restoration relative +37.5% while the entry sticker read 0% — a worked example of the method, never to be published as a print |
| Banking | **Overdraft/NSF revenue falls >50%** from 2019 to ~$5.8B (2023), other checking fees flat | 2019–2023 | Named fees, falling — enters as a **negative** restoration series: the standing proof the operator goes down |

The gallery demonstrates the *phenomenon* — unbundling, tiering, and menu
removal as recurring pricing events with documented dates and amounts. What
the index will add is the discipline: incidence weights or published
utilization bounds, link-year assignment, the CPI-stratum concordance, and
the Gap — which, per §4, we expect to be small exactly where CPI's
specification already covers the attribute.

## 7. Limitations (carried in every release; abridged from spec §12)

1. **Upper bound, not truth.** RX ≥ the constant-experience cost-of-living
   index by construction; the Gap is informative about the
   unbundling/tiering margin, not about aggregate CPI bias sign. The
   consensus that CPI *overstates* COLI growth and this measure are answers
   to different questions and can both be right.
2. **Priced restorations only.** Silent degradation — worse ingredients,
   thinner staffing, longer holds, more ads within an unchanged tier — is
   excluded; the Exclusion Register counts it but the index cannot price it.
   The index therefore *understates* total effective-price degradation while
   bounding the COLI from above.
3. **Non-users gained.** Unbundling made light users better off; the index
   measures the bundle-replicating population's cost, incidence-weighted,
   and says so.
4. **Reproducible experiences only.** Items whose base experience cannot be
   repurchased at any price exit the ledger, logged.
5. **Research-series posture.** Larger measurement error than official
   statistics; CEX coverage and quintile-ranking caveats inherited and
   disclosed; scraped panels are auditable censuses of posted menus, not
   probability samples — no standard errors are claimed.
6. **Aggregate all-in averages are flat in air travel.** The claim is
   distributional and experience-constant, never an average-spend claim.

And **Assumption Q**, verbatim from the codebook (§11), because the bracket
claim depends on it:

> "The bracket interpretation — that the chained CPI and the Restoration
> Index together bound constant-experience cost growth — holds only under
> Assumption Q: no economically material unmeasured quality *improvements*
> in covered items over the link year. The Restoration Index itself is an
> upper bound on constant-experience cost growth regardless; Assumption Q
> affects only the bracket claim."

## 8. How to replicate

- **Repository.** Everything binding is public in one repository —
  github.com/arthurculang/bpi [owner-verify: repository public and the
  cited commit history reachable at publication; the repo codename predates
  the public naming decision and is documented in
  `docs/naming-decision.md`] — including the spec, codebook, both band
  files, the pre-registrations, the inputs files, the decision records, and
  the corrections logs.
- **Executable checks.** `python3 -m unittest discover engine` pins every
  worked number in the spec, the retrospective, and the Phase 1
  pre-registration; `engine/retro_2008.py` recomputes the full G0 result
  and sensitivity grid from the inputs pinned in
  `data/retro-2008-inputs.md` (mirrored as committed constants in the
  harness and cross-referenced in its header);
  `pipeline/select_routes.py` reproduces the route panel from the T-100
  file whose SHA-256 commits to `data/phase1-inputs.md` at the owner's pull
  [owner-verify: hash committed and route list generated before
  publication]; `pipeline/build_weights.py` and
  `pipeline/restate_coverage.py` assert the published weight and coverage
  anchors against SHA-256-registered BLS source files.
- **Archive access.** Menu snapshots are hash-committed: manifests (SHA-256)
  live in the repository; snapshot files are archived per plan P10 — public
  where redistribution rights allow, access-on-request where a seller's
  terms bar public release, with the access rule documented per source.
  Releases are re-derivable from the archive plus the codebook; gate G1's
  test GD requires a named third party to actually do so before the first
  print, with disclosure parity.
- **Verification posture.** Every public number carries a provenance tag
  (pattern in `data/incidence-proxies.md`); facts triangulated through
  search snippets rather than byte-verified are labeled as such, and this
  draft's [owner-verify] tags are the pre-publication checklist.

## 9. Discussant comments

*[PLACEHOLDER — fills after the August–October 2026 methods review. The
review packet went to an index-number-theory seat, a critical-prior seat,
and a distributional seat (docs/discussant-packet-memo.md); written comments
are published here with the reviewers' permission, favorable or not. Gate
G1-GA — sign-off from at least one sympathetic-methods AND one
critical-prior reviewer — gates the Q1 2027 first print, and there is no
bypass path.]*

## 10. Acknowledgments

*[PLACEHOLDER — reviewers (with permission), data sources (BLS, BTS, GAO,
CFPB series; the verified CE mirrors), and tooling acknowledgments; single
authorship and its structural dependency are disclosed in §5.2. Funding
disclosure per the workstream-H budget memo.]*

---

## Publication checklist (owner actions, October 2026)

1. Mint the DOI (Zenodo or SSRN, per plan P10) and add it to this header;
   deposit the snapshot-archive manifest alongside.
2. Resolve every [owner-verify] tag on an unblocked connection: BLS
   factsheet re-quotes; the PPI 1.6% quotation; Brueckner Table 1; R-CPI-SC
   and GAO figures; all gallery fee amounts and streaming prices (including
   the AA Main-cabin fee reconciliation between the 4/9 and 5/18 rows); the
   T-Mobile migration outcome; commit-hash reachability, the §3.1
   local-time convention, and the repository-public date.
3. Commit the T-100 SHA-256 to `data/phase1-inputs.md` (owner pull) and
   generate the route list with `pipeline/select_routes.py` — both must
   precede publication of this note's §5.1 and §8 claims.
4. Freeze codebook v0's header from "draft" to its public pre-registration
   stamp in the same commit that publishes this note.
5. Fill §9 (discussant comments, with permission) and §10.
6. Publish on restorationgap.org (static HTML, no build step) with the
   standing disclaimer strip until the first print replaces it.

## Changelog

- v0 (2026-07-12, same-day revision after adversarial review) — spec
  citations moved to v00.02.01 (2026-07-12 errata to v00.02.00); §5.3 item 3
  rewritten as flagged-then-reconciled (two annualization conventions, one
  byte-verified R-CPI-I series, per the spec errata); coverage stated in
  both weight spaces with denominators labeled (17.68% true-B40 CPI-weight /
  18.9–20.7% CE consumption-scope) and the first print's own ≈2%/≈12%
  coverage added to §5.2; the §3.1 pre-commitment claim narrowed to what the
  commit graph proves (band-before-inputs-committed, band-before-result),
  with UTC labeling, the single-session disclosure, the a52e85c
  acknowledgment, and server-side merge anchors; JetBlue second-bag
  correction in §3.2; §3.3 band tests relabeled to avoid the trigger-rule
  T-code collision; T-100 hash claims tagged [owner-verify] and added to the
  checklist; quote-exactness fixes (≈1.2pp, GD disclosure-parity list
  including Exclusion Register entries, harness constants-transcription
  wording, R-CPI-SC scope, the 80% designation wording,
  reservation-price/hedonics attribution split, RX-100 tier definitions,
  Disney+ worked-example relabel, AA fee-seam [owner-verify]); abstract
  split into three paragraphs and qualified to the pre-committed primary
  with the out-of-band corner disclosed.
- v0 (2026-07-12) — first complete draft, synthesized from the binding
  artifacts: spec v00.02.01, codebook v0, `docs/g0-plausibility-band.md` +
  `data/retro-g0-result-2026-07-04.md` (quoted exactly),
  `data/retro-2008-inputs.md`, `docs/phase1-preregistration.md`,
  `docs/g1-band.md` (numeric limits deliberately not reproduced),
  `data/ledger-events.json`, `data/coverage-restatement-2026-07-12.md`, and
  the site's standing disclaimer language. Drafted for October 2026
  publication; all [owner-verify] tags outstanding.
