# Methods-review packet — cover memo and reading guide

`v0 · 2026-07-12 · workstream F · accompanies the August outreach (drafts: docs/discussant-outreach-drafts.md); the review gates the first print (G1 test GA: written sign-off from ≥1 sympathetic-methods AND ≥1 critical-prior reviewer; no bypass path — failed outreach slips the date, never bends the gate)`

## What is being reviewed, in one paragraph

A conditional replication-cost price measure: freeze the attribute vector of
what a bottom-40%-income household actually bought last year — including
formerly-included features — and price the cheapest same-seller bundle on
today's menu that weakly dominates it. Published **only as a spread** (the
"Restoration Gap") over the matching official CPI series, with Konüs
upper-bound language in every artifact; never a rival index, never a "true
inflation" claim. Validation is pre-committed: the 2008–09 checked-bag
retrospective **landed inside a numeric band hash-committed before any inputs
existed** (gate G0, passed 2026-07-04). The Phase 1 collection design is
signed and frozen; collection starts October 2026; first print target Q1 2027,
gated on this review.

## The packet (11 artifacts, roles)

| # | Artifact | Role | Status |
|---|---|---|---|
| 1 | Spec v00.02.01 | The formal statement (§2), event grammar, worked examples run as unit tests | Frozen; errata applied 2026-07-12 |
| 2 | Codebook v0 | Binding operating rules: equivalence, triggers, links, incidence discipline | Freezes publicly with the Oct note |
| 3 | G0 band (`docs/g0-plausibility-band.md`) | The pre-commitment instrument — committed before inputs, owner-signed | **Passed**; may not change |
| 4 | G0 result (`data/retro-g0-result-2026-07-04.md`) | The retrospective: all four band tests hold at the byte-verified primary | Official |
| 5 | Phase 1 pre-registration | The frozen collection design: 18-route panel by executable formula, paired-quote protocol, controls | Signed 2026-07-06 |
| 6 | G1 band (`docs/g1-band.md`) | This review's own gate (GA–GD), committed before any Phase 1 computation | Signed |
| 7 | RX-100 proposal (`docs/rx-100-proposal.md`) | **Forward-looking, under review, not adopted**: the full-basket partial-identification corridor | Concept behind its own gate (G4) |
| 8 | Tier map (`docs/rx-100-tier-map.md`) | 187 CPI strata classified R/A/B with real weights — attack the rubric on cases, not in the abstract | Draft, pre-review |
| 9 | Audit protocols (`docs/rx-100-audit-protocols.md`) | The Tier-A CPI-adequacy audit machinery (grocery null generalized) | Draft, pre-review |
| 10 | Coverage restatement (`data/coverage-restatement-2026-07-12.md`) | The weights chain: CE 2024 → CPI-U/CPI-W → true B40 (R-CPI-I Dec-2023 vintage), byte-registered end to end | Computed |
| 11 | Incidence register (`data/incidence-proxies.md`) | Every utilization share with provenance; gaps print as [0%,100%], never assumptions | Standing |

Everything is public in one repository, including this memo, the decision
records, and the corrections log.

## Read this first: the corrections trail (we consider it the strongest exhibit)

Three of our own published hypotheses have already been **corrected downward,
in public, with logged amendments**, before any reviewer asked:

1. Coverage restated in basket space was hypothesized at ~30–35%; real B40
   data showed the pensions exclusion buys ≈1pp — computed **18.9–20.7%** of
   the consumption basket (bottom-40 households put only 6.6% into
   pensions/insurance).
2. The tier map's mock shares (R≈29/A≈33/B≈40) corrected to **23/28/49** under
   the registered true-B40 weights — owners' equivalent rent (24% of the B40
   basket) keeps Tier B near half, which is stated as the corridor's central
   design problem, not hidden.
3. The spec's Seam-2 reweighting figure (≈0.28pp/yr) initially looked
   inconsistent with our byte-grade computation (≈0.43pp/yr) — the flag was
   published, then resolved in spec v00.02.01 as a convention difference
   (geometric-annualized vs simple per-year, same registered series). The
   sequence — flag publicly, then reconcile — is the discipline itself.

The Southwest honesty exhibit is the same posture applied forward: CPI
captures the first checked bag on ~80% of designated quotes, so the measure
**predicts its own headline event prints a small Gap** — a prediction that can
fail in public.

## Suggested reading orders (by seat)

**Index-number theory seat (Fox).** Spec §2 (the conditional cost function:
min-cost permits procurement substitution, forbids attribute substitution) →
G0 band + result (the pre-commitment mechanics) → Phase 1 pre-registration §4
(the paired-quote identification and T3 attribution) → RX-100 proposal §§1–3
(estimand, tier partition, sharpness note, the A-K outcome-space bound) with
the tier map beside it → codebook. The §7 questions we most want your view on:
the estimand's interpretability over the full basket, and whether any
cross-stratum restriction is credible enough to narrow [L, U] beyond the
rectangular bound.

**Critical-prior seat (Greenlees; Sichel alternate).** G0 band **first** —
the claim to attack is that the band predates the inputs (the git history is
the evidence) → G0 result → the honesty exhibits (Southwest small-gap
prediction; groceries null; banking negative) → spec §5 (what CPI already
captures — we expect you to test whether we've been fair to it) → Phase 1
pre-registration (the anti-discretion machinery: executable panel formula,
missingness taxonomy, de-scope order) → RX-100 §7, which ends with the
question we most want answered: **what would make you reject the corridor
outright, and is there a construction you would accept?**

**Distributional seat (Jaravel).** Coverage restatement (the weights chain,
including the corrections) → Phase 1 pre-registration §3 (profiles and
incidence, the [0%,100%] carry-on interval) → RX-100 §4 (the weighting-effect
floor — kept as a floor, never the product) → the Seam-2 discrepancy flag
(item 3 above) → spec §9.1 (incidence as the binding constraint). The question
we most want your view on: whether incidence-weighted experience profiles
fairly represent the coping margin your work documents, and whether the
R-CPI-I inheritance survives the CE ranking critiques.

## Logistics

Paid formal review (honorarium per the project budget memo), written comments
at roughly referee-report depth, September–October window, ahead of the
October pre-registration note. Comments are published alongside the methods
note with the reviewer's permission — favorable or not. The gate is real: no
sign-off structure, no first print.

## Changelog

- v0 (2026-07-12) — first draft, written after the weights-chain closure so
  the packet ships with final computed numbers rather than mocks.
