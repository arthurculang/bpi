#!/usr/bin/env python3
"""Snapshot pipeline v0 — The Restoration Gap (WS-B).

Captures posted price/fee/plan menus as timestamped, hash-committed raw HTML.
The archive is the project's base-period evidence; every Inclusion Ledger
line item must trace back to a snapshot in a run manifest.

Usage:
  python3 pipeline/capture.py                     # capture all targets
  python3 pipeline/capture.py --sector wireless   # one sector
  python3 pipeline/capture.py --slug tmobile-plans
  python3 pipeline/capture.py --manual saved.html https://example.com/page slug-name
      # register a manually saved page (for bot-blocked sites: save from a
      # real browser via "Save Page As", then register it here so it enters
      # the manifest with a hash)

Output:
  pipeline/snapshots/<UTC-run-id>/<slug>.html
  pipeline/snapshots/<UTC-run-id>/manifest.json

Snapshots are gitignored (the archive belongs in durable storage, not the
site repo); manifests can be copied out for hash-commitment. Sub-minute
politeness delay between fetches; failures are recorded, never retried
into hammering.
"""

import argparse
import datetime as dt
import hashlib
import json
import sys
import time
import urllib.request
from pathlib import Path

HERE = Path(__file__).resolve().parent
TARGETS = HERE / "targets.tsv"
SNAPDIR = HERE / "snapshots"

UA = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/126.0 Safari/537.36 RestorationGapArchive/0.1"
)
TIMEOUT = 20
DELAY_S = 2.0


def load_targets():
    rows = []
    for line in TARGETS.read_text().splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        parts = line.split("\t")
        if len(parts) != 4:
            print(f"skipping malformed target line: {line!r}", file=sys.stderr)
            continue
        slug, sector, urgency, url = parts
        rows.append({"slug": slug, "sector": sector, "urgency": urgency, "url": url})
    return rows


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def fetch(url: str):
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "text/html,*/*"})
    with urllib.request.urlopen(req, timeout=TIMEOUT) as resp:
        return resp.status, resp.read()


def run_capture(sector=None, slug=None):
    targets = load_targets()
    if sector:
        targets = [t for t in targets if t["sector"] == sector]
    if slug:
        targets = [t for t in targets if t["slug"] == slug]
    # needs-url rows are placeholders awaiting owner verification — fetching
    # them would archive the wrong page under an authoritative-looking hash.
    skipped = [t for t in targets if t["urgency"] == "needs-url"]
    for t in skipped:
        print(f"SKIP needs-url (verify path first): {t['slug']}")
    targets = [t for t in targets if t["urgency"] != "needs-url"]
    if not targets:
        print("no matching targets")
        return 1

    run_id = dt.datetime.now(dt.timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    outdir = SNAPDIR / run_id
    outdir.mkdir(parents=True, exist_ok=True)
    manifest = {"run_id": run_id, "tool": "capture.py v0", "entries": []}

    ok = blocked = 0
    for t in targets:
        entry = dict(t)
        entry["fetched_at"] = dt.datetime.now(dt.timezone.utc).isoformat()
        try:
            status, body = fetch(t["url"])
            path = outdir / f"{t['slug']}.html"
            path.write_bytes(body)
            entry.update(
                {"http_status": status, "sha256": sha256(body), "bytes": len(body), "file": path.name}
            )
            ok += 1
            print(f"  ok    {t['slug']}  ({len(body)} bytes)")
        except Exception as e:  # urllib raises on 4xx/5xx too
            entry.update({"http_status": None, "error": str(e)[:200]})
            blocked += 1
            print(f"  FAIL  {t['slug']}  {str(e)[:120]}")
        manifest["entries"].append(entry)
        time.sleep(DELAY_S)

    (outdir / "manifest.json").write_text(json.dumps(manifest, indent=1))
    urgent_failed = [
        e["slug"] for e in manifest["entries"] if e.get("error") and e["urgency"] == "urgent"
    ]
    print(f"\nrun {run_id}: {ok} captured, {blocked} failed -> {outdir}")
    if urgent_failed:
        print(
            "URGENT targets failed (capture these from a real browser and register "
            f"with --manual before their deadline): {', '.join(urgent_failed)}"
        )
    return 0


def run_manual(filepath: str, url: str, slug: str):
    data = Path(filepath).read_bytes()
    run_id = dt.datetime.now(dt.timezone.utc).strftime("%Y%m%dT%H%M%SZ") + "-manual"
    outdir = SNAPDIR / run_id
    outdir.mkdir(parents=True, exist_ok=True)
    dest = outdir / f"{slug}.html"
    dest.write_bytes(data)
    manifest = {
        "run_id": run_id,
        "tool": "capture.py v0 (manual registration)",
        "entries": [
            {
                "slug": slug,
                "url": url,
                "method": "manual-browser-save",
                "registered_at": dt.datetime.now(dt.timezone.utc).isoformat(),
                "sha256": sha256(data),
                "bytes": len(data),
                "file": dest.name,
            }
        ],
    }
    (outdir / "manifest.json").write_text(json.dumps(manifest, indent=1))
    print(f"registered {slug} ({len(data)} bytes) -> {outdir}")
    return 0


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--sector")
    ap.add_argument("--slug")
    ap.add_argument("--manual", nargs=3, metavar=("FILE", "URL", "SLUG"))
    args = ap.parse_args()
    if args.manual:
        sys.exit(run_manual(*args.manual))
    sys.exit(run_capture(sector=args.sector, slug=args.slug))


if __name__ == "__main__":
    main()
