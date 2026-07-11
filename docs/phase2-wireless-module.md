# Phase 2 wireless/telecom module — attribute dictionary, T-Mobile 2026-link design, seller panel, profiles

`v0 · 2026-07-11 · workstream D (sector module; collection hooks in B) · STATUS: DRAFT — nothing here is frozen; the dictionary and computation design freeze with the Phase 2 pre-registration and its own pre-committed band file, and no wireless-link computation may run before that band commits (the G0/G1 first-existence discipline). This document contains no numeric pass limits by design.`

This document drafts the Phase 2 wireless/telecom module: the attribute
dictionary v1 (codebook §13 names this as a Phase-2 deliverable), the
computation design for the flagship event — T-Mobile's 2026-07-13 forced
migration of 8M+ customers (the captured unit; the ledger entry's "lines"
wording is a logged discrepancy — open item 10), pre-assigned to the **2026
link** by codebook §6 and already fully captured in `data/ledger-events.json`
(`wireless-tmobile-202607`) plus
`data/captures/tmobile-premigration-2026-07-04.json` and
`data/captures/tmobile-legacy-vectors-2026-07-04.json` — the seller panel, the
profiles and incidence sources, and a broadband sidecar sketch. It
operationalizes Spec v00.02.00 and codebook v0; where anything here conflicts
with those, they govern and the conflict is a logged erratum. Posture, restated
because every artifact must: the measure is an **upper bound published only as
a spread** over the matching CPI series; it is not a cost-of-living index and
makes **no "true inflation" claim** in any artifact; negative and zero prints
are features; every public number carries a provenance tag; posted national
plan menus make this a **census of menus**, not a sample — no standard errors
are claimed anywhere in this module.

**The module's claim is complementarity, not correction (plan P6, binding).**
Telecom is where CPI has the *most* quality machinery: since July 2025, CPI
wireless is built from vendor-scraped near-universe *advertised* plan menus
under expenditure-weighted full-menu hedonic regressions (plan §2.2,
web-verified). Grandfathered rates are not advertised offers, so the
migration's bill impact largely falls **outside CPI's measurand**, not inside
it mismeasured. CPI answers constant-quality offer inflation; this module
answers what it costs the 8M+ migrated customers to keep last year's bill.
Both statements appear in every wireless release.

Companion binding files (existing): `docs/codebook-v0.md` (§2 equivalence, §3
dictionaries, §4 triggers, §5 route hierarchy, §6 link years, §7 re-freeze, §8
incidence), the two capture JSONs above, `data/ledger-events.json`,
`pipeline/targets.tsv` (wireless rows: `att-plans` and `verizon-plans`
standing; the five T-Mobile-event rows are `urgent` one-shots whose
post-migration disposition is an owner task — §4.2). Companion files that do
**not yet exist** and must exist before any computation: the Phase 2
pre-registration and its band file (commit ordering: band → pre-registration →
pinned inputs → results — never another order), which **commit before the
December-2026 link wave runs** (§3.5, open item 8).

---

## 1. Scope and unit of account

- **Sector**: consumer postpaid wireless phone service (the CPI stratum
  currently mapped as "Wireless telephone services" in `docs/rx-100-tier-map.md`,
  mock B40 share 1.80% — the official BLS stratum name carries the tier map's
  standing byte-verification flag [owner-verify]).
