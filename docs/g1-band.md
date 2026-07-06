# Gate G1 — Pre-committed pass criteria

`v0 · 2026-07-06 · workstream E · STATUS: committed before any Phase 1 in-scope computation (the git hash of this commit is the timestamp of record) · SIGNED OFF by owner 2026-07-06, accepted as-is (post-adversarial-review text)`

## What G1 tests

Gate G1 governs the first public release (target Q1 2027: the archival-denominator
air exhibit + the exact streaming link + the controls) and the panel's first fully
in-sample annual link — **the 2027 link, December 2026 → December 2027, measured
from the December 2027 wave** (links are December-to-December per codebook §6;
the panel attains 12 months of live coverage in October 2027, a coverage
milestone, not a link). Tests are named **GA–GD** — deliberately not
T1–T4, which would collide with both the codebook's trigger rules (T1–T3) and the
G0 result file's band-test labels. If a test cannot be passed, the release does
not ship; a methods note ships instead. The gate is allowed to bite.

## The tests (binding)

**GA — external discussant review.** The review package (spec + codebook + G0
band and result + the Phase 1 pre-registration + honesty exhibits) goes to the
`docs/discussant-shortlist.md` trio in August 2026. Pass = **written sign-off
from at least one sympathetic-methods reviewer AND at least one critical-prior
reviewer** before publication. No current BLS employees. There is no bypass
path: failed outreach slips the release date; it never bends the gate.

**GB — grocery null control.**
- **GB-archival (gates the Q1 2027 release):** the archival grocery
  reconciliation — the GAO-based downsizing contribution restated under the
  codebook §3 per-unit convention — prints in **[−0.5pp, +0.5pp]** on its
  12-month-equivalent basis. The live-window print (panel spans ~3 months at
  Q1 2027) is **disclosed with its window length and carries no numeric gate**
  — no annualization of a quarter-length window.
- **GB-live (gates the first in-sample release — the 2027 link, Dec 2026 →
  Dec 2027, measured from the December 2027 wave, which is also the first wave
  to close a full 12-month window on the frozen grocery basket):** the first
  fully in-sample 12-month grocery result satisfies BOTH:
  - **GB-i (same-basket downsizing wedge):** the per-unit-minus-sticker wedge
    on the frozen basket ∈ **[−0.5pp, +2.0pp]**. Width rationale: GAO-25-107451
    puts the economy-wide downsizing contribution at ~0.06pp over five years;
    the basket is deliberately tilted toward downsizing-prone categories, which
    can only raise the wedge, so the band tops at +2.0pp; the floor admits
    modest upsizing. A wedge above +2.0pp on a 12-item basket means the
    convention (not the world) is manufacturing a gap.
  - **GB-ii (comparator gap):** |frozen-basket per-unit 12-month relative −
    the CPI food-at-home comparator's 12-month relative| ≤ **3.5pp**. Comparator
    selection rule (fixed now): the CPI food-at-home per-unit research series
    if a covering vintage exists at print time, else the CPI-U food-at-home
    stratum index; the choice is logged, and the full R-CPI-SC reconciliation
    publishes as an addendum when the covering vintage ships. Width rationale:
    a deliberately tilted 12-item basket differs from the full stratum by
    composition; 3.5pp is a measurement-based composition tolerance (item-level
    12-month relatives in food-at-home routinely disperse ±5pp around the
    stratum in commodity-shock years). No sampling language: this is a census
    of a frozen basket, not a sample, and no standard errors are claimed.

**GC — banking negative control.** The archival 2019→latest replication-cost
series for the checking-plus-overdraft profile prints **strictly negative.
Sign test only; magnitude unrestricted** — banding a control's magnitude
invites tuning. The forward quarterly series prints whatever it prints; a flat
2026 live link at 0.0 is a correct zero, not a failure.

**GD — independent rerun.** A named third party (not the owner; the
discussant's designee or an independent RA, executor documented in the release)
reproduces, from the hash-committed archive + public code + the codebook +
the pre-registration alone:
1. the route panel and cell list — the script's output on the hash-committed
   T-100 input file, **plus the logged wave-0 schedule-check additions** (each
   recorded in `data/phase1-inputs.md`'s amendment log with a registered
   capture as evidence; the operating cell list = script output ∪ logged
   additions, and the rerun verifies both parts);
2. every published event relative and every sensitivity-grid cell from archived
   snapshots + the pinned-inputs file;
3. the exact streaming link;
4. both control prints;
each to within **±0.01pp**, and with **disclosure parity**: blocked cells,
Exclusion Register entries, and out-of-band sensitivity corners must appear in
the rerun output exactly as published. (The December link-wave manual-save
upgrade exists precisely so the flagship gap statistic rests on hashed
artifacts, not the author's own agent extractions.)

## Failure handling (fixed now)

Fix-inputs-then-rerun **once**; a second miss fails the gate — no Q1 2027
publication, and a methods note publishes instead. Any post-hoc case for
revising a limit or test is, by definition, a G1 failure with a methods note —
not a re-draw.

## What may and may not change after owner sign-off

The commit introducing this file is the timestamp of record — it precedes any
Phase 1 in-scope computation, which is the property that matters. Between
commit and owner sign-off, corrections from the pre-commit adversarial review
may be applied with a logged amendment; **no in-scope computation may run
before the sign-off checkbox is checked**, so nothing can be tuned to a result.

- MAY (after sign-off): input corrections (dates, amounts, data vintages,
  comparator vintage selections under GB-ii's fixed rule) — every change
  logged in the amendment log; the discussant roster (the shortlist file
  governs; GA's two-sign-off structure does not move).
- MAY NOT (after sign-off): the numeric limits; the four tests and their pass
  conditions; the GB two-stage structure; GC's sign-only form; GD's ±0.01pp
  and disclosure-parity requirements; the failure-handling rule.

## Amendment log

- 2026-07-06 (pre-sign-off, from the adversarial review of the draft package;
  permitted under the correction window above — no in-scope computation has
  run): (1) the GB-live anchor "the October 2027 link" corrected to the 2027
  link (Dec 2026 → Dec 2027, measured from the December 2027 wave) — links are
  December-to-December per codebook §6, and no October "link" exists under the
  binding convention; October 2027 is retained only as the coverage milestone.
  This also fixes GB-live's grocery timing (the basket's first 12-month window
  closes at the same December 2027 wave). (2) GD item 1 extended to cover the
  wave-0 schedule-check additions, which the script's output alone can never
  contain — the rerun now verifies script output ∪ logged additions. No
  numeric limit, test structure, or pass condition changed.

## Sign-off

- [x] **Owner reviewed and accepted the G1 pass criteria as-is — 2026-07-06**
      (decision recorded via session review, after the plain-language decision
      walkthrough and the adversarial-review amendments). The four tests and
      their numeric limits are now fully binding under the MAY/MAY-NOT wall.
