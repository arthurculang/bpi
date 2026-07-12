# Proposal for external review — the Restoration Corridor (RX-100)

`v0 · 2026-07-07 · workstream E/F · FORMAL PROPOSAL for the August methods-review packet (companion to the internal concept note docs/rx-100-concept.md). Submitted for discussant evaluation, not adopted: RX-100 becomes part of the measure only through a dedicated pre-registration and a new pre-committed gate (G4), and only after this review. It does not modify the signed-off Phase 1 pre-registration, the G0/G1 bands, or the collection schedule. Illustrative magnitudes are labelled "mock."`

## Abstract

The Restoration Gap prices a conditional replication cost — the change in the
minimum-cost, same-seller bundle that weakly dominates a household's frozen
base-period experience — and publishes it *only* as a spread over the matching
official CPI series. At maturity it restoration-prices a computed **18.9–20.7% of the bottom-40%
consumption basket** at the Phase-2 composition (2024 CE data,
`data/coverage-restatement-2026-07-12.md`; an earlier ~30–35% hypothesis was
corrected downward when real B40 data showed pensions/insurance are only 6.6%
of B40 outlays — the correction is logged); under the true B40 weights
(Dec-2023 R-CPI-I vintage, registered) the Phase-2 composition is **17.7% of
the B40 CPI basket** and full Tier R is **≈23%**; the remainder is currently
zero-imputed in the composite.
We propose to replace that zero-imputation — which is an unacknowledged point
restriction — with a **partial-identification interval over 100% of the CPI
consumption basket**: the Restoration Corridor. Every CPI item stratum is
assigned, by a rule committed before computation, to one of three evidentiary
tiers (measured / audited-adequate / register-bounded); each tier contributes a
sub-interval to the aggregate; interval arithmetic returns a sharp bound
`G* ∈ [L, U]` under stated, ordered, falsifiable assumptions. One component —
the reweighting effect — is point-identified for the whole basket today. We ask
the reviewer to evaluate the estimand, the identifying assumptions, the audit
mechanism, and whether the resulting interval supports a defensible broad
statement about price pressure on lower-income households without becoming a
cost-of-living or "true inflation" claim (which the project does not make).

## 1. Motivation and the estimand