- **Coverage disclosure (prepaid), stated up front:** the CPI stratum this
  module differences against — and the 1.80% mock share it would be weighted
  by — covers **all** wireless service including prepaid, where
  budget-constrained households (the project's own target population)
  concentrate. v1 prices postpaid only. The release therefore publishes the
  **postpaid share of the stratum as the module's coverage figure** —
  [0%, 100%] until the owner pulls carrier/FCC disclosures on an unblocked
  connection [owner-verify] — and the Phase 2 pre-registration states whether
  the sector weight is scoped down to postpaid or the release carries the
  partial-coverage caveat. Prepaid (Metro by T-Mobile, Cricket, Visible,
  Boost et al.) is the obvious v2 extension: flanker menus are posted,
  national, and cheap to capture.
- **Unit of account**: the monthly recurring charge for a fixed line
  configuration (line count frozen per profile), posted **list** price
  (codebook §2.3: no promo, no AutoPay/paperless conditioning in the headline).
  **For taxes-exclusive plans the monthly unit of account is all-in as far as
  the menu posts it: FCC-label list price plus the label's itemized
  carrier-imposed recurring fee lines** (Regulatory/Telco recovery and kin —
  captured at $4.49/line on the 2026 labels, $2.71/voice line in 2016);
  government taxes are excluded and the exclusion is stated (they are
  unposted). This is a rule, not a footnote: codebook §4 defines non-events on
  **all-in replication cost**, and the W6 guarantee's "taxes/fees excluded"
  carve-out makes the surcharge line the carrier's stated safe harbor — a
  carrier can hold the label price and raise its own fee lines, so those lines
  are in C(z; t), in the Step-5 diff (§4.2), and a surcharge move on an
  unchanged menu enters ρ as a scalar move (the §4.3 pattern). One-time fees
  (device connection charge, $35/line on the captured 2026 labels) are
  recorded and excluded from the monthly headline; they enter only at a forced
  re-search event, amortized — the rent-module P5 parallel — and the
  2026-07-13 migration itself imposed none (automatic migration; no connection
  charge observed in the captured notice [owner-verify against the first
  post-migration bill evidence]).
- **Menu M_t**: the carrier's publicly posted consumer plan menu **plus, for a
  migrated cohort, the migration-target plan codes assigned to it in the
  T-Mobile-internal crosswalk as published by tmo.report** (carrier-adjacent
  press — the capture's own notes record the outlet as unofficial, its figures
  from its own reporting/sources; the "seller-published" upgrade happens only
  if authenticity verifies at the download, §3.3) — those codes are the menu
  those households actually face, and excluding them would overstate the gap.
  This union ruling is a design decision the Phase 2 reviewer is asked to
  evaluate, with its rejection fallback pre-registered (open item 1).
- **Device financing exclusion rule (binding in v1):** device installment
  plans, trade-in credits, and "on us" device promotions are **credit and
  financing arrangements, not service-menu attributes**. They never appear in
  the dictionary, never enter C(z; t), and never offset a service repricing.
  A phone is a good with its own CPI stratum; this module prices the service.

## 2. Attribute dictionary v1 (freezes with the Phase 2 pre-registration)

Codebook §3 style: attributes are enumerated **before** collection; no
attribute may be added retroactively to an already-frozen base. Every attribute
below is evidenced as contractible by the captures — each appears as a named
tier delta, line item, or documented inclusion on an archived T-Mobile menu.

| # | Attribute | Definition (ledger language) | Contractibility evidence (captured) |
|---|---|---|---|
| W1 | Line count | Number of voice lines on the account; per-line price structure recorded verbatim (1–5+ lines) | Every captured menu prices per line count; FCC labels give 1–5-line list prices |
| W2 | Unlimited talk/text | Unlimited domestic voice minutes and SMS | Universal on captured menus 2016→2026; still recorded (a future metering event must be detectable) |
| W3 | Data allowance class | Two recorded fields: (a) high-speed allowance in GB ("unlimited" admitted); (b) **premium/deprioritization threshold** — the GB point before which the line is not deprioritized (Essentials "50GB premium data"; 2017 ONE ">30GB (top 3%)" prioritization note; 2019 Magenta ">50GB" congestion note — all captured verbatim). A current plan weakly dominates on W3 iff both fields weakly dominate. **≥10% threshold reductions are separate attribute events**, mirroring the codebook §2.1 bag-size rule. | Simple Choice 2GB/line; Essentials 50GB premium; Experience tiers "unlimited premium data" |
| W4 | Hotspot allowance | High-speed tethering GB + the fallback class (none / unlimited-at-3G / N GB high-speed / unlimited). **Capture silence is never encoded as attribute absence** (the Simple Choice rule, §3.2). | Magenta 3GB then 3G; Magenta Plus 20GB; Experience More 60GB (post-allowance fallback class not captured — [owner-verify], §3.4); Beyond "unlimited" on the public card vs "250GB" in the crosswalk narrative — discrepancy recorded, resolved at crosswalk download [owner-verify] |
| W5 | Taxes-and-fees-included pricing | Whether the posted price is all-in (taxes and regulatory fees included) or exclusive. A genuine attribute, not a footnote: ONE, Magenta, and Magenta Plus were taxes-included, Essentials and Simple Choice were not; the migration-target menu has explicit "(TI)" and "TE (Tax Exclusive)" variants (captured), so the seller itself contracts on it. **Direction of the wedge, stated because the upper-bound posture depends on it:** where a taxes-exclusive comparison is unavoidable, the TE price plus the itemized carrier fee stack (captured: Regulatory/Telco recovery $4.49/line 2026, $2.71/voice line 2016; Federal & Local Surcharges typ. $0.36–4.79/line on the Beyond 55+ label) is a **flagged floor on the wedge, never a ceiling** — the captured labels itemize carrier surcharges and expressly leave government taxes out ("govt taxes vary"), so TE + fee stack *understates* the all-in cost of replicating a taxes-included vector. §3.3's numerator rule treats it accordingly. "TI" read as tax-inclusive is an inference from the captured "TE (Tax Exclusive)" label [owner-verify at crosswalk download]. | Captured labels + crosswalk variant names |
| W6 | Price-lock / guarantee terms | The guarantee wording as captured, with its scope: the captured record of the Experience guarantee reads "5-year price guarantee on talk/text/5G data (taxes/fees excluded)" — both capture files carry that string; the exact on-page wording is re-verified verbatim at the December wave [owner-verify]. Recorded every wave. A guarantee is a term of the purchased experience; its breach or narrowing is a detectable attribute event (the "Un-contract"/Price Lock erosion is already in class-action litigation, plan §2.2). This module records terms; it does not adjudicate the litigation. | Migration notice page + plan cards |
| W7 | Bundled streaming/perk inclusions | Named third-party inclusions recorded verbatim (Netflix tier, Apple TV offer price, Hulu, AAA, Scam Shield, T-Satellite; seller-stated values captured: Netflix "up to $8.99/mo value", Apple TV "$9.99 monthly value", Scam Shield "$4.00"). **Equivalence ruling (binding): perks do not restore core connectivity attributes and connectivity does not restore perks** — dominance is attribute-by-attribute (codebook §2.1), and a Netflix inclusion cannot compensate a hotspot cut any more than United's gate-check path restores a carry-on. **W7 is excluded from the connectivity replication minimum by rule (§3.3)**; perk-tier degradations are priced as **separate, labeled line items via the perk seller's own posted menu delta** (named-fee cap, codebook §5), never blended into the connectivity headline — see the worked trace in §3.4. Perk *additions* never offset anything, and the mechanism is the frozen-vector dominance argument, not menu-expansion monotonicity: an attribute absent from the frozen vector z cannot lower C(z; t) and is worth exactly nothing to the frozen profile — the AT&T April-2026 hotspot pairing is the named precedent (§4.3, plan §2.2). Spec P2 menu-expansion monotonicity separately covers the genuinely-new-plan case. | Plan cards 2019 (Netflix Basic/Standard) and 2026 (Netflix w/ads, Apple TV $3/mo, Hulu) |
| W8 | Watch/tablet line pricing | Per-line price for wearable/tablet companion lines ($5/mo on captured Experience cards; $20 tablet / $5 wearable on 2017 ONE) | Captured both eras; the migration reprices them (trade-press +$3/line — §3.1) |
| W9 | AutoPay/paperless conditioning | **Not an attribute — a price-menu conditioning**, recorded per codebook §2.3: list price is the headline; the AutoPay price is retained as a labeled sensitivity. The captures already encode this split (Experience Beyond 3-line: $230 list on the Wayback FCC label vs $170 AutoPay card price — a ~$60/3-line wedge the capture's own reconciliation attributes to **AutoPay plus promo discount**, which must be held consistent across both sides of any relative; the 2017 ONE capture pins the era's differential at +$5/line without AutoPay). | Both capture files; reconciliation block in the legacy-vectors JSON |

**Dictionary discipline for legacy micro-features.** Retired conveniences not
in the dictionary (Data Stash rollover, Binge On, T-Mobile Tuesdays, the
KickBack credit) are recorded in event narratives but are **non-binding for
dominance** — the dictionary is the ex-ante enumeration and stays that way.
KickBack ruling: a conditional bill credit, i.e. conditioning/promo, not a menu
attribute; its termination routes to the **Exclusion Register with magnitude**
(the captured example: $10/line on a 5-line account) rather than into ρ. The
credit's qualifying condition (low data usage) is stated from training
knowledge [owner-verify]. This is the ACP pattern from plan §2.2: counted,
not priced.

**Plan identity and renames (freezes with the dictionary).** Plan identity =
the W1–W8 attribute vector plus the line-count price structure, with the
FCC-label plan id as the diff key (the Beyond 55+ capture recovered a full
plan id — these ids are the plan-code key). The flagship seller renames on a
~2-year cadence (Simple Choice → ONE → Magenta → Experience; lettered A/B/C/D
variants; SOC codes captured as "subject to change at any time"), so the rule
is stated now, the Phase 1 fare-family-crosswalk pattern applied: **a rename
at constant attribute vector and constant all-in price is a logged
label-reshuffle non-event** (codebook §4 relabeling rule); a rename
accompanied by any vector or price change is diffed **on the vector, never on
the name**. A rename can therefore neither draft a spurious event nor hide a
repricing or an attribute strip behind new branding.

## 3. The flagship computation: T-Mobile 2026-07-13 → the 2026 link

### 3.1 Event and evidence (all already captured)

`wireless-tmobile-202607`, verified-preprint 2026-07-04: forced migration of
**8M+ customers** (Simple Choice / ONE / Magenta / legacy Sprint) to Experience
tiers on bill cycles starting 2026-07-13, no opt-out. Provenance split, stated
exactly because the tags travel into releases:

- **Carrier-stated (primary notice page, captured):** "The rate of your phone
  plan will increase by up to $6/line per month"; "Some customers will see no
  change to their monthly bill"; 5-year price guarantee on talk/text/5G data
  (taxes/fees excluded); updated bill in T-Life after July 13; no customer
  action required. Tag: `carrier-statement`.
- **Trade-press figures (tmo.report's own reporting — the capture notes the
  outlet as unofficial):** 8M+ customers; voice +$6/line, watch/tablet
  +$3/line, 5G Home Internet +$6; average +$4/line (also in plan §2.2,
  web-verified, without a captured carrier attribution); ~1,100 plan codes
  retired; 62 migration-target codes. Tag:
  `carrier-adjacent-press/usable-with-caveat`; [owner-verify any primary
  T-Mobile statement pinning the count, its unit, or the average — open
  item 5].

Evidence: the primary-source notice page and live target menu
(`tmobile-premigration-2026-07-04.json`) and the Wayback-cited legacy and
pre-migration list vectors (`tmobile-legacy-vectors-2026-07-04.json`). Event
type: **menu-removal**; route: **tier-spread**; **superset-flagged by
construction on W3**: every migration target carries unlimited premium data, a
strict superset of every retired vector's data class. The attribute-wide
superset claim is deliberately *not* made — no target restores a
taxes-included cohort's W5 by default where its assigned variant is TE, and
none restores ad-free Netflix (§3.4) — which is exactly why dominance is
checked attribute-by-attribute and W7 prices separately. The W3 superset is
what justifies the superset flag on the connectivity line item.

**Worked date trace (codebook §6):** effective date 2026-07-13 → inside the
2026 link (December 2025 → December 2026) → the event enters exactly that link,
measured from the December-2026-wave menus, and the link computes after the
January-2027 confirmation wave under the same schedule-posted anti-promotion
rule as Phase 1 (a posted plan menu is a posted schedule; the rule is symmetric
by the same argument). An event nine days into H2 sits on the seam of two
annual links; the pre-assignment is what prevents double- or zero-counting.

### 3.2 The frozen base vectors z (from the Wayback captures)

One frozen vector per recovered legacy generation, from
`tmobile-legacy-vectors-2026-07-04.json`, each with a permanent Wayback
citation (third-party-attestable — stronger than a live extraction). **The
captured prices carry their captured conditioning, disclosed verbatim:** the
2019-era price points are 4-line, AutoPay-conditioned, third-line-free
**promo** prices, and the 2017 ONE point is a 2-line AutoPay promo price. The
table below is therefore **attribute-vector evidence plus price corroboration
at the captured line counts and conditionings only — never a denominator**
(§3.3 states the denominator instrument).

| Generation | Snapshot | Load-bearing attributes (W-numbered) + captured price basis |
|---|---|---|
| Simple Choice (2016) | 2016-05-28 | W1 per-line $50/$30/$10 (list structure, taxes extra); W3 2GB LTE/line (+$15/4GB add-on); W5 taxes EXTRA ($2.71/voice line recovery); **W4 not captured on the archived menu page — capture silence is not attribute absence; [owner-verify from the Wayback plan-detail pages / crosswalk feature descriptions before the dictionary freeze]**; W7 none binding |
| T-Mobile ONE (2017) | 2017-08-12 | W3 unlimited, >30GB deprioritization; W4 hotspot 3G-speed unlimited; W5 taxes/fees INCLUDED; captured price = 2-line AutoPay promo ($50/line), +$5/line without AutoPay — the captured list bridge for this era; ONE Plus +$5/line delta captured (10GB LTE hotspot, HD video) |
| Essentials (2019) | 2019-07-11 | W3 unlimited 4G (may see lower speeds); W4 unlimited-at-3G; W5 taxes EXTRA; W7 no Netflix; captured price = $26/line at the 4-line AutoPay + 3rd-line-free promo basis |
| Magenta (2019) | 2019-07-11 | W3 unlimited, >50GB note; W4 3GB LTE then unlimited-at-3G; W5 taxes INCLUDED; W7 Netflix Basic (1 SD screen, ad-free); captured price = $35/line at the 4-line AutoPay + 3rd-line-free promo basis ($140/mo at that basis) |
| Magenta Plus (2019) | 2019-07-11 | W3 unlimited, premium; W4 20GB LTE then unlimited-at-3G; W5 taxes INCLUDED; W7 Netflix Standard (2 HD screens, ad-free); captured price = $43/line at the 4-line AutoPay + 3rd-line-free promo basis |

Known unrecoverable pages, disclosed: the business.t-mobile.com ONE Unlimited
55+ page (zero Wayback captures at any date; the live page already redirects —
the "capture now" thesis materializing) and the Magenta MAX page (never
crawled; the 2019 Magenta Plus capture is its documented predecessor tier).
Where a cohort's exact vector is unrecoverable, its restoration is computed
from the nearest documented predecessor vector, flagged
`vector=predecessor-generation`, and the cohort is listed in the release
limitations — never silently merged.

### 3.3 The computation (tier-spread route, interval semantics)

**Dominance set (definitional; freezes with the dictionary).** The replication
minimum is taken over bundles weakly dominating z on the **connectivity set:
W1–W6 and W8** (W3 and W4 on their two-field rules; W5 on its own rule below).
**W7 is excluded from the connectivity minimum by rule** and priced
exclusively via the separate-labeled-line-item machinery of §2/§3.4. Stated
consequence of the alternative, which is why the rule exists: a W1–W8 minimum
would be taken over an **empty set** for exactly the Magenta-family cohorts —
no Experience plan restores ad-free Netflix — and an empty min is not a
computation. The connectivity line item and the perk line item never sum into
one headline number.

For each profile e (§5) with frozen vector z:

- **C(z; Dec 2025)** — the denominator. **Primary instrument: the crosswalk's
  own old-plan price column, hash-committed at download.** Honest caveats,
  each load-bearing: (i) the crosswalk is the T-Mobile-internal old→new
  mapping **as published by tmo.report** (carrier-adjacent press; the
  capture's own notes say the outlet's figures come from its own
  reporting/sources) — the download task therefore includes **authenticity
  verification** (document metadata; cross-checks against the captured
  migration notice and the 2024/2025 repricing notices), and no "seller-
  published" language is used unless authenticity verifies; (ii) **whether an
  old-price column exists at all is unverified** [owner-verify at crosswalk
  download] — the capture documents "the full row-by-row old-plan-to-new-plan
  mapping with every price" in the downloadable files, which implies but does
  not establish it. The §3.2 Wayback captures are corroboration only: their
  2019 prices are AutoPay-conditioned, third-line-free-promo, 4-line points,
  and **no AutoPay bridge alone un-promos them** — codebook §2.3 bans promo
  conditioning from headlines, so reconstructing a launch-era list price from
  them requires seller-documented de-promo evidence, not an operator
  adjustment. The two documented legacy repricings (May 2024 +$2–5/line,
  April 2025 +$5/line — plan §2.2, web-verified) enter on top of whichever
  instrument survives. **Pre-registered fallback ladder if the old-price
  column is absent or lacks a profile's line count:** (a) the cohort's
  denominator is restated at a captured line-count point (a logged, disclosed
  convention); (b) failing that, the cohort routes to the **Exclusion
  Register with magnitude** — counted, not priced. A grandfathered billed
  rate is not a posted-menu price; its admissibility as C(z; t−1) is open
  item 2, whose rejection consequence is pre-registered there. The honest
  argument for admissibility: it is the documented price of the base-period
  purchased experience, evidenced by the seller's own migration notice and —
  if authenticity verifies — the crosswalk. **The crosswalk download is the
  single most outstanding owner task in this module**; tmo.report is a blog,
  not an archive.
- **C(z; Dec 2026)** = min over M_t (public Experience menu ∪ the cohort's
  crosswalk-assigned target codes) of the **all-in monthly unit of account
  (§1)** of any bundle weakly dominating z on the connectivity set. Public-
  menu list prices come from the FCC Broadband Facts labels (the captured
  pre-migration labels pin the convention: Beyond 3-line $230, More 3-line
  $185, Essentials 1-line $65/2-line $100, 55+ and Military variants
  captured; December-2026 wave values govern). **W5 rule, defined by the
  captured W5 field, not by family: vectors whose captured field is
  taxes-included — ONE, Magenta, and Magenta Plus — must be dominated on W5
  by a (TI) variant on the cohort's menu.** Where no (TI) variant exists,
  there is **no posted upper bound** on the W5-matched replication cost
  (government taxes are unposted and unpriced): the TE price plus the
  captured carrier fee stack is recorded as a **flagged lower bound only**,
  never the point, and the cohort's headline routes to the Exclusion Register
  for the link with that context figure printed alongside. **Assigned-code
  price instrument (the union's collection reality, stated):** the 62
  crosswalk-assigned codes are not on the public plan pages the standing
  capture rows observe, and the July capture recorded that names/prices/SOC
  codes were "subject to change at any time" before July 13 — so their
  December-2026 prices have their own instrument: the hash-committed
  crosswalk price carried forward under the 5-year price guarantee, whose
  scope is talk/text/5G data only, taxes/fees excluded (captured) — a
  limitation flagged on every use — confirmed by the owner's post-migration
  check (open item 4 covers the assigned codes, not just the public labels).
- **Publication object**: the tier-spread interval **[0, gap]** with the point
  at the gap, superset-flagged (codebook §5 route 3) — the §3.1 W3-superset
  argument: every connectivity-dominating bundle buys unlimited premium data
  the frozen vectors never had, so the gap is an upper bound on the
  connectivity restoration line item *by construction*, and the release says
  so. **The point always sits at the min-cost connectivity-dominating
  bundle.** Two figures print alongside as labeled context, never as the
  point and never silently substituted: the carrier's stated maximum ("up to
  $6/line", `carrier-statement`, primary notice) as a named-fee-style cap,
  and the cohort's crosswalk per-plan delta as a labeled bill-impact figure
  (`carrier-adjacent-press`). Where the min-cost dominating bundle's gap
  exceeds the assigned target's delta, the discrepancy prints — it generally
  means the assigned target fails connectivity or W5 dominance, and that
  shortfall routes through §3.4's separate-line-item machinery; a
  non-dominating bundle never governs the point, because the point is defined
  by C(z; t) and nothing else.
- **ρ** per profile = C(z; Dec 2026) / C(z; Dec 2025); the **Gap** = ρ − π,
  where π is the CPI wireless stratum's Dec-2025→Dec-2026 12-month relative.
  Checked detail: this window does **not** span October 2025, so no
  `bridge=oct2025` flag applies to the flagship (any retrospective wireless
  ladder that spans it takes the flag per codebook §6).
- **No illustrative magnitude appears here, by design.** A stated
  expected-magnitude ceiling for the flagship result is exactly the kind of
  number whose first existence belongs to the Phase 2 band file (the G0/G1
  pattern); the December wave and the verified crosswalk produce the real
  numerator and denominator, and the band commits before either is computed.

### 3.4 Worked dominance trace (Magenta, illustrative)

Frozen Magenta vector vs the Experience menu, on the connectivity set:
W3 unlimited->50GB ≼ unlimited premium ✓; W4 GB field 3GB ≼ 60GB (More) ✓,
**fallback-class field not resolved** — Magenta's captured fallback is
unlimited-at-3G after 3GB, and Experience More's post-60GB fallback behavior
is not captured, so under W4's own two-field rule the check is GB-field-only
pending the December-wave label field [owner-verify] (handled exactly like the
W5 (TI) contingency next); W5 taxes-included → requires the More (TI) variant
✓ (public More is taxes-exclusive — where (TI) is unavailable to the cohort,
the §3.3 rule applies: flagged lower-bound context figure, Exclusion Register
for the headline); W7 **Netflix Basic (ad-free, 1 SD screen) vs Netflix
Standard with ads: NOT dominated** — ad-free playback is the codebook §2.1
worked ruling, and fewer-or-some-ads never restores it. Ruling applied: core
connectivity (the §3.3 set) is restored by Experience More (TI), subject to
the W4 fallback-class verification; the perk shortfall prices as a **separate
labeled line item** on Netflix's own posted menu — the ads-to-cheapest-ad-free
delta (~$11/mo on the ledger's verified 2026 Netflix menu: $8.99 ads vs
$19.99 cheapest ad-free), published as [0, delta] superset-flagged (the
ad-free tier also upgrades screens/resolution), with the actual
T-Mobile-to-Netflix upgrade path and price an owner-verification item
[owner-verify]. The two line items never sum into one headline number in this
module; the exclusive-partition rule keeps the perk item from double-counting
against the streaming module.

### 3.5 What prints when (plan P2 discipline: sector gaps allowed, no composite)

- **Q1 2027 (the Phase 1 release):** **no wireless Gap number.** The signed-off
  Phase 1 pre-registration fixes that release's scope (air exhibit + exact
  streaming link + controls). Wireless appears only where it already is:
  the Inclusion Ledger entry (already public on the site), the monitored-
  coverage figure, and — at most — a one-paragraph "captured, pre-registered to
  the 2026 link, publishes with Phase 2" notice. Publishing a wireless number
  before the module's own pre-registration and band exist would be exactly the
  band-after-result theater the gates forbid.
- **Phase 2 release (H2 2027, after the H1 2027 scheduled external review):**
  the wireless sector Gap for the 2026 link, computed from December-2026-wave
  menus, under the frozen dictionary, after the Phase 2 band file commits.
  Sector-level Gap series only; no composite before G3.
- **Freeze timing, dated (the codebook-§3 tension resolved, not waved at):**
  codebook §3 requires Phase 2 dictionaries to freeze **before their
  collection starts**. The 2026-link inputs are being collected now under
  Sprint-0 **preservation capture** — plan P3's exemption covers archival
  preservation, and phased publication is the plan's stated posture — but
  preservation capture is not a license for an undated freeze. The commitment,
  stated here and logged as open item 8: **the Phase 2 pre-registration
  (frozen dictionary v1, the §2 plan-identity rule, the §3.3 dominance-set,
  denominator, and W5 rules, the §4.4 missingness rules, Prompt D's frozen
  text, and the pre-committed band file) commits before the December-2026
  link wave runs**, so the link-entering observation of record is collected
  under a frozen design. If that date slips, the slip is a logged design
  failure with a methods note — never a quiet reinterpretation. Chronology
  and input corrections follow the logged-amendment pattern; the band, once
  committed, does not move.

## 4. Seller set and menu panel

### 4.1 Sellers (headline H)

**T-Mobile, AT&T, Verizon.** Brand-family rule per codebook §2.2: post-merger
billing-unified families are one seller — T-Mobile/Sprint is the codebook's
own worked example, and legacy-Sprint cohorts in the migration are same-seller
restorations, not cross-seller switches. Prepaid flanker brands (Metro by
T-Mobile, Cricket, Visible) are separately posted menus: they are **not**
same-seller restoration paths for a postpaid profile (different menu, different
service class), and they may enter the cross-seller sensitivity S **only via a
logged amendment admitting a genuinely unconditioned posted list price** —
one S definition, stated in §5; they never enter H in v1.

**Cable MVNOs (Xfinity Mobile, Spectrum Mobile): OUT of the headline seller
set; recorded as labeled context only.** Reason, stated: their headline prices
are conditioned on an active subscription to the seller's own broadband/cable
service [owner-verify current terms], which the codebook §2.3 cash-menu rule
bans from headlines exactly as it bans membership and card pricing — the
T-Mobile AutoPay lesson generalized. A price you can only get by buying a
second product is not the posted price of this product. They additionally
resell a host network's capacity (MVNO), so a "switch" to them is not a
like-for-like seller substitution for a facilities-based postpaid experience.
If a cable MVNO posts a genuinely unconditioned standalone list price, it may
enter S via the same logged-amendment route as the flankers; it never enters
H in v1.

### 4.2 Standing monthly capture and the Prompt D addition

`pipeline/targets.tsv` as it stands: `att-plans` and `verizon-plans` are
**standing** wireless rows; `tmobile-plans` is still marked **urgent** (a
pre-migration one-shot), and the section holds four more urgent/one-shot rows
(`tmobile-migration-support`, `tmobile-retired-one55` — a documented permanent
redirect, Wayback-negative — and the two tmo.report rows, both captured with
the crosswalk download pending). **Owner task, logged targets.tsv edit (open
item 9): after 2026-07-13, flip `tmobile-plans` to standing and
retire/annotate the four event rows — leaving three standing wireless rows**,
whose monthly `capture.py` hash-grade snapshot is the observation of record,
exactly the streaming pattern (static national pages; no fare-search
dynamics). What Phase 2 adds is **Prompt D**, a fourth wave prompt in the
`pipeline/wave-prompts.md` pattern. Described here; the frozen prompt text is
written into that file at the Phase 2 pre-registration — **so that the
wireless prompt freezes together with its own dictionary** (wave-prompts.md
itself is finalized at wave 0 and amendable until then; the deferral is this
module's freeze discipline, not that file's immutability):

- **Safety rails (the Prompt A/B/C carve-out, read-only variant):** read-only;
  no login, no cart, no personal detail, no line-of-service lookup; expanding
  an on-page "Broadband Facts and fees" panel is permitted (it is a display
  toggle, not a flow entry); if a page demands a ZIP, enter only the
  pre-registered ZIP (the grocery convention) and flag it.
- **Pages per wave:** each carrier's main consumer plan page + its 55+ and
  military/first-responder segment pages (the T-Mobile 55+/military label
  captures prove the segment menus carry their own FCC labels) — ~7–9 pages.
- **Fields per plan card (JSON, one fenced block, verbatim-never-computed):**
  plan name verbatim; **list price per the expanded FCC Broadband Facts label
  at 1–5 lines** (the label is the list-price instrument — the capture files
  demonstrate the card-vs-label split); card price + its stated conditioning
  (AutoPay/paperless, labeled, never headline); premium-data allowance and
  deprioritization threshold verbatim (W3); hotspot allowance **and fallback
  class** verbatim (W4); taxes-and-fees language verbatim (W5);
  price-guarantee/lock wording verbatim (W6); streaming/perk inclusions
  verbatim (W7); watch/tablet line price (W8); device connection charge;
  **itemized recurring fee lines where the label shows them** (they are part
  of the §1 unit of account); plan id where the label shows it (the Beyond
  55+ capture recovered a full plan id — the §2 identity key);
  promo/strikethrough detection + wording; loaded status; page title; URL.
- **Step-5 triage:** automated diff vs the prior wave on plan names, plan ids,
  label prices, W3–W8 fields, **and the labels' itemized carrier fee lines**
  (a surcharge move on an unchanged menu is a scalar move that enters ρ under
  §1's all-in unit of account — detected here, mirroring §4.3). Renames are
  adjudicated by the §2 plan-identity rule (vector + plan id), so a pure
  rename is a logged non-event, never a drafted event, and a rename hiding a
  vector or price change is diffed on the vector. Any substantive change
  drafts a ledger entry with T1/T2/T3 checks; decreases and re-bundlings flow
  through the identical diff (codebook §4 symmetry — a Verizon price cut or an
  AT&T re-bundling **must print negative**, and the module treats that as the
  apparatus working).

### 4.3 AT&T/Verizon legacy-repricing watch (standing ruling)

Plan §2.2 records the maneuver: AT&T's April 2026 legacy increases explicitly
paired price hikes with hotspot-data adds — the compensating-quality move that
hedonic adjustment rewards and this index correctly ignores. **Ruling
(binding, with its dependency stated):** a repricing of a grandfathered plan
that stays billed, with or without feature adds, is a **scalar move on the
household's own plan** — it enters ρ directly as ordinary replication-cost
change, it is *not* a ledger menu event unless the plan is removed or an
attribute is stripped, and **the added hotspot/feature never offsets the
hike**, because it is absent from the frozen baseline (extra hotspot is worth
exactly nothing to a household that didn't buy hotspot — the same
frozen-vector mechanism W7 cites). This ruling deliberately shares open
item 2's admissibility question: a grandfathered plan is not on M_t (codebook
§1), so pricing its repricing from the billed rate rests on the same
grandfathered-billed-rate ruling and goes to the same reviewer; if billed
rates are ruled inadmissible, the repricing enters via the menu-side minimum
instead (approximately a scalar-move print on the posted menu). Detection:
the monthly menu diff catches advertised-menu changes; grandfathered
repricings are announced by notice, not menu, so the module adds wireless
trade-press terms to the existing monthly press watch (§8 states the honest
cost), with any effective-dated notice triggering the standard 7-day urgent
capture. This is also the standing early-warning for T-Mobile's next legacy
repricing (2026-07-13 was the third in 26 months; the base-rate expectation is
that this module will have a non-empty event stream without any tuning).

### 4.4 Missingness and degradation (the Phase 1 §7 pattern, wireless-sized)

Codes: **MISS/BLOCKED, MISS/SITE-ERR, MISS/LABEL-GATED** (plan card visible
but the Broadband Facts panel will not expand — card price recorded, list
price missing, flagged), **MISS/SKIPPED.**

1. A missing monthly page flags and stays empty — no imputation, no
   interpolation; stale panels carry `stale=n` and never enter a link.
2. **December-wave miss ladder:** retry within Dec 1–15 → the owner manual
   Save-Page-As already scheduled as the December upgrade → nearest wave
   within ±45 days flagged `link-substitute` → the carrier's stated maximum
   as a named-style cap where the miss is inside the T-Mobile event's scope →
   **Exclusion Register for the link** with in-stratum weight reallocation.
   Never reservation-price imputation.
3. Assigned-code prices have their own instrument (§3.3); a failed owner
   post-migration confirmation is a flagged limitation on that instrument,
   never a substitute price.
4. Up to 2 whole non-December waves per year may be missed (flagged) with
   zero effect on the published link; December is mandatory.

## 5. Profiles and incidence

**Profiles are covered profiles, not a partition — stated because the
alternative would be false:** WLS-P1/P2/P3 leave 2-line non-55+, 4-line, and
5+-line accounts (plausibly the majority of postpaid accounts) in no profile.
The release publishes the **covered share** of postpaid accounts alongside the
profiles — [0%, 100%] until the owner's carrier/FCC pull yields a usable
line-count mix — and the Phase 2 pre-registration decides, **before the
dictionary freezes** (open item 11), between (a) a residual profile with
[0%, 100%] incidence and (b) a pre-registered line-count mapping convention
(each account priced at the nearest profile's per-line structure, disclosed as
a convention, never as representativeness). Incidence rules are codebook §8
and the register's rule 1: **usable-tagged figures or the published
[0%, 100%] interval — never a bare point, never an assumption share.**

| ID | Attribute vector | Incidence source / tag |
|---|---|---|
| WLS-P1-SINGLE | 1 voice line; unlimited talk/text; the cohort generation's W3–W7 vector; list price | Carrier-reported postpaid phone subscriber disclosures (10-K/10-Q; FCC Communications Marketplace Report as corroboration) — `administrative/usable` **once the owner pulls them on an unblocked connection**; until then **[0%, 100%]**. No subscriber counts are asserted in this document. |
| WLS-P2-FAM3 (flagship) | 3 voice lines, one account; unlimited talk/text; generation vector; list price. The 3-line anchor comes from the captured FCC-label convention (Beyond $230 / More $185, 3-line list); the captured crosswalk examples are 2-line (Experience Signature Family (B): $132 for 2 lines, $26 AAL) and 5-line (the ONE +$30 and KickBack $80 examples) and are recorded as **corroboration at other line counts**, not 3-line anchors. | Same source class; household line-count mix from carrier disclosures where published, else [0%, 100%]. |
| WLS-P3-55PLUS | 2 voice lines on an age-gated 55+ plan (the captured Essentials Choice 55 / 55+ Experience labels define the current-menu side; the unrecoverable ONE 55+ page makes this the `vector=predecessor-generation` cohort, disclosed) | **No seller-specific public take-rate found — [0%, 100%] per the register's rule 1**, stated in the release; a usable figure upgrades it via a logged amendment. |
| Within-event generation mix | Share of the 8M+ migrated customers per legacy generation (Simple Choice / ONE / Magenta / Sprint) | Not publicly disclosed → per-generation [0%, 100%], with one honest constraint published alongside: the carrier's stated **maximum** ("up to $6/line" — `carrier-statement`, primary notice, captured) and its stated **floor** ("Some customers will see no change" — same source, i.e. ≥$0/line) bracket per-line impacts; the **+$4 average is trade-press** (tmo.report; also plan §2.2, web-verified without carrier attribution) — `carrier-adjacent-press/usable-with-caveat`, [owner-verify any primary T-Mobile statement of it — open item 5] — and only with that average does the bracket bind the generation mix arithmetically. The headline count: **8M+ customers** — `carrier-adjacent-press/usable-with-caveat` (tmo.report, corroborated by the primary notice's existence and scope); the ledger entry's "lines" wording is a discrepancy queued for a logged correction (open item 10), and the customers/lines/households unit question is in the open-item-5 byte-verification set. |

