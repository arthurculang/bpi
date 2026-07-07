# Proposal for external review — the Restoration Corridor (RX-100)

`v0 · 2026-07-07 · workstream E/F · FORMAL PROPOSAL for the August methods-review packet (companion to the internal concept note docs/rx-100-concept.md). Submitted for discussant evaluation, not adopted: RX-100 becomes part of the measure only through a dedicated pre-registration and a new pre-committed gate (G4), and only after this review. It does not modify the signed-off Phase 1 pre-registration, the G0/G1 bands, or the collection schedule. Illustrative magnitudes are labelled "mock."`

## Abstract

The Restoration Gap prices a conditional replication cost — the change in the
minimum-cost, same-seller bundle that weakly dominates a household's frozen
base-period experience — and publishes it *only* as a spread over the matching
official CPI series. At maturity it restoration-prices ~26–35% of a bottom-40%
household's basket; the remainder is currently zero-imputed in the composite.
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

The project's headline object is, per the codebook, a weighted gap
`G = Σ_i w_i (ρ_i − π_i)` over covered strata `i`, where `π_i` is the published
CPI 12-month relative for stratum `i` and `ρ_i` is the *restoration relative* —
the 12-month growth of the min-cost same-seller replication cost of the frozen
base-period experience in `i`. Covered strata are those where a contractible
menu grammar exists and a commensurable CPI comparator exists (spec §3.2).

The limitation the reviewer will recognize immediately: reporting `G` on ~26% of
the basket and *imputing zero* on the rest is not "covering 26%." It is a
**point estimate on 100%** — the point being `ρ_i − π_i = 0` for every uncovered
stratum — advanced without evidence and defensible in neither direction.

We therefore define the target estimand over the **full** stratum set `S`
(all published CPI item strata, with bottom-40% CPI-consumption-basket weights
`w_i`, `Σ_{i∈S} w_i = 1`, built on the project's pinned R-CPI-I weight recipe):

> **G\* = Σ_{i∈S} w_i (ρ_i − π_i).**

`G*` is a spread over the B40-reweighted CPI aggregate `Σ w_i π_i`; its gap to
headline CPI-U decomposes exactly as `G* + Σ_i (w_i − w_i^{U}) π_i`, the second
term being the weighting effect (§4). We state plainly what `G*` is **not**: not
a cost-of-living index, not a welfare measure, not "true inflation." It is the
constant-experience *replication-cost* gap, and it is an upper bound on the
constant-experience cost-of-living gap only within strata where no material
unmeasured quality improvement occurs (Assumption Q, restated in §3 as A-Q and
scoped to the measured tier).

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
  apply). Illustrative B40 weight: rent, connectivity, air, lodging ≈ 30–35%.

- **Tier A (audited-adequate).** No contractible grammar, but posted per-unit or
  tariff prices make CPI's *own* concept testable. A pre-committed audit (the
  grocery null control generalized — see §5) tests `|ρ_i − π_i| ≤ δ_i`. If the
  audit passes its band, `ρ_i − π_i ∈ [−δ_i, +δ_i]`; if it fails, the stratum
  reverts to the outcome-space bound (below) and is flagged for escalation to
  Tier R candidacy by rule, never silently. Illustrative: food-at-home, motor
  fuel and household energy, utility tariffs ≈ 28–30%.

- **Tier B (register-bounded).** Neither grammar nor an auditable comparator.
  `ρ_i − π_i ∈ [−I_i/E_i, +M_i/E_i]`, where `E_i` is base expenditure, `M_i` is
  the Exclusion Register's monetized documented-degradation magnitude for the
  stratum, and `I_i` is the symmetric magnitude from a proposed **Improvements
  Register** (§5). Illustrative: medical out-of-pocket, owners' equivalent rent,
  apparel/personal-care/misc ≈ 35–40%.

A universal outcome-space restriction applies to every stratum:

> **A-K:** `|ρ_i − π_i| ≤ K` for all `i` in a link year.

The identified set for each stratum is the intersection of its tier band with
`[−K, K]`. Because the per-stratum sets are independent rectangles, the
identified set for `G*` is the sharp interval

