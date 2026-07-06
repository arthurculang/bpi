# Monthly wave prompts v0 — Phase 1 collection (Claude for Chrome)

`v0 draft · 2026-07-06 · workstream B · finalized at wave 0 (Sept 2026); cell lists are generated per-wave from the panel output of pipeline/select_routes.py · governed by docs/phase1-preregistration.md §4/§6`

Three prompts per wave, run on the owner's browser. Placeholders in
`{{DOUBLE_BRACES}}` are filled by the wave worksheet (runbook Step 0) from the
frozen panel — the prompts themselves never choose routes or dates.
Provenance: these are **content-grade** captures (`browser-agent-extraction`);
the December link wave and the rotating 2-cell audit are additionally captured
as owner manual saves registered via `capture.py --manual` (archival grade).

**The safety-rail carve-out (pre-registration §4), stated in full in every
prompt:** the agent MAY enter routes/dates into public fare-search forms, click
Search, select a flight, and open seat-map/bag add-on displays. It may NOT log
in, enter credentials, enter any name/email/payment detail, hold a fare, or
take any purchase/reserve action — hard stop at the passenger-information page.
WS-G counsel reviews this carve-out before the October go-live.

## Prompt A — legacy + Alaska paired quotes (UA / AA / DL / AS)

```
You are operating my Chrome browser. Task: capture paired airline fare quotes
for a research price panel. Read-and-record only, plus the narrow search-flow
exception below. Work cell by cell; if a cell fails twice, mark it blocked and
move on — never improvise a substitute route, date, or carrier.

SAFETY (strict):
- You MAY: enter the route and dates below into the carrier's public fare
  search, click Search, select a flight to view fare families, and open
  seat-map or bag add-on displays.
- You may NOT: log in; enter credentials; enter any name, email, phone, or
  payment detail; hold, reserve, or purchase anything. HARD STOP the moment a
  page asks for passenger information.
- Use the carrier's own .com site (never metasearch), logged out, US site.

GRID (fixed; do not adjust): round trip, 1 adult, NONSTOP only.
Depart {{DEPART_DATE}} · return {{RETURN_DATE}} (blackout-iterated by the
worksheet — use exactly these dates).

CELLS ({{N_A_CELLS}}): {{CELL_LIST_A}}   [format: CARRIER route, e.g. "UA LAX-EWR"]

PER CELL, record:
- pairing rule: the nonstop with the LOWEST basic-family total; tie-break
  earliest departure. On that SAME flight from the SAME results page, record
  the basic-family and main-family all-in round-trip totals (the advertised
  total including taxes/fees), fare family names verbatim, and flight numbers.
- If no basic family is offered: record the single family, pair_status="pair=absent".
- If the basic family is sold out on every nonstop: pair_status="basic-soldout".
- cheapest advance standard seat price (outbound leg, from the seat map if
  reachable without passenger info; else "not-reached").
- same-day-change terms if displayed on the fare-family comparison, verbatim.
- any membership/card-conditioned price shown (record it, labeled — it never
  enters the headline).
- a Google Flights cross-check total for the same cell (one lookup, recorded
  as sanity only) — do this AFTER all carrier-direct cells, never before.

OUTPUT: EXACTLY ONE fenced JSON block, an array with one object per cell:
{cell, route, carrier, depart_date, return_date, flight_numbers,
 fare_family_basic_verbatim, total_basic_rt_usd, fare_family_main_verbatim,
 total_main_rt_usd, pair_status, seat_price_usd, same_day_change_verbatim,
 conditioning_notes, gf_crosscheck_usd, loaded, page_title, url, notes}.
Prices verbatim as displayed, never rounded, never computed by you.
```

## Prompt B — ULCC in-flow ancillaries (NK / F9 / B6)

```
You are operating my Chrome browser. Task: capture at-booking ancillary prices
(carry-on, checked bags, seat) for a research price panel. These carriers price
ancillaries dynamically INSIDE the booking flow, so you will advance into the
flow — under the strict stop rule below.

SAFETY (strict):
- You MAY: search the route/dates below, select the flight per the pairing
  rule, and advance ONLY as far as the bag/seat add-on page.
- You may NOT: log in; enter any name, email, phone, or payment detail; hold
  or purchase anything. HARD STOP at the passenger-information page — if bags
  are priced after passenger info on some carrier, record "gated-behind-pax-info"
  and stop that cell.
- Carrier's own site only, logged out, US site. Decline seat-selection and
  bundle upsells by choosing "skip" options only where a skip exists.

GRID (fixed): round trip, 1 adult, NONSTOP only.
Depart {{DEPART_DATE}} · return {{RETURN_DATE}}.

CELLS ({{N_B_CELLS}}): {{CELL_LIST_B}}

PER CELL, record: lowest-fare-family all-in RT total (and the second family's
total where one exists, same flight — B6 Blue Basic vs Blue; F9 basic vs
bundle; NK is single-cabin: pair_status="pair=not-applicable"); at-booking
carry-on price; first and second checked bag prices; cheapest standard seat;
B6 peak/off-peak calendar flag if shown; bag size/weight limits verbatim;
loaded status.

OUTPUT: EXACTLY ONE fenced JSON block, one object per cell:
{cell, route, carrier, depart_date, return_date, flight_numbers,
 fare_family_low_verbatim, total_low_rt_usd, fare_family_second_verbatim,
 total_second_rt_usd, pair_status, carryon_usd, bag1_usd, bag2_usd,
 seat_usd, peak_flag, bag_limits_verbatim, loaded, page_title, url, notes}.
Prices verbatim, never rounded, never computed by you.
```

## Prompt C — streaming tiers + grocery basket (static pages)

```
You are operating my Chrome browser. Task: read-only capture of posted prices.
Do NOT log in, subscribe, add to cart, or enter any personal detail anywhere.

PART 1 — STREAMING ({{N_STREAMING_PAGES}} pages): {{STREAMING_URLS}}
Per page: every plan tier's name and posted monthly price verbatim; which
tiers include ad-free playback; the extra-member price where posted; loaded
status; page title; URL.

PART 2 — GROCERIES ({{N_GROCERY_ITEMS}} items × 2 retailers): {{GROCERY_URLS}}
Per item page: product name verbatim; net quantity/package size verbatim;
LIST price (record any member/club price separately, labeled — it never
enters the headline); unit price if displayed; in-stock status; loaded status.

OUTPUT: EXACTLY ONE fenced JSON block:
{"streaming": [...], "groceries": [...]} with the fields above per entry.
Prices and quantities verbatim, never rounded, never computed by you.
```

## Southwest (owner-manual — never agent-driven)

WN cells are captured by the owner by hand (Kiwi.com injunction; WS-G rule):
southwest.com search on the grid dates, `File → Save Page As → Web Page,
Complete` for the fare-results and bag-policy pages, then register:
`python3 pipeline/capture.py --manual <file>.html "<url>" wn-<route>-wave<NN>`.
~45 min for the 4 capped cells.