**W8 disclosure (component honesty):** no v1 profile carries a wearable or
tablet line, so the trade-press +$3/line watch/tablet component of the
seller's own event description is **dictionary-monitored but unpriced in
v1** — recorded in the event narrative with its magnitude, disclosed rather
than silently orphaned. A wearable-carrying profile variant (incidence
[0%, 100%]) is a v1.1 candidate, decided at the pre-registration.

**Sensitivity S (cross-seller), one definition:** the cheapest
connectivity-set weakly dominating list-priced plan across the three headline
sellers **plus any flanker or MVNO admitted by the §4.1 logged-amendment
unconditioned-list-price test**, same profile — published beside H as the
brand-switching coping margin, exactly the Phase 1 H − S construction. **W5
inside S, stated:** AT&T and Verizon post taxes-exclusive, so a
taxes-included frozen vector (ONE/Magenta family) is never W5-dominated
cross-carrier, and the captured fee-stack evidence is T-Mobile-only. S for
those cohorts is therefore computed and labeled **"connectivity-only,
W5-unmatched, taxes-exclusive basis," flagged** — each carrier priced on its
own posting convention, never presented as comparable to a taxes-included
figure. If the reviewer judges the flag too weak, S prints empty for those
cohorts — a fact about the market's posting conventions, not a failure.

