# RX-100 Tier-A CPI-adequacy audit protocols — draft

`v0 · 2026-07-11 · workstreams E/B · STATUS: DRAFT — PRE-REVIEW companion to docs/rx-100-proposal.md §5, ships in the August discussant packet beside the proposal. NOT adopted, NOT binding: these protocols enter the measure only through the corridor's own pre-registration and its pre-committed gate (G4, proposal §8), after the review reshapes them. No audit pass band exists yet and none is stated here — each audit's numeric limits get their own band file whose commit is their first existence anywhere (§1.4). Nothing in this document modifies the signed-off Phase 1 pre-registration, the G0/G1 bands, or the wave schedule; the grocery null (GB) remains the binding G1 control exactly as committed.`

This document is the operating manual for the corridor's engine. Proposal §5
proposes generalizing the grocery null from a *control* into a rotating
*measurement instrument*; the tier map puts Tier A at ≈33% of the B40 basket
(MOCK shares, `docs/rx-100-tier-map.md`), which means the CPI-adequacy audit —
not new restoration modules — is what makes the corridor interval `[L, U]`
narrow, up to the program-level ceiling §6 states honestly. This draft
specifies the generalized audit template, the pre-committed rotation rule, the
first three concrete protocols, the rotation governance, and the Improvements
Register (the symmetric instrument the corridor's Tier-B lower bounds
require). Posture, restated because every artifact must: the measure is an
**upper bound published only as a spread** over matching CPI series; the
corridor is an *interval* over CPI, never a rival level and never a "true
inflation" claim (the project makes none, in any artifact); negative and zero
prints are features — a tariff month with no change is a correct zero, and an
audit that certifies CPI adequate is a *headline result*, not a
disappointment; every number that will appear publicly carries a provenance
tag or an owner-verification flag. Where anything here conflicts with the
spec, codebook, or the signed-off Phase 1 pre-registration, they govern and
the conflict is a logged erratum.

---

## 1. The audit template (the grocery null, generalized)

### 1.1 Object, hypothesis, and the transfer assumption

A Tier-A audit does **not** restoration-price its stratum — Tier-A strata fail
the contractible-menu test by classification, so there is nothing to restore.
The audit tests whether the **CPI stratum's own pricing concept** adequately
tracks a frozen replication object over a link year. The frozen object takes
one of two forms, both descendants of GRO-P1's divisible-good convention
(codebook §3):

- **Frozen basket** (per-unit goods): a fixed item list frozen at
  identity + net quantity (UPC, grade, cut, or grade-equivalent), priced each
  wave as current unit price × frozen base quantity. The grocery null is the
  prototype (phase1-preregistration §9).
- **Frozen tariff** (posted-tariff services): a fixed consumption profile
  priced each wave on the posted tariff sheet — every component the posted
  schedule levies on that profile (fixed/customer charges, volumetric blocks,
  posted riders/adjustments), not just the headline rate.

The audit hypothesis: `|ρ_i^obj − π_i| ≤ δ_i`, where `ρ_i^obj` is the **frozen
object's** 12-month relative under the replication convention — deliberately
not written `ρ_i`, because proposal §1 reserves `ρ_i` for the *stratum's*
restoration relative, which the audit never observes — and `π_i` is the CPI
stratum's published 12-month relative.

**The transfer assumption, named (A-T, audit transferability — proposed here
for the proposal §3 assumption ladder; the review should price it, not
discover it).** The audit measures its gap on a small, owner-chosen frozen
object — a deliberately tilted basket, a top-N utility panel, a top-P city
panel — while the corridor consumes a certificate as a bound on the stratum's
`ρ_i − π_i` inside `G* = Σ w_i (ρ_i − π_i)`. The step from object to stratum
is an identifying assumption, not a theorem: **A-T = the frozen object's
adequacy gap bounds the stratum's replication-vs-CPI gap up to the band
width.** It sits on the ladder with its own falsification test: at any
re-audit the band file MAY pre-commit an object-rotation or split-object
check, and **any two same-stratum frozen objects disagreeing by more than the
band falsifies A-T for that stratum** — certificate revoked, the stratum
reverts to A-K bounds, the falsification publishes. Every certificate in this
document is scoped **"tested-≈0 on the audited object, extended to the
stratum under A-T,"** the §6 feed table prints A-T on the certified row, and
each protocol below carries a one-line statement of what its audit does
**not** identify. This is exactly the composition-mismatch attack a reviewer
will lead with; we would rather hand it to her named and falsifiable.

**What a pass is.** A passed link is **one of the two consecutive passes
promotion requires (§6)** — a single pass changes nothing in the corridor
arithmetic by itself (the passed-but-unpromoted year contributes `[−K, +K]`,
§6). A *promoted* stratum contributes `[−δ_i, +δ_i] ∩ [−K, +K]` (§6 — the
intersection is proposal §2's own truncation, restored here). This
deliberately **tightens** proposal §2's single-pass wording ("if the audit
passes its band, `ρ_i − π_i ∈ [−δ_i, +δ_i]`"); the tightening is stated so
the discussant reads design, not contradiction. The audit is a **census of
posted prices on a frozen object**, not a sample — no standard errors are
claimed anywhere in this instrument, and the object's composition is a
labeled convention, never a representativeness claim (the grocery ZIP
pattern) — which is precisely why A-T must be named rather than smuggled.
Where a band file designates a public statistical series as the price object,
the census language is **replaced** for that protocol by the
inherited-survey-design statement (§1.3).

### 1.2 The two-part test (GB restated generically)

Every audit publishes two statistics, generalizing GB-i/GB-ii
(`docs/g1-band.md`); each gets its own limit in the stratum's band file:

- **Part 1 — channel wedge.** The pre-registered channel-isolation contrast
  named in the stratum's band file. **Default form (the GB pattern): the
  same-object wedge** — on the identical frozen object, the
  replication-convention relative minus the naive posted-price relative
  (per-unit vs sticker-per-package for baskets; frozen-profile bill vs
  headline-rate for tariffs). This isolates the exact channel CPI is
  suspected of missing in that stratum — downsizing for packages,
  fixed-charge loading and structure redesign for tariffs — and
  simultaneously tests whether the *convention itself* manufactures a gap.
  Any protocol-specific substitute contrast (there is one candidate, AP-1's
  grade-mix diagnostic, resolved in §3) must be declared and justified in the
  band file before sign-off: the MAY-NOT-pinned "two-part test structure"
  (§1.4) is the **two-statistic requirement plus Part 2's form**, not one
  specific Part-1 contrast — stated now so no band file can quietly redefine
  a statistic the template appeared to fix. Objects deliberately tilted
  toward the suspected channel are biased *toward* finding a wedge, so a ≈0
  print is affirmative evidence, stated up front every time (the GB
  conservative-tilt discipline).
- **Part 2 — comparator gap.** `|frozen-object 12-month relative − CPI
  stratum 12-month relative| ≤` the band limit. The comparator selection rule
  (which CPI series, which fallback, which vintage rule) is fixed in the band
  file before computation; comparator windows spanning October 2025 carry the
  codebook §6 `bridge=oct2025` convention.

**Stated consequence — the power/width dilemma, which frames §9 item 4(a)
rather than hiding under it.** An audit is corridor-informative **iff
δ_i < K**: a certified stratum must contribute a set no wider than an
untested one, so **each band file must demonstrate δ_i < K at commit, or the
audit runs as a control only, never for corridor credit**. The dilemma is
real: GB's own width rationale shows an honest comparator band must absorb
composition dispersion in shock years, and the one precedent comparator limit
already sits above the proposal's mock `K` (compare `docs/g1-band.md` GB-ii —
whose numbers live there and only there — with proposal §3's mock
calibration); a δ narrow enough to be informative will fail strata for
composition reasons and flood the Tier-R escalation queue. We do not pretend
this is settled; it is the sharpest question the audit program puts to the
discussant.

