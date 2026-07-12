# The Restoration Corridor (RX-100) — a 100%-of-basket concept

`v0 · 2026-07-07 · workstream E · STATUS: CONCEPT / design direction — owner-greenlit 2026-07-06 to document, NOT binding. Any full-basket headline goes through discussant review and a dedicated pre-committed gate first; nothing here touches the signed-off Phase 1 pre-registration, the G0/G1 bands, or the wave schedule. All numbers are illustrative (mock), for shape only.`
`Formalized for external review as docs/rx-100-proposal.md (2026-07-07) — the estimand + partial-identification version submitted to the August methods packet. This note remains the internal design record; the proposal is the discussant-facing artifact.`

## Why this exists

The mature product covers ~26% of bottom-40 spending with the Gap and
zero-imputes the rest. The owner's objection (2026-07-06): *"if we only express
a gap on 26% of spending, the other 74% could be going the opposite direction —
then you haven't learned anything about how much the consumer is hurting."*

The objection is correct, and it exposes a real flaw: **zero-imputation is a
disguised point estimate.** "Cover 26%, impute zero on the rest" silently
assumes the gap is *exactly zero* on 74% of the basket — an assumption that can
be wrong in either direction and that is currently invisible. The fix is not to
defend the 26% number. It is to **stop assuming a value for the remainder and
start bounding it**, over 100% of the CPI consumption basket, with named and
falsifiable assumptions in place of the hidden one.

This memo conceptualizes that extension: the **Restoration Corridor**, a
partial-identification interval `[CPI + L, CPI + U]` covering the whole basket,
published as the full-basket companion to the point-identified covered-sector
Gap. It never becomes a rival index and never makes a "true inflation" claim
(the no-"true-inflation" house rule; the unconditional upper-bound property, spec P4; spread-only publication, Knob 3) — it is a spread interval over official CPI.

## 1. Two things wrong with "26%", one of them just arithmetic

- **The denominator argument, now computed — and corrected downward
  (2026-07-12, `data/coverage-restatement-2026-07-12.md`).** The hypothesis
  here originally read: CE total outlays include ~11% pensions/insurance
  outside the CPI basket, so restating coverage in basket space lifts ~26% to
  ~30–35%. **Real B40 data says otherwise: bottom-40 households put only 6.6%
  into pensions/insurance/cash contributions, so the scope restatement buys
  ≈1pp — the computed restoration-priced share is 18.9–20.7% of the B40
  consumption basket at the Phase-2 composition.** The bigger CE-vs-CPI-weight
  wedge ran through the OER treatment — now computed with the registered
  Dec-2023 R-CPI-I vintage: Phase-2 composition **17.7% of the true B40
  basket**, full Tier R ≈23%, OER 24.0% (rent 12.9%). The
  original overstated hypothesis is retained here struck-through in spirit and
  logged, because correcting our own optimistic numbers in public is the
  measure's posture.
- **The "remainder" is not one undifferentiated unknown.** It decomposes into
  sectors where CPI is adequate *by construction or by audit* and a genuinely
  hard tail — see the tier map below.

## 2. The architecture — three evidentiary tiers over 100% of the basket

Every published CPI item stratum is classified, by a **pre-registered mechanical
rule committed before any corridor arithmetic** (the anti-cherry-picking spine,
parallel to hash-committing the G0 band before results), into exactly one tier:

| Tier | Meaning | Example strata (illustrative B40 CPI-basket weight) | Contribution to the corridor |
|---|---|---|---|
| **1 — Measured** | Restoration-priced: menu grammar holds and a commensurable CPI comparator exists | rent (~18–20%), connectivity + streaming (~6%), air (~0.6%), lodging (~0.6%) | the measured point, keeping existing superset `[0, tier-gap]` and incidence `[0%,100%]` sub-intervals |
| **2 — Tested** | No menu grammar, but posted per-unit / tariff prices let us *audit whether CPI already captures the sector* and publish that it passed | food-at-home (~11%, the grocery null control generalized), motor fuel + household energy (~8%), utility tariffs (~9%) | a tight, verified band `w·[−δ, +δ]` conditional on the audit passing its pre-committed band; an audit **failure** escalates the stratum to Tier 1 candidacy by rule, never silently |
| **3 — Bounded** | Neither grammar nor an auditable comparator — bounded by documented magnitudes, not silence | medical OOP (~7%), owners' equivalent rent (~19%), apparel / personal care / misc (~5%) | `w·[−I/E, +M/E]`, where M is the Exclusion Register's monetized degradation magnitude and I is the symmetric magnitude from a new **Improvements Register** |