## 6. Comparator: CPI wireless telephone services — stated honestly

The Gap differences ρ against the official CPI wireless stratum 12-month
relative. What every wireless release states about that comparator:

- The stratum has a long history of steep measured price decline driven in
  substantial part by quality/hedonic adjustment for expanding data capacity —
  including the well-known 2017 episode in which unlimited-data plan
  introductions produced a sharp measured drop [owner-verify the episode's
  dates, magnitude, and BLS's stated mechanism before any release uses it; the
  sandbox cannot reach bls.gov]. Since July 2025 the stratum is built from
  vendor-scraped near-universe advertised menus under full-menu hedonic
  regressions (plan §2.2, web-verified).
- **Coverage:** the stratum includes prepaid, which v1 does not price; every
  wireless release carries the §1 postpaid-coverage figure or the
  partial-coverage caveat.
- **Why the Gap is still well-defined:** the Gap is a spread, not a
  correction. π is CPI's published answer to constant-quality offer inflation;
  ρ is the replication cost of a frozen experience; the spread *quantifies the
  wedge between two differently-defined measurands* and claims nothing about
  either being "true inflation" (the project makes no such claim anywhere).
  A large positive wireless Gap in 2026 would mean exactly what the module
  says it means: keeping last year's bill cost more than the advertised-offer
  concept registered — a statement BLS itself would not dispute, because
  grandfathered rates are outside the advertised-offer measurand by design.
