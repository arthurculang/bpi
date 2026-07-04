"""Restoration engine v0 — The Restoration Gap (workstream D).

Implements the codebook-v0 primitive: the minimum posted cost of any
same-seller bundle on today's menu that weakly dominates a frozen
attribute vector, with route classification (named-fee / à-la-carte /
tier-spread), superset flagging, link relatives, and profile-weighted
sector aggregation.

Scope note: this module computes; it does not decide. Trigger rules,
equivalence rulings, and incidence sourcing live in docs/codebook-v0.md.
Per the G0 gate (docs/g0-plausibility-band.md), this engine must not be
run against the 2008-09 retrospective inputs until the owner signs off
the band; its test fixtures are the spec's worked examples only.

Stdlib only. Menus are small by construction (posted consumer menus),
so replication uses bounded exhaustive search — correctness and
auditability over cleverness.
"""

from dataclasses import dataclass, field
from itertools import product as cartesian
from typing import Mapping, Optional, Sequence, Tuple

INFEASIBLE = None


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
    interval: Optional[Tuple[float, float]]  # [0, gap] published for tier-spread supersets

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


def _dominates(delivered: Mapping[str, float], required: Mapping[str, float]) -> bool:
    return all(delivered.get(k, 0.0) >= v for k, v in required.items())


def _bundle_attrs(bundle: Sequence[Tuple[Item, int]]) -> dict:
    out: dict = {}
    for item, qty in bundle:
        for k, v in item.attrs.items():
            out[k] = out.get(k, 0.0) + v * qty
    return out


def _is_superset(delivered: Mapping[str, float], required: Mapping[str, float]) -> bool:
    extra_attr = any(k not in required and v > 0 for k, v in delivered.items())
    over_delivery = any(delivered.get(k, 0.0) > v for k, v in required.items())
    return extra_attr or over_delivery


def _classify_route(bundle: Sequence[Tuple[Item, int]], required: Mapping[str, float],
                    superset: bool) -> str:
    fees = [i for i, _ in bundle if i.kind == "fee"]
    products = [i for i, _ in bundle if i.kind == "product"]
    if fees and all(f.targets <= frozenset(required) for f in fees):
        return "named-fee"
    if len(products) + len(fees) > 1:
        return "a-la-carte"
    return "tier-spread" if superset else "exact"


def replicate(menu: Sequence[Item], required: Mapping[str, float], seller: str,
              max_qty: int = 4, prior_cost: Optional[float] = None) -> Replication:
    """Min-cost same-seller bundle weakly dominating `required`.

    Bounded exhaustive search over quantities 0..max_qty per candidate item.
    Ties break on (cost, item count, ids) for determinism/auditability.
    `prior_cost` (when given) sets the tier-spread interval upper bound as
    max(0, cost - prior_cost) per codebook §5 route 3.
    """
    candidates = sorted((i for i in menu if i.seller == seller), key=lambda i: i.id)
    if not candidates:
        return Replication(INFEASIBLE, (), False, "infeasible", None)

    best: Optional[Tuple[float, int, Tuple[Tuple[Item, int], ...]]] = None
    for qtys in cartesian(range(max_qty + 1), repeat=len(candidates)):
        bundle = tuple((i, q) for i, q in zip(candidates, qtys) if q > 0)
        if not bundle:
            continue
        cost = sum(i.price * q for i, q in bundle)
        if best is not None and cost > best[0]:
            continue
        if not _dominates(_bundle_attrs(bundle), required):
            continue
        key = (cost, sum(q for _, q in bundle), tuple(i.id for i, _ in bundle))
        if best is None or key < (best[0], best[1], tuple(i.id for i, _ in best[2])):
            best = (cost, key[1], bundle)

    if best is None:
        return Replication(INFEASIBLE, (), False, "infeasible", None)

    cost, _, bundle = best
    delivered = _bundle_attrs(bundle)
    superset = _is_superset(delivered, required)
    route = _classify_route(bundle, required, superset)
    interval = None
    if route == "tier-spread" and superset and prior_cost is not None:
        interval = (0.0, max(0.0, cost - prior_cost))
    return Replication(cost, bundle, superset, route, interval)


def named_fee_bound(menu: Sequence[Item], attr: str, seller: str) -> Optional[float]:
    """Codebook §5: where a named fee prices an attribute directly, it caps
    the line item attributed to that attribute (identification, not min-cost)."""
    fees = [i.price for i in menu if i.seller == seller and i.kind == "fee"
            and attr in i.targets and i.attrs.get(attr, 0) > 0]
    return min(fees) if fees else None


def link_relative(profile: Profile, menu_t: Sequence[Item], seller: str,
                  max_qty: int = 4) -> Tuple[Optional[float], Replication]:
    """rho_t(e) = C(z_e; t) / C(z_e; t-1); None when replication is infeasible
    (the item exits the ledger per codebook §4)."""
    rep = replicate(menu_t, profile.required, seller, max_qty=max_qty,
                    prior_cost=profile.base_cost)
    if not rep.feasible:
        return None, rep
    return rep.cost / profile.base_cost, rep


def sector_relative(profiles: Sequence[Profile], menu_t: Sequence[Item], seller: str,
                    max_qty: int = 4) -> Tuple[float, dict]:
    """Young-type arithmetic mean of link relatives over feasible profiles,
    base-share weighted; infeasible profiles are excluded with their weight
    reallocated proportionally (codebook §4 exit rule), and reported."""
    details, feasible = {}, []
    for p in profiles:
        rho, rep = link_relative(p, menu_t, seller, max_qty=max_qty)
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
