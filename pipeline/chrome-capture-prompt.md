# Chrome-assisted capture prompt (browser-agent path)

`v0 · 2026-07-04 · workstream B · for Claude for Chrome, run on the owner's browser (the sandbox proxy blocks these hosts)`

## Why this exists

The snapshot pipeline (`capture.py`) cannot run from the project's sandbox — the
egress proxy 403-blocks carrier/retail hosts. Claude for Chrome runs in the
owner's browser, which can reach them. This prompt has it extract the
**content** we need (plan menus, prices, the migration crosswalk) before
T-Mobile's forced migration on bill cycles from **2026-07-13** changes those
pages. The owner pastes the returned block back into the project session, where
it is committed as a dated pre-migration capture and folded into
`data/ledger-events.json` / the wireless module's frozen plan-feature vectors.

**Provenance honesty:** a browser-agent extraction is a *content* capture, not a
byte-exact hash-committed raw-HTML archival snapshot. It is labeled as such on
ingestion. For a true archival copy of the 2–3 most critical T-Mobile pages,
also do `File → Save Page As → Web Page, Complete` in the browser and keep the
`.html`; those register later via `python3 pipeline/capture.py --manual`. The
git commit time is the authoritative timestamp of record either way.

## The prompt (paste into Claude for Chrome)

```
You are operating my Chrome browser (Claude for Chrome). Task: capture the
PUBLIC, pre-migration state of several T-Mobile plan pages before T-Mobile's
forced plan migration begins on bill cycles from July 13, 2026 — after that
date these menus change and the old plan details disappear. This is a
read-only archival task.

SAFETY (strict):
- Do NOT log in, enter credentials, or open any account/sign-in page.
- Do NOT click any control that buys, checks out, submits, adds, or changes
  anything. Read and extract only.
- Public marketing/plan pages need no login — stay on those. If a page demands
  sign-in, skip it and record it as blocked.

CAPTURE THESE IN PRIORITY ORDER. Pages 1–5 are time-critical (they change on
July 13); do them first and completely.
  1. https://tmo.report/2026/07/heres-every-t-mobile-experience-migration-plan-along-with-prices/
     (the old→new plan crosswalk WITH prices — the single highest-value page)
  2. https://www.t-mobile.com/cell-phone-plans
     (current public plan menu)
  3. https://www.t-mobile.com/customers/plan-update-vo-b2-2026
     (the migration notice page)
  4. https://business.t-mobile.com/support/plans-features/one-plan-unlimited-55-plus
     (an example "(Retired)" legacy-plan feature page)
  5. https://tmo.report/2026/06/breaking-t-mobile-to-force-migrate-over-8-million-customers-to-more-expensive-plans/
     (the migration story, for stated figures)
If you have capacity, also capture (less urgent):
  6. https://www.xfinity.com/learn/broadband-labels
  7. https://www.att.com/broadbandlabels/
  8. https://www.spectrum.com/policies/broadband-labels

FOR EACH page, record:
  - captured_at: the current date-time when you loaded it (system clock; if
    unsure, write "unknown")
  - loaded: "yes" | "partial" | "blocked"
  - title: the page title
  - key_facts: a list of short strings QUOTING exact plan names and dollar
    prices VERBATIM — never paraphrase, round, or infer a price
  - content, structured to the page:
      * plan menus: each plan's name, monthly price, line/term basis, included
        features
      * the crosswalk (page 1): each row as old_plan → new_plan, old_price,
        new_price, stated per-line delta if given
      * broadband labels: provider, plan, monthly price, intro vs post-intro
        price, and every itemized fee with its amount
  - notes: anything that affects interpretation (e.g., "prices shown for a NYC
    ZIP", "banner: offer ends 7/12", "some rows truncated")

OUTPUT: return EXACTLY ONE fenced code block marked ```json containing a JSON
array, one object per page, with fields:
  slug, url, captured_at, loaded, title, key_facts, content, notes
Use these slugs, matching the project's target list:
  1=tmobile-crosswalk  2=tmobile-plans  3=tmobile-migration-support
  4=tmobile-retired-one55  5=tmoreport-migration-story
  6=xfinity-broadband-labels  7=att-broadband-labels  8=spectrum-broadband-labels