- Upper-bound language rides on every number (superset-flagged intervals,
  [0, gap] semantics); negative prints (a carrier re-bundling, a price cut on
  a dominating plan) publish with the same machinery.
- Comparator continuity: the flagship 2026-link window avoids October 2025
  (checked in §3.3); any wireless series window spanning it takes the codebook
  §6 bridge convention and flag.

## 7. Internet/broadband sidecar (sketch only — not a design)

The sidecar exists in this document to record status and blockers, not to
freeze anything:

- **Capture status:** the three broadband-label landing URLs in `targets.tsv`
  are marked `needs-url` — verified 404/redirect on 2026-07-04. The structural
  finding (captured): **FCC Broadband Facts labels surface per-plan inside
  shopping/checkout flows, not at label landing pages.** Wireless dodged this
  because carrier plan pages embed the label panels; wired broadband does not.
- **What the module needs before it can freeze:** (i) corrected per-plan label
  capture paths — owner-machine, in-flow navigation to each plan's label at a
  fixed service address (blocked hosts make this owner work by construction);
  (ii) a pre-registered service-address/ZIP convention, because wired
  broadband menus are address-specific — the labeled-convention pattern the
  grocery control already uses, honestly disclosed as a convention rather than
  a representativeness claim; (iii) a seller-set formula committed before the
  panel (top ISPs by subscribers from a hash-committed public input — the FDIC
  top-5 pattern from the banking control); (iv) an attribute dictionary
  (speed tier, data cap, equipment fee line items, taxes/fees treatment,
  promo-to-standard step) drafted with the same W-numbering discipline;
  (v) resolution of the FCC label rollback FNPRM (final rule expected 2H 2026,
  plan P3) — if machine-readability dies, capture pivots to in-flow full-page
  saves and the pivot is a logged collection break, not a silent splice.