Audit readings are December-to-December links (codebook §6); the non-December
waves supply evidence, change detection, and descriptive dispersion, and are
**never chained** (the spec §2.5 discipline). Schedule-posted tariff changes
of either sign follow the Phase 1 anti-promotion rule for schedule-posted
fees: a single-wave level change without seller documentation is held
pending-confirmation, the following wave's hash-captured tariff sheet counts
as the corroborating document, and **the annual audit link computes after the
following January confirmation wave completes** — symmetric by construction,
dips and spikes alike. That January wave is therefore **link-entering**: it
is carved out of §6's 2-skippable allowance and has its own miss ladder (§6),
so a December reading heading for a failure can never be shelved by missing
January.

### 1.3 Evidence and provenance grade

The Phase 1 provenance ladder applies unchanged (phase1-preregistration §4):
(1) `capture.py` static pages, raw HTML/PDF + SHA-256 manifest — full archival
weight; (2) owner manual Save-Page-As registered via `capture.py --manual` —
full archival weight; (3) browser-agent extraction — content-grade, flagged.
**Every link-entering audit observation (the December and confirming January
readings) must be grade 1 or 2.** Third-party public series (government or
industry averages) are corroboration only — never the observation of record —
*unless* a stratum's band file explicitly designates a named public
statistical series as the audit price object, states why own-capture is
infeasible for that surface, and records the independence check against CPI's
own collection for that stratum (the AP-1 case, §3, where this is a live
design question for the reviewer). Two further rules attach to any such
designation, because a survey cannot wear census clothes: (i) the census /
no-standard-errors language of §1.1 is **replaced** for that protocol by a
disclosed **inherited-survey-design statement** — the object inherits the
series' own frame, sampling, and revision behavior, including that its
composition floats with the publisher's frame (a partial un-freezing of the
object, stated, not hidden); (ii) the band file's Part-2 width rationale must
account for the series' own revision and sampling noise. All captures run on
the owner's machine — the sandbox proxy blocks the relevant hosts — via
`targets.tsv` rows added at each protocol's activation.

### 1.4 Band files: naming, commit ordering, first-existence discipline

**No numeric limit for any audit appears in this document, in the
pre-registration that adopts it, or anywhere else before its band file
exists.** Per audited stratum (or per protocol where strata share one
apparatus, stated in the band file):

1. **File:** `docs/audit-band-<protocol-slug>.md` (e.g.
   `docs/audit-band-ap1-motor-fuel.md`). The band file states the numeric
   limits for Part 1 and Part 2, the δ_i < K demonstration (§1.2), the width
   rationale, the comparator selection rule, **the pinned numeric sample
   parameters (the N/M/P of §4–§5) — pinned as numbers in the band file
   before the input-file pull**, the archival-vs-live scope (§6), and its own
   MAY/MAY-NOT wall. "The committed script's output governs" cannot govern
   its own parameter; Phase 1 pinned N = 18 in the pre-registration itself,
   and these protocols do the same one document later, in the band file,
   under the same MAY-NOT clause as the limits.
2. **Commit ordering (the G0 pattern, copied exactly):** band file first (its
   git hash is the timestamp of record; limits AND sample parameters) → the
   protocol's sample formula as executable code (`pipeline/select_audit_*.py`)
   → hash-committed input files (weight/customer/population files,
   owner-pulled on an unblocked connection) → the computed sample as the
   script's output → results. Band, then inputs, then results — never another
   order. No in-scope 12-month computation for a stratum may run before its
   band file's owner sign-off checkbox is checked.
3. **MAY / MAY NOT:** inputs (URLs, vintages, dates, sample-file hashes) MAY
   be corrected with logged amendments; the numeric limits, the pinned sample
   parameters, the two-statistic structure and Part 2's form, and the pass
   conditions MAY NOT change after sign-off. Any post-hoc case for changing
   them is a logged design failure with a methods note, never a re-draw.
4. GB's existing limits live in `docs/g1-band.md` and only there; this
   document cites the machinery, never restates the numbers. **GB is
   retro-designated audit #0 in lineage only: it is permanently a control,
   outside certification.** Its 12-item basket spans roughly nine CPI strata
   across two groups (four items sit in housing-group strata) and its
   comparator is the food-at-home *aggregate*, so under this document's own
   rules — a frozen object never certifies a stratum it does not cover; one
   basket certifies one stratum (§2) — GB can promote nothing: it carries
   **no promotion clock** and certifies no stratum to tested-≈0, ever.
   Per-stratum food-at-home audits are new instruments with their own
   single-stratum objects and band files. GB itself is untouched: it remains
   the binding G1 control on its signed-off terms.

### 1.5 Failure semantics (generic; the standing consequence, stated)

Evaluation failure handling is fixed now, per protocol instance:
fix-inputs-then-rerun **once**; a second miss is an audit failure. On failure:

- The stratum's corridor contribution reverts to the outcome-space bound
  `[−K, +K]` for that link year — `[L, U]` widens, visibly and non-fatally,
  and the release says which stratum did it.
- The audited reading itself **publishes as data** — it is a measured spread
  over CPI and is never suppressed; if it prints beyond `K`, it falsifies the
  A-K calibration and forces the published `K` reset (proposal §2–§3) — the
  data disciplines the bound, never the reverse.
- The stratum is **escalated to Tier-R candidacy by rule, never silently**
  (proposal §2): a scope memo is drafted within one release cycle. The rule
  runs even where the memo's likely conclusion is "no restoration grammar
  exists" (motor fuel) — the memo then publishes the dead end rather than the
  protocol presuming it. (Demotion after a second failure, and its floor
  rule, live in §6.)
- A failure is never tuned away. If CPI misses something real in a Tier-A
  stratum, that is a *finding of the project*, published as such with its
  provenance — it is the second-best outcome the instrument can produce, and
  the release treats it that way.

---

## 2. Rotation order (formula, not a list)

