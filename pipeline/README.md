# Snapshot pipeline v0

Workstream B. Captures posted price/fee/plan menus as timestamped raw HTML with
SHA-256 manifests. The archive is the project's base-period evidence — every
Inclusion Ledger line item traces to a snapshot.

## Run

```bash
python3 pipeline/capture.py                    # everything in targets.tsv
python3 pipeline/capture.py --sector wireless  # one sector
```

Output lands in `pipeline/snapshots/<UTC-run-id>/` with a `manifest.json`
(URL, timestamp, HTTP status, SHA-256, bytes). Snapshots are **gitignored** —
copy each run to durable storage (and keep the manifests; they are the
hash-commitment record).

## Deadlines driving urgency flags

- **T-Mobile targets: run before July 13, 2026.** Bill cycles from that date
  migrate 8M+ legacy lines to Experience plans and ~1,100 legacy plan codes
  leave the menu. The pre-migration state is unreconstructible afterward.
- **FCC broadband labels:** the machine-readability requirement faces a
  rollback final rule expected 2H 2026. Capture monthly until it resolves.
- Everything else: monthly cadence (first business day), same targets file.

## Bot-blocked sites

Many carrier/retail sites 403 automated fetches — and the project sandbox blocks
them wholesale. Three ways to capture, best evidentiary weight first:

1. **Run `capture.py` on an unblocked machine** — raw HTML + SHA-256 manifest.
2. **Manual browser save** — open the URL, `File → Save Page As → Web Page,
   Complete`, then register the file (raw HTML, hashed):
   ```bash
   python3 pipeline/capture.py --manual saved.html "https://original.url" slug-name
   ```
3. **Chrome-agent content extraction** — `chrome-capture-prompt.md` drives Claude
   for Chrome to extract plan menus/prices/crosswalks and return a JSON block.
   This captures the *content* (not a byte-exact hashed snapshot) and is the
   fastest way to beat a dated menu change (e.g. the T-Mobile 2026-07-13
   migration) when the owner can't run the pipeline. Ingested to
   `data/captures/` with a `browser-agent-extraction` provenance tag.

Manual (1–2) registrations get their own run directory and hashed manifest
entry, so they carry full archival weight; (3) is content-grade, labeled.

## Not yet in v0 (scheduled with the August codebook)

- Rental listing panel (fixed unit sample, Zillow Total Price / Apartments.com
  fee fields, stratified by market and building class).
- Paired same-flight Basic/Economy fare quotes (route panel goes live October;
  pre-registration freezes after gate G0).
- Per-ISP machine-readable label JSON capture (v0 grabs the label landing pages).
