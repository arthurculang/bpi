"""Executable form of the Phase 1 pre-registration's worked example (§13).

The paired same-flight quote separates menu structure from scalar fare moves:
between two December waves, fares rise ~20% while the Basic/Main tier gap
NARROWS $60 -> $50. The profile relative carries the scalar move (which also
sits in the CPI comparator side of the Gap); the published attribute interval
[0, g] is baselined on TODAY's menu (trigger rule T3) and tightens. Run:

    python3 -m unittest discover engine
"""

import unittest
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))
from restoration import Item, Profile, link_relative  # noqa: E402

CARRIER = "carrier-x"

# AIR-P1-CARRYON against the base-wave menu: Basic $200 (no carry-on),
# Main $260 (carry-on + seat selection included) — tier gap $60.
P1 = Profile("AIR-P1-CARRYON", {"trip": 1, "carryon": 1}, 260.0, 1.0)


def menu(basic, main):
    return [
        Item("basic", CARRIER, basic, {"trip": 1}),
        Item("main", CARRIER, main, {"trip": 1, "carryon": 1, "seat_sel": 1}),
    ]


class TestArchivalGapComposition(unittest.TestCase):
    """Pre-registration §11 / phase1-inputs §7 worked number: the archival-
    regime published object is EC over the matched-carrier scalar-fare
    comparator, with a predicted residual Gap where CPI's quote spec captures
    the attribute. Executable per the house rule."""

    def test_worked_number(self):
        dfee, segments = 10.0, 2                 # $10/segment fee step, RT
        denom_oneway = 325.0                     # route-average one-way fare
        incidence = 0.17                         # fee-payer administrative ratio
        cpi_capture = 0.80                       # first bag in ~80% of quotes
        event_rel = (dfee * segments) / (2 * denom_oneway)
        self.assertAlmostEqual(event_rel, 0.030769, places=5)      # +3.08%
        ec_gross_pp = incidence * event_rel * 100
        self.assertAlmostEqual(ec_gross_pp, 0.52, places=2)        # +0.52pp
        residual_pp = ec_gross_pp * (1 - cpi_capture)
        self.assertAlmostEqual(residual_pp, 0.10, places=2)        # +0.10pp


class TestPairedQuoteWorkedExample(unittest.TestCase):
    def test_base_wave_gap_and_interval(self):
        rho, rep = link_relative(P1, menu(200.0, 260.0), CARRIER)
        self.assertAlmostEqual(rho, 1.0, places=6)          # base = itself
        self.assertTrue(rep.superset)                        # seat_sel rides along
        self.assertEqual(rep.route, "tier-spread")
        self.assertEqual(rep.interval, (0.0, 60.0))          # gap = 260 - 200

    def test_next_wave_scalar_rise_menu_improvement(self):
        rho, rep = link_relative(P1, menu(240.0, 290.0), CARRIER)
        self.assertAlmostEqual(rho, 290.0 / 260.0, places=4)  # +11.5% (scalar)
        self.assertEqual(rep.route, "tier-spread")
        self.assertTrue(rep.superset)
        # T3 discipline: the interval baselines on TODAY's menu, so the
        # narrowed gap prints as a tighter interval even as fares rose.
        self.assertEqual(rep.interval, (0.0, 50.0))          # 290 - 240
        self.assertLess(rep.interval[1], 60.0)               # menu improved

    def test_naive_fee_tracker_contrast(self):
        # The naive reading is "Basic +20%"; the paired design separates the
        # +11.5% profile relative (scalar, also in the CPI comparator) from
        # the menu-structure component (the gap), which moved DOWN.
        self.assertAlmostEqual(240.0 / 200.0, 1.20, places=6)
        rho, rep = link_relative(P1, menu(240.0, 290.0), CARRIER)
        self.assertLess(rho, 1.20)
        self.assertLess(rep.interval[1], 60.0)


if __name__ == "__main__":
    unittest.main()
