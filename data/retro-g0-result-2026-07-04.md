# Phase 0 retrospective — OFFICIAL G0 RESULT

`2026-07-04 · engine/retro_2008.py · band committed 57581d6 (owner-signed),
conventions pinned da8f599, fare anchors byte-verified from BTS. Inputs open
items 4 and 7 closed. This is the official gate evaluation, not a dry run.`

## GATE: PASS

Evaluated at the pre-committed primary point — byte-verified annual anchor
(2007 $325.26 → 2008 $346.38, BTS current dollars,
+6.49% matched-fare) at primary incidence 45%:

| Band test | Value | In band |
|---|---|---|
| T1 line item (online) | $30.00 | **yes** |
| T2 one-bag profile EC | +9.22% | **yes** |
| T3 sector gap | +4.15pp | **yes** |
| T4a zero-bag EC = 0 | +0.0000% | **yes** |
| T4b negative print <= 0 | -1.21% | **yes** |

All four band tests hold at the primary. The retrospective reproduces the
documented 2008-09 checked-bag unbundling within the band committed before
any inputs existed — the primitive is validated; Phase 1 is unblocked.

## Sensitivity grid (incidence x anchor)

Reported per pinned convention 2; the gate is the primary above, not the grid.
| Test | Case | Value | In band |
|---|---|---|---|
| T1 line item (airport) | airport fees | $40 | yes |
| T2 profile EC | anchor $250 | +12.00% | yes |
| T2 profile EC | anchor $300 | +10.00% | yes |
| T2 profile EC | anchor $325 | +9.23% | yes |
| T2 profile EC | anchor $350 | +8.57% | yes |
| T2 profile EC | anchor $400 | +7.50% | yes |
| T3 sector gap | inc 35% x $250 | +4.20pp | yes |
| T3 sector gap | inc 35% x $300 | +3.50pp | yes |
| T3 sector gap | inc 35% x $325 | +3.23pp | yes |
| T3 sector gap | inc 35% x $350 | +3.00pp | yes |
| T3 sector gap | inc 35% x $400 | +2.62pp | yes |
| T3 sector gap | inc 40% x $250 | +4.80pp | yes |
| T3 sector gap | inc 40% x $300 | +4.00pp | yes |
| T3 sector gap | inc 40% x $325 | +3.69pp | yes |
| T3 sector gap | inc 40% x $350 | +3.43pp | yes |
| T3 sector gap | inc 40% x $400 | +3.00pp | yes |
| T3 sector gap | inc 45% x $250 | +5.40pp | yes |
| T3 sector gap | inc 45% x $300 | +4.50pp | yes |
| T3 sector gap | inc 45% x $325 | +4.15pp | yes |
| T3 sector gap | inc 45% x $350 | +3.86pp | yes |
| T3 sector gap | inc 45% x $400 | +3.37pp | yes |
| T3 sector gap | inc 50% x $250 | +6.00pp | yes |
| T3 sector gap | inc 50% x $300 | +5.00pp | yes |
| T3 sector gap | inc 50% x $325 | +4.62pp | yes |
| T3 sector gap | inc 50% x $350 | +4.29pp | yes |
| T3 sector gap | inc 50% x $400 | +3.75pp | yes |
| T3 sector gap | inc 55% x $250 | +6.60pp | over |
| T3 sector gap | inc 55% x $300 | +5.50pp | yes |
| T3 sector gap | inc 55% x $325 | +5.08pp | yes |
| T3 sector gap | inc 55% x $350 | +4.71pp | yes |
| T3 sector gap | inc 55% x $400 | +4.12pp | yes |

Grid corners outside the band: 1 — all at incidence ABOVE the 45% primary and the lowest ($250) anchor (e.g. 55% x $250 = +6.60pp). The band's own rationale anticipates the upper edge as the incidence assumption is pushed up; these are sensitivity, not gate failures, and are shown, not hidden.