If a page is blocked or empty, still include its object with loaded:"blocked"
and empty content — do NOT fabricate anything. Put nothing outside the code
block except a single summary line above it. Keep every price and plan name
byte-exact.
```

## Reporting back

Paste the returned ```json block into the project session. On ingestion it is
saved to `data/captures/tmobile-premigration-<date>.json` with a
`method: browser-agent-extraction` provenance tag, the ledger's T-Mobile event
(`wireless-tmobile-202607`) gains its pre-migration evidence, and the wireless
attribute dictionary can freeze the base plan-feature vectors.

---

## Follow-up B — Wayback recovery of legacy plan feature vectors

The live-site legacy plan pages are already vanishing (the ONE 55+ page redirects
to the current menu as of 2026-07-04). The **base-experience (z) side** of the
T-Mobile event — what customers are migrating FROM — must come from the Wayback
Machine. A Wayback snapshot URL is permanently pinned and third-party-attestable,
so **the archive URL itself is the citable evidence** (stronger than a live
extraction). This is Phase 2 prep, not time-critical. Prompt for Claude for
Chrome (Wayback is reachable from a browser; the project sandbox blocks it):

```
You are operating my Chrome browser (Claude for Chrome) on the Internet Archive's
Wayback Machine (web.archive.org). Task: recover the feature vectors of retired
T-Mobile consumer plans from archived snapshots, so I can reconstruct what
customers were migrated away from. Read-only; do not log in anywhere.

METHOD: for a target original URL, jumping to
  https://web.archive.org/web/<YYYYMMDD>000000/<original-url>
redirects to the nearest archived snapshot at or before that date. Use that to
land on a snapshot from each plan generation. If a page 404s in the archive,
use Wayback's URL search ( https://web.archive.org/web/*/t-mobile.com/cell-phone-plans* )
to list archived plan sub-pages and pick relevant ones.

CAPTURE these generations of the evergreen plan-menu page (the plan lineup
changed over time, so different dates surface different legacy plans):
  - Simple Choice era:  https://web.archive.org/web/20160601000000/https://www.t-mobile.com/cell-phone-plans
  - T-Mobile ONE era:   https://web.archive.org/web/20180601000000/https://www.t-mobile.com/cell-phone-plans
  - Magenta era:        https://web.archive.org/web/20210601000000/https://www.t-mobile.com/cell-phone-plans
  - Just pre-migration: https://web.archive.org/web/20260601000000/https://www.t-mobile.com/cell-phone-plans
And these segment / specific legacy pages (try each; use Wayback search if the
direct URL isn't archived):
  - Unlimited 55+:      https://web.archive.org/web/20260601000000/https://www.t-mobile.com/cell-phone-plans/55-older-plans
  - the redirected one: https://web.archive.org/web/20260601000000/https://business.t-mobile.com/support/plans-features/one-plan-unlimited-55-plus
  - Military:           https://web.archive.org/web/20260601000000/https://www.t-mobile.com/cell-phone-plans/military
  - Magenta MAX:        https://web.archive.org/web/20220601000000/https://www.t-mobile.com/cell-phone-plans/premium-unlimited-data

FOR EACH plan you find on any captured snapshot, record:
  - plan_name (e.g., "Simple Choice", "T-Mobile ONE", "Magenta", "Magenta MAX",
    "Unlimited 55+")
  - wayback_url: the FULL permanent snapshot URL you are reading (with its
    timestamp) — THIS IS THE EVIDENCE, capture it exactly
  - snapshot_date: the archive capture date shown in the Wayback toolbar
  - original_url
  - monthly_price and lines_basis (e.g., "$70 for 1 line", "$140 for 2 lines"),
    quoted VERBATIM
  - features: high-speed/premium data, mobile hotspot GB, streaming perks
    (Netflix/Apple TV/etc.), Canada/Mexico data, international data, taxes-in
    vs taxes-extra — whatever the snapshot states, verbatim
  - notes: anything odd (partial capture, price shown for a region, etc.)

OUTPUT: return EXACTLY ONE fenced code block (start it with three backticks
followed by the word json) containing a JSON array, one object per plan found,
with fields: plan_name, wayback_url, snapshot_date, original_url, monthly_price,
lines_basis, features, notes. If a target yielded no usable snapshot, include one
object with plan_name, the attempted wayback_url, and notes:"no snapshot found".
Do NOT fabricate prices or features — quote only what the archived page shows.
Put nothing outside the code block except a one-line summary above it.
```

On paste-back this is ingested to `data/captures/tmobile-legacy-vectors-<date>.json`
and becomes the frozen base (z) plan-feature vectors for the wireless module's
Phase 2 build; the `wayback_url` per plan is its permanent citation.
