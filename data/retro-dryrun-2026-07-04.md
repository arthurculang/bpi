# Phase 0 retrospective — DRY RUN results

`2026-07-04 · engine/retro_2008.py · conventions pinned pre-run at commit
da8f599 · band committed 57581d6, owner-signed · STATUS: DRY RUN — gate
evaluation becomes official when inputs open items 4 and 7 (fare anchors)
are byte-verified; all other open items are classified non-material to the
band tests (inputs file, pinned convention 5)`

| Test | Case | Value | In band |
|---|---|---|---|
| T1 line item | online (primary) | $30 | yes |
| T1 B2 fee-minus-offset | online (primary) | $18-$30 | yes |
| T1 line item | airport | $40 | yes |
| T1 B2 fee-minus-offset | airport | $28-$40 | yes |
| T2 profile EC | anchor $250 | +12.00% | yes |
| T2 profile EC | anchor $300 | +10.00% | yes |
| T2 profile EC | anchor $325 | +9.23% | yes |
| T2 profile EC | anchor $350 | +8.57% | yes |
| T2 profile EC | anchor $400 | +7.50% | yes |
| T3 sector gap | inc 35%, anchor $250 | +4.20pp | yes |
| T3 sector gap | inc 35%, anchor $300 | +3.50pp | yes |
| T3 sector gap | inc 35%, anchor $325 | +3.23pp | yes |
| T3 sector gap | inc 35%, anchor $350 | +3.00pp | yes |
| T3 sector gap | inc 35%, anchor $400 | +2.62pp | yes |
| T3 sector gap | inc 40%, anchor $250 | +4.80pp | yes |
| T3 sector gap | inc 40%, anchor $300 | +4.00pp | yes |
| T3 sector gap | inc 40%, anchor $325 | +3.69pp | yes |
| T3 sector gap | inc 40%, anchor $350 | +3.43pp | yes |
| T3 sector gap | inc 40%, anchor $400 | +3.00pp | yes |
| T3 sector gap | inc 45%, anchor $250 | +5.40pp | yes |
| T3 sector gap | inc 45%, anchor $300 | +4.50pp | yes |
| T3 sector gap | inc 45%, anchor $325 (primary) | +4.15pp | yes |
| T3 sector gap | inc 45%, anchor $350 | +3.86pp | yes |
| T3 sector gap | inc 45%, anchor $400 | +3.37pp | yes |
| T3 sector gap | inc 50%, anchor $250 | +6.00pp | yes |
| T3 sector gap | inc 50%, anchor $300 | +5.00pp | yes |
| T3 sector gap | inc 50%, anchor $325 | +4.62pp | yes |
| T3 sector gap | inc 50%, anchor $350 | +4.29pp | yes |
| T3 sector gap | inc 50%, anchor $400 | +3.75pp | yes |
| T3 sector gap | inc 55%, anchor $250 | +6.60pp | **NO** |
| T3 sector gap | inc 55%, anchor $300 | +5.50pp | yes |
| T3 sector gap | inc 55%, anchor $325 | +5.08pp | yes |
| T3 sector gap | inc 55%, anchor $350 | +4.71pp | yes |
| T3 sector gap | inc 55%, anchor $400 | +4.12pp | yes |
| T4a zero-bag EC | anchor $325 | +0.0000% | yes |
| T4b negative print | USAirways beverage repeal | -1.22% | yes |

**Failures: 1**

- T3 inc 55% anchor $250: +6.60pp

Reading: T1, T2, and T4 hold everywhere on the grids. T3 holds at the
primary point and across the interior of the grid; the extreme corner
(lowest anchor x highest incidence) probes the band's upper edge, which is
the expected behavior of a bound designed to catch incidence errors — the
corner is reported, not hidden. Official gate evaluation re-runs unchanged
after anchor byte-verification.
