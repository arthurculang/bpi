# Restoration Index — Project Plan

`v00.01.00 · 2026-07-04 18-40 · internal working doc · companion to: Restoration Index Spec v00.01.00`

---

## 0. The big picture, made operational

The product is not an airfare fee tracker. The end state is **a standing annual audit of what it costs a bottom-40% household to keep living last year's life** — the holistic consumer experience, sector by sector, with air travel serving as the methods lab it deserves to be and nothing more. The numbers force this framing: airline fares are **~0.5%** of a bottom-two-quintile budget; rent alone is **~14%** (Q1: 16.5% of all spending in 2024). A project that stayed in the airport would measure the sharpest case and miss the household.

Every release ships **three artifacts**, and together they carry the holistic goal:

1. **The composite Restoration Gap** — covered-sector, bottom-40-weighted, decomposed into pricing-concept vs weighting effects, with zero-imputation for uncovered spend and the coverage share printed on the front page.
2. **Sector gaps with the Inclusion Ledger** — every restoration event as an auditable line item (what was included, what it costs to get back, via which route).
3. **The Exclusion Register** — the census of *unpriced* degradation: counts and affected base expenditure for everything the scope rule keeps out (skimpflation, healthcare facility fees, subsidy lapses). This is how "holistic" survives the priced-restoration boundary: **what the index cannot price, it still counts.** The full story of the consumer experience = the Gap (priced) + the Register (unpriced), and the plan treats the Register as a first-class product, not a disclaimer.

**North-star metric:** share of bottom-40 expenditure inside monitored sectors. Trajectory: Phase 1 ≈ 12% (honest and stated) → Phase 2 ≈ 30% (rent + connectivity + lodging enter) → Phase 3 ≈ 36%+ (food-away/delivery, ticketing). The remainder is never hidden — it is priced at a zero gap in the composite and itemized in the coverage statement.

**One structural principle falls out of this research pass: capture now, publish later.** The archival record is the scarce asset, and it is newly rich but fragile: Zillow's Total Price display went live July 15, 2025; FCC broadband labels became machine-readable October 2024 but face a rollback FNPRM with a final rule expected 2H 2026; T-Mobile deletes ~1,100 legacy plan codes from its menu on **July 13, 2026**. Snapshot pipelines for *all* planned sectors therefore start in Sprint 0 — publication is phased, collection is not. Every month of delay costs baseline that cannot be reconstructed.

---

## 1. The coverage map (the plan's spine)

Bottom-two-quintile expenditures, BLS CE Table 1101 — 2024 vintage where available, 2023 detail otherwise (release USDL-25-1586, Dec 19, 2025; values cross-verified against two independent mirrors of BLS API/flat-file data; refresh the 2023-vintage cells when BLS/FRED access allows). Q1 total: $35,046. Q2 total: $50,054. Expansion priority = budget weight × restoration-test fit — never fee salience.