- Until (i)–(iii) exist there is nothing to pre-register; broadband stays
  capture-only (Sprint-0 posture: collection is not waiting for publication).

## 8. Hours (honest), freeze mechanics, open items

**Standing monthly (marginal over the Phase 1 runbook):** wireless target
snapshots ride inside the existing Step 1 (2 standing pages today, 3 after the
§4.2 disposition — minutes); **Prompt D agent pass ~7–9 pages at the measured
Phase 1 agent-cell basis (8 min/cell — label-expanding, many-field plan pages
are cell-like, not grocery-like) ≈ 1–1.2 h**, an estimate until measured:
Prompt D's first run is timed wave-0-style and the committed reading governs;
Step-5 wireless diff ~10 min. **Press watch: the wireless terms ride the
existing fixed 60-minute budget, which buys reduced per-sector depth, stated
plainly — not a free widening**; if the December review finds the watch
missing effective-dated notices, the budget is raised and the raise is
logged, never hoped down. **Marginal ≈ 1.3–1.5 h/month. Combined with
Phase 1's honestly-stated ~9.7 h/month, the monthly total crosses into double
digits: ≈ 11 h/month** — the components sum there and the total is stated
rather than hoped down. (Phase 1's de-scope machinery governs the air panel
only; this module's own de-scope lever, if ever needed, is dropping Prompt D's
segment pages — logged, never silent.) The module is still cheap for what it
buys: the menus are national, posted, and static — no routes, no grids, no
dynamic pricing.

