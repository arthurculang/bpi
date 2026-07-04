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

Many carrier/retail sites 403 automated fetches. For any target the run marks
`FAIL`, open the URL in a real browser, save the complete page
(`File → Save Page As → HTML only` is fine for menus), then register it:

```bash
python3 pipeline/capture.py --manual saved.html "https://original.url" slug-name
```

Manual registrations get their own run directory and hashed manifest entry, so
they carry the same evidentiary weight.

## Not yet in v0 (scheduled with the August codebook)

- Rental listing panel (fixed unit sample, Zillow Total Price / Apartments.com
  fee fields, stratified by market and building class).
- Paired same-flight Basic/Economy fare quotes (route panel goes live October;
  pre-registration freezes after gate G0).
- Per-ISP machine-readable label JSON capture (v0 grabs the label landing pages).
