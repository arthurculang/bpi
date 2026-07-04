# The Restoration Gap

**What does it cost to live last year's life?** A replication-cost price
measure for bottom-40%-income US households: freeze the consumption experience
a household actually bought last year — including formerly-included features —
and price the cheapest way to reproduce it on today's menu. Published as a
spread over official CPI series (the "Restoration Gap"), never as a rival
index. Public site: `site/` (deploys to restorationgap.org).

**Status:** pre-launch. Methods pre-registration: Oct 2026 · first print:
targeted Q1 2027. No index values are published yet; everything numeric in
this repo is verified event data or test fixtures, not index output.

## Why

Firms increasingly raise *effective* prices by unbundling included features
into fees (airline bags), moving the old standard behind a premium tier
(ad-free streaming), and redesigning menus so the cheapest option is a thinner
one. Matched-specification CPI answers a different (compensated) question, and
average-spending weights read household coping as savings. This measure holds
the experience fixed and prices its restoration, line item by line item — an
explicit **upper bound** on constant-experience cost growth, reconciled to the
official series it differs from in every release. It is not a "true inflation"
number, and says so everywhere.

## Repository map

| Path | What it is |
|---|---|
| `_~Restoration Index Spec v*.md` | The methodology specification (formal object, worked examples, decisions, hazards) |
| `_~Restoration Index Project Plan v*.md` | Phased plan: coverage map, sector rulings, gates G0–G3, workstreams, next steps |
| `docs/codebook-v0.md` | Operating rules: equivalence protocol, trigger rules, route hierarchy, conventions — freezes as the public pre-registration |
| `docs/g0-plausibility-band.md` | Pre-committed pass/kill band for the 2008–09 retrospective (committed before any inputs/results, by design) |
| `docs/` (other) | Discussant shortlist, DOT docket comment draft, budget memo |
| `data/ledger-events.json` | The Inclusion Ledger event registry (verified unbundling/tiering events, with schema) |
| `data/retro-2008-inputs.md` | Phase 0 inputs: the 2008–09 bag-fee chronology + designated negative-print episode |
| `data/incidence-proxies.md` · `data/cex-b40-quintiles.csv` | Utilization-weight register · bottom-two-quintile CE expenditures (byte-verified) |
| `pipeline/` | Menu-snapshot capture (`capture.py`), targets, weights builder — the evidence archive tooling |
| `engine/` | The replication-cost computation engine; its tests are the spec's worked examples |
| `site/` | The public site (plain static HTML, no build step) |

## Run things

```bash
python3 -m unittest discover engine -v      # engine tests = executable spec examples
python3 pipeline/capture.py                 # snapshot posted menus (see pipeline/README.md)
python3 pipeline/build_weights.py           # rebuild CE quintile weights from source
```

## Method governance, in one paragraph

Pre-registered methods frozen before live collection; a retrospective
validation gate (G0) with a band committed before results existed; external
review before the first print and again before any composite; negative
controls (groceries ≈ 0, banking < 0) shipped alongside the headline; an
Exclusion Register that counts what the measure refuses to price; open code;
hash-committed evidence snapshots; a public correction log.

License: TBD. Contact: see the site's About page.