**December-wave extras:** owner manual Save-Page-As of the three carriers'
plan pages + expanded label panels, registered via `capture.py --manual`
(archival grade for the link-entering menus — the Phase 1 December-upgrade
pattern), ~30–45 min.

**One-time owner tasks (unblocked connection), estimated honestly:** crosswalk
.xlsx/.pdf download + hash-commit **+ authenticity verification** (document
metadata; cross-checks against the captured migration and 2024/2025 repricing
notices; the "seller-published" upgrade happens only if authenticity
verifies) (~1 h; **do this first — it is the event's price mapping and it
lives on a blog, not an archive**); legacy denominator reconstruction for the
three profile cohorts against the crosswalk old-price column (existence
[owner-verify]) and the 2024/2025 repricing notices (~3–4 h); subscriber-mix
**and postpaid-share-of-stratum** pull from carrier filings + FCC report
(~1–2 h); CPI stratum name + quality-adjustment-history byte-verification on
bls.gov (~1 h); MVNO conditioning-terms verification (~30 min); the
targets.tsv disposition edit (§4.2, minutes). **Total ≈ 7–9 h one-time.**

**What freezes when:** this document is DRAFT and stays amendable. The
dictionary (§2, including the plan-identity/rename rule), the M_t union
ruling, the dominance-set definition, the denominator instrument and its
fallback ladder, the W5 rule, and the assigned-code instrument (§3), the
missingness rules (§4.4), the seller set and MVNO/flanker rulings (§4), and
the profiles and coverage conventions (§5) **freeze with the Phase 2
pre-registration, which commits before the December-2026 link wave** (§3.5;
open item 8 logs the codebook-§3 tension and its resolution); the band file
commits first (band → pre-registration → pinned inputs → results); the
numeric pass limits for the wireless module appear in that band file and
**nowhere else, including nowhere in this document** — first-existence
discipline, the G0/G1 pattern copied exactly. No wireless-link computation
runs before the band's commit and the owner sign-off. Single-operator
disclosure, unchanged from Phase 1: every capture, the crosswalk pull, and
the December wave run through one person; the standing targets.tsv snapshots
are the only redundancy.

**Open items:**

1. The M_t union ruling (public menu ∪ crosswalk-assigned target codes) goes
   to the Phase 2 reviewer — defensible but novel relative to codebook §1's
   menu definition. **Pre-registered rejection fallback:** M_t = public menu
   only; the gap computes against the public (TI)/(TE) tiers, and the release
   flags that the cohort's actually-assigned codes were excluded by ruling.
