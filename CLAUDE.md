# Conventions for this repository

## What this project is
"The Restoration Gap" (public brand, adopted 2026-07-04; formal measure name:
Restoration Index / RX; repo codename `bpi` predates the naming decision — do
not rename the repo or resurrect "Better Price Index" publicly, the acronym is
blocked by collisions). Read the spec and project plan at repo root first;
`docs/codebook-v0.md` holds the binding operating rules.

## Hard rules
- **Gate ordering:** `docs/g0-plausibility-band.md` is pre-committed. Do NOT
  compute 2008–09 retrospective *results* until the owner signs off the band
  (checkbox in that file). Chronology/inputs may be corrected with a logged
  change; the band's numeric limits and tests may not.
- **No "true inflation" claims, ever** — in any doc, page, commit, or comment.
  The measure is an upper bound published as a spread; bound language ships in
  every artifact (spec §12, plan P10/P14 discipline).
- **Working docs are versioned in the filename**:
  `_~<Name> vXX.YY.ZZ (YYYY-MM-DD HH-MM).md`, stamp on line 3, changelog at
  bottom. Any substantive edit = version bump + `git mv` + changelog entry.
  Take the timestamp from `date '+%Y-%m-%d %H-%M'` at write time.
- **Spec worked numbers are executable**: if a spec revision changes a worked
  example, update `engine/test_restoration.py` in the same commit
  (`python3 -m unittest discover engine`).
- **Site** (`site/`) is plain static HTML, no build step (plan P15) — keep it
  that way; generators may write committed HTML but nothing builds at deploy.
- Branch: work on `claude/inflation-measure-spec-9jjw9o` unless told otherwise;
  push with `git push -u origin <branch>`.

## Environment gotchas (remote sandbox)
- The egress proxy 403-blocks most non-GitHub hosts: bls.gov, bts.gov, gao.gov,
  ftc.gov, federalregister.gov, carrier/retail sites, web.archive.org, FRED,
  rdap.org. Research agents work via search-snippet triangulation — label such
  sourcing and flag byte-verification as an owner task on an unblocked
  connection. `pipeline/capture.py` runs must happen on the owner's machine.
- GitHub raw works. Verified CE data mirrors:
  `mtkonczal/Blog-Posts-Presentations-and-Testimony` (CE flat-file extract,
  through 2024; path `blogs_2026/01_cex_food_consumption/data/cex_data.csv`)
  and `v4lue4dded/inflation_by_income_percentile` (BLS API JSONs, through 2023).
  `pipeline/build_weights.py` asserts the published anchors — keep it that way.

## Posture
Every number that will appear publicly needs provenance (see
`data/incidence-proxies.md` for the tag pattern) and, where post-Jan-2026,
web verification. Negative and zero prints are features — never tune them
away. When in doubt between rigor and reach, choose rigor; the plan's
credibility-sequencing risk row explains why.
