# Restoration Index — Specification

`v00.02.00 · 2026-07-04 21-51 · internal working doc · status: decisions adopted; codebook v0 and engine v0 implement this spec`

---

## 0. Verdict: does the frame hold?

**Yes, with three structural amendments and one demotion.** The core is sound and — after an aggressive prior-art sweep — genuinely unoccupied: no statistical agency, academic group, or think tank publishes a constant-experience replication-cost index. But the frame as scoped would have been killed on page one by any competent referee, on four specific points. All four are fixable, and the fixes make the measure stronger, not weaker:

1. **The primitive is right but needs its real name.** "Restoration index" is the correct *measurement protocol*; the correct *formal object* is a **conditional replication-cost index in characteristics space** — the cost function of a Leontief-in-characteristics consumer (Lancaster 1966) anchored at the base-period experience vector, minimized over today's product menu, which makes it a Pollak-style conditional index and a Konüs **upper bound** on the constant-experience cost of living. This is not pedantry: the name buys a known axiomatics, a bound theorem instead of a discovered flaw, and an ancestry (BLS's own R-CPI-SC is this design, for package sizes). All three adversarial reviews converged on this independently.
2. **The event trigger must be split** (fatal-unless-fixed, per all three reviewers). The index fires upward **iff the minimum cost of replicating the base experience rises**. If Basic Economy launches at $260 beside standard Economy unchanged at $300, the profile that needs the carry-on prints **exactly 0%** — menu expansion is not inflation, and an index that prints positive on it measures resentment, not prices. (Refined in v00.02.00: where a new option *weakly dominates* a profile's frozen experience at a lower price, replication cost genuinely falls and the index prints negative for that profile — menu expansion can never raise the index, and sometimes lowers it.) This monotonicity is the design's single strongest defense: it is what separates it from a junk-fee counter.
3. **The operator must be symmetric** (fatal-unless-fixed). Re-bundling, fee elimination, and tier merges must print **negative** restoration relatives on equal footing, and the published sector set must include demonstrated negative/zero cases (banking overdraft revenue fell >50% since 2019; groceries ≈ 0 by construction). An index that can only go up is unfalsifiable advocacy.
4. **Shrinkflation is demoted from motivation to validation.** CPI captures packaged-goods downsizing *contemporaneously* via per-unit price standardization (a 64→60 oz shrink at constant price records as +6.7%/oz the same month), and BLS publishes R-CPI-SC quantifying the residual at ~0.01pp/yr on all-items (GAO: ~0.06pp of the 34.5% rise 2019–24). Mechanism (c) stays in scope but becomes the **null-test channel**: the Restoration Gap on pure downsizing should be ≈ 0 against CPI, and R-CPI-SC is the external benchmark proving the method isn't a ratchet.

One more correction to the animating example before it goes anywhere public: **"CPI misses bag fees" is false and BLS can rebut it in one line.** The CPI airline-fares quote specification *includes* taxes, fuel surcharges, airport/security fees, and the **first checked bag** (80% of quotes are designated to include one). What CPI verifiably does not track — factsheet language — is *"the price of carry-on bags and any additional checked luggage."* The United carry-on strip is therefore the right flagship: it is structurally invisible, not merely lagged. And the strongest single piece of supporting evidence is internal to BLS: the **PPI** made an explicit unbundling correction in March 2009, without which the air-travel PPI *"would have been 1.6 percent lower in December 2009"* — a statistical agency's own admission that matched-fare pricing misses fee unbundling.

The rest of this document is the rebuilt spec: formal statement (§2), event grammar and scope (§3), worked examples with verified numbers (§4), the CPI seams restated precisely (§5), all decisions as a table (§6), prior art (§7), data feasibility (§8), hazards (§9), phased build (§10), credibility defenses (§11), limitations (§12), and open items with deadlines (§13).

---

## 1. Definition and unit of account

**Object.** The **Restoration Index (RX)** for a covered sector measures the change in the minimum cost of *replicating, on today's menu, the consumption experience actually purchased in the base period* — where "experience" includes every discretely contractible attribute that was included in the base-period purchase (carry-on allowance, checked bags, ad-free playback, seat selection, net quantity, mandatory-fee-free occupancy), documented in an evidence-backed **Inclusion Ledger**.

**Headline product.** Publicly branded **"The Restoration Gap"** (restorationgap.org; plan decision P13) — formally, the **Restoration Gap (G)**: the 12-month restoration inflation rate of covered sectors **minus** the corresponding official CPI item-stratum inflation rate, in percentage points, published per sector and as a covered-sector composite with a mandatory two-way decomposition (pricing-concept effect vs weighting effect). The Gap — not a rival all-items level index — is the product.

**Unit of account.** Dollars per base-period *experience profile* (e.g., "domestic round trip, one full-size carry-on, no checked bag"). Elementary relatives are dimensionless ratios of replication costs; the Gap is in percentage points on 12-month changes.

**Population.** Households in the bottom two equivalized-income quintiles (BLS R-CPI-I definition: before-tax imputed income ÷ √household size), with expenditure weights built per §6-D5.

**What it is not.** Not a cost-of-living index (it is an upper bound on a conditional one); not a claim that headline CPI is wrong (it targets a different concept: reproduction cost, not compensated cost); not an all-items index (covered sectors only, coverage share published every release).

---

## 2. Formal statement

### 2.1 Setup

- Let $\mathcal{A}$ be a finite set of **contractible attributes**: discrete features that appear as named line items or tier deltas on a seller's price menu. Attributes are defined *ex ante* in the Inclusion Ledger with an equivalence protocol (e.g., *carry-on* = "full-size bag travels in cabin, no gate surrender" — a gate-checked bag is **not** equivalent).
- The **menu** at time $t$: $M_t = \{(j, p_{jt}, a_j)\}$ — purchasable products/fees $j$ with posted price $p_{jt}$ and attribute vector $a_j \in \mathbb{R}_+^{K}$.
- The **base experience** for elementary profile $e$: $z_e^{t-1} = $ the attribute vector of the configuration actually purchased at $t-1$ (modal configuration per profile), documented in the Ledger.

### 2.2 The primitive: replication cost

$$
C(z;\, t) \;=\; \min_{q \ge 0} \Big\{ \textstyle\sum_{j \in M_t} p_{jt}\, q_j \;:\; \sum_j a_j q_j \succeq z, \;\; \text{seller}(j) = \text{seller}(e) \Big\}
$$

— the cheapest bundle on today's **same-seller** menu that weakly dominates the frozen experience attribute-by-attribute. No attribute substitution (Leontief in characteristics); free *procurement* substitution (re-bundling, à-la-carte reassembly). The optimal basis of this program yields the per-inclusion **restoration line items**. A cross-seller variant $C^S$ (min over all sellers in the market) is published as a sensitivity; the headline is same-seller ($H$), because cross-seller restoration re-imports exactly the substitution-as-costless logic the index exists to reject, and the $H{-}S$ spread itself measures how much coping relies on brand switching.

**Elementary link relative:** $\rho_t(e) = \dfrac{C(z_e^{t-1};\, t)}{C(z_e^{t-1};\, t-1)}$, where the denominator normally equals the observed $t-1$ transaction price.

**Sector index (annually chained, Young-type arithmetic over profiles):**
$$
RX_t \;=\; RX_{t-1} \cdot \sum_e s_e^{t-1}\, \rho_t(e)
$$
with $s_e^{t-1}$ = base-period expenditure shares of experience profiles, *including utilization incidence* (§9.1).

**Restoration Gap (per covered item stratum $i$, then aggregated):**
$$
G_t \;=\; \underbrace{\sum_{i} w_i^{\text{CPI-U}} \big[\rho_t(i) - \pi_t^{\text{CPI}}(i)\big]}_{\text{pricing-concept effect}} \;+\; \underbrace{\sum_{i} \big(w_i^{B40} - w_i^{\text{CPI-U}}\big)\, \rho_t(i) \;+\; \dots}_{\text{weighting effect}}
$$
where $\pi_t^{\text{CPI}}(i)$ is the official item-stratum relative. Covered items form an **exclusive partition**: an item priced by restoration is removed from the ordinary pool for that period (public concordance), which mechanically prevents double-counting fee changes that CPI also captures.

### 2.3 Side-by-side with the incumbents

| Index | Formula | Price argument | Quantity/share argument |
|---|---|---|---|
| CPI-U (headline) | Lowe: $\dfrac{\sum p_t\, q_b}{\sum p_0\, q_b}$ | matched-specification posted quote | expenditure basket lagged ~24 months (annual updates since Jan 2023) |
| C-CPI-U | Törnqvist: $\ln P = \sum_i \tfrac{1}{2}(s_i^0 + s_i^t) \ln\dfrac{p_{it}}{p_{i0}}$ | matched-specification posted quote | contemporaneous shares (final ~12 months later) |
| **RX** | chained Young: $\prod_t \sum_e s_e^{t-1} \rho_t(e)$ | **replication cost $C(z^{t-1}; t)$ of the frozen experience** | **shares frozen at $t-1$, never contemporaneous** |

Note CPI-U is a **Lowe** index, not strictly Laspeyres (weights predate the price-reference period by ~24 months on average) — the weight lag is itself part of why new fee categories enter the basket slowly.

**The three divergence points.** (i) The price argument: RX prices the *frozen experience*, the others price a *specification that follows the menu* (when the spec is "lowest available fare," the menu redesign flows straight into the price). (ii) New varieties: CPI links them in — the level difference between old and new items is never differenced into the index; RX admits them only as *replication routes*. (iii) Substitution: C-CPI-U's share-updating treats migration to Basic as (compensated) substitution; RX forbids experience substitution by construction.

### 2.4 Properties (the defense battery)

- **P1 — No-event neutrality.** Menu unchanged except scalar price moves ⇒ RX coincides with a matched-model index.
- **P2 — Menu-expansion monotonicity** *(refined in v00.02.00; surfaced by the engine implementation)*. Adding a product without changing existing ones can never **raise** RX. Profiles the new option does not dominate are unchanged: *Basic launches at $260 beside unchanged $300 Economy ⇒ the carry-on profile prints 0% — while a lowest-available-fare CPI quote prints −13.3% for every traveler, including those who got nothing.* Profiles the new option **weakly dominates** at lower cost print a genuine replication-cost **decrease** (consistent with P3): in that exhibit the personal-item profile prints −13.3% and the S3-share-weighted sector ≈ −4.0%. RX cannot be pushed up by menu expansion; it can be pulled down by it.
- **P3 — Symmetry.** $C$ is a min over the full current menu: re-bundling, fee elimination, or a cheaper restoring tier lowers $C$ and prints negative. (Proof case: overdraft/NSF fees, §4.4.)
- **P4 — Bound (theorem, with stated conditions).** If the base bundle was cost-minimal for $z^{t-1}$ on $M_{t-1}$, then for any preferences $V$ over characteristics with $V(z^{t-1}) = u$: $\;C_V(u;\,t) \le C(z^{t-1};\,t)$, hence $\rho_t \ge$ the conditional Konüs relative at base experience. **RX is an upper bound on the constant-experience COLI — by design, stated in every release.**
- **P5 — The bracket is an assumption, not a theorem.** $[\text{C-CPI-U},\, RX]$ brackets constant-experience cost growth only under **Assumption Q**: no unmeasured quality *improvements* in covered items over the link year. State Q explicitly; with material unmeasured improvements the bracket can invert. (One-year links make Q plausible; a 37-year window — the Cost-of-Thriving mistake — would not.)
- **P6 — Superset conservatism.** When the cheapest replicating bundle strictly dominates $z$ (the Economy fare also buys seat selection), $C$ *understates* the pure attribute cost; the bias runs against the thesis. Superset-only events are flagged and published as an interval (§3.4).

### 2.5 Chaining discipline

Annual links only; headline = 12-month relative (each link answers the well-posed question *"what does last year's experience cost today?"*). The cumulated chain is published solely as a caveated memo item — a long-horizon no-substitution level index would relitigate Boskin and lose. Base experiences re-freeze annually **via the Ledger**, so incidental superset extras do *not* roll into next year's base (kills the ratchet), and permanently degraded defaults do not silently become the entitlement mid-cycle. No monthly chaining with the min operator (a one-month fee promotion is always selected by the min — textbook chain-drift bait; cf. Szulc 1983; Ivancic–Diewert–Fox 2011; BLS's own C-CPI-U drift study, Cage et al., MLR 2021). Drift diagnostic: chained-vs-direct comparison published annually.