The project's covered-sector object is a weighted gap
`G = Σ_i w_i (ρ_i − π_i)` over covered strata `i`, where `π_i` is the published
CPI 12-month relative for stratum `i` and `ρ_i` is the *restoration relative* —
the 12-month growth of the min-cost same-seller replication cost of the frozen
base-period experience in `i`. (The codebook §9 publishes its own two-part
decomposition, with CPI-U weights on the pricing-concept term and the weighting
effect isolated separately; the corridor's estimand below is defined directly
on B40 weights, with its weighting term stated in §4 — the two groupings
reconcile but are not the same identity, and we do not claim codebook §9's
authority for this one.) Covered strata are those where a contractible menu
grammar exists (spec §3.2's priced-restoration test) and a commensurable CPI
comparator exists (a condition that follows from the Gap's definition as a
spread over CPI, not from §3.2).

The limitation the reviewer will recognize immediately: reporting a covered gap on ~26% of
the basket and *imputing zero* on the rest is not "covering 26%." It is a
**point estimate on 100%** — the point being `ρ_i − π_i = 0` for every uncovered
stratum — advanced without evidence and defensible in neither direction.

We therefore define the target estimand over the **full** stratum set `S`
(all published CPI item strata, with bottom-40% CPI-consumption-basket weights
`w_i`, `Σ_{i∈S} w_i = 1`, built on the project's pinned R-CPI-I weight recipe):

> **G\* = Σ_{i∈S} w_i (ρ_i − π_i).**

`G*` is the spread of the B40 restoration aggregate `Σ w_i ρ_i` over the
B40-reweighted CPI aggregate `Σ w_i π_i`. The **restoration aggregate's** gap
to the recomposed headline aggregate `Σ_i w_i^{U} π_i` then decomposes as
`G* + Σ_i (w_i − w_i^{U}) π_i`, the second term being the weighting effect
(§4). (Recomposition caveat: the published all-items CPI-U is a Lowe index
with price-updated weight vintages and special aggregations, so
`Σ w_i^{U} π_i` approximates rather than equals the published 12-month
relative; the reconciliation between the two is published, not assumed.) We state plainly what `G*` is **not**: not
a cost-of-living index, not a welfare measure, not "true inflation." It is the
constant-experience *replication-cost* gap. Within measured strata the
restoration relative is an upper bound on constant-experience cost growth **by
construction, unconditionally** (spec P4); Assumption Q touches only the
*bracket* interpretation — that chained CPI and the Restoration Index together
bound constant-experience cost growth (codebook §11) — and A-Q (§3)
operationalizes exactly that bracket claim for the corridor, scoped to the
measured tier.

## 2. Partial identification: the tier partition

`ρ_i` is directly observed only where the measure prices it. For the rest we do
not impute `ρ_i`; we **bound** `ρ_i − π_i`. A pre-registered classification rule
(an extension of the spec §3.2 priced-restoration test, run over the entire
stratum list and hash-committed before any corridor arithmetic — the
anti-cherry-picking spine, parallel to the G0 band's commit-before-results
discipline) assigns each stratum to one tier:

- **Tier R (measured).** Menu grammar and a commensurable comparator both hold.
  `ρ_i − π_i ∈ B_i^R`, the measured point (retaining the measure's existing
  superset `[0, tier-gap]` and incidence `[0%,100%]` sub-intervals where those
  apply). Computed B40 consumption-basket weight at the Phase-2 composition:
  rent, connectivity, air, lodging: **≈23% of the true-B40 CPI basket**
  (Dec-2023 R-CPI-I vintage; 17.8% under CPI-U; the strict Phase-2
  composition is 17.7% B40 / 12.5% CPI-U) (2024 CE data,
  `data/coverage-restatement-2026-07-12.md`; a prior ~30–35% mock corrected
  downward, correction logged).

- **Tier A (audited-adequate).** No contractible grammar, but posted per-unit or
  tariff prices make CPI's *own* concept testable. A pre-committed audit (the
  grocery null control generalized — see §5) tests `|ρ_i − π_i| ≤ δ_i`. If the
  audit passes its band, `ρ_i − π_i ∈ [−δ_i, +δ_i]`; if it fails, the stratum
  reverts to the outcome-space bound (below) and is flagged for escalation to
  Tier R candidacy by rule, never silently. Illustrative: food-at-home, motor
  fuel and household energy, utility tariffs — computed **24.3% of the CPI-U
  basket** (Dec-2024 relative importance joined to the tier map, 2026-07-12).

- *(A draft classification of the full stratum list under this rule —
  187 strata, six classifier groups harmonized by a cross-group judge — is
  `docs/rx-100-tier-map.md`, supplied as a pre-review input so the reviewer
  can attack the rubric on concrete cases rather than in the abstract.)*

- **Tier B (register-bounded).** Neither grammar nor an auditable comparator.
  `ρ_i − π_i ∈ [−I_i/E_i, +M_i/E_i]`, where `E_i` is base expenditure, `M_i` is
  the Exclusion Register's monetized documented-degradation magnitude for the
  stratum, and `I_i` is the symmetric magnitude from a proposed **Improvements
  Register** (§5). Illustrative: medical out-of-pocket, owners' equivalent rent,
  apparel/personal-care/misc — computed **53.8% of the CPI-U basket**, of
  which owners' equivalent rent alone is 26.3% (Dec-2024 join; **under the
  registered true-B40 vintage: Tier B 47.6%, OER 24.0%, rent rising to
  12.9%**). Tier B's near-half share survives the correct weights — 43–58% of
  B40 households own, so OER stays the corridor's width driver, which makes
  the A-O bracketing assumption the review's single most consequential
  question.

An outcome-space restriction applies to the **unmeasured** strata:

> **A-K:** `|ρ_i − π_i| ≤ K` for all `i` in Tiers A and B, per link year.

The identified set for each Tier-A/Tier-B stratum is the intersection of its
tier band with `[−K, K]`. **Tier R contributes its measured set `B_i^R`
untruncated** — measured points are data and are never censored by an a-priori
bound; instead, any *measured or audited* gap beyond `K` falsifies the
calibration and forces the published `K` reset (§3), so the data disciplines
the bound rather than the reverse. Writing `B_i` for the resulting per-stratum
set (`B_i^R` for Tier R; the tier band ∩ `[−K, K]` otherwise), the per-stratum
sets are rectangular intervals with no cross-stratum restrictions, so the
identified set for `G*` is the sharp interval

> **[L, U] = [ Σ_i w_i · inf(B_i), Σ_i w_i · sup(B_i) ].**

This is the object we would publish: a spread interval over CPI covering 100% of
the basket, with the **width `U − L`** reported as a first-class statistic — the
honest measure of what is not yet identified — which contracts mechanically as
strata migrate R←A←B (a passed audit or a new module), giving the coverage
roadmap a visible identification-progress series.