**Ranking rule.** Ranking unit = the **protocol bundle**. The bundle
enumeration is not rule-generated and we do not pretend it is — whoever draws
bundles draws the order — so **the enumeration is frozen here, in this
document, as a convention** (conventions are not pass bands; the
first-existence discipline does not bar them): AP-1 = Gasoline (all types) +
Other motor fuels; AP-2 = Electricity + Utility (piped) gas service; AP-3 =
Water and sewerage maintenance + Garbage and trash collection; **every
food-at-home stratum is its own single-stratum bundle.** The food-at-home
rule is the deliberate one: pooled, the 46 strata (~11.5 mock pp) would rank
first on borrowed weight while each certificate still needs its own
single-stratum object under A-T — bundling for rank without bundling for
certification would let the ranking claim mass the apparatus cannot certify.
Certification remains **per stratum** in all bundles — a bundle never
certifies a stratum its own frozen object does not cover. Ranking statistic =
Σ(bundle B40 weight) × cheapness multiplier c, with **c = 1.0 for A-1 and 0.5
for A-2, frozen here, not at G4** — a design constant chosen after the August
weight pull, with its flip point already published below, would be a tuning
surface, and freezing it now closes that surface. A bundle mixing A-1 and A-2
strata (none of the three do) takes the weight-share-weighted average of its
strata's c values, computed in the script. Ties break alphabetical on the
protocol slug, and **the slug list freezes with this enumeration**
(`ap1-motor-fuel`, `ap2-household-energy`, `ap3-water-sewer-trash`;
per-stratum food slugs derive mechanically from the hash-committed stratum
list) — a tie-break on names the designer may later coin is not a tie-break.
**Bundles, c, and slugs MAY NOT change after the weight file's hash is
committed.** `pipeline/audit_rotation.py` (pre-committed at G4 as executable
code) implements these frozen conventions; the binding order is the script's
output on the **hash-committed real weight file** (the August Table 1101 /
R-CPI-I pull); everything below is the EXPECTED order under the tier map's
MOCK shares and is overridden mechanically by the script.

Worked ranking (MOCK weights from `docs/rx-100-tier-map.md`, labeled as such):

| Rank | Protocol | Strata (tier map) | Σ mock weight | c | Statistic |
|---|---|---|---|---|---|
| 1 | **AP-1 motor fuel** | Gasoline (all types) [A-1] + Other motor fuels [A-1] | 4.10 | 1.0 | 4.10 |
| 2 | **AP-2 household energy** | Electricity [A-2] + Utility (piped) gas service [A-2] | 5.20 | 0.5 | 2.60 |
| 3 | **AP-3 water/sewer/trash** | Water and sewerage maintenance [A-2] + Garbage and trash collection [A-2] | 1.90 | 0.5 | 0.95 |
| 4+ | per-stratum food-at-home audits | Other miscellaneous foods (0.68), nonfrozen juices (0.50), snacks (0.48), … | — | 1.0 | ≤0.68 each |

Stated consequences, so no reader mistakes them: (a) the fuel-vs-energy
*ordering* is not robust to the multiplier — it flips near c ≈ 0.8 — while
top-3 *membership* is robust across a wide c range; c is frozen above
precisely because this document publishes that flip point. (b) The pure
formula puts the residual catch-all food strata ahead of the tier map's
informal showcase list (milk, eggs) because weight, not audit elegance, ranks
— catch-alls are audited by sampled baskets with the sampling disclosed (the
tier map's own caveat), and we keep the formula pure rather than hand-reorder
toward cleaner objects. (c) Protocol names are AP-1/AP-2/AP-3 — deliberately
not colliding with profiles P1–P4, tests GA–GD, triggers T1–T3, or
assumptions A-K/A-R/A-Q/A-H/A-O (or A-T, proposed here).

---

## 3. AP-1 — motor fuel

**Strata.** Gasoline (all types); Other motor fuels. Mock B40 weight ≈4.1% —
the top-ranked bundle under the rotation statistic (4.10 × 1.0): AP-1 ranks
first because of the cheapness multiplier, not raw mass (the AP-2 bundle is
heavier at 5.20 mock, and electricity alone ties gasoline at 4.00). Both
official BLS stratum names need owner byte-verification on an unblocked
connection (§9), regardless of the tier map's per-row flags.

**Frozen object.** A frozen fuel-consumption profile per grade: base-period
annual gallons of regular unleaded (the B40 modal grade), with midgrade,
premium, and diesel priced as separate lines at their own frozen gallons.
Divisible-good per-unit convention: replication cost = current posted
per-gallon price × frozen base gallons. **The frozen gallons are pinned per
grade at band commit from a hash-committed public source [owner-verify: the
EIA household/consumption tables as the pinning source].** Within a single
grade line the frozen gallons cancel — the line relative is just the
per-gallon price relative — so the gallons do work only in cross-grade
aggregation, and the aggregation rule is pinned now: the gasoline stratum's
Part-2 object is the **gallon-weighted aggregate of the gasoline grade
lines** against CPI Gasoline (all types); the other-motor-fuels stratum's is
the **diesel line** against that stratum's own CPI series; **no
parent-aggregate comparison is run** — the motor-fuels parent is
gasoline-dominated, and testing the second stratum against it would be a
second gasoline test wearing a diesel label. Grade identity is the matched
identity; a posted grade redefinition (octane respecification, ethanol-blend
relabeling E10→E15 at the same pump position) is logged as an identity-break
event, never silently substituted [owner-verify whether any such
redefinition is live in 2026].

**Why first, honestly.** Fuel is sold per gallon — no package to shrink — so
**Part 1 is the default same-object wedge and is degenerate by
construction**: replication-convention relative minus posted per-gallon
relative on the identical grade line ≡ 0. That degeneracy is the point. AP-1
is deliberately the **calibration anchor**: the protocol where the instrument
must certify trivially, so that a nonzero Part-1 print indicts the audit
arithmetic before it indicts the world. The grade-mix contrast an earlier
draft had put in Part 1's seat (frozen-grade relative minus all-grades-mix
relative) is **demoted to a labeled diagnostic**: it compares two different
objects, not one, and grade-mix drift is genuinely nonzero in exactly the
shock years that matter, so no ≈0 expectation attaches to it — it publishes
unbanded, as descriptive evidence for grade-identity drift.

**Sample and capture design.** The design finding that shapes this protocol:
pump prices are posted *physically*; the web surface is aggregator-mediated
(ToS-encumbered, ephemeral) and club-store fuel pages are membership-priced,
which the cash-menu rule (codebook §2.3) bars from any headline use. The
protocol therefore proposes designating **named public statistical series as
the audit price object** — the EIA weekly retail gasoline/diesel price tables
by grade [owner-verify: exact product name, series IDs, publication day, and
URL stability] as primary, with AAA daily average pages [owner-verify: page
structure and archivability] as corroboration — both captured monthly on
wave day via `capture.py` on the owner's machine, hash-committed, so
reproducibility rests on the archived vintages, not on live lookups. Because
the EIA tables are a **station-survey average**, §1.3's
inherited-survey-design rule applies in full: AP-1 claims no census, its
object's station composition floats with EIA's frame (stated, a partial
un-freezing of the object), and the band file's Part-2 width rationale must
absorb the series' own revision and sampling noise. Two further disclosed
caveats travel with this design: (i) it is the one protocol where the audit
object is a third-party series rather than own-captured menus — §1.3's
band-file designation rule exists for exactly this case; (ii) the
**circularity check is an owner task**: verify that CPI's motor-fuel
collection is independent of the designated series (if CPI ingested the same
survey, Part 2 would be a near-tautology and the band file must say what the
audit then demonstrates — comparator-concept adequacy, not collection
independence) [owner-verify].

