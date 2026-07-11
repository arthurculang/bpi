# Phase 2 rent module — design draft: the rented-dwellings fee-stack panel and the posted-vs-realized audit

`v0 · 2026-07-11 · workstreams D/B/G/H (plan §2.1, decision P5; codebook §3 Phase-2 dictionary mandate) · STATUS: DRAFT — design only, nothing in this document is frozen; the binding freeze is a dedicated pre-registration + band file (§8), committed band-first before any collection enters a published link. No numeric pass-band limit appears anywhere in this document, by rule.`

This document is the executable design for the Phase 2 flagship: **rented
dwellings** — the project's real thesis sector, ~16.5% of a bottom-quintile
budget ($5,781/yr Q1, $6,225/yr Q2 at 12.4% — plan §1, CE Table 1101 2024
vintage) against airfare's 0.5%. The target concept is already decided (plan
decision P5, adopted 2026-07-04): **advertised-rent-plus-mandatory-fees** —
the recurring mandatory-fee stack needed to reproduce last year's tenancy,
plus amortized mandatory one-time fees at a forced re-search event, with a
mandatory **posted-vs-realized audit** because fees were historically revealed
at application, not in listings. This document's job is to turn that ruling
into an attribute dictionary, a panel formula, a wave protocol, an audit
protocol, and link mechanics, in the phase1-preregistration mold.

Posture, restated because every artifact must: the measure is an **upper bound
published only as a spread** over the matching CPI series; it makes no
"true inflation" claim, in this document or anywhere; negative and zero prints
are features; every public number carries a provenance tag; the panel is a
**census of posted menus at named properties and managers**, not a sample —
no standard errors are claimed anywhere in this module. Single-operator
dependency is structural and disclosed (§7).

Companion binding files **at freeze, none of which exists yet** (§8 fixes the
ordering): `docs/phase2-rent-band.md` (pass criteria — committed first;
numeric limits will live there and only there; its header states its relation
to plan gate G2, whose label it deliberately does not borrow — the g1-band
GA–GD precedent, which renamed its tests precisely to avoid colliding with a
different binding object), `docs/phase2-rent-preregistration.md` (the frozen
successor of this draft), `pipeline/select_rent_panel.py` (the panel formula
as executable code), `data/phase2-rent-inputs.md` (pinned inputs).

---

## 0. What this module measures, and what it deliberately does not