*(Sharpness note for the reviewer: `[L, U]` is sharp under the maintained
per-stratum rectangular (interval) sets with no cross-stratum restrictions. Any credible **cross-stratum** restriction
— e.g., a bound on the weighted dispersion `Σ w_i (ρ_i − π_i)^2`, or a sign
restriction tied to a common shock — would narrow it. Whether such a restriction
is defensible here is one of our questions in §7.)*

## 3. The assumption ladder (Manski's law of decreasing credibility, made explicit)

Every narrowing assumption is named, ordered least-restrictive-first, and
paired with a falsification test; the release prints the ladder, so no single
assumption is silently load-bearing and the reader sees the identification
cost of each.

| Assumption | Identifying content | Falsification test / failure mode |
|---|---|---|
| **A-K** (outcome space; least restrictive, always on) | Bounds `ρ_i − π_i` to `[−K, K]` on the unmeasured tiers (A and B; Tier R data is never truncated — §2); without *any* outcome-space bound the unmeasured strata's identified set is `±∞` and the release says so | `K` calibrated from observed dispersion (measured/audited-sector gaps, R-CPI-SC, and BLS's 2012 counterfactual estimate that the 2009 scheduled-air PPI would have been 1.6% lower without its fee adjustment; mock `K ≈ 3pp`). Falsified whenever a measured or audited stratum prints beyond `K` → published `K` reset, corridor widens |
| **A-R** (register completeness; load-bearing) | Lets Tier B use Register bounds `[−I/E, +M/E]` instead of `[−K, K]` | Falsified by any third party documenting a missed above-threshold event (wired to the correction protocol — a public bounty). If it falls, Tier B degrades to A-K bounds; corridor widens, visibly and non-fatally |
| **A-Q** (no unmeasured improvement; pre-registered, codebook §11) | Scopes the *bracket* interpretation (chained CPI and RX jointly bounding constant-experience cost growth) to Tier R — the upper-bound property itself is unconditional (spec P4); operationalized (not merely assumed) by the Improvements Register — material improvements enter `I_i` and move `L` rather than breaking the bracket | Falsified by a documented material improvement absent from the Register |
| **A-H** (healthcare one-sided band; most fragile, flagged) | Medical-OOP lower contribution 0 under "no documented unmeasured improvement in the OOP experience," upper = Register magnitude (HCCI/MedPAC/KFF). The P7 out-ruling stands — healthcare is *bounded*, never *priced* | Sensitivity row prints the corridor with A-H dropped; revisit trigger = state facility-fee disclosure laws maturing a menu-posted slice |
| **A-O** (OER bracketing; most fragile with A-H, flagged) | Owner-occupant degradation `∈ [0, measured rent-sector gap]` (HOA-fee/escrow analog of the renter fee stack, no lease-event repricing) | Falsifiable against HOA-fee and insurance-escrow data; sensitivity row with A-O dropped |

Pensions, most insurance, and cash contributions are **excluded from `S` by
definition of the CPI consumption basket** — not imputed. A computed caveat,
logged 2026-07-12 (`data/coverage-restatement-2026-07-12.md`): this exclusion
buys less than originally hypothesized, because bottom-40 households put only
6.6% of outlays into pensions/insurance/contributions — the computed
restoration-priced share is **18.9–20.7% of the B40 consumption basket** at
the Phase-2 composition, not the ~30–35% an earlier mock claimed. The larger
CE-vs-CPI-weight wedge runs through the OER treatment (B40 renters 57%/42%,
captured 2024) and resolves with the R-CPI-I relative-importance vintage.

## 4. The point-identified component (shippable now)

