# The Restoration Gap — Codebook v0

`v0 draft · 2026-07-04 · workstream A · freezes as the public pre-registration with the Phase 0 note (Oct 2026)`
`Amendment policy: versioned, append-only after pre-registration; no retroactive changes to conventions ever apply to already-published links`

This codebook operationalizes Spec v00.02.00 (P2 refined to menu-expansion
monotonicity, 2026-07-04). Where the two disagree, the spec's
formal statement governs and the discrepancy is logged as a codebook erratum.

---

## 1. Definitions

- **Attribute** — a discretely contractible feature that appears (or appeared) as a
  named line item, tier delta, or documented inclusion on a seller's price menu.
  Attributes are enumerated per sector in the attribute dictionary (§3) *before*
  collection. No attribute may be added retroactively to an already-frozen base.
- **Menu (M_t)** — the set of purchasable configurations and fees posted by a seller
  at time t, as evidenced by snapshots in the archive (pipeline manifests).
- **Experience profile (e)** — a base-period configuration actually purchased, defined
  by its attribute vector (e.g., "domestic RT, 1 full-size carry-on, 0 checked bags").
  Profiles partition a sector's base-period buyers; profile shares are utilization
  incidence (§8).
- **Inclusion Ledger event** — a dated menu change satisfying all three trigger
  conditions (§4), recorded per the registry schema (`data/ledger-events.json`).
- **Replication cost C(z; t)** — the minimum posted cost of any same-seller bundle on
  M_t that weakly dominates the frozen attribute vector z, attribute-by-attribute.

## 2. Equivalence protocol

Attribute equivalence is decided by this codebook ex ante, never ad hoc:

1. **Identity of function, not of label.** An attribute is restored only by a
   configuration delivering the same function on the ledger definition. Worked
   rulings (binding):
   - *Carry-on* = "full-size bag travels in the cabin with the passenger, no gate
     surrender." A gate-checked bag, checked bag, or shipped bag does **not**
     restore it. (United's $75 gate charge prices a different attribute.)
   - *Ad-free playback* = "no interruptive advertising in on-demand playback."
     Fewer-ads tiers do not restore it.
   - *Included trash service (rental)* = "waste collection available without a
     separate mandatory line item," regardless of vendor.
   - *Checked bag* = "one bag ≤ standard weight/size transported in hold on the
     same itinerary." Weight/size threshold changes ≥10% are separate attribute
     events, not equivalents.
2. **Same-seller (headline).** seller(j) = seller(e) for the headline series H;
   the cross-seller minimum S is computed as a sensitivity. Brand families count
   as one seller only where billing is unified (T-Mobile/Sprint post-merger: one
   seller; Disney+/Hulu: separate unless bundled purchase is the base).
3. **Purchase-point convention.** Posted standard price at a fixed acquisition
   point: airlines = at-booking, prepaid-online rate, 3-week advance where fares
   are date-dependent; ULCC dynamic fees = at-booking; B6 bags = peak-calendar
   date-matched; subscriptions = posted monthly rate, no promo; rentals = listed
   total price fields. Membership/credit-card-conditioned prices are never used
   for the headline (cash-menu rule); the conditioning is noted.
4. **Quantity normalization.** Package-size attributes use per-standard-unit
   prices (matching CPI practice); size-threshold changes per 2.1.

## 3. Attribute dictionaries (v0 scope)

- **Air (Phase 1):** carry-on-in-cabin; first checked bag; second checked bag;
  advance seat selection; same-day change rights; fare-class family.
- **Streaming (Phase 1):** ad-free playback; concurrent streams count;
  out-of-household member slot; resolution tier (recorded, not priced in v0).
- **Groceries (null control):** net quantity per package (per-unit price only).
- **Banking (negative control):** overdraft fee, NSF fee (per-item posted amounts).
- Phase 2 dictionaries (rental, wireless, lodging) are drafted with their modules
  and freeze before their collection starts.

## 4. Trigger rules

A restoration event exists for profile e at t iff **all three** hold:

- **T1 (documented base inclusion).** The attribute is present in the modal
  purchased configuration at t−1, evidenced by an archived snapshot, carrier
  document, or equivalent primary record cited in the event entry.
- **T2 (priced path).** A named fee, à-la-carte item, or tier delta on M_t prices
  the attribute (the non-emptiness condition).
- **T3 (replication cost rose).** C(z_e; t) > C(z_e; t−1) attributable to the menu
  change, not to a pure scalar price move (which flows through as ordinary price
  change, not an event).

**Non-events (no upward print, by rule):** downward tier introduction with the
incumbent's price and inclusions unchanged — menu expansion can never raise the
index; where the new tier weakly dominates a profile's frozen experience at
lower cost, the decrease prints via the negative-event rule below (spec
v00.02.00 P2 refinement, menu-expansion monotonicity); fee relabeling at
constant all-in replication cost; pure price moves on an unchanged menu.
**Negative events (must print):** re-bundling; fee elimination; a cheaper
restoring path appearing.
**Exits:** if T2 fails (no priced path at any cost), the item leaves the ledger,
weight reallocates within the stratum, and the exit is logged in the Exclusion
Register. No reservation-price imputation, ever.

## 5. Route hierarchy

Routes are ranked lexicographically; a cheaper lower-ranked route never overrides
a priced higher-ranked route's *identification*, but the min-cost is always
reported alongside:

1. **Named fee** for the attribute (cleanest identification; caps the line item).
2. **À-la-carte reassembly** on the same seller's menu.
3. **Tier upgrade** (superset): published as interval **[0, tier gap]** with the
   point estimate at the gap, superset-flagged. Incidental superset extras never
   roll into the next base (§7).

## 6. Link-year and comparator conventions

- **Link-year convention.** Links run December-to-December. An event belongs to
  exactly the link year containing its effective date. Pre-registered
  assignments: Southwest bags → 2025 link; April-2026 fee wave, AA Basic
  surcharge, Netflix March-2026 step → 2026 link; **T-Mobile 2026-07-13 →
  2026 link**; Disney+ ad tier → 2022 link (retrospective exhibits only).
- **Comparator continuity.** The Gap differences against official CPI item-stratum
  12-month relatives. For any comparator window spanning **October 2025** (index
  never published): use BLS's own published bridge treatment where one exists;
  otherwise an 11-month annualized bridge, flagged `bridge=oct2025` in the
  release table. The same convention applies to R-CPI-SC/R-CPI-I reconciliations,
  which additionally cite the vintage used (`vintage=` field) with addenda
  published when covering vintages ship.

## 7. Base re-freeze

Base experiences re-freeze annually **from the Ledger's attribute records**, not
from the replicating purchase: extras acquired via superset routes do not enter
the next base (no upward ratchet), and degraded defaults do not become the
entitlement mid-cycle (no forgiveness drift). The cumulated chain is a caveated
memo item only; the headline is always the 12-month link.

## 8. Incidence and profiles

Restoration line items are weighted by base-period utilization shares (profile
shares). Sources in order of preference: administrative ratios (e.g., BTS bag-fee
revenue ÷ enplanements with an average-fee divisor), carrier/platform
disclosures, third-party panels, published survey estimates. Where no source
meets the bar, the release publishes the **[0%, 100%]-utilization interval** —
never a bare point, never an assumption share. Every incidence figure carries a
provenance tag in the release table.

## 9. Aggregation and the Gap

- Elementary link relatives per profile; sector index = Young-type arithmetic
  mean over profiles with base-period expenditure-x-incidence shares.
- **Exclusive partition:** an item stratum priced by restoration in a period is
  removed from the ordinary pool for that period; the public concordance maps
  ledger items to CPI strata.
- **Gap** = Σ w^CPI-U [ρ − π^CPI] (pricing-concept effect) + (w^B40 − w^CPI-U)-term
  (weighting effect); both published every release. Weights per R-CPI-I recipe
  (equivalized imputed income, multi-year pooled, smoothed; vintage pinned per
  plan P11).

## 10. Drift diagnostics

Annual links only; no monthly chaining. Published annually: chained-vs-direct
comparison over the available span; any divergence > 0.5pp cumulative triggers a
methods note before the next release.

## 11. Assumption Q (release text, verbatim)

> "The bracket interpretation — that the chained CPI and the Restoration Index
> together bound constant-experience cost growth — holds only under Assumption Q:
> no economically material unmeasured quality *improvements* in covered items
> over the link year. The Restoration Index itself is an upper bound on
> constant-experience cost growth regardless; Assumption Q affects only the
> bracket claim."

## 12. Evidence and reproducibility

Every ledger entry cites: (a) a snapshot manifest hash (or a registered manual
capture), (b) the seller's own document where available, (c) at least one
independent corroboration for amounts/dates. Releases are re-derivable from the
archive plus this codebook; access rules for ToS-restricted snapshots are
documented per plan P10 (public where rights allow, access-on-request otherwise).

## 13. Known open items for v1 (freeze deadline: Phase 0 note)

- Rental, wireless, lodging attribute dictionaries (with Phase 2 module designs).
- Air route-panel definition (top-N T-100 routes, booking-grid) — frozen only
  after gate G0 passes. **G0 passed 2026-07-04; the panel pre-registration is
  drafted at `docs/phase1-preregistration.md` (formula:
  `pipeline/select_routes.py`; pass criteria: `docs/g1-band.md`; pinned inputs:
  `data/phase1-inputs.md`), binding on owner sign-off.** The streaming
  attribute dictionary v1 freezes with it (ad-free playback; out-of-household
  member slot; concurrent-stream/resolution tier).
- Incidence source register per sector (§8) with the first provenance tags.
- The G0 plausibility band is committed separately (`docs/g0-plausibility-band.md`)
  and is already binding.