**Facts the design rests on (plan §2.1, web-verified 2026-07-04).** CPI Rent
of Primary Residence prices *contract rent* — all services the landlord
provides in exchange for rent — and quality-adjusts for utility-bundling
changes and extra charges like pet fees. One-time fees (application ~$50
typical, paid by 79% of recent renters; admin; move-in) have **no home in the
rent index**; separately billed mandatory recurring fees (valet trash $25–50/mo,
tech/package fees, RUBS utility billing, payment "convenience" fees) enter
only if respondents report them as rent; and the 6-month continuing-tenant
panel structurally underweights fees loaded at new-lease events. The fee stack
is litigated and large: FTC v. Invitation Homes ($48M; fees up to ~$1,700/yr
on top of advertised rent), FTC & Colorado v. Greystar ($24M, Dec 2025 —
"hundreds of dollars more per month": package delivery, trash, technology
packages). Posting is being forced onto the menu: Zillow's Cost of Renting
Summary (2023) → **Total Price display (live 2025-07-15)**; Minnesota's Total
Monthly Payment law (2024); Colorado HB25-1090 (in force 2026-01-01); the FTC
rental-fee ANPRM (2026-03-13; comments closed 2026-04-13; docket
**FTC-2026-0266**; no NPRM as of the plan's 2026-07-04 verification). ~53% of
bottom-quintile households rent; 83% of <$30k renters are cost-burdened with
median residual income of $250/month.

**The target concept (P5, restated precisely).** The module prices, per panel
unit (§2.1) and frozen unit type, the monthly cost of

> advertised rent (new-lease, posted) **+** the recurring mandatory-fee stack
> required to weakly dominate the frozen tenancy's attribute vector **+**
> (mover profile only, exhibit-only in v1 — §1.2) mandatory one-time fees
> amortized over the 12-month link horizon,

and publishes the 12-month relative of that replication cost **only as a
spread** over the CPI Rent of Primary Residence stratum relative, with a
mandatory decomposition (§4.3). It does **not** re-price continuing-tenant
contract rent — that is CPI's concept, priced well by CPI's panel, and
re-pricing it would put the module in a fight it does not need and would
double-count the one thing CPI rent measures cleanly. The module prices the
**posted menu**: what a household would pay today, at the same property, to
acquire last year's tenancy experience, drip fees included. The wedge between
that and CPI's concept — the drip wedge plus the new-lease timing difference —
is the publication object, decomposed so neither component can masquerade as
the other.

**What routes to the Exclusion Register instead of the index:** unpriced
degradation (maintenance response times, amenity closures and hour cuts,
staffing withdrawals — no priced path, so no print, only the census); pet
fees and pet rent (always-separate line items — see ruling RD-7); usage-based
utility pass-through amounts (consumption-dependent, not a menu price — the
*billing/administration* fee is in the stack, the usage dollars are not);
mandatory third-party purchases (e.g., a renters-insurance minimum bought from
an outside insurer — breaks same-seller; where the landlord instead sells its
own mandatory "liability waiver" fee, that is a named in-stack fee).
**Conditioning, never headline:** conditioned discounts — autopay, portal or
membership programs, employer/preferred-employer pricing — are recorded as
conditioning under the cash-menu rule (codebook §2.3; the T-Mobile AutoPay
lesson): the headline stack is the unconditioned posted price. Negative
and zero prints are features: a fee elimination, a consent-decree fee-folding,
or a flat menu prints what it prints.

---

## 1. Attribute dictionary v1 — rented dwellings (draft-for-freeze; codebook §3 style)

Binding once frozen (§8); ex ante; no attribute may be added retroactively to
an already-frozen base (codebook §1). The dictionary covers the **recurring
mandatory-fee stack** plus the amortized one-time component. "Mandatory" =
required of every tenant in the frozen unit type as a condition of tenancy, as
posted (or as revealed by the §3 audit); optional add-ons are recorded as menu
context, never in H.

| ID | Attribute | Definition (equivalence, codebook §2 register) | Priced route in v1 |
|---|---|---|---|
| RENT-A1 | Included trash service | Codebook §2 ruling, binding, quoted at its exact boundary: *"waste collection available without a separate mandatory line item,"* regardless of vendor (the final clause sits outside the codebook's quotation marks, as here). Valet-trash conversion = unbundling event; the named fee prices it. | Named fee |
| RENT-A2 | Parking (one vehicle) | One on-site parking entitlement at the base tenancy's basis (unreserved-or-better; a reserved-only replacement for a base unreserved entitlement weakly dominates and is admissible; street parking does **not** restore an on-site entitlement — wrong attribute regardless of price). | Named fee; else tier spread [0, gap], superset-flagged (RD-5) |
| RENT-A3 | Package receipt | Secure package acceptance (locker, package room, or front-desk acceptance) without a separate mandatory line item. Carrier-side redelivery is not an equivalent. | Named fee |
| RENT-A4 | Technology / amenity bundle | Any posted **mandatory** recurring technology, amenity, or "community" fee (bulk wifi/smart-home fees, amenity fees). Equivalence is at the line-item level: the attribute is *occupancy without the mandatory line item*, so a newly imposed mandatory fee is the event and its amount is the price. Non-monthly cadences normalize per RD-10. | Named fee |
| RENT-A5 | Fee-free payment path | At least one non-surcharged method of paying the monthly rent obligation (the **cash-menu analog**, codebook §2.3). If every posted payment path carries a fee, the **cheapest** payment fee is mandatory by construction and enters the stack. Card-surcharge avoidance via ACH restores the attribute (function, not label). **Expected-MISS, stated now:** payment-path and surcharge schedules are rarely posted on listing platforms — they live in leases and portals — so A5 MISS-records at most properties most waves; its evidence paths are the property's own fee page where one exists and the §3 audit's application-stage revealed stack, which sees the payment schedule. | Named fee (cheapest path); MISS-recorded where unposted, audit-evidenced |
| RENT-A6 | Lease-term parity | The option to hold the tenancy at a 12-month term at the posted 12-month rate. A menu offering only month-to-month (or only short terms at a premium — plan-verified premiums run 5–20%) prices the loss as the term spread. Renewal-specific pricing is largely off-menu (tenant-specific letters); the panel prices term parity **only where term-differentiated prices are posted**; otherwise the attribute is MISS-recorded and rides the §3 audit, which sees application-stage term pricing. | Tier spread [0, MTM premium], superset-flagged |
| RENT-A7 | One-time fees at forced re-search | Mandatory application + administrative/move-in fees at today's posted amounts, amortized **straight-line over the 12-month link horizon** (fee ÷ 12 per month), priced **only** in the mover profile RENT-P3 (§1.2, exhibit-only in v1) — a continuing tenancy pays them zero times, and the dictionary says so rather than smearing them over everyone. Refundable security deposits are not fees (recorded as conditioning); a mandatory **nonrefundable** fee replacing a refundable deposit is a new one-time fee and a ledger event. | Named fee, amortized (exhibit-only via P3) |
| RENT-A8 | Utility billing basis | Recorded, priced only where a named flat billing/administration fee exists (RUBS admin fees, "utility billing service" fees). The usage dollars pass through CPI utilities and are out of scope here; a conversion from included-utilities to RUBS **without** any named fee is an Exclusion Register entry (unpriceable on the menu), not an imputation. | Named fee (admin component only) |

**Worked rulings (binding at freeze, decided now so no wave decides them ad hoc):**

- **RD-1 (trash).** Already ruled in codebook §2; restated above. Vendor
  identity is irrelevant; the function is waste collection without a separate
  mandatory line item.
- **RD-2 (relabeling non-event).** A fee folded into advertised rent at
  constant all-in replication cost is a **non-event** (codebook §4): ρ moves
  ≈ 0 even as both components move. Consequence, stated so no reader mistakes
  it: the FTC consent decrees are expected to force exactly this folding at
  some operators, and the module must print ≈ 0 on a pure folding — this is a
  standing honesty exhibit, and test GR-D (§8) exists to prove the module
  passes its own non-event rule. (The band's tolerance lives in
  `docs/phase2-rent-band.md`, not here.)
- **RD-3 (concessions are promotions).** "X weeks free" and move-in specials
  never enter H (the T-Mobile AutoPay lesson: headline = posted list terms).
  Face advertised rent is the H series; a net-effective-rent column is
  computed at ingestion and published as a sensitivity, never as H.
- **RD-4 (fee-free payment).** If a portal fee is avoidable by mailed check
  per the posted policy, the attribute is intact and the portal fee is
  conditioning. The audit (§3) checks whether the posted fee-free path is real
  at application time.
- **RD-5 (parking).** A garage upgrade that is the only path to any parking
  is a superset route: interval [0, gap], point at the gap, superset-flagged
  (codebook §5).
- **RD-6 (thresholds).** Attribute-degrading threshold changes ≥10% on a
  quantified inclusion (e.g., included parking spots 2→1 is 50%: an event;
  package-locker hours trimmed 10% is unpriced: Register) follow the codebook
  **§2.1 threshold-event ruling** (the checked-bag weight/size pattern:
  ≥10% threshold changes are separate attribute events, not equivalents),
  with §2.4 supplying only the per-unit normalization: quantified and priced
  where a named fee exists, Register otherwise.
- **RD-7 (pet fees — always-separate).** Pet fees/pet rent predate the base
  period as separate line items at effectively all professional operators, so
  T1 (documented base **inclusion**) fails by construction: there is no frozen
  base in which pets were included. Pet-fee *levels* are therefore recorded
  and routed to the **Exclusion Register as a monitored always-separate
  series** (counts + affected base expenditure), never to the index. If a
  property is found where the base tenancy documentedly included pets at no
  fee, T1 is satisfied there and the event grammar applies — the ruling is
  about evidence, not about pets.
- **RD-8 (unpriced degradation).** Maintenance response, amenity closures,
  staffing cuts: no priced path ⇒ Exclusion Register with counts and affected
  base expenditure (spec §3.2/§3.3). The Register is a first-class product
  (plan P2); "the index cannot price it" never becomes "it didn't happen."
- **RD-9 (same-band replication only).** The headline H prices **same-band
  units only**: beds/baths equal to the frozen type, sqft within the frozen
  band (§2.1). A cross-type unit that weakly dominates (a 2BR against a
  frozen 1BR) is at most a superset-flagged [0, gap] **sensitivity**, never
  H — cross-type pricing would inject unit-mix jumps into the advertised-rent
  series. An empty band is MISS/NO-VACANCY (§2.4), not an invitation to walk
  up the menu. (The draft previously said "cheapest weakly dominating listed
  unit" in §2.1 while §2.4 assumed same-band; this ruling closes that
  contradiction so no wave decides it ad hoc.)
- **RD-10 (cadence normalization).** A mandatory recurring fee posted at a
  non-monthly cadence (annual renewal/administration fees exist at
  professional operators) enters the monthly stack at amount ÷ months of
  cadence (annual ÷ 12), flagged `cadence-normalized` at ingestion — a
  stayer-stack convention, labeled distinctly from RENT-A7's mover-only
  amortization, which applies to one-time fees, not recurring ones.

### 1.2 Profiles (partition of base-period renter households in scope)

| ID | Attribute vector | Incidence source / tag (details §5) |
|---|---|---|
| RENT-P1-STAYER (flagship) | Continuing tenancy, 12-month term, frozen unit type at the panel unit; active fee stack **RENT-A1, A3–A6, A8** (A2 inactive — parking is exactly what P2 adds; listing it here would double-count it); **zero** one-time fees. Replication cost = advertised rent (same seller, frozen unit type, new-lease posted, same band per RD-9) + mandatory recurring stack. | (1 − m) × (1 − c) per the partition below. |
| RENT-P2-PARKING | P1 + one on-site parking entitlement (RENT-A2 active). | (1 − m) × c, c = car-owning renter share — [owner-verify: CE/NHTS pull]; **[0%, 100%]** until a usable source lands (codebook §8 rule). |
| RENT-P3-MOVER (**exhibit-only in v1**) | Forced re-search: an involuntary lease termination (nonrenewal, sale, uninhabitability) forcing a new application. Replication = cheapest weakly dominating listing **within the same frozen market × class stratum** + that property's fee stack + amortized one-time fees (RENT-A7). Same-seller is impossible **by construction** for this profile — the seller ended the relationship — so P3 is a cross-seller stratum-minimum: an **S-type object**, and codebook §2.2 / spec §2.2 confine S-type objects to sensitivity status; the headline H is same-seller, with no exception granted here. **P3 therefore does not enter H or the headline Gap in v1**: it publishes as a labeled exhibit with its own memo line in the decomposition (§4.3) and its own defined exhibit link (§4.1). Promotion into H is available only via a logged codebook/spec amendment if the H1 2027 review (GR-A) rules the stratum-minimum construction admissible for forced re-search — the design does not silently amend a binding convention. | m = involuntary-move rate among renter households — [owner-verify: AHS/CPS reason-for-move tables]; **[0%, 100%]** until then. |

**Partition (exact, so the aggregation arithmetic cannot double-count):**
P3 = involuntary movers (share m); P2 = (1 − m) × c; P1 = (1 − m) × (1 − c).
The three shares sum to 100% of in-scope renter households by construction;
m and c each ride their [0%, 100%] intervals until usable sources land (§5),
jointly bounded — the intervals are on the partition parameters, never on
shares free to overlap. Profile shares are the Young-mean aggregation weights
(codebook §9), which is why the partition must be exact rather than
approximately worded. With P3 exhibit-only, **the headline aggregates P1 and
P2 with their shares renormalized over (1 − m)**, and m prints alongside as
the excluded-share disclosure. The P0 analog exists here too: a base tenancy
that never included parking, packages, or paid trash prints 0 on those line
items — the phantom-loss control is built into the profile grammar, not
bolted on.

---

## 2. The fixed-panel listings census

### 2.1 Unit of observation

**CLASS-LMF (property-level).** For large multifamily, advertised rent is a
new-lease menu price observable when a unit of the frozen type is listed, and
the mandatory-fee schedule is property-level and observable every wave
regardless of vacancy. Per LMF panel property, freeze: the seller (manager of
record), one **frozen unit type** — the cheapest 1BR/2BR floorplan by lowest
posted starting rent at the §2.2 freeze snapshot (tie-break: smaller sqft,
then alphabetical floorplan name), recorded as beds/baths + the floorplan's
sqft **±10% (the frozen band)** — and the attribute vector (§1). Replication
each wave = the cheapest currently listed unit **within the frozen band**
(RD-9) plus the posted mandatory stack. Unit turnover is therefore **data,
not missingness**: the new-lease price of the frozen type is exactly the
concept.

**CLASS-SSF (manager × market).** The LMF premise — "the fee schedule is
property-level and observable every wave regardless of vacancy" — **fails**
for scattered-site single-family rentals: an occupied house has no live
listing and often no standing property page on either platform, so a
property-frozen SSF panel would go MISS on both the rent and fee fields most
waves, and the ≥3-wave DELISTED rule would churn the stratum by construction.
The SSF unit of observation is therefore the **manager × market cell**:
frozen seller = the qualified manager (§2.2); fee stack of record = the
manager's posted market-level fee schedule / resident-services page
[owner-verify at the §8 pilot: existence and URL stability of these pages for
the candidate managers — the FTC order machinery compels fee disclosure at
Invitation Homes, which is why this stratum is plausibly observable at all];
advertised rent = the cheapest active listing in the frozen SSF band —
**3BR, matching the single-family stock; the 1BR/2BR convention is
LMF-only** — across the manager's listings in the CBSA, with the count of
active listings recorded every wave (a manager-level census statistic and the
vacancy-thinness disclosure). One-off mom-and-pop listings remain excluded —
same-seller replication requires a standing seller who can be re-observed —
a disclosed coverage limitation, not a hidden one. **Pre-committed fallback
(a design ruling now, not a reviewer question deferred):** if the §8 pilot
parser round-trip shows the manager-level object non-executable (no posted
market fee schedule; unstable listing attribution), v1 ships **LMF-only with
SSF as a named coverage gap**.

### 2.2 Selection formula (deterministic; full definition in `pipeline/select_rent_panel.py` at freeze)

**Freeze ordering (the G0 pattern, copied exactly; parser step added — see
§8 for the full ordering).** (1) `docs/phase2-rent-band.md` commits first.
(2) The §8 pre-freeze parser validation passes on the pilot snapshot. (3) The
pre-registration + `select_rent_panel.py` commit — the formula freezes before
its inputs. (4) The owner downloads the market-ranking file on an unblocked
connection and commits its SHA-256 to `data/phase2-rent-inputs.md`. (5) The
market list is the script's output on the hashed file. (6) The owner captures
the **freeze-wave platform snapshot** (hash-committed, owner machine — the
sandbox proxy blocks the platforms) per the walk protocol below. (7) The
panel list is the script's output on that hashed snapshot. Markets and panel
units are **outputs of the freeze, never inputs to it**; test GR-C (§8)
re-executes both steps and must reproduce the identical panel.

**Market strata.** Ranking source: the latest published **ACS 1-year
estimates of renter-occupied housing units by CBSA** (expected table B25003
"Tenure" — [owner-verify table ID and available vintage on an unblocked
connection; the 2025 federal data disruptions may force the 2023 1-year file,
and the pinned-inputs file records whichever vintage is hashed]). Selection,
**M = 6 CBSAs**: (i) top-2 nationally by renter-occupied units,
unconditionally; (ii) walk national rank order, adding the first CBSA in each
Census region not yet represented, until all four regions are covered —
**region assignment is deterministic: a CBSA's region = the Census region of
the state of its first-named principal city** (multi-state CBSAs are
otherwise unassignable — Philadelphia spans Northeast and South states),
stated in `select_rent_panel.py`; (iii) fill remaining slots in pure rank
order; (iv) **disclosure-jurisdiction constraint** (the air hub-span analog):
the panel must contain ≥1 CBSA in a state with a mandatory all-in
rent-posting law in force at freeze (Colorado, Minnesota per plan §2.1) — if
the walk has not produced one, the last pure-rank slot is filled by the
highest-ranked such CBSA, logged in the script's audit output. Tie-break
alphabetical on CBSA title. This constraint exists because the module
pre-registers a falsification prediction on it (§3.4). **Pinned M = 4
de-scope variant** (because §7's de-scope order can shrink M to 4, where
top-2 plus the four-region walk consumes every slot and no pure-rank slot
remains for the disclosure replacement): top-2 unconditional; the region walk
fills the remaining two slots; if no selected CBSA sits in a disclosure
state, the disclosure CBSA **replaces the lowest-ranked region fill and that
region's coverage requirement is dropped**, the relaxation logged in the
script's audit output — the phase1 fixed-relaxation-order pattern.

**Building-class strata (2 per market).**
- **CLASS-LMF** — large professionally managed multifamily: property page
  shows ≥50 units (or, where unit count is not displayed, ≥5 distinct active
  floorplans — a deterministic snapshot-computable proxy). This is where the
  litigated fee stacks live (Greystar).
- **CLASS-SSF** — single-family / small multifamily operated by a
  multi-property manager (the Invitation Homes stratum), observed as
  manager × market cells per §2.1. **The qualification is deterministic, not
  "identifiable" by judgment:** a manager qualifies when its normalized
  manager-of-record string (case-folded, whitespace/punctuation-normalized;
  **exact-string matching only** — near-miss names are logged, never merged
  by operator judgment) appears on **≥ N distinct captured property pages
  within the same hashed CBSA snapshot** (N frozen in the pre-registration;
  expected N = 5).

**Snapshot object and search geography (pinned, because neither platform
exposes a CBSA-level search — "search results for the CBSA" is not otherwise
a defined object).** Per CBSA, the pre-registration commits a **search-URL
list** built from a frozen geography rule: platform search scoped to the
CBSA's **first-named principal city** (the same city that fixes the region in
step (ii)), logged-out, US point of access, filters = the stratum definition
where the platform supports them; the URL list is hashed into
`data/phase2-rent-inputs.md`. The freeze-wave snapshot = the search-results
pages 1..P in order, **plus every property page opened in walk order**, all
under one hash manifest. The stratum filters (unit counts, floorplan counts,
manager strings) are computable only from property pages, not result cards —
so the snapshot's extent is defined by the walk itself: property pages open
in walk order until each stratum's quota is satisfied or a pre-registered
page budget **P_max** is exhausted, and the manifest records exactly the
pages the walk touched. GR-C reproduces the walk from the manifest.

**Walk order (deterministic, platform-agnostic).** Candidate properties are
ordered by the **SHA-256 hash of the canonical property-page URL, ascending
hex-lexicographic** — an arbitrary-but-deterministic labeled convention (the
grocery control's pre-registered ZIP again: "a labeled convention, not a
representativeness claim"). Canonical URL = the platform's own listing URL
stripped of query parameters by a pinned rule. The hash key exists for every
candidate, sorts unambiguously, and does not depend on platform property IDs
(whose existence and stability would otherwise need verifying **before** the
formula could freeze — the §8 parser round-trip verifies all extracted fields
pre-freeze instead of deferring them to first capture).

**CLASS-LMF selection:** the first **K = 4** properties in walk order that
satisfy the LMF filter and have ≥1 active listing in the 1BR/2BR band.
**CLASS-SSF selection:** the walk proceeds in the same hash order until
**K = 4 managers** qualify (≥ N pages each) or P_max is reached; managers
qualify in walk order (the order in which each reaches N pages); if fewer
than 4 qualify within P_max, the cell ships with the qualifying count,
disclosed. **Panel = 6 markets × (4 LMF properties + 4 SSF manager cells)
= 48 panel units.** K, M, N, and P_max are sized to honest hours (§7) and are
provisional until the rent wave-0 timing pilot commits a measured
per-unit basis; the frozen values are set in the pre-registration, and any
post-freeze shrinkage follows a pre-registered de-scope order, never
improvisation.

**Succession rule (no mid-year discretion).** A panel unit dead on the
platform ≥3 consecutive waves stays in the panel flagged MISS/DELISTED
through December; at the **December re-freeze only**, dead units are replaced
by the next candidate in the original frozen walk order that satisfies the
stratum filters, logged as a succession in `data/phase2-rent-inputs.md`'s
amendment log. Mid-year replacement is banned — churn is a finding, not a
nuisance.

**Expected example markets** (labeled EXPECTED/ILLUSTRATIVE — the script's
output on the hashed file overrides mechanically): New York, Los Angeles
(top-2); Chicago (Midwest fill); Houston or Atlanta (South fill); Dallas,
Denver or Minneapolis (rank fill / disclosure constraint).

### 2.3 Capture protocol and cadence

- **Wave day:** shared with the Phase 1 runbook — first Tuesday of each month
  (holiday shift rule inherited; rent has no travel-date grid, so no blackout
  iteration). Preservation capture (unfrozen, plan P3, exempt from gates)
  starts as soon as the owner runs it — the Sprint-0 rental panel v0 (plan §9
  item 2) is **overdue** and is the module's most time-sensitive owner task.
  The frozen panel's baseline wave is the **December 2026 wave (Tue
  2026-12-01)**, which requires the §8 freeze to complete before that date.
- **Price concept (codebook §2.3, cited because it is binding).** Codebook
  §2.3 already pins the rental purchase point: *"rentals = listed total price
  fields."* The module honors that convention **component-wise**: the all-in
  replication cost (advertised rent + mandatory stack) is the component-built
  equivalent of the listed total price — the components, not a single
  displayed total, are what make the §4.3 decomposition and the fee-event
  grammar possible — and Zillow's **Total Price** display (live 2025-07-15)
  is the **pinned cross-check**: recorded every wave where shown, with any
  divergence from the component sum flagged `fee-conflict`. The codebook's
  rentals clause is queued for a logged amendment to this component-built
  wording at the codebook's next revision (§9 item 7); until then this
  paragraph is the reconciliation, stated rather than silent.
- **Platform assignment (deterministic).** Primary platform per panel unit:
  **Apartments.com where the unit has a page with a populated fees section at
  the freeze snapshot, else Zillow.** The primary platform supplies **both
  the advertised rent of record and the fee stack of record**. The secondary
  platform is **conflict-detection and corroboration only** — a per-field
  union across platforms would be an upward ratchet (a fee eliminated on the
  primary would survive in the union via the stale secondary, breaking the
  codebook §4 symmetry this module claims) and would jump spuriously at every
  quarterly sweep. Both platforms are captured in March/June/September/
  December waves (the quarterly dual-platform sweep); single-platform in
  other months.
- **Cross-platform fee conflict:** disagreement **in amount or in
  presence/absence** of a mandatory fee → flag `fee-conflict`, held, and
  resolved at the **next dual-platform wave** (never on a single-platform
  wave, which cannot adjudicate); the property's own posted fee page (where
  one exists in `pipeline/targets.tsv`) is the tie-breaking document. For
  units with **no own fee page**, the confirmation rule is persistence: a
  changed reading must persist across **two consecutive readings of the same
  source** before it enters. Symmetric by construction: conflicts and holds
  work identically whichever direction they point.