**What this audit does not identify.** Prices on any surface other than the
designated series (pump-posted, club, cash-discount menus); anything about
stations outside EIA's frame; any restoration content — a gallon has no
attribute stack. A pass certifies the CPI concept adequate on the designated
series' object, extended to the stratum only under A-T.

**Cadence and effort.** Monthly capture inside the Phase 1 Step-1 static
layer (~10–15 min/wave: 2–3 static pages); annual evaluation after the
January confirmation wave.

**Comparator.** Per-stratum defaults, certified separately: CPI Gasoline
(all types) for the gasoline stratum; CPI Other motor fuels for the
diesel/other stratum [owner-verify official series names]; the motor-fuels
parent aggregate appears only as a disclosed fallback in the band file's
comparator selection rule. `bridge=oct2025` where a window spans October 2025
(relevant if the archival-first option in §6 is exercised).

**Failure semantics.** Generic §1.5 applies. The Tier-R escalation memo will
almost certainly conclude "no grammar" (a gallon has no attribute stack) and
publishes that conclusion; the informative failure mode here is a comparator
gap, which prints as a finding with the anchor-role caveat stated.

---

## 4. AP-2 — household energy (electricity + utility piped gas)

**Strata.** Electricity; Utility (piped) gas service. Mock B40 weight ≈5.2%.
Both A-2: tariffs are utility-specific with riders and adjustment clauses —
the panel is regional and gnarly, which is priced into the rotation statistic.

**Frozen object (frozen-tariff replication).** A fixed residential
consumption profile — pinned monthly kWh with a pinned seasonal shape, and
pinned monthly therms — priced each wave on the **posted tariff sheet** of
each sampled utility: customer/fixed charge + volumetric energy/delivery
blocks at the frozen usage + all posted riders and fuel/purchased-gas
adjustment values as of wave day. The consumption profile is a labeled
convention pinned at band commit from a hash-committed public source
[owner-verify: EIA average-consumption tables as the pinning source], not a
representativeness claim. The tax-inclusion rule (whether the frozen bill
includes purchase-associated taxes/surcharges, matching CPI's concept) is
pinned in the band file [owner-verify: CPI's treatment of taxes and mandated
surcharges in the electricity and piped-gas strata].

**What the audit tests.** This is the corridor's most policy-live Tier-A
audit: the suspected channel is **fixed-charge loading and tariff-structure
redesign** (block restructuring, mandatory riders, delivery/supply
re-splits) that a headline ¢/kWh reading could misstate for a frozen
consumption level. Part 1 = frozen-profile bill relative minus the naive
volumetric-rate relative at the same usage — the structure channel isolated
(the default same-object wedge; no substitute contrast). Part 2 =
|customer-weighted frozen-bill relative across the sample − CPI electricity
(resp. piped gas) 12-month relative| ≤ band. Note the double duty: the
**plan's §1 coverage-map revisit trigger for utilities** ("fixed-charge
unbundling adopted in ≥3 large-state tariffs") currently has no detection
instrument — **this audit is that instrument**, and its Part-1 series is the
trigger's evidence feed. (The tier map mis-homes that trigger to the
codebook; the erratum is logged here once rather than propagated into the
packet, and migrating the trigger into the codebook would be an owner
amendment, not a fact.)

**Sample formula.** Deterministic, with the parameters pinned where the
determinism actually lives: **N and M are pinned as numbers in the band file
before the input-file pull** (§1.4). The top-N investor-owned electric
utilities by residential customer count from a hash-committed EIA-861 vintage
[owner-verify file and vintage], and the top-M gas distributors from the
matching gas-side file [owner-verify: whether EIA-176 or the EIA-861 gas
analog is the right source]; one pinned residential tariff class per utility
— the default schedule a non-choosing continuing residential customer is on,
pinned at freeze, **with a deterministic tie-break where the default is
non-unique** (heating vs non-heating classes, default-TOU states): the
candidate schedule with the largest residential customer count in the
hash-committed filing, alphabetical on schedule code as the final tie-break.
A utility's mandatory migration of that class (e.g. default time-of-use
adoption) is logged as a structure event, priced on the successor default by
rule. Every drop/substitution predicate is **operational, with an evidence
obligation** — an owner cannot exclude an awkward utility by declaring its
rates unposted: *unposted* = no residential rate schedule retrievable from
the seller's or jurisdiction's own domain on the freeze date, **evidenced by
a registered capture of the search attempt**; every drop and substitution
appears in the script's audit output. Expected N ≈ 10 electric, M ≈ 8 gas
(EXPECTED/ILLUSTRATIVE — the committed script's output on the pinned N/M
governs). Retail-choice states where the default supply price is a posted
regulated rate stay in-sample; states where supply is unposted at the utility
(same evidence rule) drop by the script's stated rule, logged. The bill
computation is a committed script (`pipeline/audit_energy_bill.py`, written
before the band file's sign-off and pinned by unit tests), run at ingestion —
never hand-computed.

**What this audit does not identify.** The IOU frame excludes municipal and
cooperative utilities' customers by construction, and dropped
unposted-supply retail-choice states by rule; the band file states the
frame's customer share [owner-verify: EIA-861 shares]. The certificate
extends from the sampled panel to the stratum only under A-T.

**Capture design.** Tariff sheets and rider values are posted static
pages/PDFs — `capture.py`-able monthly on the owner's machine (~30 min/wave
for ~18 pages incl. manifest inspection); riders posted only inside
commission filings rather than on the utility's site are an ownership-task
flag per utility [owner-verify at sample freeze]. Wayback is legitimate
corroboration for static tariff pages (the streaming precedent; the ban is on
airline JS pages).

**Comparator.** CPI Electricity and CPI Utility (piped) gas service 12-month
relatives, certified separately — one audit apparatus, two strata, two band
lines.

**Failure semantics.** Generic §1.5, with one wired consequence: a failure
whose Part-1 wedge attributes to fixed-charge loading auto-drafts the Tier-R
scope memo *and* feeds the plan's revisit trigger's evidence file — the
escalation path here is real, not vacuous.

---

## 5. AP-3 — water, sewer, and trash tariffs

**Strata.** Water and sewerage maintenance; Garbage and trash collection.
Mock B40 weight ≈1.9%. Both A-2 (thousands of jurisdiction-specific
schedules, often PDF).