Interval arithmetic across the tiers yields the full-basket spread. The **width
`U − L` is itself a first-class published statistic** — the honest measure of
what is not yet known — and it shrinks as strata migrate upward (a new Tier-1
module, a passed Tier-2 audit), so the coverage roadmap becomes a visible
identification-progress series: *"the corridor is tightening."*

**Tier 2 is the load-bearing idea.** It converts the grocery null control from a
*defensive* device ("look, we don't manufacture gaps") into an *offensive*
instrument ("here are the ~24% of the basket — computed, Dec-2024 CPI-U join — where we tested CPI and it passed").
Publicly showing where CPI **works** both narrows the corridor and is the
strongest available inoculation against the "you're just CPI-bashing" attack.

## 3. The point-identified floor — 100% of the basket, today, for free

One component is point-identified for the entire basket **now, from published
data, at zero collection cost**: the **weighting effect**,
`Σ (w_B40 − w_CPI-U) · π_i` — the bottom-40 basket vs. CPI-U's average-household
weights, applied to the published CPI item relatives (codebook §9 already
specifies this term). It is an R-CPI-I-style exhibit under this project's pinned
weight vintage (P11), and it reconciles against the published R-CPI-I
lowest-quintile series computed under the pinned vintage rules as a built-in correctness check (the spec's Seam-2 ≈0.28pp/yr figure is the bottom-vs-top quintile gap — an order-of-magnitude anchor for pure reweighting, not this exhibit's expected value against CPI-U).
It ships as a labeled standing exhibit almost immediately. **Near-term win #2.**

The reweighting term is kept as the corridor's *floor*, never as the product —
the spec's Seam-2 analysis shows pure reweighting buys effects on the order of ~0.3pp/yr, so the
novelty must live on the price side. The corridor keeps both, in their correct
roles.

## 4. The headline it enables — and the honest failure print

When the **lower bound clears zero**, the release can say (mock):

> *"Across 100% of the CPI basket, keeping last year's life cost a bottom-40%
> household between CPI + 0.2 and CPI + 1.4 points more over the year (over
> the B40-weighted CPI comparator; the headline-CPI-U row adds the
> point-identified weighting effect) — and it exceeded CPI **regardless of
> what happened in the parts we cannot yet price**, under the stated
> assumptions."*

That "regardless of the remainder" clause is *earned*: the possibility that the
remainder moved the other way is priced into `L`, not assumed away. When the
interval **straddles zero**, the honest print is *"the full-basket sign is not
yet identified — here are the audits that would sign it,"* which is itself
informative and is the negative-print-as-feature posture. The corridor never
claims a cost-of-living index, a welfare loss, "true inflation," or a point
value for the remainder.

## 5. The assumption ladder (Manski's law of decreasing credibility, made literal)

Every narrowing assumption is named, ordered weakest-first, and paired with a
falsification test; the release prints the ladder so no single assumption is
silently load-bearing:

- **A-K (outcome space; weakest, always on):** per-stratum `|ρ_i − π_i| ≤ K` per
  link year, K calibrated from observed dispersion (audited-sector gaps,
  R-CPI-SC, and BLS's 2012 counterfactual estimate that the 2009 scheduled-air PPI would have been 1.6% lower without its fee adjustment; mock K ≈ 3pp). Falsified the moment any
  audited sector prints beyond K — which forces a published K reset and a wider
  corridor. Without *any* outcome-space bound the identified set is vacuous
  (±∞), and the release says so — which is itself the answer to "why not just
  extrapolate the measured sectors?" (you can't; extrapolation is banned
  imputation and a selection-bias machine, since Tier-1 sectors were *chosen*
  for restoration fit).
- **A-R (Register completeness; the load-bearing one):** the two Registers
  capture all material menu-adjacent changes above a stated threshold in Tier-3
  strata. Falsified by any third party documenting a missed above-threshold
  event (wire to the correction protocol — effectively a public bounty). If it
  falls, Tier 3 degrades from Register bounds to K bounds and the corridor
  widens — visibly, mechanically, non-fatally.
- **A-Q (no unmeasured improvements; already pre-registered, codebook §11):** now
  *operationalized* by the Improvements Register rather than merely assumed —
  material improvements get monetized into `I_i` and move `L`, instead of
  breaking the bracket.