- **Anti-promotion rule (split by price type, the §4-of-phase1 pattern).**
  *Fee-schedule items* (the mandatory stack): a single-wave level change of
  either sign without a corroborating posted document is held
  pending-confirmation (`suspected-promotion` / `suspected-error`); the same
  wave's hash-captured property fee page counts as the corroborating
  document (else the two-consecutive-readings rule above); **the annual link
  computes after the following January wave**, so a December-effective change
  gets its confirmation wave and still enters the link its effective date
  assigns (codebook §6). *Advertised rent* is a dynamic price — it IS the
  menu, like ULCC ancillaries — so no multi-wave screen applies; concessions
  are recorded per RD-3 and never enter H.
- **December advertised-rent sessions (ruled, so the deviation from phase1's
  ULCC pattern is a choice, not an omission).** Phase1's December
  median-of-three-sessions exists because ULCC in-flow ancillaries are
  session-priced dynamic quotes where a single session can catch an A/B draw.
  An advertised asking rent is a **posted per-unit list price, not a
  session-priced flow**; the documented failure mode here is cross-platform
  disagreement, not within-session randomization — which the December
  dual-platform sweep plus the Total Price cross-check field already screen.
  One session per platform therefore suffices; the primary platform's reading
  is the field of record, and any December cross-platform rent disagreement
  carries its `fee-conflict` flag into the link row as disclosure.