| Sector | Q1 $/yr (share) | Q2 $/yr (share) | Restoration-test fit | Disposition |
|---|---|---|---|---|
| Shelter — rented dwellings | 5,781 (16.5%) | 6,225 (12.4%) | **Strong**: named mandatory fees (valet trash $25–50/mo, package/tech fees, convenience fees, month-to-month premiums 5–20%), posting now forced by law and litigation | **Phase 2 flagship**; forward panel starts Sprint 0 |
| Food at home | 3,843 (11.0%) | 4,952 (9.9%) | Weak by design — CPI per-unit capture works | **Phase 1 null control** (vs R-CPI-SC) |
| Healthcare | 3,445 (9.8%) | 4,826 (9.6%) | **Fails** (see §2.3) | **Out** — Exclusion Register with magnitudes |
| Utilities | 2,941 (8.7%)* | 3,987 (8.2%)* | Weak: regulated tariffs, few contractible inclusions | Out for now; watch fixed-charge unbundling |
| Transportation (all) | 5,105 (14.6%) | 8,430 (16.8%) | Mostly weak (vehicles, gasoline = commodities) | Out, except air travel below |
| — Airline fares | 167 (0.5%)* | 274 (0.6%)* | **Strongest** (verified events, paired menus) | **Phase 1 methods lab** |
| Connectivity + subscription media (cellular + internet + pay-TV/streaming) | ≈1,540 (4.5%)* | ≈2,220 (4.4%)* | **Strong**: tier deltas, ad-free spreads, extra-member fees, forced migrations, equipment fees; menus national and archived | **Phase 1** (streaming sidecar) + **Phase 2** (wireless, T-Mobile flagship); broadband Phase 3 |
| Food away from home / delivery | 1,655 (4.7%) | 2,448 (4.9%) | Medium: priced service/delivery fees, but baselines ambiguous (delivery was never free) | Phase 3 candidate; scope memo required |
| Entertainment fees & admissions | 168 (0.6%)* | 339 (0.7%)* | Medium-strong: ticketing fees now FTC-disclosed all-in | Phase 3 candidate |
| Lodging on out-of-town trips | 166 (0.5%)* | 338 (0.7%)* | Strong post-5/12/25 (FTC all-in display); broken series backward | **Phase 2** (with the compression falsification test) |
| Banking fees | n/a (fee, not CEX line) | n/a | Strong, and *falling* | **Phase 1 negative control** |
| Apparel, personal care, education | 1,124 / 427 / 828 | 1,328 / 659 / 407 | Poor (no priced restoration grammar) | Exclusion Register |

\* 2023 vintage. Education shows the classic Q1 > Q2 anomaly (students with low current income) — one more reason weights follow the R-CPI-I equivalized-income recipe rather than raw CE income ranks.

---

## 2. Sector rulings from this research pass

### 2.1 Rental housing — IN, Phase 2 flagship; collection starts now

**Facts (web-verified).** CPI Rent of Primary Residence prices *contract rent* — all services the landlord provides in exchange for rent — and quality-adjusts for utility bundling changes and extra charges like pet fees. But one-time fees (application $50 typical, paid by 79% of recent renters; admin; move-in) have no home in the rent index, and separately billed mandatory recurring fees (valet trash, tech/package fees, RUBS utility billing, payment "convenience" fees) enter only if respondents report them as rent; the 6-month continuing-tenant panel structurally underweights fees loaded at new-lease events. The fee stack is litigated and large: FTC v. Invitation Homes ($48M, fees up to ~$1,700/yr on top of advertised rent), FTC & Colorado v. Greystar ($24M, Dec 2025, "hundreds of dollars more per month" — package delivery, trash, technology packages). Posting is being forced onto the menu: Zillow Cost of Renting Summary (2023) → Total Price display (July 15, 2025); Minnesota Total Monthly Payment law (2024); Colorado HB25-1090 (Jan 1, 2026); FTC rental-fee ANPRM (Mar 13, 2026 — comments closed Apr 13; no NPRM yet). ~53% of bottom-quintile households rent; 83% of <$30k renters are cost-burdened with median residual income of $250/month.

**Module design (decision P5).** Target concept: **advertised-rent-plus-mandatory-fees** — this avoids double-counting against CPI's contract-rent concept and measures exactly the drip wedge. Components: the recurring mandatory-fee stack needed to reproduce last year's tenancy (trash service on the old basis, parking, fee-free payment, lease-term parity), plus amortized one-time fees at a forced re-search event. Always-separate fees (pet) and unpriced degradation route to the Register. A **posted-vs-realized audit** (paired secret-shopper applications vs listed fees) is mandatory, because fees were historically revealed at application, not in listings. Backcasting before ~2023 leans on enforcement exhibits (Invitation Homes/Greystar complaints carry dated fee schedules), the FTC-2026-0266 docket corpus, and archived listings.

**Implication.** The forward panel (Zillow Total Price + Apartments.com fee fields, fixed unit sample stratified by market and building class, monthly, hash-committed snapshots) starts in Sprint 0 even though publication is Phase 2.

### 2.2 Telecom — IN, Phase 2; T-Mobile July 13, 2026 is the flagship event

