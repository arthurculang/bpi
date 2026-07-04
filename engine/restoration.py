"""Restoration engine v0 — The Restoration Gap (workstream D).

Implements the codebook-v0 primitive: the minimum posted cost of any
same-seller bundle on today's menu that weakly dominates a frozen
attribute vector, with route classification (named-fee / à-la-carte /
tier-spread), superset flagging, tier-gap intervals, link relatives,
and profile-weighted sector aggregation.

Scope note: this module computes; it does not decide. Trigger rules,
equivalence rulings, and incidence sourcing live in docs/codebook-v0.md.
Per the G0 gate (docs/g0-plausibility-band.md), this engine must not be
run against the 2008-09 retrospective inputs until the owner signs off
the band; its test fixtures are the spec's worked examples only.

Stdlib only. Menus are small by construction (posted consumer menus),
so replication uses bounded exhaustive search — correctness and
auditability over cleverness.

v0.1 (post-review): route classification fixed for mixed product+fee
and fee-only bundles; tier-gap interval re-baselined on the current
menu (excluding pure scalar price moves per trigger rule T3);
requirement-derived quantity bounds replace the fixed cap; deterministic
total-order tie-break; cent-quantized cost comparisons and epsilon
attribute comparisons.
"""

from dataclasses import dataclass
from itertools import product as cartesian
from math import ceil
from typing import Mapping, Optional, Sequence, Tuple

INFEASIBLE = None
EPS = 1e-9


@dataclass(frozen=True)
class Item:
    """One purchasable line on a menu: a product, tier, or named fee."""
    id: str
    seller: str
    price: float
    attrs: Mapping[str, float]          # attribute quantities delivered per unit
    kind: str = "product"               # "product" | "fee"
    targets: frozenset = frozenset()    # for fees: the attributes the fee is a named price for


@dataclass(frozen=True)
class Replication:
    cost: Optional[float]
    bundle: Tuple[Tuple[Item, int], ...]  # (item, quantity), deterministic order
    superset: bool                        # bundle delivers more than required
    route: str                            # "exact" | "named-fee" | "a-la-carte" | "tier-spread" | "infeasible"
    interval: Optional[Tuple[float, float]]  # [0, tier gap] when a superset tier component exists

    @property
    def feasible(self) -> bool:
        return self.cost is not None


@dataclass(frozen=True)
class Profile:
    """A base-period experience profile (codebook §1)."""
    id: str
    required: Mapping[str, float]  # frozen attribute vector z
    base_cost: float               # observed t-1 transaction cost, C(z; t-1)
    share: float                   # base-period expenditure-x-incidence share


def _cents(x: float) -> int:
    return round(x * 100)


def _dominates(delivered: Mapping[str, float], required: Mapping[str, float]) -> bool:
    return all(delivered.get(k, 0.0) >= v - EPS for k, v in required.items())


def _bundle_attrs(bundle: Sequence[Tuple[Item, int]]) -> dict:
    out: dict = {}
    for item, qty in bundle:
        for k, v in item.attrs.items():
            out[k] = out.get(k, 0.0) + v * qty
    return out


def _is_superset(delivered: Mapping[str, float], required: Mapping[str, float]) -> bool:
    extra_attr = any(k not in required and v > EPS for k, v in delivered.items())
    over_delivery = any(delivered.get(k, 0.0) > v + EPS for k, v in required.items())
    return extra_attr or over_delivery


def _classify_route(bundle: Sequence[Tuple[Item, int]], required: Mapping[str, float],
                    superset: bool, product_superset: bool) -> str:
    """Codebook §5 hierarchy, applied to the *chosen* bundle.

    "named-fee" only when fees with non-empty targets inside the required set
    price the whole delta over a non-superset product base (or stand alone) —
    a fee never launders a tier upgrade, and a fee with targets beyond the
    required set is not a named price for this restoration.
    """
    fees = [i for i, _ in bundle if i.kind == "fee"]
    products = [i for i, _ in bundle if i.kind == "product"]
    fees_named = bool(fees) and all(f.targets and f.targets <= frozenset(required) for f in fees)

    if fees and not products:
        return "named-fee" if fees_named else "a-la-carte"
    if fees and products:
        return "named-fee" if (fees_named and not product_superset) else "a-la-carte"
    if len(products) > 1:
        return "a-la-carte"
    return "tier-spread" if superset else "exact"


def _qty_bound(item: Item, required: Mapping[str, float]) -> int:
    """Largest quantity of `item` that could be needed: enough of it alone to
    satisfy any single required attribute it delivers."""
    bounds = [ceil(v / item.attrs[k]) for k, v in required.items()
              if item.attrs.get(k, 0.0) > EPS]
    return max(bounds) if bounds else 0