- **Fields per unit-wave:** wave_id; capture_timestamp_utc; platform +
  capture_channel + provenance_grade + manifest_or_commit_ref; market; class;
  canonical_url + url_sha256 (the walk key); property_id_verbatim (recorded,
  not load-bearing); seller/manager of record (verbatim + normalized);
  frozen_unit_type; listed_units_matching_band (count; RD-9);
  advertised_rent_usd (cheapest same-band listed unit, verbatim);
  zillow_total_price_usd where shown (the pinned codebook §2.3 cross-check);
  each named recurring fee: name_verbatim, amount, cadence +
  cadence-normalized monthly amount (computed at ingestion, RD-10),
  mandatory_flag, source_platform; one_time_fees (application, admin/move-in,
  other — name_verbatim + amount); lease_terms_posted + term-differentiated
  prices where shown; parking (basis + price); trash basis; package basis;
  payment_methods + surcharges (expected-MISS per A5); utility_billing_basis
  + any named admin fee; pet_fees (→ Register series); deposit_terms
  (conditioning); concession_text_verbatim + promo_detected_flag;
  net_effective_rent (computed at ingestion, never by the agent);
  fee-conflict flag; loaded (yes | partial | blocked); missing_code (§2.4);
  no_priced_path_entries (→ Exclusion Register feed); page_title + url;
  saved_file_sha256 where manual; notes. SSF manager cells additionally
  record active_listing_count and the fee-page URL of record. All arithmetic
  (amortization, cadence normalization, stacks, net-effective) happens **at
  ingestion** (`pipeline/validate_capture.py` gains a rent record schema),
  never in the agent.
- **Whole-menu census obligation.** A unit-wave is complete only when
  every dictionary attribute has a recorded price/path or an explicit
  no-priced-path entry feeding the Exclusion Register. Decreases and
  eliminations flow through the identical diff (codebook §4 symmetry) — "you
  only collected fee increases" is false by construction here exactly as in
  air.
- **Safety rails (Prompt D, added to `pipeline/wave-prompts.md` at freeze).**
  The agent MAY: open listing/property pages, expand fee and policy sections,
  paginate floorplans. It may NOT: log in, contact a property, submit any
  form with personal details, schedule a tour, or begin any application —
  hard stop at any identity or contact field. Blocked pages record
  `loaded=blocked` and fall to the owner-manual path. WS-G counsel reviews
  the carve-out (platform ToS exposure; snapshot redistribution sits in the
  access-on-request tier per plan P10/WS-G) — **and, added to the WS-G scope
  explicitly, any automated capture of the listing platforms themselves**
  (see the provenance ladder below; CoStar litigates scraping aggressively).

