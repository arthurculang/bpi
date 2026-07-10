"""Tests for the wave-0 build kit: build_worksheet.py + validate_capture.py.

The blackout-iteration date traces are the load-bearing pins — they must match
the worked examples frozen in docs/phase1-preregistration.md §2 and
data/phase1-inputs.md §2. Run: python3 -m unittest discover engine
"""

import datetime as dt
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "pipeline"))
from build_worksheet import (build, fourth_thursday_november, grid_dates,  # noqa: E402
                             in_blackout, wave_number)
from validate_capture import validate  # noqa: E402


def panel_fixture():
    # two carriers per route so audit rotation has legacy cells to walk
    return {
        "panel": [
            {"route": "LAX-LAS", "band": "SHORT", "cells": ["AA", "WN"]},
            {"route": "ATL-MCO", "band": "SHORT", "cells": ["DL", "WN"]},
            {"route": "DEN-ORD", "band": "MEDIUM", "cells": ["UA", "AS"]},
            {"route": "JFK-LAX", "band": "LONG", "cells": ["AA", "B6"]},
        ],
        "wn_manual_routes": ["LAX-LAS", "ATL-MCO"],
    }


class TestBlackoutTraces(unittest.TestCase):
    def test_thanksgiving_computation(self):
        self.assertEqual(fourth_thursday_november(2026), dt.date(2026, 11, 26))
        self.assertEqual(fourth_thursday_november(2027), dt.date(2027, 11, 25))

    def test_blackout_endpoints_inclusive(self):
        self.assertTrue(in_blackout(dt.date(2026, 12, 18)))   # window start
        self.assertTrue(in_blackout(dt.date(2027, 1, 4)))     # window end
        self.assertFalse(in_blackout(dt.date(2027, 1, 5)))    # just outside
        self.assertTrue(in_blackout(dt.date(2026, 7, 1)))
        self.assertTrue(in_blackout(dt.date(2026, 7, 7)))
        self.assertFalse(in_blackout(dt.date(2026, 7, 8)))

    def test_december_2026_wave_prices_january(self):
        # pre-registration §2 worked trace: Dec 1 2026 wave -> Jan 5 / Jan 12
        depart, ret, shifted = grid_dates(dt.date(2026, 12, 1))
        self.assertEqual(depart, dt.date(2027, 1, 5))
        self.assertEqual(ret, dt.date(2027, 1, 12))
        self.assertTrue(shifted)

    def test_december_2027_wave_trace(self):
        # pre-registration §2 worked trace: Dec 7 2027 wave -> Jan 11 / Jan 18
        depart, ret, shifted = grid_dates(dt.date(2027, 12, 7))
        self.assertEqual(depart, dt.date(2028, 1, 11))
        self.assertEqual(ret, dt.date(2028, 1, 18))
        self.assertTrue(shifted)

    def test_normal_wave_no_shift(self):
        # wave 1: Oct 6 2026 -> depart Oct 27, return Nov 3, no blackout
        depart, ret, shifted = grid_dates(dt.date(2026, 10, 6))
        self.assertEqual(depart, dt.date(2026, 10, 27))
        self.assertEqual(ret, dt.date(2026, 11, 3))
        self.assertFalse(shifted)


class TestWorksheet(unittest.TestCase):
    def test_wave_number_anchor(self):
        self.assertEqual(wave_number(dt.date(2026, 10, 6)), 1)
        self.assertEqual(wave_number(dt.date(2026, 12, 1)), 3)
        self.assertEqual(wave_number(dt.date(2027, 10, 5)), 13)

    def test_build_excludes_wn_from_agent_cells(self):
        ws = build(panel_fixture(), dt.date(2026, 10, 6))
        carriers = {c["carrier"] for c in ws["agent_cells"]}
        self.assertNotIn("WN", carriers)
        self.assertEqual(ws["wn_manual_routes"], ["LAX-LAS", "ATL-MCO"])
        self.assertEqual(ws["n_agent_cells"], len(ws["agent_cells"]))

    def test_audit_rotation_deterministic_and_legacy_only(self):
        a = build(panel_fixture(), dt.date(2026, 10, 6))["audit_cells"]
        b = build(panel_fixture(), dt.date(2026, 10, 6))["audit_cells"]
        self.assertEqual(a, b)                         # deterministic
        self.assertEqual(len(a), 2)
        for cell in a:
            self.assertIn(cell["carrier"], ("AA", "DL", "UA", "AS"))

    def test_audit_rotation_advances_with_wave(self):
        w1 = build(panel_fixture(), dt.date(2026, 10, 6))["audit_cells"]
        w2 = build(panel_fixture(), dt.date(2026, 11, 3))["audit_cells"]
        self.assertNotEqual(w1, w2)                    # rotates

    def test_december_flag(self):
        self.assertTrue(build(panel_fixture(), dt.date(2026, 12, 1))["december_link_wave"])
        self.assertFalse(build(panel_fixture(), dt.date(2026, 10, 6))["december_link_wave"])


class TestCaptureValidator(unittest.TestCase):
    def _air(self, **over):
        rec = {"wave_id": "w1", "route": "LAX-LAS", "carrier": "AA",
               "pair_status": "paired-same-flight", "loaded": "yes",
               "basic_outbound_leg_usd": 100.0, "basic_return_leg_usd": 100.0,
               "main_outbound_leg_usd": 130.0, "main_return_leg_usd": 130.0}
        rec.update(over)
        return rec

    def test_clean_air_record_passes(self):
        self.assertEqual(validate([self._air()], "air"), [])

    def test_qc2_basic_over_main_fails(self):
        bad = self._air(main_outbound_leg_usd=90.0, main_return_leg_usd=90.0)
        errs = validate([bad], "air")
        self.assertTrue(any("QC-2" in e for e in errs))

    def test_bad_pair_status_fails_unless_flagged(self):
        self.assertTrue(validate([self._air(pair_status="nonsense")], "air"))
        # a recognized missing_code exempts the enum check
        ok = self._air(pair_status="nonsense", missing_code="MISS/BLOCKED")
        self.assertFalse(any("bad pair_status" in e for e in validate([ok], "air")))

    def test_unknown_missing_code_fails(self):
        self.assertTrue(any("unknown missing_code" in e
                            for e in validate([self._air(missing_code="MISS/WHATEVER")], "air")))

    def test_bad_bag_source_fails(self):
        self.assertTrue(any("first_bag_source" in e
                            for e in validate([self._air(first_bag_source="carrier-pigeon")], "air")))

    def test_streaming_and_grocery(self):
        s = {"seller": "Netflix", "tier_name": "Standard", "monthly_price_usd": 17.99,
             "ad_free": True, "loaded": "yes"}
        self.assertEqual(validate([s], "streaming"), [])
        g = {"upc": "0001", "product_name": "Cereal 18oz", "net_quantity": "18 oz",
             "list_price_usd": 4.29, "loaded": "yes"}
        self.assertEqual(validate([g], "grocery"), [])
        self.assertTrue(validate([{**g, "net_quantity": ""}], "grocery"))


if __name__ == "__main__":
    unittest.main()
