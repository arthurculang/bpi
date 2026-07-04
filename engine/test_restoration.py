"""Engine tests — fixtures are the spec's worked examples (Spec v00.02.00 §4)
plus the codebook's binding equivalence rulings. Run:

    python3 -m unittest discover engine -v

These tests are the executable form of the spec: if a spec revision changes a
worked number, a test must change with it, in the same commit.
"""

import json
import unittest
from pathlib import Path

from restoration import (Item, Profile, gap, link_relative, named_fee_bound,
                         replicate, sector_relative)

UA = "united"

# --- Spec §4.1 fixtures: base year -------------------------------------------
# Base: standard Economy RT $300 incl. full-size carry-on + seat selection.
# Profiles (S3 assumption shares): P1 carry-on 55%, P0 personal-only 30%,
# P2 carry-on + 1 checked bag each way 15% (base cost $300 + 2x$35 = $370).
P1 = Profile("P1-carryon", {"trip": 1, "carryon": 1}, 300.0, 0.55)
P0 = Profile("P0-personal", {"trip": 1}, 300.0, 0.30)
P2 = Profile("P2-bag", {"trip": 1, "carryon": 1, "checked": 2}, 370.0, 0.15)


def menu_s1():
    """S1 — price-point takeover: Basic $300 (no carry-on), Economy $385,
    checked-bag fee $45/segment, gate-check $75 (delivers checked, NOT carryon)."""
    return [
        Item("basic", UA, 300.0, {"trip": 1}),
        Item("economy", UA, 385.0, {"trip": 1, "carryon": 1, "seat_sel": 1}),
        Item("bagfee", UA, 45.0, {"checked": 1}, kind="fee", targets=frozenset({"checked"})),
        Item("gatecheck", UA, 75.0, {"checked": 1}, kind="fee", targets=frozenset({"checked"})),
    ]


def menu_s2():
    """S2 — undercut launch: Basic $260 beside unchanged Economy $300;
    bag fee unchanged $35."""
    return [
        Item("basic", UA, 260.0, {"trip": 1}),
        Item("economy", UA, 300.0, {"trip": 1, "carryon": 1, "seat_sel": 1}),
        Item("bagfee", UA, 35.0, {"checked": 1}, kind="fee", targets=frozenset({"checked"})),
    ]


class TestS1PricePointTakeover(unittest.TestCase):
    def test_p1_superset_tier_spread(self):
        rho, rep = link_relative(P1, menu_s1(), UA)
        self.assertAlmostEqual(rho, 385.0 / 300.0, places=4)      # +28.3%
        self.assertTrue(rep.superset)                              # seat_sel came along
        self.assertEqual(rep.route, "tier-spread")
        self.assertEqual(rep.interval, (0.0, 85.0))                # [0, gap]

    def test_equivalence_gate_check_does_not_restore_carryon(self):
        # Basic + bag fees = $390 delivers 'checked', not 'carryon' — must not
        # be selected for P1 even though the codebook ruling is the only guard.
        rep = replicate(menu_s1(), P1.required, UA)
        ids = {i.id for i, _ in rep.bundle}
        self.assertEqual(ids, {"economy"})

    def test_p0_unchanged(self):
        rho, rep = link_relative(P0, menu_s1(), UA)
        self.assertAlmostEqual(rho, 1.0, places=6)                 # Basic replicates P0
        self.assertFalse(rep.superset)

    def test_p2_bag_profile(self):
        rho, _ = link_relative(P2, menu_s1(), UA)
        self.assertAlmostEqual(rho, (385.0 + 90.0) / 370.0, places=4)  # +28.4%

    def test_profile_weighted_sector(self):
        agg, _ = sector_relative([P1, P0, P2], menu_s1(), UA)
        self.assertAlmostEqual(agg, 0.55 * (385/300) + 0.30 * 1.0 + 0.15 * (475/370), places=6)
        self.assertAlmostEqual((agg - 1) * 100, 19.9, delta=0.1)   # spec: +19.9%

    def test_gap_vs_flat_cpi_quote(self):
        agg, _ = sector_relative([P1, P0, P2], menu_s1(), UA)
        self.assertAlmostEqual(gap(agg, 1.0), 19.9, delta=0.1)     # CPI lowest-fare reads 0%


class TestS2UndercutLaunch(unittest.TestCase):
    """Menu expansion never RAISES the index; a new option that dominates a
    profile's frozen experience prints as a genuine replication-cost DECREASE
    (Spec v00.02.00 P2 restatement — surfaced by this engine build)."""

    def test_p1_exact_zero(self):
        rho, rep = link_relative(P1, menu_s2(), UA)
        self.assertAlmostEqual(rho, 1.0, places=6)                 # Economy unchanged
        self.assertEqual({i.id for i, _ in rep.bundle}, {"economy"})

    def test_p0_prints_genuine_decrease(self):
        rho, _ = link_relative(P0, menu_s2(), UA)
        self.assertAlmostEqual(rho, 260.0 / 300.0, places=4)       # −13.3%

    def test_sector_never_above_one_on_menu_expansion(self):
        agg, _ = sector_relative([P1, P0, P2], menu_s2(), UA)
        self.assertLessEqual(agg, 1.0)
        self.assertAlmostEqual((agg - 1) * 100, -4.0, delta=0.05)  # ≈ −4.0%