**Frozen object.** Same frozen-tariff pattern: a pinned residential profile —
monthly water gallons at a standard meter size, sewer on the jurisdiction's
posted basis (flat or water-volumetric, as posted), one standard-cart weekly
trash service — priced on the posted municipal (or franchised-hauler) rate
schedule. Stormwater and similar mandatory posted line items on the same bill
are in the frozen bill; the component list freezes per city at band commit.

**The two statistics (stated so a band file can actually be written).**
Part 1, in the AP-2 pattern (the default same-object wedge): frozen-profile
bill relative minus the naive volumetric/headline-rate relative at the same
usage — the marginal volumetric water rate on the water/sewer side, the
standard-cart headline rate on the trash side — isolating fixed/meter-charge
loading, tier redesign, and new mandatory line items, which is this section's
own named failure channel and the trigger-relevant structure wedge. Part 2:
the comparator gap per stratum, per §1.2.

**Sample formula.** Deterministic: **P pinned as a number in the band file
before the input pull** (§1.4); the top-P cities by population from a
hash-committed Census vintage [owner-verify file/vintage], with a stated
substitution rule under the same operational-predicate discipline as §4 —
*unposted* (investor-owned water with no residential schedule on the
utility's or jurisdiction's own domain on the freeze date) and *open-market
unfranchised* (no franchised or municipal hauler named on the jurisdiction's
own domain, same date) are each **evidenced by a registered capture of the
search attempt**; substitution is the next city in rank order, every
substitution logged in the script's audit output. Expected P ≈ 10
(EXPECTED/ILLUSTRATIVE; script output on the pinned P governs).

