"""Tests for the frozen Phase 1 route-panel formula (pipeline/select_routes.py).

The formula is a MAY-NOT-change artifact after owner sign-off
(docs/phase1-preregistration.md §14) — these tests pin its behavior the same
way engine tests pin the spec's worked numbers. Run:

    python3 -m unittest discover engine
"""

import csv
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "pipeline"))
from select_routes import (_band, load_routes, main, select_panel)  # noqa: E402


def write_csv(rows, path):
    with open(path, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["ORIGIN", "DEST", "UNIQUE_CARRIER", "PASSENGERS", "DISTANCE"])
        w.writerows(rows)


def synthetic_fixture(drop_nk=False, no_hubs=False):
    """24 routes, 8 per band, national rank interleaved across bands.

    Per band (i = 0..7, pax descending):
      i 0-2: AA 30 / DL 30 / UA 25 / WN 15  -> competitive, WN cell
      i 3  : UA 70 / AA 20 / DL 10          -> hub-dominated (unless no_hubs)
      i 4  : NK 40 / F9 30 / B6 30          -> ULCC coverage (NK->F9 if drop_nk)
      i 5  : AS 50 / B6 25 / AA 25          -> AS coverage
      i 6-7: AA 40 / DL 35 / UA 25          -> filler
    Top-3 per band are all competitive, so hub-span forces the step-(ii)
    constraint walk to reach past them.
    """
    rows = []
    dists = {"S": 400, "M": 1000, "L": 2000}
    for i in range(8):
        for b in "SML":
            o, d = f"{b}{i}A", f"{b}{i}B"
            pax = 1_000_000 - (i * 3 + "SML".index(b)) * 30_000  # interleaved rank
            dist = dists[b]
            if i <= 2:
                mix = [("AA", .30), ("DL", .30), ("UA", .25), ("WN", .15)]
            elif i == 3:
                mix = ([("AA", .40), ("DL", .35), ("UA", .25)] if no_hubs
                       else [("UA", .70), ("AA", .20), ("DL", .10)])
            elif i == 4:
                mix = ([("F9", .70), ("B6", .30)] if drop_nk
                       else [("NK", .40), ("F9", .30), ("B6", .30)])
            elif i == 5:
                mix = [("AS", .50), ("B6", .25), ("AA", .25)]
            else:
                mix = [("AA", .40), ("DL", .35), ("UA", .25)]
            for c, s in mix:
                # split each carrier's pax across the two directions
                rows.append([o, d, c, int(pax * s * 0.5), dist])
                rows.append([d, o, c, int(pax * s * 0.5), dist])
    return rows


class TestAggregationAndRollup(unittest.TestCase):
    def test_directional_sum_rollup_and_cells(self):
        rows = [
            ["LAX", "JFK", "AA", 1000, 2475],
            ["JFK", "LAX", "AA", 800, 2475],
            ["LAX", "JFK", "MQ", 200, 2475],   # wholly-owned regional -> AA
            ["JFK", "LAX", "B6", 500, 2475],
            ["LAX", "JFK", "HA", 0, 2475],     # zero-pax rows are skipped
        ]
        with tempfile.TemporaryDirectory() as td:
            p = Path(td) / "t100.csv"
            write_csv(rows, p)
            routes = load_routes(p)
        self.assertEqual(len(routes), 1)
        r = routes[0]
        self.assertEqual(r["route"], "JFK-LAX")           # undirected, sorted
        self.assertEqual(r["pax"], 2500)
        self.assertAlmostEqual(r["shares"]["AA"], 0.8)    # 2000/2500 incl. MQ
        self.assertAlmostEqual(r["shares"]["B6"], 0.2)
        self.assertEqual(r["band"], "LONG")
        self.assertTrue(r["hub_dominated"])               # 0.8 >= 0.60
        self.assertEqual(r["cells"], ["AA", "B6"])        # both >= 5%

    def test_band_boundaries(self):
        self.assertEqual(_band(750.0), "SHORT")
        self.assertEqual(_band(750.5), "MEDIUM")
        self.assertEqual(_band(1500.0), "MEDIUM")
        self.assertEqual(_band(1500.1), "LONG")

    def test_tiebreak_alphabetical(self):
        rows = [["ZZA", "ZZB", "AA", 500, 400],
                ["AAA", "AAB", "AA", 500, 400]]
        with tempfile.TemporaryDirectory() as td:
            p = Path(td) / "t.csv"
            write_csv(rows, p)
            routes = load_routes(p)
        self.assertEqual([r["route"] for r in routes], ["AAA-AAB", "ZZA-ZZB"])