The restoration aggregate's gap to the recomposed CPI-U aggregate is
`G* + Σ_i (w_i − w_i^{U}) π_i` (§1, with the recomposition caveat). The second
term — the **weighting effect** — is fully observed for 100% of the basket
*today*, from published CPI item relatives and the pinned R-CPI-I weights, at
zero collection cost. Its validation is agreement with the published R-CPI-I
lowest-quintile series computed under the pinned vintage rules (the spec's
Seam-2 figure — ≈0.28pp/yr — is the bottom-vs-**top** equivalized-income
quintile gap, cited here only as the order of magnitude of pure reweighting,
not as this exhibit's expected value against CPI-U), and we propose to ship it
first as a standing exhibit and the corridor's floor. We keep it as a *floor
component*, never the product: reweighting alone buys effects on the order of
~0.3pp/yr, so the measure's novelty must remain on the price (restoration)
side. The reviewer should read the corridor as the
price-side interval *plus* this observed reweighting anchor.

## 5. Two new instruments this requires

- **The CPI-adequacy audit (Tier A).** The existing grocery null control is the
  prototype: a frozen per-unit basket priced against the CPI stratum's own
  concept, with a pre-committed pass band (the GB machinery: ±0.5pp archival,
  a `[−0.5, +2.0]`pp same-basket wedge, ≤3.5pp comparator gap). We propose to
  generalize it from a *control* into a rotating *measurement instrument*:
  pre-committed rotation order (basket weight × grammar prior, to bar
  cherry-picking), a two-consecutive-link promotion rule to "tested-≈0" status,
  a 3-year re-audit, and a demotion/escalation rule on failure. Auditing "does
  CPI already capture this?" is far cheaper than building a restoration module,
  which is what makes 100% coverage tractable.

- **The Improvements Register.** The symmetric counterpart to the Exclusion
  Register: a public ledger of menu-adjacent quality *improvements* with
  monetized magnitudes. It is the operational form of Assumption Q — and, we
  submit, a credibility asset: a degradation-focused measure that also maintains
  a public ledger of things getting *better* is materially harder to dismiss as
  advocacy.

## 6. Relationship to prior art, and what this is not

- **Partial identification (Manski).** The corridor is a straightforward
  application: bound what you cannot point-identify, order assumptions by
  credibility, report the identified set, treat its width as information. We
  claim no methodological novelty in the identification apparatus — only in its
  application to a full-basket constant-experience replication cost.
- **Democratic / income-specific price indexes (Jaravel; Kaplan–Schulhofer-Wohl;
  Handbury).** The weighting term (§4) is exactly this literature; we keep it as
  the observed floor, not the headline.
- **Non-official indexes published as spreads (Cavallo/PriceStats).** Precedent
  for a credible index reported as a spread over official series rather than a
  rival level — the discipline we maintain (Knob 3 / spread-only).
- **What this is not:** not a cost-of-living index; not a rival all-items level
  index (we never relitigate Boskin or the shelter debate); not a "true
  inflation" claim (the project makes none, in any artifact); not a
  hedonic/imputation exercise — we explicitly do **not** extrapolate measured
  `ρ_i` to unmeasured strata (that would be banned imputation and a
  selection-bias machine, since Tier-R strata are *selected* for restoration
  fit; the measured sectors inform only `K`'s dispersion calibration — and
  whether grammar-fit sectors bound the dispersion of opaque,
  non-contractible sectors is itself an assumption, not a theorem: it is
  stated as part of A-K, and any audited stratum printing beyond `K`
  falsifies it and forces the published `K` reset).

## 7. What we are asking the reviewer

1. **The estimand.** Is `G* = Σ w_i (ρ_i − π_i)` over the full CPI basket the
   right target for a "broad statement about price pressure on lower-income
   households," or does the constant-experience conditioning make the full-basket
   aggregate less interpretable than the sector-level gaps? Where should we set
   the boundary between "reportable interval" and "report sectors only"?
2. **A-K calibration.** Is calibrating `K` from our own audited-sector dispersion
   defensible, or does it need an external anchor (e.g. a bound derived from the
   PCE–CPI wedge, or from R-CPI-SC)? Is there a *cross-stratum* restriction you
   would consider credible enough to narrow `[L, U]` beyond the rectangular
   bound?
3. **Audit power (Tier A).** Is the generalized CPI-adequacy audit powerful
   enough to certify `≈0` usefully in energy/food strata, or will those remain
   "classified, untested" (a smaller certified share, never a false claim)? Is
   the pass-band construction sound?
4. **The first-print width.** At realistic magnitudes, will the corridor be
   narrow enough to support a signed statement, or is the honest first print
   necessarily "sign not identified"? If the latter, is publishing it as the
   identification-progress baseline worthwhile, or does a wide interval read as
   evasion?
5. **The decisive question we most want answered:** what, specifically, would
   make you *reject* the corridor as a defensible full-basket object — and is
   there a construction you would accept in its place?

## 8. Governance and standing

RX-100 enters the measure only via its own pre-registration and a new
pre-committed gate (**G4**, either a sub-gate of the Phase 3 composite gate or a
standalone round — a question for the reviewer), with the assumption
classification hash-committed before any corridor computation, exactly as the
G0 band was. Nothing in this proposal alters the signed-off Phase 1
pre-registration, the G0/G1 bands, or the wave schedule; the only near-term
deliverables (the coverage restatement and the weighting-effect exhibit) are
published-data desk work. This review is the corridor's first and hardest
audience by design — an ambitious full-basket claim should meet a skeptical
methodologist before it ever shapes a public number.

## Changelog

- v0 (2026-07-07) — first formal draft, for the August discussant packet;
  formalizes the internal concept note `docs/rx-100-concept.md` into an
  estimand + partial-identification proposal with a pointed reviewer ask.