**Facts (web-verified).** T-Mobile force-migrates 8M+ customers on Simple Choice/ONE/Magenta/legacy-Sprint plans to "Experience" tiers on bill cycles starting **July 13, 2026** — average +$4/line (voice +$6, watch/tablet +$3, 5G Home Internet +$6), **no opt-out** ("There's no going back to the old plans" — T-Mobile CMO), ~1,100 plan codes retired, 62+ migration-target codes, with a published plan-to-plan crosswalk. It is the third legacy repricing in 26 months (May 2024 +$2–5, April 2025 +$5) and erodes the "Un-contract"/Price Lock promises now in class-action litigation. AT&T's April 2026 legacy increases explicitly paired hikes with hotspot-data adds — the compensating-quality maneuver hedonic adjustment rewards and the Restoration Index correctly ignores (extra hotspot is irrelevant if absent from the frozen baseline).

**The honest CPI framing (decision P6).** Telecom is where CPI has the *most* quality machinery: since July 2025, CPI wireless is built from vendor-scraped near-universe *advertised* plan menus under expenditure-weighted full-menu hedonic regressions. Grandfathered rates are not advertised offers — so the migration's bill impact largely falls **outside CPI's measurand**, not inside it mismeasured. The module therefore claims **complementarity, not correction**: CPI answers constant-quality offer inflation; the Restoration Index answers what it costs 8M households to keep last year's bill. Module design: freeze per-carrier plan-feature vectors from archived menus and carriers' own "(Retired)" plan support pages; restoration price = cheapest same-carrier current-menu plan weakly dominating the frozen vector (superset-flagged — these are supersets by construction); cross-carrier/MVNO as sensitivity. ACP's June 2024 end is a subsidy lapse, not firm unbundling → Exclusion Register with magnitude ($30/mo), since ACP households concentrate in the target population.

**Time-critical:** archive the pre-migration menu, the retired-plan feature documentation, and the crosswalk **before July 13** (9 days). Also begin FCC broadband-label capture now — the machine-readability and archiving requirements face a rollback final rule expected 2H 2026.

### 2.3 Healthcare — OUT (printable ruling), with a standing revisit trigger

Healthcare exhibits the project's phenomena at scale — facility fees add ~$100 to a ~$116 primary-care visit; site-neutral misalignment was worth $6.0B in Medicare Part B plus $1.5B in beneficiary cost-sharing in 2021 alone; average single deductibles are up 43% in ten years — **and it still fails the index's own scope machinery, on both candidate slices, differently:**

- **Facility fees** fit the event grammar superficially (a named mandatory fee on an unchanged visit — the resort-fee analog) but fail the *menu condition*: billed ex post, payer-specific, typically undisclosed before care. No posted replication price exists, the consumer's cost runs through plan cost-sharing (breaking same-seller minimization), and paying the fee restores nothing.
- **Cost-sharing tiering** has posted menus (ACA metal tiers) but the frozen experience is actuarial: actuarial value is model-imputed against a standard population — hedonics by another name — networks and formularies are uncontractible, and the 2026 enhanced-PTC expiry repriced coverage ~+114% with no firm menu event, which the index would misread as a restoration print driven by politics.
- **Decisive:** CPI's health-insurance stratum prices insurer *retained earnings*, not premiums, and CPI medical weights are out-of-pocket-only (8.9% CPI vs 22.3% PCE) — there is **no commensurable CPI comparator, so the Gap — the shipping product — is undefined here.** The constant-coverage corner is also already occupied (Milliman Medical Index, 20 years running; BLS MLR total-premium research) — the novelty claim is weakest exactly here.

**Ruling:** facility fees and coverage erosion go to the **Exclusion Register with their magnitudes** (HCCI, MedPAC, KFF cites) — counted, not priced. Revisit trigger: a menu-posted slice matures (state facility-fee disclosure laws — nine states now ban some fees; cash-price telehealth).

### 2.4 Confirmed corrections entering the ledger (from the open-items sweep)