class TestSouthwestNamedFee(unittest.TestCase):
    """Spec §4.2: fare unchanged $300, +$35/bag/way ⇒ +23.3%, named-fee route,
    no superset, no interval."""

    def test_one_bag_profile(self):
        wn = "southwest"
        base = Profile("wn-1bag", {"trip": 1, "checked": 2}, 300.0, 1.0)
        menu = [
            Item("wga", wn, 300.0, {"trip": 1}),
            Item("bagfee", wn, 35.0, {"checked": 1}, kind="fee", targets=frozenset({"checked"})),
        ]
        rho, rep = link_relative(base, menu, wn)
        self.assertAlmostEqual(rho, 370.0 / 300.0, places=4)
        self.assertEqual(rep.route, "named-fee")
        self.assertFalse(rep.superset)
        self.assertIsNone(rep.interval)
        self.assertEqual(named_fee_bound(menu, "checked", wn), 35.0)


class TestDisneyTierSpread(unittest.TestCase):
    """Spec §4.3: ad tier launches at old ad-free price $7.99; ad-free $10.99
    ⇒ +37.5% for the ad-free holder; exact match, not superset."""

    def test_ad_free_holder(self):
        dp = "disneyplus"
        base = Profile("adfree", {"service": 1, "ad_free": 1}, 7.99, 1.0)
        menu = [
            Item("ads", dp, 7.99, {"service": 1}),
            Item("adfree", dp, 10.99, {"service": 1, "ad_free": 1}),
        ]
        rho, rep = link_relative(base, menu, dp)
        self.assertAlmostEqual(rho, 10.99 / 7.99, places=4)        # +37.5%
        self.assertEqual(rep.route, "exact")
        self.assertFalse(rep.superset)


class TestSymmetry(unittest.TestCase):
    def test_rebundling_prints_negative(self):
        # Base: fare $300 + $35 fee (base_cost 335). t: all-inclusive fare $320.
        s = "carrier"
        base = Profile("rebundle", {"trip": 1, "checked": 1}, 335.0, 1.0)
        menu = [Item("incl", s, 320.0, {"trip": 1, "checked": 1})]
        rho, _ = link_relative(base, menu, s)
        self.assertLess(rho, 1.0)
        self.assertAlmostEqual(rho, 320.0 / 335.0, places=4)

    def test_falling_named_fee_prints_negative(self):
        b = "bank"
        base = Profile("overdraft", {"overdraft_cover": 1}, 35.0, 1.0)
        menu = [Item("odfee", b, 5.0, {"overdraft_cover": 1}, kind="fee",
                     targets=frozenset({"overdraft_cover"}))]
        rho, _ = link_relative(base, menu, b)
        self.assertAlmostEqual(rho, 5.0 / 35.0, places=4)


class TestExitRule(unittest.TestCase):
    def test_infeasible_exits(self):
        s = "seller"
        base = Profile("gone", {"trip": 1, "vanished_attr": 1}, 100.0, 1.0)
        menu = [Item("only", s, 90.0, {"trip": 1})]
        rho, rep = link_relative(base, menu, s)
        self.assertIsNone(rho)
        self.assertEqual(rep.route, "infeasible")

    def test_same_seller_discipline(self):
        # A cheaper competitor never enters the headline replication.
        base = Profile("p", {"trip": 1}, 100.0, 1.0)
        menu = [Item("mine", "a", 120.0, {"trip": 1}),
                Item("rival", "b", 80.0, {"trip": 1})]
        rho, rep = link_relative(base, menu, "a")
        self.assertAlmostEqual(rho, 1.2, places=6)
        self.assertEqual({i.id for i, _ in rep.bundle}, {"mine"})


class TestLedgerData(unittest.TestCase):
    """data/ledger-events.json stays loadable and schema-complete."""
    REQUIRED = {"id", "sector", "seller", "event", "effective", "event_type",
                "restoration_route", "line_item", "superset_flag", "status",
                "verified", "sources"}

    def test_schema(self):
        path = Path(__file__).resolve().parent.parent / "data" / "ledger-events.json"
        doc = json.loads(path.read_text())
        events = doc["events"]
        self.assertGreaterEqual(len(events), 10)
        for e in events:
            missing = self.REQUIRED - set(e)
            self.assertFalse(missing, f"{e.get('id')}: missing {missing}")
            self.assertIn(e["event_type"], {"unbundling", "tiering", "menu-removal",
                                            "fee-increase", "negative", "non-event"})
            self.assertIn(e["restoration_route"], {"named-fee", "a-la-carte", "tier-spread"})


if __name__ == "__main__":
    unittest.main()