**Double-count guard (binding, from the tier map's concordance rule).** Trash
and water bundled into leases are the R-active rent module's territory; this
audit covers **directly billed** service only, and the concordance table at
the August Table 1101 restatement is where the boundary is made binding —
restated here so it is not lost.

**What this audit does not identify.** Bundled-into-rent service (the rent
module's, per the guard above); anything outside the top-P city frame; the
certificate extends to the stratum only under A-T.

**Capture design.** Municipal rate pages are static and slow-moving —
`capture.py` monthly (~20–30 min/wave for ~10–14 pages). Most rate cycles are
annual, so most waves print no change: **correct zeros, features**. Rate
changes typically adopt by dated ordinance — the posted effective date is the
event date, and the schedule-posted confirmation rule (§1.2) applies.

**Comparator.** CPI Water and sewerage maintenance; CPI Garbage and trash
collection [owner-verify names] — again certified separately.

**Failure semantics.** Generic §1.5. The plausible failure channel is
structure (fixed/meter charges, tier redesign, new mandatory line items) —
exactly the fee-stack grammar that would justify Tier-R candidacy, so the
escalation memo has a live question to answer.

---

## 6. Rotation governance and the corridor feed

**Activation.** Protocols activate in the script's binding rank order, **at
most one per link year, activating at the December wave** (the activation
window, defined so activation timing carries no discretion), each gated on
the hours rule in §8. Preservation-grade capture (adding `targets.tsv` rows
and archiving tariff pages) MAY begin before G4 under the plan's
capture-now-publish-later posture (P3) — preservation is exempt;
**computation is not**: no audit statistic is computed for a stratum before
its band file is signed off.

**Promotion — two consecutive links.** A stratum is promoted to
**tested-≈0** when two *consecutive, evaluated* December-to-December audit
links both pass their band. **A stratum whose first link has passed but which
is not yet promoted contributes `[−K, +K]` exactly like an untested one** —
the pass publishes as data but buys no corridor credit until the second
consecutive pass (the smaller-certified-share posture, proposal §7 Q3; and
the deliberate tightening of proposal §2's single-pass wording, §1.1). Until
promotion the stratum is "classified, untested" and contributes the A-K
bound. Void links (a December capture lost through the missingness ladder
below) count as neither pass nor fail and **break the consecutive chain** —
strategic missingness can therefore only delay promotion, never dodge a
failure, because a captured December reading MUST be evaluated (no
discretionary voiding) and the January confirmation wave has its own
non-skippable ladder below.

**Post-promotion cadence (the stop rule the rotation needs to actually
rotate).** A promoted stratum's protocol drops to **December +
January-confirmation capture only** (the link-entering waves); full monthly
capture resumes only in a re-audit year where the band file's evidence rules
require it. This is priced into §8's arithmetic — without it, activated
protocols accumulate monthly load forever and "rotating instrument" is
rotating in name only.

**Archival-first option (band-file decision, GB's own two-stage precedent).**
Where the designated price object has a public archived history (AP-1's
series; utility tariff archives via Wayback), the band file MAY pre-commit an
archival stage: retrospective 12-month links computed from hash-committed
archived vintages, with the band committed before any retrospective
computation (the G0 ordering). Whether archival links may count toward the
two-link promotion, or only live links (with archival as corroboration), is
**a question we put to the discussant rather than decide here** — it trades
years of promotion clock against the strength of the certification claim.

**Worked promotion trace (live-only reading, EXPECTED dates).** If G4 adopts
after the August review and AP-1 capture starts by the December 2026 wave:
first evaluable link = the 2027 link (Dec 2026 → Dec 2027, evaluated after
the January 2028 confirmation wave); second = the 2028 link; earliest
tested-≈0 promotion lands with the 2028-link evaluation in early 2029. The
consequence, stated plainly: **the corridor's certified Tier-A share is zero
at the first corridor print and grows on a multi-year clock** — the width
`U − L` contracts as a published identification-progress series, not as a
launch-day fait accompli; if the archival-first option is ruled legitimate,
AP-1 could promote years earlier, which is exactly why the ruling belongs to
the reviewer and not to us. **And the program-level ceiling, stated rather
than implied:** under §8's hours model the certified Tier-A mass saturates
around the three lead bundles — ≈11pp mock of the ≈33pp Tier-A mass — because
per-stratum food-at-home certification (46 separate objects at ≤0.68 mock pp
each) cannot clear the activation gate at meaningful scale. Narrowing beyond
that plateau requires the archival-first ruling, delegation beyond one
operator, or accepting that most of Tier A stays at A-K bounds. That ceiling
goes in front of the discussant beside §9 item 4; the opening page's "the
audit is what makes `[L, U]` narrow" is true only up to it.

**Re-audit — 3 years, mechanical expiry.** Certification expires at the end
of the third link year following promotion unless a fresh audited 12-month
link has closed in-band within that window (the post-promotion cadence's
December + January captures supply it). Expiry is mechanical: the stratum
reverts to "classified, untested" (A-K bounds) with no discretion and no
grace period — a stale certificate is not a certificate.

**Demotion.** One failed link → §1.5 (A-K for that link + escalation flag +
scope memo). Two consecutive failed links → reclassification at the next
classification re-commit, **with the failure mode decided by a pre-stated
observable, never post-hoc judgment**: *identity churn* iff the share of
panel cells with logged identity-break events exceeds the band file's
pre-committed threshold; *structure grammar* iff the Part-1 wedge accounts
for the Part-2 miss above the band file's pre-committed attribution share
(both thresholds are numbers that live in the band file — first-existence
discipline); an observable satisfying neither classifies to Tier B by the
tier map's shrinkflation-pushes-to-B principle. **Floor rule — failure never
buys narrowness:** a stratum demoted to Tier B after audit failure
contributes **no interval narrower than `[−K, +K]`** until its Register lines
are populated by documented events covering the failure channel, and its last
measured audit gap enters the Exclusion side as a minimum `M_i` magnitude,
provenance-tagged to the audit itself. Without this rule an empty-register
Tier-B bound (`[−I/E, +M/E]` with both zero) would collapse toward a point at
zero, and two documented CPI-tracking failures would *tighten* the published
interval — the exact zero-imputation the corridor exists to kill,
reintroduced as a reward for failure. A stratum reclassified **R-queued**
contributes `[−K, +K]` until its module ships. All reclassification is by
logged amendment, never silent.

**Missingness.** Phase 1 §7's codes and posture reuse directly: a missing
monthly capture flags and stays empty, no imputation; stale pages carry
`stale=n` and never enter a link. **December miss ladder:** retry within
Dec 1–15 → nearest wave within ±45 days flagged `link-substitute`, **with a
tariff-specific rule the air-travel import would otherwise get wrong**:
municipal and utility rate changes cluster at January-1 and fiscal-year
boundaries, so a substitute reading MUST compute the frozen bill on the
tariff schedule **in force as of the December wave date** — computable
because posted schedules carry effective dates, the same fact §5's event
dating relies on; where the in-force-as-of-December schedule cannot be
reconstructed from the substitute capture, the link is **void** for that
stratum (contributes A-K that year, chain broken as above). **January
confirmation wave (link-entering, §1.2) — carved out of the skippable
allowance, with its own ladder:** retry within Jan 1–15 → the next available
wave's hash-captured tariff sheet counts as the confirming document → if no
confirming capture exists by the band file's pre-stated evaluation deadline,
then any pending-confirmation change makes the link **void with chain break,
and the captured December reading still publishes as data** (a December
reading heading for a failure cannot be shelved by skipping January); where
nothing is pending-confirmation, the link computes on the December capture
and the January miss is logged. Up to 2 whole audit waves per year **other
than December and January** may be missed with zero effect on the link.

**How audit status feeds `[L, U]`.** Per stratum, per link year:

| Status | Corridor contribution |
|---|---|
| tested-≈0, certificate current | `[−δ_i, +δ_i] ∩ [−K, +K]` (band-file δ; certificate scoped to the audited object, extended to the stratum **under A-T** — printed on this row in every release) |
| first link passed, not yet promoted | `[−K, +K]` (the pass publishes as data; no corridor credit until the second consecutive pass) |
| classified, untested / void link / expired certificate | `[−K, +K]` |
| failed link | `[−K, +K]` + escalation; the audited reading publishes as data, and a reading beyond `K` forces the published `K` reset (proposal §2–§3) |
| demoted to Tier B after two failures | Register bound, **floored at no narrower than `[−K, +K]`** until the Register documents the failure channel (Demotion, above) |

Each release prints the per-tier width accounting, so the reader sees exactly
which certificates, expiries, and failures moved `U − L` — the corridor's
identification-progress series is this table over time.

---

## 7. The Improvements Register

**Purpose.** The symmetric counterpart to the Exclusion Register and the
operational form of Assumption Q (codebook §11): material menu-adjacent
quality *improvements* are documented, monetized, and entered as `I_i`, so
that in Tier B they **move the corridor's lower bound `L`**
(`ρ_i − π_i ∈ [−I_i/E_i, +M_i/E_i]`) instead of silently breaking the bracket
interpretation. It is also, we submit with the proposal, a credibility asset:
a degradation-focused measure that maintains a public ledger of things
getting *better* is materially harder to dismiss as advocacy. The scaffold is
committed as `data/improvements-register.json`, mirroring
`data/ledger-events.json`'s `_schema`-plus-array pattern **with the
deviations stated in the scaffold itself rather than a false mirror claim**
(the ledger's array key is `events`, the register's is `entries`; the
register adds link-year, tier, corridor-use, and interval-flag fields and
extends the status enum).

**Link-year scoping (load-bearing, so stated as a rule, not left implicit).**
`I_i` and `M_i` bound a 12-month object — A-K is explicitly *per link year* —
so every register magnitude is link-year-scoped: **an improvement belongs to
exactly the link year containing its effective date (codebook §6 applied
symmetrically) and feeds that link year's `I_i` only.** Stated consequence:
both Tier-B candidates below (AEB ~2023, the OTC contraceptive 2024) fall in
link years that precede any corridor print this project will ever make, so
**neither can ever feed live `I_i` arithmetic** — they are machinery
demonstrations and A-Q evidence-base entries, filed as exactly that.

**Inclusion threshold (structural; the numeric de-minimis floor is NOT set
here).** An improvement is registrable iff all four hold:

1. **Documented and dated** — a seller-attributable, dated menu change
   evidenced by a primary record (the T1 discipline run in reverse), not
   diffuse quality drift and not a hedonic judgment;
2. **Menu-adjacent** — the improvement appears on the posted menu as an
   inclusion added, a named fee eliminated or reduced, or a new tier that
   weakly dominates a frozen profile at lower cost (menu-expansion
   monotonicity's negative-event grammar, codebook §4);
3. **Monetizable by the reverse route hierarchy** — the codebook §5 ladder
   run in reverse (named fee eliminated > à-la-carte price removed > tier
   delta compressed), with the same interval-and-flag discipline where only a
   superset-style route prices it (the scaffold's `superset_route_flag`);
4. **Above the materiality floor.** Stated plainly, because a discussant can
   ask to see the mirror: **no Exclusion-side floor exists today** — the spec
   keeps the Exclusion Register a census (counts + affected expenditure)
   precisely so boundary migration stays observable, and A-R's
   "above-threshold event" phrase is uncommitted anywhere. The G4 register
   commit therefore sets **one shared numeric floor governing both registers'
   corridor arithmetic simultaneously** — it gates `M_i` and `I_i` corridor
   entry only, while the Exclusion census itself stays floor-free for
   observability. A mirror by construction, not a reference to a nonexistent
   referent; its first existence is that commit (§9 item 6).

**The admissibility asymmetry, named (it was previously shipped as
"parity", which it is not).** The evidence *format* bar is Exclusion-parity
(codebook §12: manifest hash, seller's own document, ≥1 independent
corroboration, provenance tags per `data/incidence-proxies.md`, incidence per
codebook §8 — usable tag or the published [0%, 100%] interval). The
*admissibility* bar is deliberately stricter: `M_i` admits diffuse,
third-party-monetized degradations (the plan's P7 route — facility fees and
coverage erosion with HCCI/MedPAC/KFF magnitudes), while `I_i` additionally
requires menu-adjacency (condition 2) and reverse-route monetizability
(condition 3). The direction of the resulting bias matters and is the
opposite of comfortable: understating `I_i` does not make the corridor
conservative — it can push the true `ρ_i − π_i` below `−I_i/E_i` and
**invalidate `L`**, quietly breaking the bracket rather than widening it. We
keep the strict bar — monetizing diffuse improvements by hedonic judgment is
exactly what this register must never do — and we therefore name what the
choice assumes: **the A-Q residual clause (proposed for the proposal §3
ladder with its own sensitivity row): no economically material
non-menu-adjacent improvement in a Tier-B stratum whose omission would push
`ρ_i − π_i` below `−I_i/E_i`.** Two teeth keep it falsifiable rather than
decorative: (a) the **threshold-rejection log publishes as a public
artifact** — every candidate rejected at the menu-adjacency or
monetizability test, with its rejection reason; (b) the **A-Q bounty extends
to rejected candidates** — a third party defensibly monetizing a rejected
improvement is an A-Q hit under the correction protocol, closing the
loophole by which a rejected candidate was never "missed" and so escaped the
bounty by construction. Whether this bar or full admissibility parity
(third-party-monetized improvements entering `I_i` at the `M_i` evidence
bar, interval-and-flagged where monetization is weak) is the right rule is
put to the discussant (§9 item 4(f)).

**No netting**: improvements and degradations never offset within an entry or
a stratum line — `I_i` and `M_i` are separate sums, published separately.
**No double-counting across tiers, with the semantics split correctly:**

- **Tier R (measured):** an improvement prints through codebook §4's
  negative-event grammar in the Inclusion Ledger **only where it creates a
  cheaper weakly-dominating path or eliminates/reduces a named fee**;
  otherwise it is a **frozen-vector non-event** (irrelevant to every frozen
  baseline — the AT&T exhibit below). In both cases it contributes **zero**
  to `I_i`, and the register entry is evidence/cross-reference:
  `ledger_crossref` is required once the ledger event exists in the first
  case, and stays **null by rule, with the non-event ruling cited**, in the
  second.
- **Tier A (audited):** strata are unmeasured — no Inclusion-Ledger path
  exists at all. Register entries are A-Q evidence only, zero `I_i`.
- **Tier B (register-bounded):** the entry feeds its link year's `I_i`,
  incidence-weighted exactly as `M_i` events weight (codebook §8).

**Symmetric bounty**: A-R's third-party falsification channel applies to this
register identically — a documented improvement we missed is an A-Q hit
handled by the correction protocol, exactly as a missed degradation is an A-R
hit; and per the extension above, so is a defensibly-monetized rejected one.

**First candidate entries — EXAMPLES ONLY, none evidence-grade.** All three
are `status: candidate` in the scaffold, with null verification dates; no
magnitude is asserted for any of them, because none has been byte-verified
and this project does not print unverified numbers:

- **New vehicles (Tier B):** automatic emergency braking becoming standard
  equipment across the US new-vehicle fleet (the industry voluntary
  commitment reported substantially complete circa 2023–24, with a federal
  standard finalized subsequently) — a documented inclusion added to the
  posted configuration at the stratum level. Its link year (~2023) precedes
  the corridor's first computed link: **a machinery demonstration and A-Q
  evidence-base entry, never a live `I_i` feed.** [owner-verify: commitment
  completion reporting, FMVSS rule number and compliance date, and whether
  the change is menu-posted per seller or industry-wide.]
- **Medical OOP (tier pending an owner ruling, A-H territory):** the first
  over-the-counter daily oral contraceptive (launched 2024), converting a
  prescription-gated experience into a posted-price retail path — an
  access-expansion candidate. Filed with **tier null**, because the natural
  destination stratum (Nonprescription drugs) is **Tier A in the tier map**
  while the improved experience originates in the prescription-gated
  medical-OOP path (Tier B under A-H): a B-stratum ruling makes it a
  link-year-dead `I_i` machinery demonstration; an A-stratum ruling makes it
  A-Q evidence with zero `I_i` — both branches are spelled out in the entry,
  and rejection at the menu-adjacency test is an acceptable outcome on
  either. [owner-verify: launch date, posted national price, stratum ruling,
  menu-adjacency ruling given the persisting prescription path.]
- **Wireless (Tier R — the non-event cross-reference case):** AT&T's April
  2026 legacy-plan increases paired with hotspot-data additions (already
  web-verified in the plan, §2.2). This is the boundary exhibit, and it is a
  **codebook §4 non-event**: wireless is measured, and extra hotspot is
  irrelevant to a frozen baseline that lacked it — the plan's stated point is
  that the index *correctly ignores* it — so **no ledger event will ever
  exist to cross-reference, and the entry's `ledger_crossref` is null by
  rule**, non-event ruling cited. The entry exists to demonstrate that the
  register does not launder hedonic offsets into measured strata.
  [owner-verify: capture the AT&T notice pages before they rotate.]

---

## 8. Hours, honestly

Single-operator dependency is structural and disclosed, here as everywhere:
every audit capture, evaluation, and register entry runs through one person,
on top of a Phase 1 load **estimated** at ≈8.7–9.7 h/month (the
pre-registration §6 component sums; wave 0 — September 2026 — is the first
committed wall-clock *measurement*, so nothing is "measured" yet) with a
9.0 h de-scope trigger that reads **the committed whole-wave wall-clock
total** (Step-0 through Step-6, all sectors — only the de-scope *order* sheds
air cells first). The corridor does not get to pretend otherwise, so:

- **Steady-state incremental load, all three protocols live (estimate, to be
  replaced by measured timings):** AP-1 ~10–15 min/wave + AP-2 ~30 min/wave +
  AP-3 ~20–30 min/wave + ingestion/diff ~20 min/wave ≈ **1.3–1.6 h/month**,
  riding inside the Step-1 static-capture layer; **December/January extras**
  (annual bill computations, band evaluation, register refresh) ≈ **2–4 h**
  in the first cycle, less once the bill scripts exist. Promoted strata drop
  to December + January capture (§6), which is what lets the program add
  protocols without unbounded accretion.
- **The arithmetic, stated, because an earlier draft's gate was dead on
  arrival by its own numbers:** at the Phase 1 estimates, even AP-1 alone
  puts the combined monthly total at ≈10.0 h, and all three protocols give
  ≈10.0–11.3 h — **never single-digit**. A gate written on a single-digit
  *combined* total therefore admits zero protocols forever while presenting a
  three-protocol steady state; we do not ship that. Three-protocol steady
  state at single-digit combined hours is reachable only if the Phase 1
  de-scope to 15 routes fires (~7 h/wave, restoring ≈9.3–9.6 h/month combined
  headroom) or measured timings come in under estimate.
- **Activation gate (re-specified so it can neither deadlock nor silently
  bloat):** each protocol's first wave is an unpublished dry run whose
  wall-clock time is logged in the capture JSON and committed. The next
  protocol in rotation activates only if the **audit program's committed
  incremental monthly total** stays within the **audit-program hours ceiling
  — a number whose first existence is the G4 commit** (the same
  first-existence treatment as the register floor). Every activation prints
  the combined monthly total (Phase 1 + audits); two consecutive waves of
  double-digit combined totals de-scope the audit program **last activated,
  first shed** (deterministic — the reverse of rotation order), mirroring
  Phase 1's own 9.0 h machinery without double-counting against it. And the
  consequence in both directions, printed: if Phase 1 stays at estimate and
  its de-scope never fires, the audit program plateaus below three protocols,
  the certified Tier-A share stays correspondingly small (§6's ceiling), and
  the release says so.
- The register is event-driven, not wave-driven: entries are drafted when the
  monthly press watch or a third-party submission surfaces a candidate
  (~0–1 h/month, honestly lumpy).

---

## 9. Open items

1. **Real weights.** The binding rotation order needs the owner's Table
   1101 / R-CPI-I pull; every share above is MOCK from the tier map.
2. **Owner byte-verification queue:** EIA weekly fuel series (IDs, URLs,
   publication cadence) and AAA pages; the EIA gallons-pinning source (§3);
   the CPI-vs-EIA circularity check (§3); EIA-861 and the gas-side analog,
   plus the IOU frame-share figure (§4); Census city-population file
   vintage; **official CPI stratum names for all six audited strata — all
   six need byte-verification on an unblocked connection regardless of the
   tier map's per-row flags** (only one of the six carries a ✓verify flag in
   the map; the flags mark name-uncertainty, not the verification
   obligation); CPI's tax/surcharge treatment in the utility strata;
   per-utility rider-posting surfaces; the three register candidates' facts.
   All flagged inline above.
3. **Scripts to exist before any band file signs off:**
   `pipeline/audit_rotation.py` (implementing §2's frozen bundle/c/slug
   conventions), `pipeline/select_audit_utilities.py`,
   `pipeline/select_audit_cities.py`, `pipeline/audit_energy_bill.py` (+
   tests), and `targets.tsv` audit rows.
4. **Discussant questions carried from proposal §7 Q3, sharpened here:**
   (a) band-width construction for tariff audits, now framed by §1.2's
   power/width dilemma — GB's width rationale was grocery-specific,
   commodity-shock dispersion in energy is larger, and δ_i < K is required
   for corridor credit; (b) the archival-first promotion ruling (§6); (c)
   whether a government series may be an audit's observation of record under
   the inherited-survey-design rule (§1.3/§3); (d) whether per-stratum
   certification with bundle-level apparatus is the right granularity, or
   certification should be per protocol; (e) **A-T** — is the
   object-to-stratum transfer, with the object-rotation falsification test,
   an acceptable ladder rung as drafted (§1.1), and should it enter the
   proposal §3 ladder in that form; (f) the Improvements Register
   admissibility choice — strict bar plus the named A-Q residual clause, or
   full admissibility parity (§7).
5. **G4 placement** (sub-gate of G3 vs standalone) — proposal §8's open
   question; this document inherits whatever the review decides.
6. **The shared materiality floor** — one number governing both registers'
   corridor arithmetic (`M_i` and `I_i` entry; the Exclusion census stays
   floor-free), first existence = the register's binding G4 commit, not
   before [owner decision at commit].
7. **Proposal §3 ladder additions** — A-T (§1.1) and the A-Q residual clause
   (§7) are proposed here but enter the ladder only through the proposal's
   own governance after the review.

## Changelog

- v0 (2026-07-11, same-day revision from two independent adversarial reviews;
  31 findings adjudicated, none rejected) — load-bearing corrections: A-T
  named, scoped, and given a falsification test (certificates read "on the
  audited object, under A-T"; ρ_i^obj notation un-overloads proposal §1's
  ρ_i; per-protocol what-this-audit-does-not-identify lines); §1.1/§6
  certification unified (a pass = one of two consecutive; the
  passed-but-unpromoted year contributes [−K,+K]; the feed table restores
  proposal §2's ∩[−K,+K] truncation; δ_i < K informativeness requirement and
  the power/width dilemma stated as §9.4(a)'s framing); GB re-scoped to
  control-only audit #0, no promotion clock; Part 1 generalized to a
  band-file-named contrast with the same-object wedge as default (AP-1's
  grade-mix statistic demoted to an unbanded diagnostic; the degenerate
  same-object wedge is AP-1's Part 1; inherited-survey-design rule for
  public-series objects; gallons source and cross-grade aggregation pinned;
  per-stratum comparators, parent aggregate demoted to fallback); AP-3's
  Part 1 defined; rotation bundles, c, and the slug list frozen in this
  document with a MAY-NOT wall at the weight-file hash (tuning surface
  closed; mixed-bundle c defined; activation window defined); N/M/P pinned
  in band files before input pulls, drop/substitution predicates made
  operational with registered-capture evidence obligations, default-schedule
  tie-break added; the January confirmation wave carved out of the skippable
  allowance with its own miss ladder; the tariff-specific
  in-force-as-of-December link-substitute rule; post-promotion cadence and
  the certified-share ceiling stated; demotion decided by pre-stated
  observables with the failure-never-buys-narrowness floor and the R-queued
  bound stated; Improvements Register link-year rule added (AEB/OTC
  candidates marked corridor-dead), the admissibility asymmetry named as the
  A-Q residual clause with a public rejection log and bounty extension, the
  nonexistent-mirror floor claim replaced by the shared-G4-floor
  construction, the OTC entry's tier made conditional on the owner ruling,
  the Tier-R/Tier-A cross-reference semantics split (non-event crossrefs
  null by rule); §8 hours restated as estimates with the whole-wave trigger
  corrected and the activation gate re-specified around a G4 audit-program
  ceiling, dead-gate arithmetic printed; the utilities revisit trigger
  re-homed to the plan §1 coverage map (tier-map erratum logged); "largest
  non-food Tier-A mass" corrected to the rotation-statistic statement;
  six-strata verification task corrected; register JSON schema/id/field
  repairs (link_year, superset_route_flag, owner_tasks, id-granularity rule,
  stated deviations from the ledger pattern, incidence's role in I_i
  pinned).
- v0 (2026-07-11) — first draft for the August discussant packet: audit
  template generalized from GB (object, two-part test, provenance ladder,
  band-file first-existence discipline, failure semantics); pre-committed
  rotation formula with the AP-1/AP-2/AP-3 worked ranking (MOCK weights);
  the three lead protocols specified (frozen objects, deterministic sample
  sketches, owner-machine capture designs, comparators, failure semantics);
  rotation governance (two-link promotion, 3-year mechanical expiry,
  demotion, void semantics, corridor feed table, worked promotion trace);
  Improvements Register (threshold, evidence parity, no-netting,
  cross-reference rule, three [owner-verify] candidates); honest hours with
  the activation gate; companion scaffold `data/improvements-register.json`.
  Pre-review; becomes binding only via the proposal §8 governance (G4).