- **April 2026 bag-fee wave, now fully verified:** AA $45/$55 prepaid, $50/$60 airport (from Apr 9; Basic Economy $55/$65 from May 18); DL $45/$55 (Apr 8); AS/Hawaiian $45/$55 (Apr 10); B6 moved **March 31** with peak/off-peak calendars ($39–49 first / $59–69 second, +$10 within 24h or at airport) — the B6 fee menu requires **date-dependent pricing**, a collection-design detail.
- **R-CPI-I vintage:** latest verifiable is data through **Dec 2024**; the March 2026 update is unconfirmed and likely delayed (Oct 2025 CPI never published; Oct–Nov 2025 CE data missing; 2025 weights reach CPI only with Jan 2027 indexes). Weights module pins to the Dec-2024 vintage and tolerates an irregular successor.
- **Novelty claim, precisely worded:** EU Implementing Regulation 2020/1148 already mandates that changes in a tariff's *conditions* count as **price** change in the HICP — the principle exists in EU law. No agency anywhere publishes a worked *procedure* for pricing an unbundling transition. The project's contribution is **the procedure and the conditional-experience basket, not the principle** — cite 2020/1148 as bounding prior art.
- **Competitor scan:** no restoration-style index launched Jan–Jul 2026. Environment note: May 2026 CPI is running 4.2% y/y post-fuel-shock and the Fed chair is publicly courting alternative price measures — a receptivity tailwind that the positioning discipline (§6, P10) deliberately does not chase.

---

## 3. Workstreams (continuous; cut across phases)

| WS | Scope | Standing outputs |
|---|---|---|
| A — Methodology | Codebook: equivalence protocol, route hierarchy, trigger rules, event-registry schema; drift diagnostics; Assumption Q | Pre-registration; versioned codebook |
| B — Collection infrastructure | Menu snapshot pipeline (scrapers + manual capture), hash-committed timestamped archive, per-sector collectors | The archive; collection-risk log |
| C — Weights & population | CE quintile tables → PUMD R-CPI-I replication; annual refresh; incidence proxies per sector | Weight vintages with shutdown footnotes |
| D — Sector modules | Ledger + collector + event registry + gap calculation + write-up per sector (template = air travel) | Sector Gap series |
| E — Validation | Phase 0 retrospective; reconciliation vs CPI-U / C-CPI-U / R-CPI-SC / R-CPI-I; negative controls; falsification tests (lodging post-FTC compression) | Reconciliation table each release |
| F — Publication & review | External methods discussant; open code/data; release template with bound language and limitations; correction protocol | Releases; correction log |
| G — Governance & legal | Scraping counsel (WN = manual capture only); ATPCO/ARC licensing decision; regulatory comments; continuity plan | Legal register |

---

## 4. Phase plan, gates, and kill criteria

**Sprint 0 — preservation and posture (July 2026, ~3 person-weeks).**
Time-critical captures: T-Mobile pre-migration menus/crosswalk/retired-plan pages (**before Jul 13**); FCC broadband labels (machine-readable while they last); rental listing-fee panel v0 (Zillow Total Price + Apartments.com fields); streaming tier pages; all carrier bag-fee pages incl. B6 peak calendars. File the DOT NPRM comment (**due Jul 31**). Ledger schema + codebook v0. CEX weight pull via BLS API / verified mirrors. BLS factsheet re-quotes from an unblocked connection.

**Phase 0 — retrospective validation (Aug–Oct 2026, ~8–10 pw).**
Reconstruct the 2008–09 checked-bag unbundling (archived fee tables, DB1B, Form 41 acct 3906.2); publish the Gap the method *would have printed*, reconciled against the PPI's 1.6% correction and Brueckner's fee-minus-offset wedge. Find and price one historical re-bundling episode (negative print). Doubles as the public pre-registration.
**Gate G0:** retrospective lands within a pre-stated plausibility band of the PPI/Brueckner benchmarks. **Kill criterion:** if the method cannot reproduce a documented historical event, stop and revise the primitive before any live collection spend.