class TestPanelSelection(unittest.TestCase):
    def _run(self, **kw):
        with tempfile.TemporaryDirectory() as td:
            p = Path(td) / "t100.csv"
            write_csv(synthetic_fixture(**kw), p)
            routes = load_routes(p)
        return select_panel(routes)

    def test_full_panel_satisfies_all_constraints(self):
        panel, wn_manual, audit = self._run()
        self.assertEqual(len(panel), 18)
        for band in ("SHORT", "MEDIUM", "LONG"):
            in_band = [r for r in panel if r["band"] == band]
            self.assertEqual(len(in_band), 6)
            self.assertTrue(any(r["hub_dominated"] for r in in_band))
            self.assertTrue(any(r["competitive"] for r in in_band))
        counts = {}
        for r in panel:
            for c in r["cells"]:
                counts[c] = counts.get(c, 0) + 1
        for c in ("AA", "DL", "UA", "WN", "AS", "B6", "NK", "F9"):
            self.assertGreaterEqual(counts[c], 2, c)
        # the walk had to jump rank order to satisfy hub-span + coverage
        self.assertTrue(any(a.startswith("step-ii") for a in audit))
        self.assertFalse(any(a.startswith("step-iv") for a in audit))

    def test_wn_manual_cap(self):
        panel, wn_manual, audit = self._run()
        wn_cells = [r for r in panel if "WN" in r["cells"]]
        self.assertEqual(len(wn_cells), 4)                # capped
        self.assertEqual(len(wn_manual), 4)
        self.assertTrue(any(a.startswith("wn-cap") for a in audit))
        # kept cells are exactly the top-4 by WN passengers
        kept = {r["route"] for r in wn_cells}
        self.assertEqual(kept, set(wn_manual))

    def test_relaxation_is_logged_not_silent(self):
        panel, _, audit = self._run(drop_nk=True)
        self.assertEqual(len(panel), 18)                  # panel still fills
        relaxed = [a for a in audit if a.startswith("step-iv")]
        self.assertTrue(any("carrier-coverage:NK" in a for a in relaxed))

    def test_hub_relaxation_when_no_hub_routes_exist(self):
        panel, _, audit = self._run(no_hubs=True)
        relaxed = [a for a in audit if "hub-span" in a and a.startswith("step-iv")]
        self.assertEqual(len(relaxed), 3)                 # one per band, logged

    def test_deterministic(self):
        a = self._run()
        b = self._run()
        self.assertEqual([r["route"] for r in a[0]], [r["route"] for r in b[0]])
        self.assertEqual(a[1], b[1])
        self.assertEqual(a[2], b[2])

    def test_main_end_to_end_provenance(self):
        with tempfile.TemporaryDirectory() as td:
            p = Path(td) / "t100.csv"
            out = Path(td) / "panel.json"
            write_csv(synthetic_fixture(), p)
            result = main([str(p), "--out", str(out)])
            self.assertTrue(out.exists())
        self.assertEqual(len(result["_provenance"]["input_sha256"]), 64)
        self.assertEqual(result["n_cells"],
                         sum(len(r["cells"]) for r in result["panel"]))


if __name__ == "__main__":
    unittest.main()