2. Admissibility of a grandfathered billed rate as C(z; t−1) — same reviewer;
   the crosswalk's old-price column (if it exists — item 3) is the evidence
   that makes it answerable. **Pre-registered rejection fallback:** ρ
   collapses to posted-menu-vs-posted-menu (approximately a scalar-move
   print), and the migration's bill impact routes to the **Exclusion Register
   with magnitude — counted, not priced** (the ACP/KickBack pattern). Stakes
   stated plainly: this denominator choice is what makes the flagship gap
   non-zero, which is exactly why its fallback is written down before any
   computation. §4.3's repricing ruling shares this question.
3. Crosswalk download + hash-commit + authenticity verification (owner;
   time-insensitive but do it soon — third-party blog hosting is not an
   archive). The old-price column's existence is [owner-verify at download];
   §3.3's fallback ladder (captured-line-count restatement → Exclusion
   Register) governs if it is absent or incomplete.
4. Post-migration confirmation capture, **extended to the assigned codes**: a
   December-2026-wave check that the public Experience list labels match the
   captured May-2026 labels (or the diffs are logged — the July capture noted
   prices "subject to change at any time" before July 13), plus an owner
   check that assigned-code prices match the hash-committed crosswalk under
   the guarantee's stated scope (§3.3's instrument).
5. Byte-verification set: CPI stratum name + hedonic history; the 2017
   episode; AutoPay differentials by era; the "TI" reading; MVNO terms;
   Beyond hotspot unlimited-vs-250GB; Experience More's post-60GB fallback
   class (W4, §3.4); Simple Choice-era hotspot inclusion (W4, §3.2); the
   Netflix perk upgrade path; any primary T-Mobile statement pinning the 8M+
   count **and its unit (customers vs lines vs households)** or the +$4
   average; the postpaid share of the CPI stratum (§1).
6. Whether the 55+ cohort's predecessor-vector treatment (ONE 55+
   unrecoverable) survives review or forces that cohort to the Exclusion
   Register.
7. The wireless module's Improvements-Register posture (rx-100 proposal §5):
   perk additions and premium-data expansions are the obvious first entries if
   that instrument is adopted — noted for the RX-100 review, decided there,
   not here.
8. **Codebook-§3 freeze-timing tension, logged:** standing wireless capture
   (Sprint-0 preservation, plan P3 exemption) predates this dictionary, while
   codebook §3 requires the dictionary to freeze before collection starts.
   Resolution: the dated commitment in §3.5 — pre-registration before the
   December-2026 link wave; a slip is a logged design failure with a methods
   note.
9. targets.tsv disposition (owner, logged edit): flip `tmobile-plans` to
   standing post-2026-07-13; retire/annotate `tmobile-retired-one55`
   (permanent redirect, Wayback-negative, documented) and the two captured
   tmo.report one-shots (crosswalk download pending) → three standing
   wireless rows.
10. Ledger correction (logged, chronology/inputs rule): `wireless-
    tmobile-202607` says "8M+ lines"; the captured source says "8M+
    customers." Correct the ledger to the captured unit with the discrepancy
    noted.
11. Profile coverage decision before the dictionary freezes: residual profile
    vs pre-registered line-count mapping convention (§5).

## Changelog

- 2026-07-11 — v0 revised against the two-reviewer adversarial pass (36
  findings across the two lists; all applied, none rejected — overlapping
  findings merged). Load-bearing corrections: dominance formalized as the
  connectivity set W1–W6+W8 with W7 priced separate-line-item-only (a W1–W8
  min was empty for the Magenta cohorts) and the §3.1 superset claim restated
  as the W3 premium-data superset; the publication point never moves to a
  non-dominating assigned target (crosswalk delta = labeled context, carrier
  "up to $6/line" = the only carrier-stated cap); denominator instrument
  inverted — crosswalk old-price column primary (existence [owner-verify],
  fallback ladder pre-registered), Wayback prices demoted to corroboration at
  their captured conditionings (4-line AutoPay + 3rd-line-free promo — an
  AutoPay-only bridge cannot un-promo them); W5 fee-stack claim reversed to a
  flagged floor (govt taxes unposted) with Exclusion-Register routing where no
  (TI) variant exists; TE all-in unit of account defined incl. carrier
  surcharge lines + Step-5 fee-line diff (the guarantee-carve-out safe
  harbor); plan-identity/rename non-event rule added; assigned-code price
  instrument stated and a §4.4 missingness section added (Phase 1 §7
  pattern); provenance repaired (+$6 max and "no change for some" = carrier
  primary notice; +$6/+$3/+$6, +$4 avg, and 8M+ = tmo.report,
  carrier-adjacent-press [owner-verify]; crosswalk = tmo.report-published
  internal mapping pending authenticity verification); the wrong illustrative
  bound deleted (its arithmetic was 12.9%, not single-digit, on a mislabeled
  promo base — and pre-band magnitude language is banned by first-existence
  discipline regardless); prepaid coverage disclosure added (§1, §6);
  profiles restated as covered-profiles with a published covered share and a
  pre-freeze decision item; S given one definition with the W5 cross-carrier
  comparability rule; open items 1–2 given pre-registered rejection
  fallbacks; hours restated at the measured 8 min/cell basis (marginal
  ≈1.3–1.5 h; combined ≈11 h/month stated, press-watch "+0" replaced with the
  fixed-budget/reduced-depth statement); the freeze dated before the
  December-2026 wave with the codebook-§3 tension logged (open item 8);
  targets.tsv described as it actually is with the disposition queued (open
  item 9); the headline unit standardized to the captured "8M+ customers"
  with a ledger correction queued (open item 10); W6 guarantee wording quoted
  as captured; the W8 +$3 component disclosed as monitored-but-unpriced; W7's
  never-offset mechanism recited from frozen-vector dominance (spec P2 kept
  for the new-plan case); Simple Choice W4 recorded as not-captured
  [owner-verify] instead of "n/a-era"; the §3.4 W4 trace annotated for the
  uncaptured fallback-class field; the wave-prompts deferral reason corrected
  (freeze-with-own-dictionary, not immutability).
- 2026-07-11 — v0 initial draft (workstream D). Dictionary v1 (W1–W9) built
  on the two 2026-07-04 T-Mobile capture files; flagship 2026-link computation
  design with the tier-spread [0, gap] semantics and the list-vs-AutoPay
  consistency rule the captures encode; seller set with the brand-family rule
  and the cable-MVNO OUT ruling; Prompt D described; AT&T/Verizon
  legacy-repricing watch ruling (scalar move; compensating adds never
  offset); profiles WLS-P1/P2/P3 with register-rule incidence; comparator
  honesty section; broadband sidecar status. No numeric pass limits anywhere
  in this document, by design.