**Phase 1 — MVP and first print (Sep 2026 – Q1 2027, ~16–24 pw).**
Air travel (pre-registered T-100 route panel, paired same-flight Basic/Economy quotes, 2025→2026 event ledger — largely archival) + streaming sidecar + groceries and banking controls. Weights from published CE quintile tables. External discussant review **before** publication.
**Gate G1:** discussant passes; controls print as predicted (groceries ≈ 0, banking negative); independent rerun from archived snapshots reproduces the number. First public release: **target Q1 2027**.

**Phase 2 — the holistic turn (2027, ~30–40 pw).**
Rent module (flagship; panel already 12+ months deep by then) + telecom (T-Mobile event year lands in the 2026→2027 link — the timing is exact) + lodging (with the post-FTC compression test as a falsification exhibit). Healthcare ruling published in the release. PUMD-based weights with standard errors. Incidence proxy build-out.
**Gate G2:** coverage ≥ ~25–30% of bottom-40 spend; per-sector reproducibility; no unresolved methods disputes from review.

**Phase 3 — composite (2028).**
Covered-sector composite Gap with zero-imputation and printed coverage share; annual cadence locked to CE releases; small incidence survey; food-away/delivery and ticketing scope memos; institutional-partnership decision.
**Gate G3:** second external review round before any composite headline.

---

## 5. Resourcing (Assumptions — labeled)

Core team of two (one economics/methods, one data engineering), counsel hours for scraping/ToS review, discussant honorarium. Year-one load ≈ 30–40 person-weeks — feasible for two people at substantial part-time. Recurring cost center is scraper maintenance; storage is trivial. Contingency: ATPCO/ARC licensing (unquoted — WS-G obtains quotes in Phase 1) if scraping proves too brittle for production. These are planning assumptions, not estimates from experience with this exact stack.

---

## 6. Project-level risk register (beyond the spec's §9 methods hazards)

| Risk | Handling |
|---|---|
| Airfare capture — the methods lab becomes the product | Coverage map is the spine (§1); north-star metric is coverage share; airfare's 0.5% weight printed in every release |
| Method fails the retrospective | G0 kill criterion — no live-collection spend until the primitive reproduces 2008–09 |
| Baseline evaporation (menus deleted, labels rolled back, listings churn) | Capture-now-publish-later (P3); Sprint 0 snapshots for all planned sectors; hash-committed archive |
| Data continuity — DOT relaxes posted all-in fares; FCC label rollback; scraper blocks; WN legal exposure | NPRM comment (Jul 31); label capture now; fixed pre-registered panels; manual capture for WN; ATPCO/ARC fallback |
| Credibility sequencing — publishing before review | G1 hard-gates the first print behind the discussant; correction protocol pre-committed |
| Political capture — the number gets mislabeled "true inflation" in discourse | Bound language in every artifact; no "true inflation" claims ever; standing reconciliation table; the receptive macro moment (4.2% CPI, Fed courting alternative gauges) is explicitly *not* chased |
| Solo-author / bus-factor risk | Open code and data from Phase 0; the pre-registration and codebook make the method executable by others |
| Competitor emerges | Field verified clear as of 2026-07-04; scan repeated each phase; first-mover advantage compounds through the archive (uncopyable backfile) |

---

## 7. Success metrics and falsification commitments

- **Coverage:** monitored bottom-40 expenditure share ≈12% (P1) → ≈30% (P2) → ≈36%+ (P3), printed every release.
- **Validation:** Phase 0 retrospective within the pre-stated band; groceries null ≈ 0 vs R-CPI-SC; banking prints negative; lodging Gap compresses after May 12, 2025 (if the seam is real, the FTC rule should shrink it — a prediction that can fail in public).
- **Reproducibility:** every published number re-derivable by a third party from the archived snapshots and open code.
- **Review:** external discussant sign-off before first print; second round before the composite.
- **Honesty exhibits in print:** the Southwest case (CPI captures most of it; Gap small) and the telecom complementarity framing appear in the releases that cover them.

---

## 8. Decisions

Reply **"go"** to adopt all, or **"go on rows …"** to adopt selectively. (Spec decisions 1–14 stand; these are plan-level.)

