# Gate G0 — Pre-committed plausibility band

`v0 · 2026-07-04 · workstream E · STATUS: committed before any retrospective computation (the git hash of this commit is the timestamp of record) · SIGNED OFF by owner 2026-07-04, accepted as-is`

## What G0 tests

Phase 0 reconstructs the 2008–2009 US airline checked-bag unbundling and computes
the air-travel Restoration Gap the method (codebook v0) *would have printed* for
the 2008 link year. The gate passes iff the results land inside the band below.
If the method cannot reproduce a documented historical event within these bounds,
the primitive is revised before any live-collection spend (plan §4, P8).

## External benchmarks (fixed, already published — not adjustable)

- **B1 — PPI correction:** without BLS's fee adjustment, the PPI for scheduled
  passenger air transportation would have been **1.6% lower in December 2009**
  (BLS Beyond the Numbers vol. 1, 2012). This is a realized, incidence-included
  average-revenue effect of the fee introductions.
- **B2 — Fee-minus-offset wedge:** first-bag fees of **$15–20 per segment**
  against base-fare declines of **~3% (~$5)** (Brueckner–Lee–Picard–Singer 2015;
  Henrickson–Scott ~$0.11 offset per fee dollar) ⇒ net wedge ≈ **$10–15 per
  bag-checking segment**, ≈ $20–30 per round trip for a one-bag profile.

## The band (binding)

Let ρ(P1) be the retrospective link relative for the one-checked-bag round-trip
profile, RX_air the incidence-weighted sector relative, and G_air the sector
Restoration Gap over the matched-fare comparator for the same window.

1. **Line-item bound.** The computed one-bag round-trip restoration line item
   (2×fee − fare offset) must lie in **[$18, $42]** at end-2009 fee schedules
   (= 2×[$15,$20] adjusted by an offset in [$0, $12]). Outside this range the
   event ledger inputs are wrong, not the method — fix inputs first, then
   re-run once; a second miss fails the gate.
2. **Profile-relative bound.** ρ(P1) − 1 ∈ **[+4%, +14%]** on a base one-bag
   round-trip cost in the $250–$400 range (BTS average-fare anchor to be
   documented in the inputs file). Below +4% the method is losing a documented
   event; above +14% it is manufacturing one.
3. **Sector-gap bound.** Incidence-weighted G_air for the 2008 link ∈
   **[+1.0pp, +6.0pp]**. Rationale: RX weights by *base-period* (pre-fee)
   checked-bag incidence, which exceeds the realized post-fee fee-paying share
   embedded in B1's 1.6%; so the gate expects G_air ≥ ~1pp and materially above
   zero, but within the same order of magnitude as B1 — a print above 6pp would
   indicate incidence or superset handling errors.
4. **Sign tests (must both hold).**
   - The zero-bag profile prints **0% event contribution** (menu-expansion
     monotonicity under the trigger rules: no new option in the 2008-09 episode
     weakly dominates the zero-bag profile at lower cost, so its print is exactly
     0%; a dominated profile would print ≤ 0%, never > 0%).
   - The designated historical re-bundling episode (to be selected in the inputs
     file *before* computation, from candidates compiled independently) prints
     **≤ 0%**.

## What may and may not change after this commit

- MAY: the event-ledger *inputs* (dates, amounts) as better primary evidence is
  found — with every change logged; the incidence source chosen for weighting —
  provided it is selected before the sector computation runs.
- MAY NOT: the band's numeric limits; the four tests; the definition of the
  profiles; the choice of comparator window. Any post-hoc case for revising
  these is, by definition, a G0 failure with a methods note — not a re-draw.

## Amendment log

- 2026-07-04: sign-test 4's parenthetical renamed from "option-introduction
  invariance" to "menu-expansion monotonicity" following the spec v00.02.00 P2
  refinement. Wording of rationale only — numeric limits, the four tests, the
  profiles, and the comparator window are unchanged (permitted under "MAY").

## Result

- **2026-07-04 — GATE PASSED.** Evaluated at the byte-verified primary anchor
  (BTS 2007 $325.26 → 2008 $346.38) and primary incidence (45%): line item $30
  (band [18,42]), one-bag profile event contribution +9.22% (band [+4%,+14%]),
  incidence-weighted sector gap +4.15pp (band [+1.0,+6.0]), zero-bag EC exactly
  0%, and the designated negative-print episode (US Airways beverage repeal)
  −1.21% (≤ 0). All four tests hold. The method reproduces the documented
  2008–09 unbundling within limits committed before any inputs existed. Full
  result and sensitivity grid: `data/retro-g0-result-2026-07-04.md`. Phase 1 is
  unblocked (plan §4, P8).

## Sign-off

- [x] **Owner reviewed and accepted the band as-is — 2026-07-04** (decision
      recorded via session review). The band is now fully binding; retrospective
      computation may begin once the input open-items in
      `data/retro-2008-inputs.md` are closed.