**Provenance ladder (grades identical to phase1 §4; assignments corrected to
what the tooling can actually do):** (1) `capture.py` static pages, same day
= raw HTML + SHA-256 manifest, full archival weight — **reserved for
property- and manager-owned fee pages** (rows added to `pipeline/targets.tsv`
at freeze). The listing platforms are **not** grade-1 targets: `capture.py`
is a urllib fetcher, both platforms are bot-protected JS applications whose
raw fetch returns blocks or data-less shells, and their ToS bar automated
access; until WS-G counsel and a working fetch say otherwise, the platforms
are captured at grades (2)–(3) only. (2) Owner manual Save-Page-As
(rendered DOM) registered via `capture.py --manual` = full archival weight —
covers **every link-entering December observation (all ≈48 panel units,
priced in §7's December extras, not hoped away)** and a rotating audit
subsample (rotation deterministic, same (2w, 2w+1) mod N pattern as phase1
§4). (3) Chrome-agent extraction = content-grade,
`browser-agent-extraction`, authoritative timestamp = git commit of the
ingested JSON. The December link therefore rests on hashed manual-save
artifacts plus grade-1 fee pages, not agent text — and that claim is priced
in §7, not asserted.

### 2.4 Missingness and degradation rules (the rent MISS codes)

Codes: **MISS/NO-VACANCY** (no listed unit in the frozen band this wave —
the structurally common case; the fee stack is still captured and the rent
field stays empty: no imputation, no interpolation, stale displays never
enter a link), **MISS/DELISTED** (property page gone from the platform; for
SSF manager cells: the manager's fee page gone AND zero attributable listings
in the CBSA), **MISS/RECONFIG** (frozen unit type no longer exists at the
property — a menu-removal fact, drafted as a ledger/Register entry, not a
mere miss), **MISS/OWNERSHIP-CHANGE** (manager of record changes — a
seller-identity break: logged structural break, never a silent splice, base
re-freezes at the next December; spec §9.2), **MISS/SITE-ERR, MISS/BLOCKED,
MISS/SKIPPED.**

1. A missing monthly observation flags and stays empty. Up to 2 whole
   non-December waves per year may be missed (flagged) with zero effect on
   the published link; December is mandatory.
2. **December miss ladder (rent analog of phase1 §7, with the substitute
   window narrowed for the rent component — stated why):** retry within Dec
   1–15 → for the **advertised-rent component**, nearest wave within **±15
   days only**, flagged `link-substitute` — the air ladder's ±45-day window
   was defensible because both sides of the air link price a common fixed
   travel window under the same rule; advertised new-lease rents are
   seasonal, NO-VACANCY is the structurally common miss, and an
   October-for-December substitution on one side of the link would import
   the seasonal gradient into the link itself — → for MISS/NO-VACANCY with a
   posted fee stack, the fee-stack component still enters and the
   advertised-rent component is excluded for the link with in-stratum weight
   reallocation → full Exclusion for the link. The **fee-stack component**,
   which is schedule-posted and not seasonal, keeps the ±45-day window.
   Never reservation-price imputation.
3. A platform blocking capture ≥3 consecutive waves triggers the
   platform-continuity decision (secondary platform promotes to primary,
   logged as a structural break) and a collection-risk disclosure.

**Base re-freeze (units that turn over; codebook §7 applied).** The base
re-freezes annually at the December wave **from the Ledger's attribute
records**, never from any realized lease: the base advertised rent for link
t = the t−1 December-wave advertised rent of the same panel unit × frozen
unit type (or its miss-ladder substitute); the base fee stack = the t−1
recorded mandatory stack. Turnover between waves changes nothing — the
concept is the posted new-lease menu. Extras acquired via superset routes (a
reserved spot when unreserved was frozen) do not enter the next base (no
ratchet); a degraded default (trash fee imposed mid-year) does not become the
entitlement (no forgiveness drift): the event stays priced until the December
re-freeze closes the link it belongs to.

---

## 3. The posted-vs-realized audit (mandatory per P5)

**Why it exists.** The panel prices *posted* menus, but the sector's
documented failure mode is that fees were historically revealed at
application, not in listings (the NCLC record; the FTC complaints). Without
an audit, the module's fee stack is a lower bound on the realized stack and
nobody knows by how much. The audit measures that wedge and publishes it.

**Governance (all pre-committed in the plan, restated as binding here):**
counsel-gated per WS-G — **no application is filed before written counsel
review** of the protocol (mystery-shopping exposure: misrepresentation,
FCRA/credit-pull mechanics of rental applications [owner-verify with
counsel], state landlord-tenant law); budgeted per WS-H (memo lines 5–6:
counsel $750–2,000; application fees $1,000–2,500/wave — the memo line's
basis reads *"~$50 typical fee × 20–50 paired applications"* verbatim, and
under this protocol the "pair" is **posted-vs-realized, not
tester-vs-tester** (point 3 below), so the basis restates to **20–50
single-trace applications** spanning the same dollar range; the WS-H memo
line is queued for that restatement when the memo finalizes in August, and
the memo's open audit-sizing question should be answered with this module's
rotation arithmetic); **piloted Q4 2026**; **≥2 waves inside the Phase 2
panel year** (plan §2.1/§4).

**Protocol (design; counsel selects the legal form).**
1. **Subsample:** a deterministic rotation over panel units (the (2w,
   2w+1) mod N pattern, sized by the budget line), stratified so each
   market × class cell is audited at least once across the ≥2 waves, and so
   the disclosure-jurisdiction CBSA is always represented (§3.4).
2. **Design forms, in counsel's order of preference** (plan §6 wording:
   *"disclosed-tester or document-based designs where required"*): (a)
   **document-based** — request the lease packet / itemized fee schedule
   before applying, which mandatory-disclosure statutes increasingly compel
   (CO/MN); (b) **disclosed-tester** — identify as a researcher after fee
   disclosure is received (the fair-housing tester tradition is the legal
   anchor here — [owner-verify with counsel: tester-standing precedent and
   its applicability to fee auditing]); (c) **true-applicant** — a genuine
   application withdrawn immediately after the fee disclosure point, only
   where (a)/(b) fail and counsel approves. Hard rules in all forms: never
   sign a lease, never pay beyond the application/admin fees being audited,
   never proceed past the disclosure receipt, withdraw promptly and politely,
   minimize property-staff burden.
3. **Single-operator honesty and the binding tester profile.** Classic
   paired-tester designs (two matched humans) are impossible for a one-person
   team, and this document says so. The audit is a **fee-disclosure audit,
   not a discrimination test**: one trace per audited unit per wave,
   comparing the posted stack (that wave's hash-captured panel record)
   against the application-stage revealed stack (the disclosure documents,
   registered via `capture.py --manual`). **Binding profile clauses,
   pre-registered — this is what makes "not a discrimination test" true ex
   ante rather than asserted:** (i) one tester profile only — the owner's
   true identity, truthful application information, one frozen inquiry script
   used verbatim at every audited unit; (ii) no protected-class attribute
   varies across audited units, and the audit makes and implies no
   fair-housing claim. **Feasibility facts for counsel [owner-verify with
   counsel]:** whether rental applications trigger hard credit pulls, and how
   20–50 applications in one person's name interact with screening-vendor
   serial-applicant flags (several screening vendors are platform-affiliated)
   — both feed the form selection in point 2, and the document-based form (a)
   exists partly because it avoids the problem entirely.
4. **What is recorded per audited unit:** posted stack (from the panel);
   revealed stack (document-grade); every fee present in one and absent in
   the other, name verbatim + amount; term-differentiated pricing revealed at
   application (feeds RENT-A6 and RENT-A5, both under-observed in listings);
   application/admin amounts as actually charged; refund outcomes of
   withdrawn applications (a budget fact and an honesty fact).

**What discrepancies feed.**
- The **posted-fee correction factor**: the published ratio/increment between
  the posted mandatory stack and the realized mandatory stack, by market ×
  class, provenance-tagged `audit/document-grade`, published **alongside**
  the posted-stack series — both gross (posted-only) and audit-corrected
  series print, and the correction is never silently folded into H. Whether
  the corrected series may enter the headline Gap, and within what tolerance
  the two audit waves must agree for the factor to be usable, are **band-file
  questions (GR-B)** — no limit is stated here, by the first-existence rule.
- Fees revealed only at signing with **no posted path** → Exclusion Register
  entries (the leak detector for the posting boundary), plus a drafted ledger
  event where T1–T3 are satisfiable from documents.
- The audit is also the module's **A-R-style completeness check** (rx-100
  vocabulary): a third party documenting a mandatory fee the panel missed is
  wired to the correction protocol, not to embarrassment management.

**3.4 Pre-registered falsification prediction (direction only, no band
here).** In the mandatory-disclosure CBSA (CO/MN), the posted-vs-realized
discrepancy should be **smaller** than in non-disclosure markets — the
lodging post-FTC compression test transplanted (plan §7). If disclosure laws
work, the wedge compresses where they bind; the prediction can fail in
public, and the release will print it either way. **Confound, stated before
any number:** the audit form itself varies with jurisdiction — disclosure
states compel the document-based form while non-disclosure markets may need
tester or true-applicant forms — so a naive wedge comparison conflates the
jurisdiction effect with the measuring instrument. Counsel permitting, the
audit form is **held fixed across all audited cells**; where it cannot be,
form is a recorded stratification variable printed on every exhibit row, and
the exhibit text states the confound before the numbers.

---

## 4. Link mechanics and the comparator

### 4.1 Links

December-to-December, per codebook §6; an event belongs to exactly the link
year containing its effective date. Fee-schedule events (a valet-trash fee
imposed effective 2027-03-01 → 2027 link) enter by effective date from posted
documents; the advertised-rent component is measured December-wave to
December-wave. The 11 non-December waves supply T1 evidence, event detection,
the transient screen, and descriptive dispersion; **they are never chained**
(spec §2.5).

**The P3 exhibit link (defined now, because an undefined link is not a
design).** The P3-MOVER exhibit relative links December-to-December as a
minimum over the **same frozen market × class candidate set** (the panel's
frozen stratum membership) in **both** December waves, with amortized
one-time fees (RENT-A7) included in **both** years' replication cost at their
respective posted amounts — numerator and denominator are the same object one
year apart. The arg-min unit's identity is recorded each wave and every
identity change is logged: the min-operator composition splice spec §2.5
warns against is disclosed on the exhibit rather than hidden, and it is one
more reason the exhibit does not enter H (§1.2).