> **[L, U] = [ Σ_i w_i · inf(B_i), Σ_i w_i · sup(B_i) ].**

This is the object we would publish: a spread interval over CPI covering 100% of
the basket, with the **width `U − L`** reported as a first-class statistic — the
honest measure of what is not yet identified — which contracts mechanically as
strata migrate R←A←B (a passed audit or a new module), giving the coverage
roadmap a visible identification-progress series.

*(Sharpness note for the reviewer: `[L, U]` is sharp under the maintained
per-stratum, rectangular assumptions. Any credible **cross-stratum** restriction
— e.g., a bound on the weighted dispersion `Σ w_i (ρ_i − π_i)^2`, or a sign
restriction tied to a common shock — would narrow it. Whether such a restriction
is defensible here is one of our questions in §7.)*

## 3. The assumption ladder (Manski's law of decreasing credibility, made explicit)

Every narrowing assumption is named, ordered weakest-first, and paired with a
falsification test; the release prints the ladder, so no single assumption is
silently load-bearing and the reader sees the identification cost of each.

| Assumption | Identifying content | Falsification test / failure mode |
|---|---|---|
| **A-K** (outcome space; weakest, always on) | Bounds every `ρ_i − π_i` to `[−K, K]`; without *any* outcome-space bound the identified set is `±∞` and the release says so | `K` calibrated from observed dispersion (audited-sector gaps, R-CPI-SC, the PPI's 1.6% 2009 correction; mock `K ≈ 3pp`). Falsified whenever an audited sector prints beyond `K` → published `K` reset, corridor widens |
| **A-R** (register completeness; load-bearing) | Lets Tier B use Register bounds `[−I/E, +M/E]` instead of `[−K, K]` | Falsified by any third party documenting a missed above-threshold event (wired to the correction protocol — a public bounty). If it falls, Tier B degrades to A-K bounds; corridor widens, visibly and non-fatally |
| **A-Q** (no unmeasured improvement; pre-registered, codebook §11) | Scopes the *upper-bound* interpretation to Tier R; operationalized (not merely assumed) by the Improvements Register — material improvements enter `I_i` and move `L` rather than breaking the bracket | Falsified by a documented material improvement absent from the Register |
| **A-H** (healthcare one-sided band; weak, flagged) | Medical-OOP lower contribution 0 under "no documented unmeasured improvement in the OOP experience," upper = Register magnitude (HCCI/MedPAC/KFF). The P7 out-ruling stands — healthcare is *bounded*, never *priced* | Sensitivity row prints the corridor with A-H dropped; revisit trigger = state facility-fee disclosure laws maturing a menu-posted slice |
| **A-O** (OER bracketing; weak, flagged) | Owner-occupant degradation `∈ [0, measured rent-sector gap]` (HOA-fee/escrow analog of the renter fee stack, no lease-event repricing) | Falsifiable against HOA-fee and insurance-escrow data; sensitivity row with A-O dropped |

Pensions, most insurance, and cash contributions are **excluded from `S` by
definition of the CPI consumption basket** — not imputed. Stating this in the
definitions is where the "26% feels apples-to-oranges" discomfort dissolves: the
26% is a share of CE *total* outlays; restated in CPI-basket space with the
project's B40 weights it is already ~30–35% before any new work.

## 4. The point-identified component (shippable now)

The gap of `G*` to headline CPI-U is `G* + Σ_i (w_i − w_i^{U}) π_i`. The second
term — the **weighting effect** — is fully observed for 100% of the basket
*today*, from published CPI item relatives and the pinned R-CPI-I weights, at
zero collection cost. It reconciles against the published R-CPI-I
bottom-quintile series (~0.28pp/yr above CPI-U) as a correctness check, and we
propose to ship it first as a standing exhibit and the corridor's floor. We keep
it as a *floor component*, never the product: the spec's own analysis shows
reweighting alone buys only ~0.28pp/yr, so the measure's novelty must remain on
the price (restoration) side. The reviewer should read the corridor as the
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
  fit; the measured sectors inform only `K`'s dispersion calibration, where
  selection bias is conservative — it *widens* the interval).

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