---

## 3. Event grammar and scope

### 3.1 The trigger (the load-bearing rule)

A **restoration event** exists at $t$ for profile $e$ iff:

1. an attribute present in the modal purchased configuration at $t-1$ (per the Inclusion Ledger, with documentary evidence: archived fare rules, plan pages, terms) is **absent from the same-priced configuration** at $t$, **and**
2. a priced path to that attribute exists on $M_t$ (named fee, à-la-carte item, or tier delta), **and**
3. $C(z_e^{t-1};\,t) > C(z_e^{t-1};\,t-1)$ in real terms attributable to the menu change — i.e., replication cost actually rose.

**Non-events (no upward print, by rule):** downward tier introduction with the incumbent's own price and inclusions unchanged (where the new tier weakly dominates a profile's experience at lower cost, the decrease flows through the negative-event rule below — P2 refinement); fee-label reshuffles that leave the all-in replication cost unchanged; pure price moves on an unchanged menu (those flow through P1 as ordinary price change, not as an "event").

**Negative events (must print):** re-bundling; fee elimination; a cheaper restoring tier or à-la-carte path appearing.

### 3.2 The priced-restoration test (scope boundary, formalized)

Attribute $a$ is **in scope** at $t$ iff on $M_t$ either (i) a named fee or line item prices $a$ directly, or (ii) two configurations differing only in $a$ (within the Ledger's equivalence tolerance) identify its tier spread. Otherwise **out of scope** — logged in the public **Exclusion Register** with a count and the affected base expenditure, *never* imputed. No hedonics, ever: the moment the index imputes an unpriced quality delta it re-enters the swamp it was built to avoid. The Exclusion Register is also the leak detector: it makes migration across the scope boundary (firms deleting the fee *and* the feature) observable rather than invisible.

Formally, the test is the **non-emptiness condition** of the replication program: in-scope ⟺ the constraint set of $C(z;t)$ is non-empty. If some coordinate of $z^{t-1}$ is unrestorable at any price, the item exits the restoration ledger, its weight is reallocated within the stratum CPI-style, and the exit is logged. The index prices reproducible experiences only — that concession goes in the abstract, not a footnote.

### 3.3 Scope taxonomy

| Status | Cases | Rule |
|---|---|---|
| **Captured** | checked-bag and carry-on fees; resort/destination fees; seat-selection fees; ad-free tier spreads; paid restoration of formerly-included delivery; password-sharing "extra member" fees; per-unit shrinkflation deltas; forced migration to a pricier superset plan when the old plan leaves the menu (flagged superset) | direct line item or tier spread on today's menu |
| **Partially captured** | bundled-only restoration (tier upgrade buys extras → interval, §3.4); membership/credit-card-conditioned inclusions (price the unconditioned cash menu; note the conditioning); dynamic/personalized pricing (use the posted standard price at a fixed booking point) | flagged, bounded, or convention-fixed |
| **Out of scope** | skimpflation proper: worse ingredients, slower service, thinner staffing, longer holds, more ads *within* an unchanged tier when no priced alternative exists; reliability and queue degradation | Exclusion Register (counts + affected expenditure), no imputation |

The honesty of the boundary is the credibility asset: even BLS cannot value silent service degradation (no hedonic models exist for airlines, hotels, or restaurants — verified against BLS's quality-adjustment listings), and this spec does not claim a magic key BLS lacks.

### 3.4 Route hierarchy and the superset rule

Replication routes are ranked **lexicographically**, not just by the min:

1. **Named fee** for the stripped attribute (bag fee, resort fee, extra-member fee) — the cleanest identification;
2. **À-la-carte reassembly** across the same seller's menu;
3. **Tier upgrade** — only route left when the attribute is bundled: published as a **flagged interval** $[0, \text{tier gap}]$ with the point estimate at the gap, explicitly labeled an upper bound on the attribute's price.

Where both a named fee and a tier route exist, the named fee **caps** the line item. Both series (min-cost and standalone-fee) are published so the superset bias is bounded and visible.

---

## 4. Worked examples (verified numbers)

All dollar figures below were web-verified against primary or multiple independent sources in July 2026; verification statuses are in Appendix A. Profile shares marked *assumption* are illustrative pending incidence data (§9.1).

### 4.1 United carry-on (the flagship: structurally CPI-invisible)

**Setup.** United domestic Basic Economy admits only a personal item (17×10×9 in) — no full-size carry-on; bringing one to the gate costs **$75** ($50 airport first-bag fee + $25 gate-handling charge; $65 before the April 3, 2026 fee increase). Prepaid first checked bag: **$45**. Basic-vs-Main spreads (NerdWallet May 2026 survey, 5 domestic routes/airline): **$85–99 round trip** for most majors ($129 Alaska); the 2024 survey of dozens of routes found $49–80. Delta and American Basic both *include* a full-size carry-on — United is the only Big-3 carrier that strips it. The original "~$50 each way" framing survives as the bag-fee/upper-fare-delta path, but the honest statement is **restoration = min over routes, $43–50 each way on current data**.

**Ledger entry.** Attribute: *full-size bag travels in cabin, no gate surrender*. The $75 gate charge prices a **different** attribute (bag checked at gate) and is excluded by the equivalence protocol; the only replicating route is the fare-class upgrade — a **flagged superset** (Economy also buys seat selection and larger change flexibility).

**Numbers.** Base year: standard Economy round trip **$300**, carry-on included. Three event-year scenarios, three indexes:

| Scenario (event year menu) | CPI reading | C-CPI-U reading | RX reading |
|---|---|---|---|
| **S1 — price-point takeover**: Basic $300 (no carry-on), Economy $385 | lowest-available-fare quotes (≈ half the discount sample): $300→$300 = **0.0%**; fare-class-locked quotes: $300→$385 = **+28.3%**; carry-on delta itself: **$0 by construction** ("not tracked") | between the two, shaded down as shares migrate to Basic | $C$: cheapest bundle ⪰ base experience = Economy $385 (Basic + $90 RT bag fees = $390 buys the *wrong* attribute and costs more anyway) ⇒ **+28.3%**, superset-flagged interval [0, +28.3%] on the attribute, point +28.3% on the profile |
| **S2 — undercut launch**: Basic $260, Economy unchanged $300 | lowest-available-fare quotes: $300→$260 = **−13.3%** (a price cut no constant-experience traveler received) | negative, share-weighted | carry-on profile: **0.0%** (Economy unchanged); personal-item profile: **−13.3%** (Basic weakly dominates their experience — a genuine decrease); S3-share weighted: **≈ −4.0%** — RX reads menu expansion as deflation only where it truly is |
| **S3 — profile aggregation of S1** (*assumption:* 55% of base travelers carried on [profile P1], 30% personal-item-only [P0], 15% +1 checked bag [P2]) | as S1 | as S1 | P1: +28.3% · P0: **0.0%** (Basic replicates their experience) · P2: +28.4% ⇒ profile-weighted **+19.9%** |

S3 is incidence weighting in action: the traveler who never carried a bag has an unchanged replication cost, and the index says so. S2 is the design's proudest moment: where a naive fee-tracker misfires upward and CPI's lowest-fare spec hands −13.3% to every traveler indiscriminately, RX prints zero for the profile that lost nothing and gained nothing, and a genuine decrease only for the profile the new option actually serves.

### 4.2 Southwest checked bags (the clean line item — and the honesty exhibit)

The sector's largest unbundling event in decades: announced March 11, 2025; for tickets booked/ticketed or changed on/after **May 28, 2025**, first bag **$35**, second **$45** (ending a ~54-year policy); raised to **$45/$55** on April 9, 2026 amid the jet-fuel spike. Carve-outs: Choice Extra fares and A-List Preferred keep two free bags; A-List and Rapid Rewards cardmembers keep one.

**Numbers (one-bag profile).** Base: round trip **$300**, two bags included. Event year: fare unchanged, +$35/way ⇒ replication cost **$370**, RX **+23.3%** via the named-fee route — no superset flag, no interval.

**The honesty exhibit:** CPI *captures most of this event* — the first checked bag is inside the quote specification on 80% of designated quotes, so those quotes reprice +23.3% too. The expected Restoration Gap on the Southwest event is therefore **small** (residual: the 20% undesignated quotes, second bags, carve-out conditioning). The spec says so out loud. The Gap decomposition exists precisely to show where CPI already works; a measure that manufactured a gap here would be discredited by its own Appendix A.

### 4.3 Disney+ ad tier (the clean tiering case)

December 8, 2022: ad tier launches at **$7.99** — exactly the old ad-free price — while ad-free moves to **$10.99**. Day-one restoration relative for the ad-free holder: **+37.5%**; the entry sticker price read **0%**. The ladder since: ad-free $13.99 (Oct 2023) → $15.99 (Oct 2024) → **$18.99** (Oct 21, 2025), ads at $11.99 — the restoration spread widened from $3 to $7/month; cumulative ad-free restoration 2022→2025: **+137.7%** while the advertised entry price rose 50%. (Netflix parallel: cheapest ad-free went $11.99 → $19.99 between mid-2023 and March 2026 — Basic closed July 2023, retired July 2024 — while the headline price anchored at the $6.99–8.99 ad tier. The May 2023 password-sharing crackdown even created a purchasable line item: the $7.99 "extra member" slot — the purest priced restoration outside air travel.) CPI's cable/satellite/streaming methodology prices one probability-sampled service tier per outlet with hedonics on channel counts and speeds; nothing prices ad load.

### 4.4 The negative controls (P3 in production)

- **Banking:** overdraft/NSF revenue fell **>50%** from 2019 to ~$5.8B in 2023 (CFPB), with other checking fees flat — a falling restoration price. RX must print it negative.
- **Groceries:** GAO-25-107451 — downsizing contributed **~0.06pp** of the 34.5% CPI rise 2019–24, because CPI already books per-unit increases. Expected grocery Restoration Gap ≈ **0**. Published as the null test, reconciled against R-CPI-SC.

---

## 5. Why CPI misses the event — the three seams, restated precisely

The original claims survive only in narrowed form. Every claim below is anchored to verified BLS language (Appendix A; note: BLS pages were triangulated via multiple independent search extractions because bls.gov blocks automated fetch — re-quote from the live pages before any external publication; open item §13).

**Seam 1 — specification boundary (not "fees are missed").** The airline-fares CPI is web-collected against a fixed trip specification (city pair, carrier, fare-class category, advance-purchase weeks, day of week) repriced monthly. The quoted price *includes* taxes, fuel surcharges, airport/security fees, and the first checked bag on the 80% of quotes designated to include one. Verbatim: *"The CPI only tracks the price of the first piece of checked luggage. The price of carry-on bags and any additional checked luggage are not tracked."* So: **a fee is transition-captured iff it attaches to a characteristic inside the priced specification.** Checked-bag fee changes: captured (on designated quotes). Carry-on unbundling, seat-selection fees, boarding rights: structurally outside — the fee never enters, the degradation never enters. **In-scope ≠ transition-captured** resolves to: *the item definition's scope is not the quote specification's scope, and only the latter prices transitions.*

**Seam 2 — weighting, honestly relabeled.** Basket weights come from average realized spend (CEX, lagged ~24 months). People who cope contribute $0 to the fee's weight, pulling it below the price-to-maintain-the-experience. This is not a BLS "error" — plutocratic average-spend weighting is a defensible answer to a different question (Prais 1959; Deaton's estimate: the plutocratic CPI represents roughly the 75th expenditure percentile). The R-CPI-I quantifies what reweighting alone buys: the bottom equivalized-income quintile ran **0.28pp/yr** above the top over 2006–2023 (cumulative **7.67pp**; the chained R-C-CPI-I gap is *larger*: 0.42pp/yr — substitution logic does not close the distributional gap, it widens it). Democratic-vs-plutocratic weighting alone moves CPI-U by only ~0.08pp/yr (Martin, BLS/ROIW) — which is why this spec's headline population is the bottom 40%, not a democratic reweighting, and why the pricing concept, not the weights, must carry the novelty (decomposition, §2.2).

**Seam 3 — the inversion, confined to where it actually lives.** Approximately half of discount-fare quotes are assigned to the **lowest available discount fare** (factsheet: *"Usually these deeply discounted fares are limited to the lowest available fare for a given trip (e.g., basic economy and low price main cabin fares)"*). On those quotes, a stripped fare that becomes the new minimum enters as a pure price decrease — no quality adjustment exists for airline fares (BLS hedonics cover TVs since Jan 1999, smartphones since Jan 2018, residential telecom since Jan 2019 — never airfares, hotels, or restaurants). On the fare-class-locked half, there is no inversion — but the *complementary* failure holds: a new fare class enters by linking, so its level difference against the old class is never differenced in either direction; the transition price of the stripped experience is simply unmeasured. Both halves miss the event; they miss it differently.

**The internal precedent that closes the argument.** BLS's PPI faced exactly this in 2008–09 and *chose to correct for it*: using BTS fee data, it added average bag/cancellation fees per passenger to average route revenue from March 2009 onward; *"the PPI for scheduled passenger air transportation would have been 1.6 percent lower in December 2009"* without the adjustment (Beyond the Numbers, 2012). The CPI never adopted an analogous mechanism. The Restoration Index generalizes what the PPI did for one sector-event into a standing consumer-side design.

**And the theory literature affirmatively cannot fix this.** Under Feenstra (1994) CES logic, *any* new variety consumers buy — including a degraded one — mechanically *lowers* the exact price index (love of variety); Redding–Weinstein (2020) prices taste shocks such that a degraded variety gaining share reads as a price improvement. No strand of the new-goods literature treats choice-set contraction as a price increase; the closest recognitions are Hicks (1940)/Hausman (1996) reservation prices for *disappeared* goods and Pakes (2003), who states outright that matched-model indexes select from the right tail because exiting goods have falling values. RX replaces the econometric virtual price with an **observed replication price** — a nonparametric, menu-based answer to the disappeared-bundle problem. That is the defensible novelty.

---

## 6. Decisions

Reply **"go"** to adopt all, or **"go on rows …"** to adopt selectively.

| # | Question | Recommendation | Confidence | Rationale |
|---|---|---|---|---|
| 1 | Formal primitive | Conditional replication-cost index in characteristics space (Lancaster/Pollak/Konüs framing per §2); keep **"Restoration Index"** as product name, define formally in one sentence everywhere | High | All three adversarial reviews independently demanded this naming; it converts the upper-bound property from a discovered flaw into a stated theorem and inherits R-CPI-SC's publication ancestry |
| 2 | Knob 1 — price concept | Restoration/shopping-list with the lexicographic route hierarchy (§3.4); unit-value series retained only as a published contrast column | High | Unit value re-imports mix-shift bias (Basic uptake reads as deflation — the artifact the index exists to kill); BTS's own average-fare series demonstrates the failure mode |
| 3 | Event trigger | Fires iff same-seller replication cost of the frozen experience rises; downward tier introduction beside an unchanged incumbent prints 0%; symmetric negative prints mandatory | High | The two fatal-unless-fixed attacks (revealed preference; one-way ratchet); P2/P3 are the design's best defenses and cost nothing |
| 4 | Knob 2 — whose basket | Bottom-40% weights via the R-CPI-I recipe (equivalized imputed income FINCBTXM/√HH-size, weighted population rank, multi-year pooled CEX shares, smoothing), **with the pricing-vs-weighting decomposition mandatory in every release** and a democratic-weight sensitivity | Medium — two of three adversarial reviewers preferred a democratic headline | Targeting power: quintile gap 0.28pp/yr vs democratic gap 0.08pp/yr — democratic weighting buys almost nothing toward the stated purpose; copying BLS's own published methodology pre-empts the ranking attacks (income mismeasurement, students/retirees); the decomposition ensures the distributional choice is shown, never smuggled |
| 5 | Knob 3 — shipping form | Spread only: **"Restoration Gap"** over CPI-U per sector + covered composite; exclusive-partition concordance against CPI item strata; cumulated chain as caveated memo; never a standalone rival level | High | Unanimous across reviewers; R-CPI-SC and the published CPI-U/C-CPI-U gap are the institutional templates; a standalone level index inherits every CPI methodology fight (shelter/OER) and relitigates Boskin |
| 6 | Choice-set scope of the min | Same-seller headline ($H$); cross-seller cheapest ($S$) as published sensitivity; $H{-}S$ spread reported as the brand-switching coping margin | Medium-High | Unresolved by the frame and flagged by the completeness critic; same-seller matches the entitlement framing and avoids cross-brand hedonic matching ("is Delta Main the same experience?"); ex-ante matching rules frozen in a public codebook |
| 7 | Chaining and base refresh | Annual links; 12-month relative as headline; Ledger-based re-freeze (incidental superset extras excluded from next base); no monthly chaining; chained-vs-direct drift diagnostic published | High | Min operators chase promotions — monthly chaining is indefensible (Szulc; IDF 2011; BLS C-CPI-U drift study); the Ledger kills both ratchets (upward via supersets, downward via forgiveness) |
| 8 | Superset handling | Lexicographic routes; named fee caps the line item; tier-only events published as flagged interval [0, gap] with the gap as point estimate | High | Bounds the hedonic-swamp re-entry without imputing anything; bias direction is conservative (P6) |
| 9 | Shrinkflation positioning | In scope as a component; positioned as the null-test/validation channel reconciled to R-CPI-SC; never a headline motivation | High | CPI captures downsizing same-month per-unit; BLS/GAO put the residual at ~0.01pp/yr / 0.06pp per 5yr — claiming otherwise is refutable in one citation |
| 10 | Incidence (the hardest problem) | Elementary unit = experience *profile*; restoration line items weighted by base-period utilization shares; where unmeasured, publish [0%, 100%]-utilization bounds, never a bare point | Medium — data availability is the binding constraint | Without incidence, every line item is implicitly 100%-utilization and the index is attackably overstated (the "phantom loss" critique); see §9.1 for sources |
| 11 | MVP | US domestic air travel (primary) + streaming (validation sidecar) + groceries and banking (negative controls), preceded by the 2008–09 retrospective (§10, Phase 0) | High | Air travel: verified CPI-invisible flagship event + richest auxiliary data (BTS/T-100/Form 41) + two live natural experiments (Southwest 5/2025, April 2026 fee wave); streaming: national posted prices, Wayback-recoverable, near-zero collection cost; the controls make P3 demonstrable at launch |
| 12 | Sector sampling frame | Pre-registered universe: all CEX item strata above a bottom-40 expenditure-share threshold, screened by the priced-restoration test; zero-gap imputation for uncovered expenditure in the composite; covered share published every release | Medium-High | The selection-risk attack ("sectors chosen because gaps are big") is otherwise fatal to the composite's interpretability |
| 13 | Weights source & cadence | MVP: published CEX income-quintile tables (FRED `CXU*LB01*` series; UCCs 530110 airfare, 210210 out-of-town lodging, 270310 cable/streaming), bottom-two-quintile means; Phase 2: full PUMD replication of R-CPI-I ranking; annual refresh (matches BLS's own annual single-year weight practice) | High | Two-person-team feasible in days for 2–3 sectors; PUMD needed only for equivalized ranking and standard errors; note 2025 shutdown distortions (2024 data released 12/19/25; 2025 PUMD due 10/29/26) |
| 14 | Positioning discipline | Neutral formal register; no "true inflation" claims ever; pre-registered collection protocol + open code and line-item data before first release; standing reconciliation table vs CPI-U, C-CPI-U, R-CPI-SC; at least one negative print in the launch publication; solicit an external methods discussant pre-launch | High | The ShadowStats anti-pattern (an admitted constant added to CPI, no price collection) defines the failure mode; auditability substitutes for probability sampling in a satellite series |

---

## 7. Prior art and positioning

**Bottom line of the sweep: the primitive is unoccupied.** Targeted searches (constant-experience index, restoration cost index, replication cost index, de-quality-adjusted CPI, all-in price index, fee-inclusive index) return no standing concept from any agency, academic group, or think tank. The neighbors, and the one-line differentiation from each:

| Neighbor | What it is | Why RX is different |
|---|---|---|
| BLS **R-CPI-SC** (from Dec 2014 data) | counterfactual CPI stripping package-size changes, published as a wedge | **the design template** — RX generalizes the wedge from package size to service inclusions and tier composition; also the shrinkflation null benchmark |
| BLS **R-CPI-I / R-C-CPI-I** (monthly from Dec 2005) | income-quintile CPIs; same prices, reweighted | weights only — assumes all quintiles face identical price change; RX differs on the *price* side and borrows the quintile weight recipe |
| BLS **R-CPI-E** (from Dec 1982) | elderly-reweighted research CPI | the institutional proof that a caveated "research" subpopulation series can persist 40+ years and shape policy without official status — RX's posture |
| **PPI air-travel fee adjustment** (2009) | fee-revenue-per-passenger correction for unbundling | the internal-to-BLS precedent that matched-fare pricing misses unbundling (1.6% by Dec 2009); one sector, producer-side, discontinued as an approach — RX is the standing consumer-side generalization |
| Jaravel **D-CPI** (2002–present, real-time) | distributional CPIs, official methodology, by income/age/race | prices identical across groups by construction; natural *partner* series and publication-format model |
| **ONS lowest-cost groceries** (2022, experimental) | cheapest-replication tracker over a fixed 30-item list (the "Vimes Boots" index) | a floor tracker, not an experience freeze; closest agency use of a min-cost operator |
| **ONS Household Costs Indices**; **Stats NZ HLPIs** | democratic-weight / payment-approach group indices | weighting/scope innovations, matched-spec prices; NZ's dual income+expenditure quintile publication answers the Meyer–Sullivan ranking critique; ONS's decade of "in development" status is the operational warning |
| **LISEP True Living Cost** (+106% since 2001 vs CPI +77.2%) | normative minimal-adequacy basket for lower-income households | prices what a household *should* consume; RX prices what this household *did* consume, line-itemed — no adequacy judgment anywhere |
| Cass **Cost of Thriving Index** (40→62 weeks, 1985→2022) | nominal cost-to-median-male-earnings ratio, no quality adjustment, 37-year window | the cautionary tale: Winship–Horpedahl cut +22 weeks to +10 (corrections) to +4 (quality adjustment) — RX's defenses are the 1-year window (Assumption Q plausible), taxes/earnings out of scope entirely, and priced-menu-only claims |
| **CEA junk fees** ($90B/yr, Mar 2024); Senate **PSI** ($12.4B seat + $25.3B bag fees 2018–23); FTC **16 CFR 464** | dollar counts and disclosure regulation | fee-revenue accounting and unshrouding, not a price index over time; PSI's finding that fees are untethered from provision cost is motivation evidence; the FTC rule is *data infrastructure* (all-in lodging/ticket prices observable since 5/12/25) |
| **ShadowStats** | an admitted constant added to official CPI | the anti-pattern; every discipline in row 14 of §6 exists because of it |

**The IO foundation (why unbundling is directional and persistent, no conspiracy required).** Gabaix–Laibson (2006): shrouded add-on pricing survives perfect competition — unshrouding is unprofitable ("curse of debiasing"). Ellison (2005): add-on pricing raises equilibrium profits via adverse selection against price-cutting. Field causality: the StubHub platform-wide experiment (Blake–Moshary–Sweeney–Tadelis, *Marketing Science* 2021) — back-loaded fees raised spending ~21% and completion ~14%; Sullivan's FTC resort-fee analysis (2017): separated mandatory fees raise search costs with no offsetting benefit. Behavioral corroboration on the coping premise: GAO found consumers respond *less* to downsizing than to an equivalent price increase (93% of shrinkflated items showed no significant unit decline) — stealth increases evade precisely the substitution response that chained logic presumes. Scale: global ancillary revenue $67.4B (2016) → $109.5B (2019) → $148.4B (2024) → projected $157B (2025) = 15.7% of airline revenue vs 9.1% in 2016 (IdeaWorks — noting its "ancillary" includes loyalty/co-brand revenue, so legacy-carrier dollar totals overstate pure à-la-carte; the clean unbundling read is the ULCC shares: Frontier 62%, Spirit 58.7%). BTS bag-fee revenue: $5.8B (2019) → $7.27B (2024, record) → $7.4B (2025). Southwest's surrender of a 54-year bundling policy in 2025 is Gabaix–Laibson's absorbing state observed in the wild; the Fifth Circuit's vacatur of DOT's disclosure rule (Feb 3, 2026) is the persistence mechanism observed in regulation.

**The offset debate — cited at full strength, in both roles.** Brueckner–Lee–Picard–Singer (2015): when bag fees arrived (2008+), base fares fell only ~3% (~$5) against $15–20 fees — partial offset; corroborated by Henrickson–Scott (~$0.11 fare offset per fee dollar) and Scotti–Dresner (demand responds an order of magnitude less to fees than to fares — the empirical footprint of shrouding). Read honestly: (i) non-checkers genuinely gained — unbundling has a real price-discrimination welfare defense, and the spec concedes it; (ii) the fee-minus-offset wedge (~$10–15 per bag-checker segment) is, in effect, **the first Restoration Gap measurement ever taken**. And the strongest counter-evidence gets stated plainly: aggregate inflation-adjusted all-in domestic fares (base + bag/change fees per passenger) have been roughly flat since 2001 (A4A series; Eno corroborates). RX's claim is therefore explicitly *not* "average all-in spend rose"; it is that the **replication cost of the bundled experience rose for the bundle-using population** while averages were held down by the coping migration the averages cannot see. That distinction is the whole index.

**Distributional literature (why bottom-40 targeting is evidence-based, not vibes).** Jaravel (QJE 2019): bottom-vs-top quintile retail inflation gap 0.661pp/yr (2004–15; 0.885pp with variety). Kaplan–Schulhofer-Wohl (2017): household-level inflation IQR of 6.2–9.0pp/yr — group averages understate individual exposure, favoring item-level pricing. Argente–Lee (JEEA 2021): quartile gap 0.85pp/yr in 2008–13, with ~40% of it from quality-substitution and shopping-effort margins *"mostly available to richer households"* — the closest peer-reviewed statement of the coping thesis. Cheapflation (Chen–Levell–O'Connell 2024): the cheapest varieties inflated fastest in 2021–23 — coping capacity itself eroding. CBO WP 2025-04 and Cleveland Fed EC 2025-11 confirm the gradient through 2024 and normalize "bottom 40%" as an analytical grouping.

---

## 8. Data feasibility map

| Layer | Source | Status | Notes |
|---|---|---|---|
| Sector weights (bottom-40) | CEX published quintile tables (FRED `CXU*`); PUMD (FMLI/MTBI, FINCBTXM) | **Exists, free** | UCCs: 530110 airfare, 210210 out-of-town lodging, 270310 cable/streaming; ~20k interviews/yr ⇒ ~8k bottom-40 interview-quarters — pool multi-year + smooth (BLS does); CE aggregates ≈ 59% of PCE and worst in discretionary categories — disclose |
| Fee-level line-item weights | **Does not exist in CEX** | **Gap — auxiliary data** | Bag fees, resort fees, tier spreads are embedded in parent UCCs; scale within-sector via BTS Form 41 acct 3906.2 (bag fee revenue, quarterly, by carrier) + 3919.1 (change/cancel fees); seat-fee revenue **cannot be separately identified** in DOT data (GAO) — use PSI report exhibits ($12.4B, 2018–23, five carriers) |
| Airline fares (paired Basic/Economy same-flight quotes) | Google Flights / carrier sites scraping; ATPCO/ARC licensed feeds | **Feasible, gray-zone** | Mature scraper ecosystem exists; fixed pre-registered panel (top routes by T-100 passengers, fixed booking-window/day-of-week grid), self-hosted timestamped hash-committed snapshots — do **not** rely on Wayback (JS fee pages archive unreliably); **Southwest: highest legal risk** (Kiwi.com permanent injunction, 2021; WN absent from most metasearch) — manual/carrier-direct capture |
| Airline transaction fares | OD40/DB1C (replaced DB1B July 2025; monthly, 40% sample) | **Exists — wrong tool for pricing** | `Total Amount` *excludes* ancillary fees; no Basic Economy identifier (cabin-level fare class only) ⇒ unit-value trends and route weights only — this is the documented justification for primary quote collection |
| Airline fee schedules & events | Carrier pages, press releases (swamedia etc.), fee trackers | **Exists** | Verified current: UA $45/$50 first bag, $75 gate path; WN $45/$55 (4/9/26); AA Basic +$5/bag vs Main from 5/18/26 (first fare-class-conditional bag price — a pure tiering observable); April 2026 fee wave across AA/DL/UA/WN/AS/B6 |
| Streaming tier menus | Carrier posted prices; Wayback (HTML pages archive fine); trade press | **Exists, cheap** | Full verified ladders for Netflix/Disney+ 2022–2026 in §4.3; national single-schedule prices |
| Lodging all-in prices | Post-5/12/25: FTC-mandated total-price display (scrapable); pre-2025: OTA archives | **Exists going forward; broken series backward** | Treat May 12, 2025 as a structural break; falsifiable prediction: the lodging seam should *compress* post-rule — publish the test |
| CPI comparators | CPI-U item strata; C-CPI-U; R-CPI-SC; R-CPI-I | **Exists** | The reconciliation table's right-hand columns; R-CPI-I latest verified vintage through Dec 2024 (per CBO WP 61549); confirm the March 2026 release |
| Incidence/utilization | BTS fee revenue ÷ T-100 enplanements (fee-payer proxy); carrier earnings disclosures; PSI exhibits; Antenna (streaming tier mix); eventual small survey | **Partial — the binding constraint** | See §9.1 |
| Regulatory environment | FTC 16 CFR 464 (in effect, enforced — StubHub $10M, 4/9/26; rental-housing expansion rulemaking opened 3/13/26); DOT: 2024 fee rule vacated 2/3/26, 2011 standards restored 7/2/26 (FR 2026-13450), full-fare advertising NPRM 7/1/26 (FR 2026-13294, comments due **7/31/26**) | **Verified as of 2026-07-04** | Important correction from verification: 14 CFR 399.84 full-fare advertising **remains in effect** — do not claim "no federal all-in airfare mandate exists"; only the 2024 *enhanced ancillary-fee* rule is gone, and the NPRM's relaxation is proposed, not final |

---

## 9. Methodological hazards and handling

### 9.1 The single hardest measurement problem: incidence

**The problem.** A restoration line item is a loss only for base-period consumers whose experience actually included the attribute. Charging carry-on restoration to every airfare dollar overstates the average by the non-user share ("phantom losses") — and this interacts perversely with the bottom-40 framing, since low-income consumers may be disproportionately those for whom the stripped tier was already adequate. No public dataset directly reports, e.g., the share of Basic-eligible passengers who previously carried a full-size bag.

**Handling (decision row 10).** (i) Make the *experience profile* the elementary unit, so incidence is a weight, not an afterthought — the P0 profile in §4.1 mechanically prints 0%. (ii) Source utilization proxies: BTS fee revenue ÷ enplanements gives fee-payer incidence for checked bags; carrier earnings calls and the PSI exhibits give fee volumes; Antenna-type panels give streaming tier mix; the FTC rule makes lodging fee incidence observable in posted totals. (iii) Where no proxy exists, publish the [0%, 100%]-utilization interval — never a bare point. (iv) Phase 3: a small annual consumer survey keyed to the covered sectors. This hazard is first-order for the *level* of the Gap; it does not threaten the sign or the event detection.

### 9.2 The rest of the hazard register

| Hazard | Handling |
|---|---|
| Mix contamination | Restoration pricing is the fix by construction (P1/P2); unit-value published only as contrast |
| New-item bias in reverse (RX misses genuinely *better* cheap options) | Conceded openly: RX is an upper bound (P4); the C-CPI-U column of the reconciliation table carries the substitution story; Assumption Q stated every release |
| Ambiguous restoration price | Lexicographic route rule (§3.4); named fee caps; interval publication for tier-only routes; ex-ante equivalence protocol in the public codebook (gate-check ≠ carry-on) |
| Genuinely discontinued experiences | Non-emptiness rule (§3.2): item exits the ledger, weight reallocated CPI-style, exit logged in the Exclusion Register; **no reservation-price imputation ever enters the published number** |
| Chain drift / promotion-chasing min | Annual links; posted fee schedules (not transaction prices) at the elementary level; drift diagnostic (§2.5) |
| Double counting vs CPI | Exclusive partition + public concordance (§2.2): an item priced by restoration leaves the ordinary pool that period |
| Scope endogeneity (firms delete the fee *and* the feature to exit the index) | Exclusion Register census (counts + affected expenditure) makes boundary migration observable; the index is honestly labeled a *lower* bound on total effective-price degradation and an *upper* bound on the COLI — both inequalities stated |
| Scraping legality/continuity | Pre-registered fixed panel; self-hosted hash-committed snapshots; carrier-direct or manual capture for WN (Kiwi injunction); ATPCO/ARC licensing as the production-grade fallback; collection-risk section in the methods appendix |
| CEX weight noise / income mismeasurement | R-CPI-I recipe (equivalized imputed income, smoothing, pooling); Meyer–Sullivan critique disclosed; expenditure-ranked sensitivity (Stats NZ dual-publication precedent); 2025 shutdown distortions footnoted on any 2025-vintage weights |
| Structural breaks in fee observability | FTC rule (5/12/25) and any DOT change dated as break points; no backfilling across them without a break adjustment; the predicted post-rule lodging compression published as a falsification test |

---

## 10. Phased build

**Phase 0 — retrospective validation (the cheapest credibility purchase; ~weeks).** Reconstruct the 2008–09 checked-bag unbundling with archived fee tables, DB1B fares, and Form 41 acct 3906.2; publish the Restoration Gap the method *would have printed*, reconciled against the PPI's documented 1.6% correction and Brueckner's fee-minus-offset estimate. Hunt one historical re-bundling episode (e.g., a carrier or streamer restoring an inclusion) and show the negative print. This note doubles as the methods pre-registration.

**Phase 1 — MVP (first published number).** Air travel: pre-registered route panel (top T-100 routes), paired same-flight Basic/Economy quotes, fee-schedule ledger with the verified 2025–26 event set (Southwest 5/28/25 and 4/9/26; April 2026 fee wave; AA fare-class bag surcharge 5/18/26; United carry-on standing event). Streaming sidecar: full tier ladders (near-zero cost, fully archival). Negative controls: groceries (vs R-CPI-SC) and banking (falling fees). Weights: FRED CXU bottom-two-quintile tables. Output: sector Restoration Gaps + decomposition + Exclusion Register + reconciliation table, code and line items public.

**Phase 2 — expansion.** Lodging (post-FTC all-in data; publish the compression test). Telecom (the T-Mobile 7/13/26 forced migration is a clean superset-flagged event — *verify first*, §13). Rental housing scoping memo — the completeness critic's top gap: bottom-40's largest budget share, live unbundling frontier (application fees, mandatory "convenience"/amenity/valet-trash fees), and CPI's rent index prices contract rent; FTC's rental-housing fee rulemaking (opened 3/13/26) is both evidence and future data. Healthcare scope ruling (facility fees on formerly-bundled visits vs the insurance cost-sharing boundary question) — in or out, decided on the priced-restoration test, documented either way. PUMD-based weight replication with standard errors.

**Phase 3 — composite.** Covered-sector bottom-40 composite Gap with zero-imputation for uncovered expenditure and published coverage share; annual cadence locked to CEX releases; incidence survey; external methods review before any composite headline.

---

## 11. Credibility risks and built-in defenses

The three adversarial reviews (index-number theorist, statistical-agency methodologist, skeptical policy economist) produced ten distinct attack lines. Every fatal or serious one now has a structural answer *inside the design* — not a rebuttal paragraph:

| Attack | Severity (as reviewed) | Design answer |
|---|---|---|
| Revealed preference: trading down into a still-available option is welfare-improving | fatal-unless-fixed | Trigger split (§3.1) + P2: the index cannot fire on menu expansion; "welfare loss" language dropped project-wide — the claim is *replication cost*, true by construction |
| One-way ratchet / alarmism machine | fatal-unless-fixed | P3 symmetry + negative controls in the launch set + gross-up/gross-down components published separately |
| "BLS already captures fees/shrinkflation" | fatal-unless-fixed (as originally worded) | Seams narrowed to the documented residual (§5); factsheet quoted verbatim; shrinkflation demoted to null test; Southwest honesty exhibit (§4.2) shows the Gap ≈ 0 where CPI works |
| Superset pricing re-enters the hedonic swamp | serious | Lexicographic routes, fee caps, interval publication, Ledger-based refreeze (§3.4, §2.5) |
| Boskin relitigation | serious | 12-month links only; bound language in every release; cumulated chain as caveated memo; Assumption Q explicit |
| Sector cherry-picking | fatal-unless-fixed | Pre-registered CEX-share sampling frame; zero-gap imputation for uncovered items; coverage share published (§6 row 12) |
| Aggregation incoherence / double counting | serious | Exclusive partition + wedge definition (§2.2): the published object is *CPI plus a reconciliation account*, a nameable thing |
| Non-probability scraping | serious | Fixed pre-registered panel, hash-committed snapshots, BTS cross-validation, open protocol before first release |
| Bottom-40 weights soft target | serious | R-CPI-I recipe copied exactly; decomposition mandatory; democratic + expenditure-ranked sensitivities |
| Advocacy-artifact pattern-match | serious | Row 14 discipline; the reviewers' own acceptance conditions (trigger split, symmetry, partition, ledger refreeze) are all adopted — the paper-trail *is* the defense |

**Reviewer verdicts after fixes, verbatim in spirit:** the theorist — "with the removal-vs-addition split, symmetry, exclusive-partition aggregation, and fixed-cycle base refresh, I would accept as a satellite/audit statistic; without the first, I reject." The methodologist — "survives as an explicitly-labeled upper bound with narrowed seams." The policy economist — "as a bound and a mechanism-incidence measure of unbundling/tiering, citable."

---

## 12. Honest limitations (goes in every release, abridged)

1. **Upper bound, not truth.** RX ≥ the constant-experience COLI by construction; the Gap is informative about the unbundling/tiering margin, not about aggregate CPI bias sign. The profession's consensus that CPI *overstates* COLI growth (Boskin: ~1.1pp/yr in 1996; later estimates lower) and this measure are answers to different questions and can both be right.
2. **Priced restorations only.** Silent degradation is excluded — the Exclusion Register counts it but the index cannot price it. The index therefore *understates* total effective-price degradation while bounding the COLI from above.
3. **Non-users gained.** Partial offset means unbundling made light users better off; the index measures the bundle-replicating population's cost, incidence-weighted, and says so.
4. **Reproducible experiences only.** Items whose base experience cannot be repurchased at any price exit the ledger, logged.
5. **Research-series posture.** Larger measurement error than official statistics; CEX coverage and quintile ranking caveats inherited and disclosed; scraped panels are auditable, not probability samples.
6. **Aggregate all-in averages are flat in air travel.** The claim is distributional and experience-constant, not an average-spend claim.

---

## 13. Open items and immediate actions

**Status (2026-07-04, per plan v00.03.02):** 1 — comment drafted (`docs/dot-nprm-comment-draft.md`), filing is owner's, due 7/31. 2 — open (owner, unblocked connection). 3 — **closed** (verified; Phase 2 flagship; pre-migration archival due before 7/13). 4 — partial (major categories byte-verified in `data/cex-b40-quintiles.csv`; detail cells open). 5 — **closed** (latest vintage: Dec 2024 data; 2026 update delayed). 6 — **closed** (EU Reg 2020/1148 has the principle, no procedure; novelty claim reworded per plan P12). 7 — **closed** (healthcare OUT; rental module ruled IN, plan §2). 8 — partial (`data/incidence-proxies.md`; carry-on incidence is a flagged gap).

| # | Item | Deadline / trigger |
|---|---|---|
| 1 | **File a comment on DOT NPRM FR 2026-13294** (full-fare advertising flexibility) if the posted all-in price matters to collection — it does | **comments due 2026-07-31** |
| 2 | Re-quote all BLS factsheet language from live pages over an unblocked connection (this environment's proxy 403s bls.gov; all quotes were triangulated via multiple independent search extractions — high confidence, not byte-verified) | before any external use |
| 3 | Verify the T-Mobile 7/13/26 forced-migration event against T-Mobile newsroom/support pages before it enters the Phase 2 ledger (currently sourced to trade press) | before Phase 2 |
| 4 | Pull exact bottom-quintile CEX item shares from BLS Table 1101 / FRED (the shares quoted in scoping were training-recall approximations, flagged) | Phase 1 weights |
| 5 | Confirm the R-CPI-I March 2026 vintage (through Dec 2025) landed on schedule | Phase 1 reconciliation |
| 6 | Check Eurostat HICP rules for tariff-structure changes and option prices (Reg. 2020/1148; HICP Methodological Manual) and the ILO/IMF CPI Manual quality-change chapter — either an existing agency rule for this event type exists (bounds the novelty claim) or an authoritative absence (strengthens it) | before Phase 0 note |
| 7 | Decide the healthcare scope ruling (facility fees vs cost-sharing) via the priced-restoration test; write the rental-housing sector memo | Phase 2 |
| 8 | Incidence proxy build-out per §9.1 | Phase 1–3 |

---

## Appendix A — verification status of load-bearing facts

Fourteen facts were independently adversarially verified against primary sources (2026-07-04). Corrections were incorporated throughout; the notable ones:

| Fact | Status | Correction applied |
|---|---|---|
| CPI airline factsheet: carry-on/2nd-bag not tracked; 80% checked-bag designation; taxes/surcharges/bag fees in quoted price | **confirmed** (verbatim) | — |
| "Half of discount quotes at lowest available fare, typically Basic" | **partially correct** | factsheet wording is *"approximately half for the lowest available discount fare"*; Basic economy appears as an *"(e.g., …)"* example; the no-quality-adjustment consequence is inference (sound), not factsheet text |
| No hedonics for airfares/hotels/restaurants; TVs Dec 1997 | **partially correct** | TV hedonics began **Jan 1999** (Dec 1997 was a weight-reference date); absence claim for airfares confirmed |
| PPI 1.6% unbundling correction (Dec 2009) | **confirmed** | adjustment began March 2009 |
| Shrinkflation captured same-month per-unit; ~0.01pp/yr; GAO 0.06pp of 34.5% | **confirmed** | R-CPI-SC *data* begin Dec 2014; first *released* ~2023; covers food-at-home + selected strata, not all-items |
| United Basic: personal-item only; $45–50 prepaid bag; $75 gate ($65 pre-4/3/26) | **confirmed** | — |
| Basic-vs-Main spread $49–80 RT | **partially correct** | that was NerdWallet's 2024 survey; the **May 2026** survey: $85–99 RT most airlines, $129 Alaska — "~$50 each way" is now inside the plausible fare-delta range |
| Southwest: announced 3/11/25, effective bookings on/after 5/28/25, $35/$45 → $45/$55 on 4/9/26; carve-outs | **confirmed** | trigger is "booked and ticketed and/or changed"; "Choice Extra" is the post-rebrand name of the exempt top fare |
| R-CPI-I: 0.28pp/yr, cumulative 7.70pp | **partially correct** | BLS figure is **7.67pp** (2006–23); 7.70 was a Minneapolis Fed restatement; newer vintage through Dec 2024 exists (CBO: 65.6% vs 57.5% cumulative) |
| FTC fee rule effective 5/12/25, two sectors, enforced (StubHub $10M 4/9/26) | **confirmed** | — |
| DOT: no federal all-in airfare mandate remains | **refuted in part** | 2024 ancillary rule vacated 2/3/26 and 2011 standards restored 7/2/26, **but 14 CFR 399.84 full-fare advertising remains in effect**; NPRM would relax prominence rules only |
| CEA $90B/yr junk fees (3/5/24) | **confirmed** | brief's own phrasing: "approximately $90 billion per year" |
| BTS bag fees $5.8B/'19, $7.07B/'23, $7.27B/'24, $7.4B/'25; PSI $12.4B seat + $25.3B bag | **partially correct** | PSI report released **Nov 26, 2024** (hearing Dec 4); seat-fee revenue not separable in DOT data (GAO) |
| Bag-fee offset: fares fell ~3% (~$5) vs $15–20 fees (Brueckner et al. 2015) | **confirmed** | — |

Full verification transcripts, source URLs, and the research corpus are retained in the session archive.

---

## Sources (selected)

BLS: CPI airline-fares factsheet; Handbook of Methods (Calculation); Quality Adjustment in the CPI; R-CPI-SC; R-CPI-I/R-C-CPI-I (Klick & Stockburger, MLR July 2024; WP 537); R-CPI-E; Beyond the Numbers vol. 1 (PPI air-travel fees, 2012) and vol. 12 (shrinkflation, McNair 2023); MLR 2013 (PPI air transport); MLR 2021 (Cage et al., C-CPI-U chain drift); CE PUMD documentation; CE-CPI concordance. GAO-25-107451 (2025). BTS: OD-40; Form 41 Directive 289; baggage-fee releases 2019–2025. Federal Register: 2024-30293 (FTC fees rule); 2026-13450; 2026-13294. FTC: Sullivan (2017) resort fees; StubHub settlement (4/9/26). CEA, *The Price Isn't Right* (3/5/24). Senate PSI, *The Sky's the Limit* (11/26/24). Carriers: united.com, swamedia.com, news.aa.com; NerdWallet Basic-vs-Main surveys (2024, 2026). Theory: Konüs (1924/1939); Hicks (1940); Prais (1959); Lancaster (1966); Fisher & Shell (1972); Muellbauer (1974); Szulc (1983); Pollak (1989); Feenstra (1994, 1995); Hausman (1996); Boskin Commission (1996); Moulton & Moses (1997); Deaton (1998); CNSTAT *At What Price?* (2002); Pakes (2003); Gabaix & Laibson (2006); Ivancic–Diewert–Fox (2011); Ellison (2005); Brueckner–Lee–Picard–Singer (2015); Scotti & Dresner (2015); Kaplan & Schulhofer-Wohl (2017); Jaravel (2019, 2021, D-CPI 2024/25); Redding & Weinstein (2020); Blake–Moshary–Sweeney–Tadelis (2021); Argente & Lee (2021); Martin (BLS/ROIW 2022); Chen–Levell–O'Connell (2024); CBO WP 2025-04. ONS: Household Costs Indices; lowest-cost groceries (2022); shrinkflation analyses. Stats NZ HLPIs. LISEP TLC; American Compass COTI (2023); Winship & Horpedahl (AEI 2023). Hamilton, *Shadowstats debunked* (Econbrowser 2008). IdeaWorks/CarTrawler Yearbooks (2025). Légifrance JORFTEXT000049502248 (France, 2024). CFPB overdraft/NSF Data Spotlight (2024); P.L. 119-10.

---

## Changelog

- **v00.02.00** (2026-07-04 21-51) — **P2 refined from "option-introduction invariance" to menu-expansion monotonicity**, surfaced by implementing the min-cost operator (`engine/restoration.py`): a new option that weakly dominates a profile's frozen experience at lower cost genuinely lowers replication cost and prints negative (consistent with P3); menu expansion can never raise RX. S2 exhibit updated with the per-profile split (carry-on 0%; personal-item −13.3%; weighted ≈ −4.0%). Propagated to §0, §2.4, §3.1, §4.1, the codebook, plan row 3, and the site. Public brand recorded ("The Restoration Gap", plan P13). §13 open-item statuses updated (3, 5, 6, 7 closed; 1 drafted; 4, 8 partial). Worked examples are now executable: `python3 -m unittest discover engine`.
- **v00.01.00** (2026-07-04 17-50) — Initial specification. Frame adopted with amendments: primitive formalized as conditional replication-cost index in characteristics space; event trigger split (option-introduction invariance) and symmetry made mandatory; shrinkflation demoted from motivation to null-test channel; seams narrowed to verified BLS language; "~$50 each way" recast as min-over-routes with current verified fees; Knobs 1–3 resolved (restoration pricing with lexicographic routes; bottom-40 R-CPI-I-recipe weights with mandatory decomposition; spread-only publication); MVP set to air travel + streaming sidecar + negative controls, preceded by 2008–09 retrospective validation; 14 decisions tabled; 14 load-bearing facts verified (5 corrected). Built from a 28-agent research and adversarial-review workflow (9 domain researchers, 3 hostile referees, 14 independent fact verifications, 1 completeness critic).