def _search(candidates: Sequence[Item], required: Mapping[str, float]
            ) -> Optional[Tuple[Tuple[Item, int], ...]]:
    """Min-cost dominating bundle. Total-order tie-break:
    (cost in cents, distinct line count, ((id, qty), ...))."""
    ranges = [range(_qty_bound(i, required) + 1) for i in candidates]
    best_key, best_bundle = None, None
    for qtys in cartesian(*ranges):
        bundle = tuple((i, q) for i, q in zip(candidates, qtys) if q > 0)
        if not bundle:
            continue
        cost_c = sum(_cents(i.price) * q for i, q in bundle)
        if best_key is not None and cost_c > best_key[0]:
            continue
        if not _dominates(_bundle_attrs(bundle), required):
            continue
        key = (cost_c, len(bundle), tuple((i.id, q) for i, q in bundle))
        if best_key is None or key < best_key:
            best_key, best_bundle = key, bundle
    return best_bundle


def _tier_interval(menu: Sequence[Item], required: Mapping[str, float], seller: str,
                   bundle: Sequence[Tuple[Item, int]], cost: float) -> Tuple[float, float]:
    """Codebook §5 route 3: publish [0, tier gap], where the tier gap is
    measured on TODAY's menu — upgrade cost minus the current cost of the
    best same-seller bundle that needs no superset product. Baselining on
    today (not on base_cost) keeps pure scalar price moves out of the
    interval, per trigger rule T3.
    """
    sup_products = {i.id for i, _ in bundle
                    if i.kind == "product" and _is_superset(i.attrs, required)}
    reduced_menu = [i for i in menu if i.id not in sup_products]
    same_seller = [i for i in reduced_menu if i.seller == seller]
    coverable = {k: v for k, v in required.items()
                 if any(i.attrs.get(k, 0.0) > EPS for i in same_seller)}
    if not coverable:
        return (0.0, cost)  # no comparable baseline on today's menu; bound by full cost
    base_bundle = _search(sorted(same_seller, key=lambda i: i.id), coverable)
    if base_bundle is None:
        return (0.0, cost)
    base_cost_t = sum(i.price * q for i, q in base_bundle)
    return (0.0, max(0.0, cost - base_cost_t))


def replicate(menu: Sequence[Item], required: Mapping[str, float], seller: str) -> Replication:
    """Min-cost same-seller bundle weakly dominating `required`.

    Exhaustive search with per-item quantity bounds derived from the
    requirement itself (an item is never needed in greater quantity than
    would satisfy the largest single requirement it serves). Costs compare
    in cents; ties break on (cost, line count, (id, qty) tuple) — a total
    order, so the result is independent of iteration order.
    """
    candidates = sorted((i for i in menu if i.seller == seller), key=lambda i: i.id)
    if not candidates:
        return Replication(INFEASIBLE, (), False, "infeasible", None)

    bundle = _search(candidates, required)
    if bundle is None:
        return Replication(INFEASIBLE, (), False, "infeasible", None)

    cost = sum(i.price * q for i, q in bundle)
    delivered = _bundle_attrs(bundle)
    superset = _is_superset(delivered, required)
    product_superset = any(i.kind == "product" and _is_superset(i.attrs, required)
                           for i, _ in bundle)
    route = _classify_route(bundle, required, superset, product_superset)
    interval = None
    if product_superset:
        interval = _tier_interval(menu, required, seller, bundle, cost)
    return Replication(cost, bundle, superset, route, interval)


def named_fee_bound(menu: Sequence[Item], attr: str, seller: str) -> Optional[float]:
    """Codebook §5: where a named fee prices an attribute directly, it caps
    the line item attributed to that attribute (identification, not min-cost)."""
    fees = [i.price for i in menu if i.seller == seller and i.kind == "fee"
            and attr in i.targets and i.attrs.get(attr, 0) > EPS]
    return min(fees) if fees else None


def link_relative(profile: Profile, menu_t: Sequence[Item], seller: str
                  ) -> Tuple[Optional[float], Replication]:
    """rho_t(e) = C(z_e; t) / C(z_e; t-1); None when replication is infeasible
    (the item exits the ledger per codebook §4)."""
    rep = replicate(menu_t, profile.required, seller)
    if not rep.feasible:
        return None, rep
    return rep.cost / profile.base_cost, rep


def sector_relative(profiles: Sequence[Profile], menu_t: Sequence[Item], seller: str
                    ) -> Tuple[float, dict]:
    """Young-type arithmetic mean of link relatives over feasible profiles,
    base-share weighted; infeasible profiles are excluded with their weight
    reallocated proportionally within the stratum (codebook §4 exit rule),
    and reported in the details."""
    details, feasible = {}, []
    for p in profiles:
        rho, rep = link_relative(p, menu_t, seller)
        details[p.id] = {"rho": rho, "replication": rep, "share": p.share}
        if rho is not None:
            feasible.append((p.share, rho))
    if not feasible:
        raise ValueError("no feasible profiles — sector exits the ledger")
    total_share = sum(s for s, _ in feasible)
    agg = sum(s * r for s, r in feasible) / total_share
    return agg, details


def gap(sector_rho: float, cpi_relative: float) -> float:
    """Restoration Gap for one stratum, in percentage points on the link:
    (rho - pi_CPI) x 100."""
    return (sector_rho - cpi_relative) * 100.0