**Worked date trace (the phase1 §2 convention).** Frozen-panel baseline =
wave Tue **2026-12-01**. First fully in-sample annual link = **the 2027 link
(Dec 2026 → Dec 2027), measured from the December 2027 wave (Tue
2027-12-07)**. Consequence, stated so no reader mistakes it: the plan's
"first fully in-sample 12-month rent link: mid-2027" is a **panel-depth
milestone** (12 months of preservation coverage from the Sprint-0 start), not
a link — no mid-year link exists under codebook §6 (the same correction the
phase1 amendment log records for "October 2027 link"; the plan-side sentence
is queued for its own logged input correction, §9 item 8, so the binding text
stops contradicting the module's schedule). The **H2 2027 flagship release**
therefore ships: the fee-stack event series (2026- and 2027-link events by
effective date, to date — **2026-link events predate the panel freeze and
rest on unfrozen Sprint-0 preservation captures and ledger evidence: they are
labeled archival/ledger-grade, the phase1 verified-preprint pattern, never
panel output; GR-C covers panel-derived relatives only, and the release says
which numbers it does not cover**), the audit results and correction factor,
the backcast exhibits (§4.4), and a **labeled panel-year descriptive
window** — never chained, never annualized without its window length printed
— with the 2027 link following in **the first release after the January 2028
confirmation wave completes** (§2.3: the annual link computes only after the
following January wave; a release issued between the December 2027 and
January 2028 waves could not lawfully contain it).

### 4.2 Comparator

**CPI Rent of Primary Residence** item stratum, 12-month relative
([owner-verify exact series ID and current publication structure on an
unblocked connection]); `vintage=` tagged; `bridge=oct2025` flagged on any
backcast window spanning October 2025 (codebook §6). **The headline
comparator is the national stratum even though the panel is six large
CBSAs — a stated composition choice, not an oversight:** the Gap's CPI side
must be the series households and critics actually see, and a bespoke
metro-blend comparator would be a new object with its own seams. The
composition mismatch loads into the spread and is disclosed as such on every
release; BLS metro-level rent relatives for the panel CBSAs publish alongside
as context rows where they exist ([owner-verify metro series IDs and
publication cadence — several panel-scale metros publish only bimonthly]).
The BLS/Cleveland Fed new-tenant rent research series is the concept-closest
*context* series for the advertised-rent component and is shown alongside
where its vintage exists at print time — [owner-verify current name and
publication status] — but the headline comparator is the CPI stratum per P5:
the Gap must difference against what official CPI actually publishes for the
strata households see.

### 4.3 Double-counting avoidance — the P5 rationale, stated precisely

CPI rent prices **contract rent**: everything provided in exchange for rent,
continuing-tenant panel, 6-month repricing, with quality adjustment for
utility-bundling changes. The module's target concept was chosen so the two
measures partition cleanly rather than overlap:

1. **The module never re-prices contract rent.** Its rent component is the
   posted new-lease price — a different measurand. The spread ρ − π therefore
   contains a known **timing/composition difference** (new-lease rents lead
   the all-tenant stock in both directions), which is published as its own
   decomposition row, expected to dominate the spread's variance, and
   explicitly **not** claimed as mismeasurement — the complementarity
   framing, exactly as ruled for telecom (P6).
2. **One-time fees are pure wedge — and exhibit-only in v1.** Application/
   admin/move-in fees have no home in CPI rent (plan §2.1, verified) — the
   amortized RENT-A7 component can never double-count anything CPI holds. It
   rides the P3 exhibit (§1.2), outside the headline Gap.
3. **Recurring fees net out in the spread in expectation, not identically.**
   If a separately billed mandatory fee is in fact captured by CPI (a
   respondent reports it as rent, or a quality adjustment books it), then π
   contains it — but on CPI's 6-month continuing-tenant timing, spread over
   the tenant stock, while ρ books the posted change at once at the panel
   unit; and a CPI quality adjustment can shift the base rather than the
   relative. Within any single 12-month link the subtraction nets only
   approximately, and the residual timing mismatch lands in the Gap — washing
   out across links rather than within one. The honest statement is the
   expected direction plus the machinery that carries it: for each fee class
   the release states the predicted CPI capture (high for folded-into-rent,
   low for separately billed, zero for one-time) **before** the numbers — the
   Southwest-honesty machinery generalized — so a small Gap where CPI works
   is a prediction met, not a disappointment.
4. **Exclusive partition (codebook §9):** when the rent stratum is
   restoration-priced in a period, it leaves the ordinary pool for that
   period; the public concordance maps the module to the CPI stratum.

**Mandatory decomposition, every release (defined so the rows are a real
identity, not a gesture at one).** With C₍t−1₎ the base replication cost
(advertised rent + monthly mandatory stack, per profile), the headline rows
are **base-cost-share-weighted contributions that sum exactly**:

> ρ − π = [Δrent ÷ C₍t−1₎ − (π − 1)] + [Δstack ÷ C₍t−1₎],

plus a **labeled memo line** for the P3 exhibit's amortized one-time
component (outside the headline Gap, per §1.2), each row labeled with its
predicted CPI-capture status. Worked number (executable — lands with
`engine/test_phase2_rent.py` at pre-registration, per the standing repo
rule): base rent $1,500 + stack $100 ⇒ C₍t−1₎ = $1,600; current rent $1,560 +
stack $130 ⇒ ρ = 1690/1600 = **+5.625%**; π = +3.5% ⇒ rent row = 60/1600 −
3.5pp = **+0.25pp**; stack row = 30/1600 = **+1.875pp**; sum = **+2.125pp** =
ρ − π exactly. Negative prints are features: a decelerating new-lease market
or a consent-decree fee elimination prints negative, and the module's
credibility rests on printing it.

### 4.4 Backcasting (archival-grade exhibits, never chained into the live series)

Pre-~2023 fee stacks are reconstructed from: **enforcement exhibits** — the
FTC v. Invitation Homes and FTC & Colorado v. Greystar complaints and
consent-order records carry dated fee schedules ([owner-verify exhibit dates
and amounts against the filings on an unblocked connection; the plan verifies
the settlements and magnitudes]); the **FTC-2026-0266 docket corpus**
(comment record of the rental-fee ANPRM — fee schedules and tenant
documentation, dated); and **archived listings** (Wayback — legitimate for
listing HTML with the standing caveat that JS-heavy pages archive
unreliably; each exhibit carries its own capture-quality note). All backcast
output is labeled **archival-grade, exhibit-only**: it demonstrates the fee
stack's history and sizes the wedge the panel will measure; it is never
spliced into a published link (spec §9.2 — no backfilling across
observability breaks; Zillow Total Price 2025-07-15 and the state disclosure
laws are dated break points, exactly like lodging's 2025-05-12).

---

## 5. Incidence and weights (codebook §8; register rows to be added to `data/incidence-proxies.md`)

**Stratum weight.** Rented dwellings per the pinned Dec-2024 R-CPI-I recipe on
published CE bottom-two-quintile tables: Q1 $5,781/yr (16.5% of $35,046), Q2
$6,225/yr (12.4% of $50,054) — plan §1, 2024 vintage; refreshed at the
scheduled Table 1101 pull. Renter share of B40 households: **~53% of
bottom-quintile households rent** (plan §2.1, web-verified 2026-07-04);
owner-task: pull the CE homeowner/renter shares (the plan §9 item 7 series,
CXUHOMEOWNLB0102M/0103M) for the exact B40 recipe figure —
`published-table/usable` once byte-verified.

**Fee-incidence register (initial rows; rules of use are the standing ones —
a line item is weighted only by a usable-tagged figure with its assumption
stated, else the published [0%, 100%] interval applies; tags travel into
every release):**

| Quantity | Value | Provenance | Status |
|---|---|---|---|
| Application-fee incidence at re-search | 79% of recent renters paid; ~$50 typical | plan §2.1 (web-verified 2026-07-04); underlying survey source to be byte-verified — [owner-verify] | **usable-with-caveat** (flow concept: "recent renters" ≈ movers, matching P3's conditioning; P3 is exhibit-only in v1, §1.2) |
| Involuntary-move rate m (P3 share; also the headline's excluded-share disclosure) | no repo source | candidate: AHS / CPS reason-for-move tabulations — [owner-verify] | **GAP — [0%, 100%]** until a usable source lands |
| Car-owning renter share c (P2 partition parameter) | no repo source | candidate: CE detail / NHTS — [owner-verify] | **GAP — [0%, 100%]** |
| Month-to-month share (RENT-A6 exposure) | no repo source | candidate: AHS lease-term tables — [owner-verify] | **GAP — [0%, 100%]**; the 5–20% premium range (plan §2.1) is the price side, not the incidence |
| Mandatory recurring-fee prevalence | measured by the panel itself (share of panel units posting ≥1 mandatory recurring fee) | panel census statistic, labeled **panel-scope**, never national | usable within its stated scope; FTC/NCLC exhibits as `envelope/sanity` |
| Valet-trash fee level | $25–50/mo | plan §2.1 (web-verified) | price evidence, not incidence; incidence [0%, 100%] until the panel measures prevalence |

No assumption share appears anywhere in this module; where the register says
GAP, the release publishes the interval, exactly as Phase 1 does for
carry-on incidence.

---

## 6. Wave runbook integration and QC

- **Step R0 (T−1, sandbox):** rent wave worksheet appended to the existing
  Step-0 generation (`pipeline/build_worksheet.py` extension at freeze:
  panel-unit list, platform assignment, quarterly dual-platform flag,
  deterministic audit/manual-save rotation).
- **Step R1:** `capture.py --sector rent` static targets — **property- and
  manager-owned fee pages only** (§2.3 ladder: the listing platforms are not
  grade-1 targets); never run unfiltered.
- **Step R2:** Chrome-agent **Prompt D** (panel units, primary platform;
  content-grade), on the owner's browser, safety rails per §2.3.
- **Step R3 (December + rotation):** owner manual saves via
  `capture.py --manual` for **every link-entering December observation (all
  ≈48 panel units)** and the rotating audit cells.
- **Step R4:** ingest to `data/captures/rent-<YYYY-MM-DD>.json`;
  `pipeline/validate_capture.py` rent schema fails loudly on malformed
  records; all computed fields at ingestion.
- **Step R5:** fee-diff triage vs prior wave → ledger drafts with T1/T2/T3
  checks; decreases identical; MISS/RECONFIG and no-priced-path entries draft
  Register entries.

**QC (rent rows added to the standing checklist):** QC-R1 unit completeness
with missing codes; QC-R2 mandatory stack present or explicitly empty per
unit (whole-menu census); QC-R3 advertised rent verbatim + Total Price
cross-check recorded where shown (codebook §2.3); QC-R4 fee diffs → event
workflow; QC-R5 manual saves have sha256 + file; QC-R6 fee-conflict flags
resolved or held per §2.3, never dropped; QC-R7 no concession-adjusted price
in any headline field (RD-3); QC-R8 pet/deposit fields routed to
Register/conditioning, never the stack; QC-R9 same-band rule respected
(RD-9 — no cross-type unit in any H field). A wave is complete when every
check is green or every red item carries a missing code — an unflagged hole
is the only failure state.

---

## 7. Honest hours, budget, and the single operator

All timing figures below are **sizing assumptions, not measurements** — the
rent wave-0 pilot (§8: the draft formula run on an unfrozen, labeled pilot
snapshot, target October or November 2026, unpublished) logs its wall-clock
total in the capture JSON and commits it, and the frozen K/M/N/P_max are set
against that committed number at pre-registration, the same committed-number
discipline as phase1 §6. **Sizing basis, stated rather than hoped down:** the
repo's only measured per-cell number is phase1 §6's **8 min/cell**. A
property page with an expandable fee section is plausibly cheaper than a
paired two-leg fare flow — one page, no flow navigation — but "plausibly
cheaper" is a hypothesis, not a basis, so this section sizes at the measured
number until the pilot commits a rent-specific one; the hypothesized
single-page figure (~3.5 min) is shown in parentheses so the pilot's stakes
are visible.

- **Standing monthly:** Step R1 ~15 min; Step R2 ≈ 48 panel units × 8 min ≈
  **6.4 h** (≈ 2.8 h at the hypothesized basis); Steps R0/R4/R5 ~45 min ⇒
  **≈ 7.4 h/wave at the measured basis (≈ 3.8 h hypothesized)** — the
  components sum to the stated totals at either basis. Quarterly
  dual-platform sweep at the same basis ≈ **+6.4 h** in March/June/September
  (fee-fields-only extraction may prove cheaper; same rule — the pilot
  decides, not this paragraph), which is exactly why the sweep is first in
  the de-scope order below.
- **December extras (at the measured basis):** dual-platform sweep ≈ +6.4 h;
  link-wave manual-save upgrade ≈ 48 saves × ~3 min ≈ **+2.5 h** (the §2.3
  hashed-artifact claim, priced); annual re-freeze from attribute records +
  succession processing + incidence refresh ≈ +1–1.5 h ⇒ **≈ +10 h**
  (≈ +5 h at the hypothesized basis).
- **Audit:** pilot Q4 2026 ≈ 8–10 h + application-fee spend (WS-H line 6,
  restated basis per §3: $50 × 20–50 single traces = $1,000–2,500/wave).
  Counsel review before any application (WS-H line 5: $750–2,000).
  Each of the ≥2 in-panel-year waves ≈ 6–8 h.
- **One-time build:** selection script + parser round-trip (§8) + Prompt D +
  validator/worksheet extensions + targets rows ≈ **14–18 h**
  (sandbox-buildable except captures and the pilot snapshot, which are
  owner-machine).

**The stacked truth, stated rather than hoped down:** Phase 1 already runs
≈ 8.7 h/wave (~9.7 h/month with the press watch, phase1 §6 as amended). At
the measured basis this module adds ≈ 7.4 h/month standing: **≈ 17 h/month
total, before the telecom module's own standing load — nowhere near
single-digit**; even at the hypothesized single-page basis the stack is
≈ 13.5 h/month, still not single-digit. The plan's resourcing row (§5)
assumed a two-person core that does not currently exist. Consequences,
pre-stated: (i) the rent pre-registration must carry its own de-scope order
(candidate order, to be frozen there: drop the quarterly dual-platform sweep
except December (−6.4 h in three months at basis) → K 4→3 per stratum (36
units; R2 ≈ 4.8 h at basis) → M 6→4 markets **under the §2.2 pinned M = 4
variant** (24 units; R2 ≈ 3.2 h)), triggered by the committed pilot number,
not recollection; (ii) if the stacked total still exceeds what one operator
can sustain, the **plan-level** resolution (defer telecom collection, or
fund the second person per WS-H) is an owner decision this module document
cannot make and does not pretend to.

**Single-operator disclosure (structural, printed):** every wave, the
December link, the audit applications, and all owner-machine pulls run
through one person; the December ladder (§2.4), the 2-skippable-waves
allowance, and the December backup window (second Tuesday) are the only
hedges. There is no backup operator, and this document says so. The sandbox
proxy blocks Zillow, Apartments.com, carrier and government hosts — **every
capture in this module runs on the owner's machine** via
`pipeline/capture.py` and Claude-for-Chrome prompts; sandbox work is limited
to formulas, validators, worksheets, and tests.

---

## 8. What freezes when (the G0/G1 pattern; this document freezes nothing)

1. **This document is a DRAFT design.** It binds nothing; it exists so the
   freeze package can be reviewed as a whole and attacked before it hardens.
2. **Commit ordering at freeze (band first, then inputs, then results —
   never another order):** `docs/phase2-rent-band.md` (pass criteria; **the
   first and only existence of every numeric limit** for this module — audit
   tolerance GR-B, non-event tolerance GR-D, reproduction tolerance GR-C;
   its header states its relation to plan gate G2 without borrowing the G2
   label — the g1-band GA–GD collision-avoidance precedent) → **pre-freeze
   parser validation:** the wave-0 pilot's unfrozen snapshot (rendered-DOM
   Save-Page-As output, not `capture.py` raw fetches — the platforms are JS
   applications and the frozen parser must be proven against the artifact
   format it will actually read) round-trips through
   `select_rent_panel.py`'s parser — canonical URLs, unit counts, floorplan
   counts, manager-of-record strings, fee fields all extracted — **before
   the formula commits**, so a parse failure is a pre-freeze bug, never a
   post-freeze MAY-NOT design failure →
   `docs/phase2-rent-preregistration.md` + `pipeline/select_rent_panel.py` +
   the frozen attribute dictionary (§1 as amended by review) →
   `data/phase2-rent-inputs.md` (hashed ACS file; hashed per-CBSA search-URL
   lists; hashed freeze-wave walk snapshot) → computed market and panel
   lists → collection enters links. Worked-example arithmetic in the
   pre-registration lands with executable tests
   (`engine/test_phase2_rent.py`) in the same commit, per the standing repo
   rule.
3. **Band tests (named now, limits later):** **GR-A** external review — the
   module rides the scheduled H1 2027 review (plan §4, gate G2), no bypass;
   **GR-B** posted-vs-realized audit — the correction factor's usability
   condition; **GR-C** independent reproduction of markets, panel units, and
   every published relative from hashed inputs + code + the codebook, with
   disclosure parity (the GD pattern); **GR-D** the relabeling non-event
   test, **in two arms so the battery is never vacuous** (RD-2's "the
   consent decrees are expected to force exactly this folding" is a
   prediction, not a certainty): a **conditional arm** that fires only where
   a documented in-panel consent-decree fee-folding event exists inside the
   link year (existence condition stated in the band file; if no such event
   occurs the arm records not-applicable, never silent-pass), and an
   **unconditional executable arm** — a worked folding example in
   `engine/test_phase2_rent.py` proving the ρ ≈ 0 arithmetic within the
   band-file tolerance. The §3.4 compression prediction publishes as a
   falsification exhibit; whether it should also gate is a reviewer
   question.
4. **Deadline logic:** freeze complete before the **2026-12-01 wave**, or the
   first fully in-sample link slips a full year to the 2028 link — stated so
   the schedule pressure is visible now, not discovered in November.
5. **MAY / MAY-NOT after sign-off (to be enacted verbatim in the
   pre-registration):** inputs (vintages, URLs, series IDs, fee amounts in
   evidence) MAY be corrected with logged amendments; the dictionary and its
   worked rulings RD-1–RD-10, the profile definitions and the P3
   exhibit-only status (promotion only via the §1.2 logged-amendment path),
   the panel formula (M, K, N, P_max, strata, the SSF manager × market unit
   and its LMF-only fallback, the walk-order rule, the succession rule, the
   M = 4 variant), the platform-assignment and fee-conflict rules, the
   anti-promotion split and the December session ruling, the missingness
   rules and December ladder, the amortization and cadence-normalization
   conventions, the decomposition identity, the comparator, and the de-scope
   order MAY NOT change after sign-off; any post-hoc case for changing them
   is a logged design failure with a methods note.
6. **The pilot object (pinned, so the pilot–freeze circle is cut):** the
   rent wave-0 pilot runs the **draft** formula on an **unfrozen, labeled
   pilot snapshot** (the Sprint-0 preservation candidates), explicitly stated
   to neither constrain nor contaminate the frozen panel — the frozen panel
   selects from a later snapshot regardless. The pilot's committed outputs
   are exactly two: the per-unit wall-clock timing number (§7) and the
   parser round-trip (item 2). Nothing selected in the pilot carries any
   standing.
7. **Preservation capture is exempt and urgent** (plan P3): the unfrozen
   rental panel v0 (Zillow Total Price + Apartments.com fee fields at
   candidate properties) should run on the owner's machine now — baseline
   listings churn and cannot be reconstructed; the frozen panel will select
   from a later snapshot regardless, so preservation capture cannot
   contaminate the freeze.

---

## 9. Open items

1. Owner: run the overdue Sprint-0 preservation capture (plan §9 item 2) —
   the module's most time-sensitive task; it also supplies the §8 pilot
   snapshot.
2. Owner: counsel engagement for the audit protocol (WS-G; WS-H line 5) in
   time for the Q4 2026 pilot; counsel chooses among the §3 design forms and
   answers the §3 credit-pull / screening-vendor questions; the WS-G scope
   now also explicitly covers automated capture of the listing platforms
   (§2.3).
3. Owner byte-verification queue: ACS table ID + available vintage; CPI Rent
   of Primary Residence series ID + metro rent series IDs and cadences
   (§4.2); new-tenant rent series status; the 79%/$50 application-fee survey
   source; Invitation Homes/Greystar exhibit dates and fee schedules;
   AHS/CPS/NHTS incidence pulls (§5); SSF manager market-level fee-page
   existence and stability (at the §8 pilot); CO/MN statute scope details
   beyond the plan's wording.
4. Rent wave-0 pilot → committed wall-clock number + parser round-trip (§8)
   → frozen K/M/N/P_max and de-scope order in the pre-registration.
5. Reviewer questions for the H1 2027 round (and the August packet where it
   can carry them): should the fee-stack component or the full Gap lead the
   release, given the timing-difference row will dominate variance? Should
   the P3-MOVER exhibit be **promoted** into H — the v1 default is
   exhibit-only per codebook §2.2 (§1.2), and promotion requires a logged
   codebook/spec amendment the review would have to endorse? (The SSF
   feasibility question from the first draft is closed by ruling, not by a
   reviewer: §2.1 redesigns the unit and pre-commits the LMF-only fallback.)
6. Whether the audit-corrected series may enter the headline Gap (a GR-B
   band-file design question, decided at freeze, not here).
7. Codebook next-revision queue (logged amendments per its own policy): fold
   the frozen dictionary into codebook §3 per the Phase-2 dictionary
   mandate; restate codebook §2.3's rentals clause ("listed total price
   fields") to the component-built wording this module reconciles in §2.3.
8. Plan input correction (logged via the plan's changelog, the phase1
   "October 2027 link" precedent): restate plan §2.1's "First fully
   in-sample 12-month rent link: mid-2027" as "panel 12+ months deep by
   mid-2027 (preservation coverage); first fully in-sample rent link = the
   2027 link (Dec 2026 → Dec 2027), measured from the December 2027 wave."
9. WS-H memo (finalizes August): restate line 6's basis from "20–50 paired
   applications" to 20–50 single-trace applications per §3, and answer the
   memo's audit-sizing open question with this module's rotation arithmetic.

## Changelog

- v0 (2026-07-11) — first complete draft: attribute dictionary v1 with
  binding-at-freeze rulings RD-1–RD-8 and profiles P1–P3; the fixed-property
  panel formula (6 CBSAs × 2 classes × 4 properties, deterministic, G0-pattern
  freeze ordering, succession rule); capture protocol, provenance ladder, MISS
  codes, and the December re-freeze rule; the posted-vs-realized audit design
  with counsel-gated forms, the posted-fee correction factor, and the
  disclosure-jurisdiction compression prediction; Dec–Dec link mechanics with
  the mid-2027 milestone-vs-link correction and the 2026-12-01 freeze
  deadline; the P5 double-counting rationale stated precisely with the
  mandatory three-row decomposition; incidence register rows with [0%, 100%]
  defaults; honest-hours arithmetic including the stacked-total disclosure;
  freeze mechanics with named band tests GR-A–GR-D and no numeric limits
  anywhere in this file.
- v0 (2026-07-11, same-day revision) — adversarial-review pass applied: two
  independent reviewers, 39 findings (including cross-reviewer duplicates),
  all adjudicated valid and applied; none rejected. Load-bearing corrections:
  (1) RENT-P3 defaulted to **exhibit-only** per the codebook §2.2 / spec §2.2
  same-seller headline rule, with a defined exhibit link (§4.1), a
  decomposition memo line, and a logged-amendment promotion path — the draft
  had frozen a codebook violation into the headline while leaving it an open
  question; (2) the profile grammar made an exact partition (P1 stack
  excludes A2; P1/P2/P3 = (1−m)(1−c) / (1−m)c / m; headline renormalizes over
  1−m); (3) CLASS-SSF redesigned to **manager × market** cells with a 3BR
  band, deterministic ≥N-pages manager qualification, and a pre-committed
  LMF-only fallback — the property-level SSF panel was structurally
  unobservable; (4) the selection formula made executable and GR-C-
  reproducible: committed per-CBSA search-URL lists from a frozen
  principal-city rule, URL-hash walk order replacing platform IDs,
  walk-defined snapshot manifest with P_max, deterministic region assignment,
  and a pinned M = 4 de-scope variant; (5) primary platform made the fee
  stack of record (the per-field union was an upward ratchet violating
  codebook §4 symmetry), with presence/absence conflicts and a
  two-consecutive-readings rule for no-fee-page units; (6) codebook §2.3's
  binding rentals clause cited and reconciled (Total Price = pinned
  cross-check; codebook amendment queued); (7) provenance ladder corrected —
  the platforms are grades 2–3 only (capture.py is a urllib fetcher; ToS),
  grade-1 reserved for owned fee pages, automated platform capture added to
  WS-G scope, and the December manual-save obligation priced (≈48 saves);
  (8) hours re-based to the measured 8-min phase1 basis (≈7.4 h/wave, stacked
  ≈17 h/month at basis; ≈13.5 h at the hypothesized single-page basis) with
  arithmetically consistent sweep and December figures — superseding the
  draft's 3.5-min assumption and its 13–14 h sum understatement; (9) the
  §8 ordering gains a pre-freeze parser round-trip and a pinned pilot object
  (circularity cut); (10) GR-D given conditional + unconditional arms so the
  gate is never vacuous; (11) the December rent-substitute window narrowed to
  ±15 days with the seasonality rationale stated; (12) the decomposition
  defined as base-cost-share contributions with an executable worked number
  (+0.25pp / +1.875pp / +2.125pp); (13) §4.3(3)'s "the spread construction
  prevents double-counting" softened to the expected-direction statement with
  the within-link timing caveat; (14) the band file renamed
  `docs/phase2-rent-band.md` (gate-G2 label collision; the g1-band GA–GD
  precedent); (15) audit protocol given binding single-tester-profile
  clauses, credit-pull/screening-vendor owner-verify items, the
  single-trace budget-basis restatement of WS-H line 6, and the §3.4
  form-confound statement; plus RD-9 (same-band-only replication, closing
  the §2.1-vs-§2.4 contradiction), RD-10 (cadence normalization), the
  RENT-A1 quote-boundary fix, the RD-6 citation fix (§2.1, not §2.4), the
  A5 expected-MISS acknowledgment with audit routing, single-session
  December rent ruled explicitly, link-release timing corrected to after the
  January 2028 confirmation wave, 2026-link events labeled
  archival/ledger-grade with GR coverage stated, national-comparator
  composition disclosed with metro context rows, frozen-unit-type triple
  underspecification pinned (freeze snapshot; ±10% band; lowest starting
  rent with tie-breaks), portal/membership discounts defined in §0, the
  plan-§2.1 and WS-H amendment queue items added, and register-JSON
  consistency fixes (A2 superset flag on the tier route; P3 exhibit-only;
  band-file rename).