| # | Question | Recommendation | Confidence | Rationale |
|---|---|---|---|---|
| P1 | Prime directive | The holistic coverage map (§1) is the plan's spine; airfare is the methods lab, labeled as such (0.5% of the B40 budget) in every release | High | The verified budget shares make the ordering unambiguous; this is the structural answer to "don't lose the big picture" |
| P2 | Product definition | Three artifacts per release: composite Gap + sector gaps/Inclusion Ledger + Exclusion Register, with the Register treated as a first-class product | High | The Register is how the holistic goal survives the priced-restoration boundary — unpriced degradation is counted, never silently dropped |
| P3 | Collection posture | **Capture now, publish later**: Sprint 0 starts hash-committed snapshot pipelines for all planned sectors regardless of publication phase | High | Zillow Total Price (7/15/25), FCC labels (rollback expected 2H 2026), T-Mobile menu deletion (7/13/26) — the baseline is fragile and unreconstructible; the archive becomes the project's uncopyable asset |
| P4 | Phase sequence | Sprint 0 (Jul '26) → Phase 0 retrospective + pre-registration (Aug–Oct '26, gate G0) → Phase 1 first print: air + streaming + controls (target Q1 '27, gate G1) → Phase 2: rent + telecom + lodging ('27, gate G2) → Phase 3 composite ('28, gate G3) | Medium-High | Sequenced by validation-before-collection-before-coverage; dates assume the §5 resourcing envelope |
| P5 | Rent module | Enter Phase 2 as flagship; target concept = advertised-rent-plus-mandatory-fees; recurring fee stack + amortized one-time fees at forced re-search; mandatory posted-vs-realized audit; forward panel from Sprint 0 | High (entry), Medium (design details) | Passes the restoration test better than any sector except air; largest B40 budget item; law/litigation now force fee posting; the audit answers the posted-vs-revealed hazard the NCLC record documents |
| P6 | Telecom module | Enter Phase 2 with T-Mobile 7/13/26 as flagship superset event; same-carrier dominance replication, cross-carrier sensitivity; frame vs CPI as **complementarity, not correction** (different measurand — CPI prices advertised menus under full-menu hedonics since Jul 2025) | High | Cleanest menu-removal event available (no opt-out, published crosswalk, 8M+ households); the measurand distinction is what survives BLS scrutiny in the sector where BLS has the most tooling |
| P7 | Healthcare | Out of the restoration ledger; facility fees and coverage erosion logged in the Exclusion Register with magnitudes; revisit trigger = a menu-posted slice matures | High | Fails the menu condition (facility fees) and the contractibility condition (actuarial tiers); no commensurable CPI stratum exists (retained-earnings method), so the Gap is undefined; Milliman MMI already occupies constant-coverage |
| P8 | Gates & kill criteria | As specified in §4; G0 is a hard kill, G1/G3 hard-gate publication behind external review | High | The retrospective is the cheapest possible test of the whole premise; publishing an unreviewed first number is the one unrecoverable error |
| P9 | Resourcing envelope | Two-person core + counsel + discussant; year-one ≈ 30–40 person-weeks; ATPCO/ARC licensing held as contingency | Low-Medium — assumption-heavy | Sized from the MVP-shortcut findings (published CE tables, archival event ledgers); revisit at G0 with actuals |
| P10 | Publication posture | Self-published research note + open repository through Phase 2; institutional partnership explored at Phase 3, not before; pre-committed correction protocol; no news-cycle timing | Medium-High | Independence during the methods-proving phase; the receptive moment (4.2% CPI, alternative-gauge appetite) raises the value of discipline, not of speed |
| P11 | Weights vintage | Pin to R-CPI-I recipe with data through Dec 2024; treat the Mar 2026 update as delayed/unconfirmed; footnote 2025 shutdown distortions on any 2025-vintage inputs | High | Verified: Oct 2025 CPI never published, CE Oct–Nov 2025 missing, 2025 CPI weights arrive Jan 2027 — pretending otherwise would import silent irregularities |
| P12 | Novelty claim wording | Claim the **procedure and the conditional-experience basket**, not the principle; cite EU Reg 2020/1148 ("changes in the conditions of a tariff shall be shown as price changes") as bounding prior art | High | The principle exists in EU law with no worked valuation procedure anywhere — precise wording preempts the "Eurostat already does this" rebuttal at the cost of one sentence |

---

## 9. Next steps (the immediate answer)

**This week (by July 13):**
1. **Archive the T-Mobile pre-migration state** — legacy plan menus, "(Retired)" plan support pages, the plan-to-plan crosswalk, Experience-tier pricing. The before-state disappears when migration starts on bill cycles July 13. This is the single most time-critical task in the project.
2. Stand up the snapshot pipeline v0 (timestamped, hash-committed) and point it at: rental listings (Zillow Total Price / Apartments.com fee fields, fixed unit sample), FCC broadband labels, streaming tier pages, all six carriers' bag-fee pages (B6 with its peak calendar).

**By July 31 (hard deadline):**
3. **File the DOT NPRM comment** (FR 2026-13294, full-fare advertising flexibility) — the posted all-in airfare is collection infrastructure for this project; say so in the docket.

**August:**
4. Ledger schema + codebook v0 (equivalence protocol, route hierarchy, trigger rules) — the pre-registration draft.
5. Pull bottom-two-quintile weights from BLS API / CE Table 1101 (retrieval paths verified this session); refresh the nine 2023-vintage detail cells; pull renter shares (CXUHOMEOWNLB0102M/0103M).
6. Re-quote all BLS factsheet language from an unblocked connection (byte-verification of the triangulated quotes).
7. Begin Phase 0: assemble 2008–09 archives (Wayback fee tables, DB1B, Form 41 acct 3906.2) and pre-state the G0 plausibility band.

**September–October:**
8. Complete the retrospective + one historical re-bundling negative print; publish as the pre-registration note; run gate G0.
9. Air-travel route panel live by October (so the 2026→2027 link year is fully in-sample); recruit the external methods discussant.

**Q1 2027:** first Restoration Gap print (air + streaming + controls), gated on G1.

---

## Appendix — spec open items closed by this pass

| Spec §13 item | Status |
|---|---|
| 3 — Verify T-Mobile event | **Closed**: confirmed with detail (no opt-out, ~1,100 codes retired, crosswalk published); upgraded to Phase 2 flagship; pre-event archival added as the most urgent task |
| 5 — R-CPI-I March 2026 vintage | **Closed**: not released as of 2026-07-04; latest is Dec 2024 data; delay structurally likely (shutdowns) — weights pinned accordingly |
| 6 — Eurostat/HICP unbundling rules | **Closed**: Reg 2020/1148 contains the principle (condition change = price change), no procedure; novelty claim reworded (P12) |
| 7 — Healthcare ruling + rental memo | **Closed**: healthcare OUT (§2.3, printable); rental memo superseded by full module ruling (§2.1) |

Items 1, 2, 4, 8 (NPRM comment, BLS re-quotes, CEX table refresh, incidence build-out) remain open and are scheduled in §9. Fold all closures into the spec at its next revision (v00.02.00).

---

## Changelog

- **v00.01.00** (2026-07-04 18-40) — Initial project plan. Reframed around the holistic goal: coverage map as spine (real CE Table 1101 quintile dollars), three-artifact product with the Exclusion Register first-class, capture-now-publish-later collection posture. Sector rulings: rental housing IN (Phase 2 flagship, panel starts immediately), telecom IN (T-Mobile 7/13/26 flagship, complementarity framing), healthcare OUT (printable ruling). April 2026 bag-fee wave fully verified (B6 needs calendar pricing); R-CPI-I pinned to Dec 2024 vintage; novelty claim reworded against EU Reg 2020/1148; competitor field verified clear. Phases 0–3 with gates G0–G3 and kill criteria; 12 plan-level decisions; 30/60/90 next steps led by the July 13 T-Mobile archival deadline. Built on a 5-agent verified research pass (rental housing, telecom, healthcare, CE budget shares, open items).