- **A-H, A-O (the two weakest links, printed as such):** healthcare one-sided
  band (lower contribution 0 under "no documented unmeasured improvement in the
  OOP experience," upper = the Register magnitude; the P7 out-ruling stands —
  it need not be *priced*, only *bounded*); OER bracketing (owner degradation
  ∈ [0, measured rent-sector gap], falsifiable against HOA-fee / escrow data).
  Each ships with a sensitivity row showing the corridor with the assumption
  dropped.

## 6. House-rule compliance

Spread-only over CPI-U / B40-CPI (never a rival level index — Knob 3, spread-only);
no "true inflation," no cost-of-living claim; RX stays an **upper bound** on
constant-experience cost growth *within the restoration-priced strata*
(Assumption Q scoped explicitly to Tier 1); negative and zero prints are
features (the "sign-not-identified" print is one); every bound carries its
provenance and its governing assumption printed beside it.

## 7. Honest tradeoffs (the referee lens)

1. **An interval is less punchy than a number.** "+0.2 to +1.4" does not
   headline like "6% more than CPI." Lead with the sign claim when it holds, but
   accept that a bracket asks more of a reader.
2. **The corridor may be too wide to say much early.** If the Tier-3 tail
   (healthcare + OER) dominates before the Tier-2 audits land, the first prints
   could straddle zero. The audits are what collapse it — real 2027–28 work,
   not a day-one win.
3. **Healthcare (~7% OOP) and OER (~19%) are standing asterisks** — neither can be restoration-priced or audited to ≈0 today, so the corridor carries irreducible width from them for the foreseeable horizon (healthcare has a live revisit trigger — state facility-fee disclosure laws — per plan P7; OER has none). Stated, not hidden.
4. **"Shadowstats with extra steps" is the reputational risk.** The corridor is
   *more* defensible than the point estimate, not less: it is a spread, it
   prices its own ignorance, and it publicly shows where CPI passes — but the
   framing discipline must be airtight, which is why it is gated.
5. **It adds a gate and ~4–6 person-weeks of desk work** (the tier-classification
   concordance, 2–3 audit protocols, the Improvements Register, the corridor
   engine + executable tests) plus a pre-registration — all additive; none of it
   touches the signed-off Phase 1.

## 8. Phasing and governance

- **Phase W (now → alongside Phase 1, published-data desk work, no gate
  conflict):** the denominator restatement into CPI-basket space (near-term win
  #1, folded into the August Table 1101 refresh); the 100%-basket
  weighting-effect exhibit (near-term win #2); and the hash-committed
  full-stratum tier-classification file. No corridor headline; the Q1 2027 print
  is unchanged.
- **Phase A (2027, folded into Phase 2):** stand up the Improvements Register;
  clone the grocery audit to motor fuel / energy and utility tariffs with
  pre-committed bands (g1-band-style docs); publish per-stratum interval
  contributions as a *table of parts*, not a headline.
- **Phase C (2028, behind Gate G3 *and* a new corridor gate — call it G4, with
  its own discussant sign-off):** the first official Restoration Corridor print,
  side by side with the covered-sector composite Gap, with the assumption ladder
  and the width-over-time chart.

The corridor is **additive**: its only near-term deliverables are published-data
exhibits exempt from collection gates, and it never modifies a frozen artifact.
No full-basket claim ships before its gate and discussant review.

## 9. Open questions for the eventual discussant

- Is `A-K`'s dispersion calibration defensible, or does K need an external
  anchor (e.g. a bound derived from the PCE-CPI wedge) rather than
  self-calibration from our own audited sectors?
- Is the Tier-2 "audit CPI and let it pass" band (the GB machinery generalized)
  powerful enough in energy/food strata to certify ≈0 usefully, or do those
  strata stay "classified, untested" (a smaller certified share, never a false
  claim)?
- Does the corridor's width, at realistic first-print magnitudes, leave a
  publishable sign claim — or is the first honest print necessarily
  "sign not identified"? (If the latter, is that still worth publishing as the
  identification-progress baseline?)
- Governance: is G4 a sub-gate of G3 or a standalone round?

## Provenance and status

Produced from a 3-lens / 2-referee design workflow (two design lenses completed
— formal partial-identification and measurement-pragmatist — converging on this
architecture; the product and referee lenses were supplied by the owner's own
review). This is a documented design direction, not a commitment. It becomes
binding only through a dedicated pre-registration and gate, reviewed
externally, per the project's credibility-sequencing discipline.

## Changelog

- v0 (2026-07-07) — first draft; owner-greenlit to document the RX-100 /
  Restoration Corridor concept and queue the two near-term published-data wins.
