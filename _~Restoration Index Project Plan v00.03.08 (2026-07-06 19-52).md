# Restoration Index — Project Plan

`v00.03.08 · 2026-07-06 19-52 · internal working doc · companion to: Restoration Index Spec v00.02.00`

---

## 0. The big picture, made operational

The product is not an airfare fee tracker. The end state is **a standing annual audit of what it costs a bottom-40% household to keep living last year's life** — the holistic consumer experience, sector by sector, with air travel serving as the methods lab it deserves to be and nothing more. The numbers force this framing: airline fares are **~0.5%** of a bottom-two-quintile budget; rent alone is **~14%** (Q1: 16.5% of all spending in 2024). A project that stayed in the airport would measure the sharpest case and miss the household.

The mature product (Phase 3 onward) ships **three artifacts** per release; Phase 1–2 releases ship artifacts 2 and 3 plus the coverage statement — **no composite until gate G3 passes**:

1. **The composite Restoration Gap** — covered-sector, bottom-40-weighted, decomposed into pricing-concept vs weighting effects, with zero-imputation for uncovered spend and the coverage numbers printed on the front page. *(Phase 3+.)*
2. **Sector gaps with the Inclusion Ledger** — every restoration event as an auditable line item (what was included, what it costs to get back, via which route). *(Every release.)*
3. **The Exclusion Register** — the census of *unpriced* degradation: counts and affected base expenditure for everything the scope rule keeps out (skimpflation, healthcare facility fees, subsidy lapses). This is how "holistic" survives the priced-restoration boundary: **what the index cannot price, it still counts.** The full story of the consumer experience = the Gap (priced) + the Register (unpriced), and the plan treats the Register as a first-class product, not a disclaimer. *(Every release.)*

**North-star metric — printed as two numbers in every release:**
- **(a) Restoration-priced coverage** (sectors the index actually prices): Phase 1 ≈ **2%** of bottom-40 expenditure (air + streaming) → Phase 2 ≈ **20%** (rent, wireless, internet, lodging enter) → Phase 3 ≈ **26%+**.
- **(b) Monitored coverage including null controls** (adds CPI-priced validation sectors like groceries, labeled as such and never counted as restoration coverage): ≈ 12% → ≈ 30% → ≈ 36%+.

The remainder is never hidden — it is priced at a zero gap in the composite and itemized in the coverage statement.

**One structural principle falls out of this research pass: capture now, publish later.** The archival record is the scarce asset, and it is newly rich but fragile: Zillow's Total Price display went live July 15, 2025; FCC broadband labels became machine-readable October 2024 but face a rollback FNPRM with a final rule expected 2H 2026; T-Mobile deletes ~1,100 legacy plan codes from its menu on **July 13, 2026**. Snapshot pipelines for *all* planned sectors therefore start in Sprint 0 — publication is phased, collection is not. Every month of delay costs baseline that cannot be reconstructed. (Sprint-0 capture is archival preservation and is exempt from the G0 spending gate — see §4.)

---

## 1. The coverage map (the plan's spine)

Bottom-two-quintile expenditures, BLS CE Table 1101 — 2024 vintage where available, 2023 detail otherwise (release USDL-25-1586, Dec 19, 2025; values cross-verified against two independent mirrors of BLS API/flat-file data). Q1 total: $35,046. Q2 total: $50,054. Expansion priority = budget weight × restoration-test fit — never fee salience.

*Table caveats (fix scheduled in §9 item 7): asterisked cells are 2023 vintage and their shares are computed on 2023 quintile totals (Q1 ≈ $33.8k), not the 2024 header totals; rows partially overlap CE's published hierarchy (CE classes telephone services under utilities and pay-TV under entertainment — the connectivity row is a cross-cutting regrouping), so rows are not additive. The exact non-overlapping map ships with the August Table 1101 refresh.*

| Sector | Q1 $/yr (share) | Q2 $/yr (share) | Restoration-test fit | Disposition |
|---|---|---|---|---|
| Shelter — rented dwellings | 5,781 (16.5%) | 6,225 (12.4%) | **Strong**: named mandatory fees (valet trash $25–50/mo, package/tech fees, convenience fees, month-to-month premiums 5–20%), posting now forced by law and litigation | **Phase 2 flagship**; forward panel starts Sprint 0 |
| Food at home | 3,843 (11.0%) | 4,952 (9.9%) | Weak by design — CPI per-unit capture works | **Phase 1 null control** (CPI-priced; never counted as restoration coverage) |
| Healthcare | 3,445 (9.8%) | 4,826 (9.6%) | **Fails** (see §2.3) | **Out** — Exclusion Register with magnitudes |
| Utilities | 2,941 (8.7%)* | 3,987 (8.2%)* | Weak: regulated tariffs, few contractible inclusions | Out for now; revisit trigger: fixed-charge unbundling adopted in ≥3 large-state tariffs, or the Phase 3 scope memo, whichever comes first |
| Transportation (all) | 5,105 (14.6%) | 8,430 (16.8%) | Mostly weak (vehicles, gasoline = commodities) | Out, except air travel below |
| — Airline fares | 167 (0.5%)* | 274 (0.6%)* | **Strongest** (verified events, paired menus) | **Phase 1 methods lab** |
| Connectivity + subscription media (cellular + internet + pay-TV/streaming) | ≈1,540 (4.5%)* | ≈2,220 (4.4%)* | **Strong**: tier deltas, ad-free spreads, extra-member fees, forced migrations, equipment fees; menus national and archived | **Phase 1** (streaming sidecar) + **Phase 2** (wireless + internet, T-Mobile flagship); broadband labels captured from Sprint 0 |
| Food away from home / delivery | 1,655 (4.7%) | 2,448 (4.9%) | Medium: priced service/delivery fees, but baselines ambiguous (delivery was never free) | Phase 3 candidate; scope memo required |
| Entertainment fees & admissions | 168 (0.5%)* | 339 (0.7%)* | Medium-strong: ticketing fees now FTC-disclosed all-in | Phase 3 candidate |
| Lodging on out-of-town trips | 166 (0.5%)* | 338 (0.7%)* | Strong post-5/12/25 (FTC all-in display); broken series backward | **Phase 2** (with the compression falsification test) |
| Banking fees | n/a (fee, not a CEX expenditure line — excluded from coverage denominators) | n/a | Strong, and *falling* | **Phase 1 negative control** |
| Apparel, personal care, education | 1,124 / 427 / 828 | 1,328 / 659 / 407 | Poor (no priced restoration grammar) | Exclusion Register |
| **All other expenditure** — owned-dwelling shelter (~47% of Q1 households own; $2,989 + other lodging $409 in 2024), household operations/supplies/furnishings, personal insurance & pensions, cash contributions, alcohol/tobacco, miscellaneous | ≈8,000 (≈23%) — components pending the Table 1101 refresh | ≈— | Not consumption-menu priced (owned shelter, insurance/pensions) or no restoration grammar | **Zero-imputed in the composite, itemized in every coverage statement** — the remainder is disclosed, never dropped |

\* 2023 vintage (see table caveats). Education shows the classic Q1 > Q2 anomaly (students with low current income) — one more reason weights follow the R-CPI-I equivalized-income recipe rather than raw CE income ranks.

---

## 2. Sector rulings from this research pass

### 2.1 Rental housing — IN, Phase 2 flagship; collection starts now

**Facts (web-verified).** CPI Rent of Primary Residence prices *contract rent* — all services the landlord provides in exchange for rent — and quality-adjusts for utility bundling changes and extra charges like pet fees. But one-time fees (application $50 typical, paid by 79% of recent renters; admin; move-in) have no home in the rent index, and separately billed mandatory recurring fees (valet trash, tech/package fees, RUBS utility billing, payment "convenience" fees) enter only if respondents report them as rent; the 6-month continuing-tenant panel structurally underweights fees loaded at new-lease events. The fee stack is litigated and large: FTC v. Invitation Homes ($48M, fees up to ~$1,700/yr on top of advertised rent), FTC & Colorado v. Greystar ($24M, Dec 2025, "hundreds of dollars more per month" — package delivery, trash, technology packages). Posting is being forced onto the menu: Zillow Cost of Renting Summary (2023) → Total Price display (July 15, 2025); Minnesota Total Monthly Payment law (2024); Colorado HB25-1090 (Jan 1, 2026); FTC rental-fee ANPRM (Mar 13, 2026 — comments closed Apr 13; no NPRM yet). ~53% of bottom-quintile households rent; 83% of <$30k renters are cost-burdened with median residual income of $250/month.

**Module design (decision P5).** Target concept: **advertised-rent-plus-mandatory-fees** — this avoids double-counting against CPI's contract-rent concept and measures exactly the drip wedge. Components: the recurring mandatory-fee stack needed to reproduce last year's tenancy (trash service on the old basis, parking, fee-free payment, lease-term parity), plus amortized one-time fees at a forced re-search event. Always-separate fees (pet) and unpriced degradation route to the Register. A **posted-vs-realized audit** (paired secret-shopper applications vs listed fees) is mandatory, because fees were historically revealed at application, not in listings — the audit is budgeted, counsel-reviewed, and piloted in Q4 2026 so at least two waves land inside the Phase 2 panel year (§9 item 8; legal exposure logged in WS-G and §6). Backcasting before ~2023 leans on enforcement exhibits (Invitation Homes/Greystar complaints carry dated fee schedules), the FTC-2026-0266 docket corpus, and archived listings.

**Implication.** The forward panel (Zillow Total Price + Apartments.com fee fields, fixed unit sample stratified by market and building class, monthly, hash-committed snapshots) starts in Sprint 0 even though publication is Phase 2. First fully in-sample 12-month rent link: **mid-2027**; the rent flagship release lands **H2 2027**.

### 2.2 Telecom — IN, Phase 2; T-Mobile July 13, 2026 is the flagship event

**Facts (web-verified).** T-Mobile force-migrates 8M+ customers on Simple Choice/ONE/Magenta/legacy-Sprint plans to "Experience" tiers on bill cycles starting **July 13, 2026** — average +$4/line (voice +$6, watch/tablet +$3, 5G Home Internet +$6), **no opt-out** ("There's no going back to the old plans" — T-Mobile CMO), ~1,100 plan codes retired, 62+ migration-target codes, with a published plan-to-plan crosswalk. It is the third legacy repricing in 26 months (May 2024 +$2–5, April 2025 +$5) and erodes the "Un-contract"/Price Lock promises now in class-action litigation. AT&T's April 2026 legacy increases explicitly paired hikes with hotspot-data adds — the compensating-quality maneuver hedonic adjustment rewards and the Restoration Index correctly ignores (extra hotspot is irrelevant if absent from the frozen baseline).

**The honest CPI framing (decision P6).** Telecom is where CPI has the *most* quality machinery: since July 2025, CPI wireless is built from vendor-scraped near-universe *advertised* plan menus under expenditure-weighted full-menu hedonic regressions. Grandfathered rates are not advertised offers — so the migration's bill impact largely falls **outside CPI's measurand**, not inside it mismeasured. The module therefore claims **complementarity, not correction**: CPI answers constant-quality offer inflation; the Restoration Index answers what it costs 8M households to keep last year's bill. Module design: freeze per-carrier plan-feature vectors from archived menus and carriers' own "(Retired)" plan support pages; restoration price = cheapest same-carrier current-menu plan weakly dominating the frozen vector (superset-flagged — these are supersets by construction); cross-carrier/MVNO as sensitivity. ACP's June 2024 end is a subsidy lapse, not firm unbundling → Exclusion Register with magnitude ($30/mo), since ACP households concentrate in the target population. **Link-year assignment:** the codebook states the link convention before collection, and the 7/13/26 event is pre-registered to exactly one link — an event nine days into H2 sits on the seam of two annual links and must not be double- or zero-counted.

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
- **Comparator continuity (new, consequence of the shutdowns):** the Gap differences RX against official CPI 12-month item relatives — but **October 2025 CPI was never published**, so every 12-month comparator spanning that month is non-standard. The codebook adopts and pre-registers a convention (BLS's own published bridge treatment where available; otherwise 11-month annualized bridge, flagged) for all first-print comparators. Likewise, control reconciliations reference the vintages *available at print time* (see gate G1) with full reconciliation published as an addendum when covering vintages ship.
- **Novelty claim, precisely worded:** EU Implementing Regulation 2020/1148 already mandates that changes in a tariff's *conditions* count as **price** change in the HICP — the principle exists in EU law. No agency anywhere publishes a worked *procedure* for pricing an unbundling transition. The project's contribution is **the procedure and the conditional-experience basket, not the principle** — cite 2020/1148 as bounding prior art.
- **Competitor scan:** no restoration-style index launched Jan–Jul 2026. Environment note: May 2026 CPI is running 4.2% y/y post-fuel-shock and the Fed chair is publicly courting alternative price measures — a receptivity tailwind that the positioning discipline (§6, P10) deliberately does not chase.

---

## 3. Workstreams (continuous; cut across phases)

| WS | Scope | Standing outputs |
|---|---|---|
| A — Methodology | Codebook: equivalence protocol, route hierarchy, trigger rules, link-year convention, comparator-continuity convention, event-registry schema; drift diagnostics; Assumption Q | Pre-registration; versioned codebook |
| B — Collection infrastructure | Menu snapshot pipeline (scrapers + manual capture), hash-committed timestamped archive, per-sector collectors | The archive; collection-risk log |
| C — Weights & population | CE quintile tables → PUMD R-CPI-I replication; annual refresh; incidence proxies per sector | Weight vintages with shutdown footnotes |
| D — Sector modules | Ledger + collector + event registry + gap calculation + write-up per sector (template = air travel) | Sector Gap series |
| E — Validation | Phase 0 retrospective; reconciliation vs CPI-U / C-CPI-U / R-CPI-SC / R-CPI-I (vintage-aware); negative controls; falsification tests (lodging post-FTC compression) | Reconciliation table each release |
| F — Publication & review | External methods discussant (shortlist owned here); versioned publication with DOI (Zenodo or SSRN) + public code repository + snapshot archive under documented access rules; release template with bound language and limitations; correction protocol | Releases; correction log |
| G — Legal & data rights | Scraping counsel covering **capture and redistribution** (access-on-request tier where ToS bars public release; WN = manual capture only); mystery-shopping legal review (rental audit: application-fee spend, misrepresentation/FCRA/state landlord-tenant exposure); ATPCO/ARC licensing decision; regulatory comments; continuity plan | Legal register |
| H — Funding & operations | Budget and payer for: counsel hours, discussant honorarium, application-fee spend for the rental audit, scraper infrastructure, ATPCO/ARC contingency; first budget memo due **August 2026** | Budget; runway statement |
| I — Public site & brand | The public-facing artifact, scaffolded from day one (`site/` in the repo: home, releases/Gap hub, coverage, Inclusion Ledger, Exclusion Register, methods, about — placeholders labeled, verified events seeded); name finalization (P13), domain (P14), hosting via Cloudflare Pages connected to the GitHub repo (P15); the site is the release vehicle from the Phase 0 note onward | The live site; brand decision record; Appendix C deployment prompt |

---

## 4. Phase plan, gates, and kill criteria

**Sprint 0 — preservation and posture (July 2026, ~3 person-weeks).**
Time-critical captures: T-Mobile pre-migration menus/crosswalk/retired-plan pages (**before Jul 13**); FCC broadband labels (machine-readable while they last); rental listing-fee panel v0 (Zillow Total Price + Apartments.com fields); streaming tier pages; all carrier bag-fee pages incl. B6 peak calendars. File the DOT NPRM comment (**due Jul 31**). Ledger schema + codebook v0. CEX weight pull via BLS API / verified mirrors. BLS factsheet re-quotes from an unblocked connection. *Sprint-0 capture is archival preservation, exempt from the G0 gate.*

**Phase 0 — retrospective validation (Aug–Oct 2026, ~8–10 pw).**
Hash-commit the G0 plausibility band **before** assembling any retrospective results. Reconstruct the 2008–09 checked-bag unbundling (archived fee tables, DB1B, Form 41 acct 3906.2); publish the Gap the method *would have printed*, reconciled against the PPI's 1.6% correction and Brueckner's fee-minus-offset wedge. Find and price one historical re-bundling episode (negative print). Doubles as the public pre-registration.
**Gate G0:** retrospective lands within the pre-committed band. **Kill criterion:** no *publication* and no per-sector module build-out beyond preservation snapshots until G0 passes; any Phase 1 work started before G0 is labeled at-risk spend and capped at ≤4 pw. If the method cannot reproduce a documented historical event, stop and revise the primitive.

**Phase 1 — MVP and first print (Sep 2026 – Q1 2027, ~16–24 pw; start conditional on G0 trajectory, panel pre-registration frozen only after G0 passes).**
Air travel + streaming sidecar + groceries and banking controls. Weights from published CE quintile tables; incidence via BTS proxy or published utilization bounds — never bare assumption shares. **Denominator convention (pre-registered; wording corrected v00.03.08 to match the binding December-to-December link convention — codebook §6):** the live paired-quote panel goes live October 2026 and attains 12 months of coverage in October 2027 (a coverage milestone); its first fully in-sample annual link is **the 2027 link (Dec 2026 → Dec 2027), measured from the December 2027 wave**. The Q1 2027 print is an **archival-denominator exhibit** — fee-schedule event relatives priced against DB1B/DB1C route-average base fares as scalar denominators under the per-event single-product rule (DB1B covers pre-July-2025 windows, incl. the Southwest 2025-link event; DB1C/OD40 after; product printed as a column), labeled a convention, with sensitivity bands — plus the fully-archival streaming series (posted national prices make streaming's 2025→2026 link exact). External discussant review **before** publication.
**Gate G1 (tests GA–GD, pass criteria pre-committed in `docs/g1-band.md`):** GA discussant sign-offs (≥1 sympathetic-methods + ≥1 critical-prior, no bypass); GB grocery null — the archival GAO reconciliation gates the Q1 2027 print, the in-sample two-part band binds from the 2027 link (full R-CPI-SC reconciliation as an addendum when the covering vintage is released); GC banking strictly negative (sign only); GD independent rerun from archived snapshots with disclosure parity. First public release: **target Q1 2027**, labeled for what it is (archival-denominator air exhibit + exact streaming link + controls).

**Phase 2 — the holistic turn (2027; rent flagship release H2 2027; ~30–40 pw).**
Rent module (panel 12+ months deep by mid-2027; posted-vs-realized audit waves from Q4 2026) + telecom (T-Mobile event assigned to its pre-registered link) + lodging (post-FTC compression test as a falsification exhibit). Healthcare ruling published in the release. PUMD-based weights with standard errors. A **scheduled Phase 2 external review (H1 2027**, discussant or successor) covers the expanded methods.
**Gate G2:** restoration-priced coverage ≥ **25%** of bottom-40 spend; per-sector independent rerun by a named third party; the H1 2027 review closes with zero open objections in the correction log.

**Phase 3 — composite (2028).**
Covered-sector composite Gap with zero-imputation and printed coverage numbers; annual cadence locked to CE releases; small incidence survey; food-away/delivery and ticketing scope memos; institutional-partnership decision.
**Gate G3:** second external review round before any composite headline.

---

## 5. Resourcing (Assumptions — labeled)

Core team of two (one economics/methods, one data engineering), counsel hours for scraping/ToS and mystery-shopping review, discussant honorarium, rental-audit application-fee budget. Year-one load ≈ 30–40 person-weeks — feasible for two people at substantial part-time. Recurring cost center is scraper maintenance; storage is trivial. Contingency: ATPCO/ARC licensing (unquoted — WS-G obtains quotes in Phase 1) if scraping proves too brittle for production. **Dollars and payer are unresolved — WS-H's August budget memo is the forcing function.** These are planning assumptions, not estimates from experience with this exact stack.

---

## 6. Project-level risk register (beyond the spec's §9 methods hazards)

| Risk | Handling |
|---|---|
| Airfare capture — the methods lab becomes the product | Coverage map is the spine (§1); north-star is the two coverage numbers; airfare's 0.5% weight printed in every release |
| Method fails the retrospective | G0 kill criterion — no publication or module build-out beyond preservation snapshots until the primitive reproduces 2008–09; pre-G0 Phase 1 work capped as at-risk spend |
| Baseline evaporation (menus deleted, labels rolled back, listings churn) | Capture-now-publish-later (P3); Sprint 0 snapshots for all planned sectors; hash-committed archive |
| Data continuity — DOT relaxes posted all-in fares; FCC label rollback; scraper blocks; WN legal exposure | NPRM comment (Jul 31); label capture now; fixed pre-registered panels; manual capture for WN; ATPCO/ARC fallback |
| First-print overreach — printing a 2025→2026 air link the panel never observed | Pre-registered archival-denominator convention, sensitivity bands, and explicit labeling (§4 Phase 1); the first *fully in-sample* air link is Oct 2027 and the releases say so |
| Legal/ethical exposure of the rental posted-vs-realized audit | Counsel review before any application is filed; protocol designed to avoid misrepresentation (e.g., disclosed-tester or document-based designs where required); budgeted in WS-H |
| Data-republication rights — reproducibility promise vs platform ToS | WS-G covers redistribution; access-on-request tier where public release is barred; reproducibility defined against the documented access rules |
| Credibility sequencing — publishing before review | G1 hard-gates the first print behind the discussant; scheduled H1 2027 review before the Phase 2 flagship; correction protocol pre-committed |
| Political capture — the number gets mislabeled "true inflation" in discourse | Bound language in every artifact; no "true inflation" claims ever; standing reconciliation table; the receptive macro moment (4.2% CPI, alternative-gauge appetite) is explicitly *not* chased |
| Funding gap | WS-H August budget memo names dollars and payer before Phase 0 spend commits |
| Solo-author / bus-factor risk | Open code and data from Phase 0; the pre-registration and codebook make the method executable by others |
| Competitor emerges | Field verified clear as of 2026-07-04; scan repeated each phase; first-mover advantage compounds through the archive (uncopyable backfile) |

---

## 7. Success metrics and falsification commitments

- **Coverage (two numbers, §0):** restoration-priced ≈2% → ≥25% (G2 threshold) → ≈26%+; monitored-including-controls ≈12% → ≈30% → ≈36%+. Both printed every release; controls never counted as restoration coverage.
- **Validation:** Phase 0 retrospective within the pre-committed, hash-timestamped band; groceries null ≈ 0 vs the comparator available at print time (R-CPI-SC addendum when its vintage ships); banking prints negative; lodging Gap compresses after May 12, 2025 (if the seam is real, the FTC rule should shrink it — a prediction that can fail in public).
- **Reproducibility:** every published number re-derivable by a third party from the snapshot archive and open code **under the documented access rules** (public where rights allow; access-on-request where ToS bars redistribution).
- **Review:** external discussant sign-off before first print; scheduled H1 2027 review before the Phase 2 flagship; second full round before the composite.
- **Honesty exhibits in print:** the Southwest case (CPI captures most of it; Gap small), the archival-denominator labeling of the first air print, and the telecom complementarity framing appear in the releases that cover them.

---

## 8. Decisions

**Status: rows P1–P15 adopted by owner, 2026-07-04** (P1–P12 per plan review; P13–P15 per naming/domain confirmation — public brand is **The Restoration Gap**, domain restorationgap.org). (Spec decisions 1–14 stand; these are plan-level.)

| # | Question | Recommendation | Confidence | Rationale |
|---|---|---|---|---|
| P1 | Prime directive | The holistic coverage map (§1) is the plan's spine; airfare is the methods lab, labeled as such (0.5% of the B40 budget) in every release | High | The verified budget shares make the ordering unambiguous; this is the structural answer to "don't lose the big picture" |
| P2 | Product definition | Three artifacts at maturity: composite Gap (Phase 3+, behind G3) + sector gaps/Inclusion Ledger + Exclusion Register (every release), with the Register treated as a first-class product | High | The Register is how the holistic goal survives the priced-restoration boundary; phasing the composite keeps the product promise consistent with the gates |
| P3 | Collection posture | **Capture now, publish later**: Sprint 0 starts hash-committed snapshot pipelines for all planned sectors regardless of publication phase; preservation capture is exempt from the G0 spending gate | High | Zillow Total Price (7/15/25), FCC labels (rollback expected 2H 2026), T-Mobile menu deletion (7/13/26) — the baseline is fragile and unreconstructible; the archive becomes the project's uncopyable asset |
| P4 | Phase sequence | Sprint 0 (Jul '26) → Phase 0 + pre-registration (Aug–Oct '26, gate G0 with band committed in advance) → Phase 1 first print: archival-denominator air exhibit + exact streaming link + controls (target Q1 '27, gate G1) → Phase 2: rent (H2 '27 flagship) + telecom + lodging, H1 '27 external review (gate G2: restoration-priced coverage ≥25%) → Phase 3 composite ('28, gate G3) | Medium-High | Sequenced by validation-before-collection-before-coverage, with the panel's actual in-sample windows (first fully in-sample air link Oct '27; rent link mid-'27) stated rather than assumed |
| P5 | Rent module | Enter Phase 2 as flagship; target concept = advertised-rent-plus-mandatory-fees; recurring fee stack + amortized one-time fees at forced re-search; posted-vs-realized audit budgeted, counsel-reviewed, piloted Q4 2026; forward panel from Sprint 0 | High (entry), Medium (design details) | Passes the restoration test better than any sector except air; largest B40 budget item; law/litigation now force fee posting; the audit answers the posted-vs-revealed hazard the NCLC record documents |
| P6 | Telecom module | Enter Phase 2 with T-Mobile 7/13/26 as flagship superset event, pre-registered to exactly one link year; same-carrier dominance replication, cross-carrier sensitivity; frame vs CPI as **complementarity, not correction** | High | Cleanest menu-removal event available (no opt-out, published crosswalk, 8M+ households); the measurand distinction is what survives BLS scrutiny in the sector where BLS has the most tooling |
| P7 | Healthcare | Out of the restoration ledger; facility fees and coverage erosion logged in the Exclusion Register with magnitudes; revisit trigger = a menu-posted slice matures | High | Fails the menu condition (facility fees) and the contractibility condition (actuarial tiers); no commensurable CPI stratum exists (retained-earnings method), so the Gap is undefined; Milliman MMI already occupies constant-coverage |
| P8 | Gates & kill criteria | As specified in §4: G0 band pre-committed and hash-timestamped; G0 kill = no publication or module build-out beyond preservation snapshots (at-risk cap ≤4 pw); G1/G2/G3 hard-gate publication behind scheduled external review | High | The retrospective is the cheapest possible test of the whole premise; a gate whose band is set after the result, or that the schedule instructs the team to violate, is theater |
| P9 | Resourcing envelope | Two-person core + counsel + discussant + audit budget; year-one ≈ 30–40 person-weeks; ATPCO/ARC held as contingency; WS-H budget memo (dollars and payer) due August | Low-Medium — assumption-heavy | Sized from the MVP-shortcut findings; the August memo converts assumptions to commitments; revisit at G0 with actuals |
| P10 | Publication posture | Publish = versioned research note with DOI (Zenodo or SSRN) + public code repository + snapshot archive under documented access rules; self-published through Phase 2; institutional partnership explored at Phase 3, not before; pre-committed correction protocol; no news-cycle timing | Medium-High | Independence during the methods-proving phase; "publish" now has an operational definition; the receptive moment (4.2% CPI, alternative-gauge appetite) raises the value of discipline, not of speed |
| P11 | Weights & comparator vintages | Pin weights to the R-CPI-I recipe with data through Dec 2024; treat the Mar 2026 update as delayed/unconfirmed; pre-register the comparator-continuity convention for CPI relatives spanning the never-published Oct 2025 index; footnote 2025 shutdown distortions on any 2025-vintage inputs | High | Verified: Oct 2025 CPI never published, CE Oct–Nov 2025 missing, 2025 CPI weights arrive Jan 2027 — both the weights *and the Gap's comparator* inherit the hole, and pretending otherwise would import silent irregularities |
| P12 | Novelty claim wording | Claim the **procedure and the conditional-experience basket**, not the principle; cite EU Reg 2020/1148 ("changes in the conditions of a tariff shall be shown as price changes") as bounding prior art | High | The principle exists in EU law with no worked valuation procedure anywhere — precise wording preempts the "Eurostat already does this" rebuttal at the cost of one sentence |
| P13 | Public name | **"The Restoration Gap"** as the public brand and site name; "Restoration Index (RX)" stays the formal measure name; **retire "Better Price Index / BPI" for public use** (repo codename `bpi` can stay) | High on retiring BPI; Medium-High on the replacement | Collision scan verdict: BPI is **blocked** — Bank Policy Institute (bpi.com, publishes economic research in exactly this space), Bullish Percent Index, ESPN Basketball Power Index, British Phonographic Industry, Building Performance Institute (bpi.org, active), and "Better ___ Index" reads as the OECD Better Life Index family; "Better" is also a superiority claim the methodology explicitly disclaims (spec row 14). "Restoration Gap" scanned **clear** in the economics/consumer space (only benign dentistry/ecology usage), names the shipped product (the Gap *is* the headline series per Knob 3), is provocative in substance (something was taken; here's the bill to get it back) while neutral in register, and is journalist-quotable ("the restoration gap widened to…"). Runner-up if overruled: "Fine Print Index" (clear scan, but reads fees-only — narrower than the tiering/menu-redesign scope) |
| P14 | Domain | **restorationgap.org** primary (research register; .org signals non-commercial measurement) — **registered and LIVE (2026-07-06)**. The defensive **.com is SHELVED by owner decision (2026-07-06)** — revisit if the project gains public traction | High — the .org is operating; the .com is a cheap, reversible option whose case strengthens only with visibility | .org is the right register for a methods-first research artifact; the confusing-neighbor risk the .com would hedge is proportional to traffic the site does not yet have, so deferral costs nothing now and stays available (barring squatting, the accepted residual risk) |
| P15 | Hosting architecture | Cloudflare Pages connected to the GitHub repo (`arthurculang/bpi`), build command none, output directory `site/`, production branch `main` (after merging the working branch); Cloudflare Registrar for the domain so DNS, registrar, and hosting live in one account | High | Static HTML with zero build step is the most durable, auditable, and cheapest option (free tier); the site deploys on every push, which makes the repo the single source of truth; matches the user's Cloudflare + GitHub setup |

---

## 9. Next steps (the immediate answer)

**Execution status (2026-07-06):** items 3–4 **DONE** — name + tagline adopted; `main` synced (PR #2) with G0 PASS, the T-Mobile captures, and the tagline site; and **the site is LIVE at https://restorationgap.org** (Cloudflare Pages off `main`, output dir `site`, valid cert; `www.restorationgap.org` 301-redirects to the apex with path/query preserved; Git integration reconnected — the Cloudflare Workers-and-Pages GitHub App was scoped to only `yamorseal` and now includes `arthurculang/bpi`, so pushes to `main` auto-deploy; homepage hero/title/OG copy aligned to the canonical "keep" tagline). The `.com` was **not** registered (deferred; optional defensive buy per P14, 301→.org when done); item 5 drafted (`docs/dot-nprm-comment-draft.md` — review and file); item 6 substantially drafted (`docs/codebook-v0.md`); item 7 partially done (major categories byte-verified in `data/cex-b40-quintiles.csv` + reproducible builder; detail cells and renter shares still need unblocked BLS/FRED access); item 8 drafted (`docs/ws-h-budget-memo-draft.md`, `docs/discussant-shortlist.md` with first-approach trio); item 9 partially done (incidence proxy register `data/incidence-proxies.md`; carry-on incidence flagged as a gap); item 11's band **already hash-committed** (`docs/g0-plausibility-band.md`, commit 57581d6, before any retrospective inputs) and the 2008–09 chronology inputs compiled (`data/retro-2008-inputs.md`, negative-print episode designated: US Airways beverage-fee repeal, 2009-03-01). Items 1–2 (captures) and the NPRM filing remain owner actions — the sandbox proxy blocks the target hosts.

**This week (by July 13):**
1. **Archive the T-Mobile pre-migration state** — legacy plan menus, "(Retired)" plan support pages, the plan-to-plan crosswalk, Experience-tier pricing. The before-state disappears when migration starts on bill cycles July 13. This is the single most time-critical task in the project.
2. Stand up the snapshot pipeline v0 (timestamped, hash-committed) and point it at: rental listings (Zillow Total Price / Apartments.com fee fields, fixed unit sample), FCC broadband labels, streaming tier pages, all six carriers' bag-fee pages (B6 with its peak calendar).
3. **Close the naming decision (P13) and domain (P14)** — "go" on the rows or overrule; site scaffold is live in `site/` and rebrands with a find-and-replace either way.
4. ~~**Register the domain and deploy the site**~~ **DONE (2026-07-06)** — restorationgap.org is registered and the site is live on Cloudflare Pages off `main` (output `site/`), with `www`→apex 301 and an auto-deploying Git pipeline. Executed via Claude-for-Chrome with a stop-on-error / idempotent-state-check instrument; the only snag was the Cloudflare GitHub App's repo scope (fixed by granting it `arthurculang/bpi`). Remaining optional: register `.com` defensively and 301 it to `.org`.

**By July 31 (hard deadline):**
5. **File the DOT NPRM comment** (FR 2026-13294, full-fare advertising flexibility) — the posted all-in airfare is collection infrastructure for this project; say so in the docket.

**August:**
6. Ledger schema + codebook v0 (equivalence protocol, route hierarchy, trigger rules, link-year convention, comparator-continuity convention) — the pre-registration draft.
7. Pull bottom-two-quintile weights from BLS API / CE Table 1101 (retrieval paths verified this session); refresh the nine 2023-vintage detail cells; build the non-overlapping coverage map; pull renter shares (CXUHOMEOWNLB0102M/0103M).
8. **WS-H budget memo** (dollars, payer, honorarium, audit application-fee budget, infra, domain/site costs); **shortlist and approach three discussant candidates** (owner: WS-F); design the rental posted-vs-realized audit protocol and obtain counsel review (mystery-shopping exposure) so a pilot wave can run Q4 2026.
9. Build air-travel incidence proxies (BTS Form 41 acct 3906.2 ÷ T-100 enplanements); the first print uses proxy weights or published utilization bounds — never the spec §4.1 assumption shares.
10. Re-quote all BLS factsheet language from an unblocked connection (byte-verification of the triangulated quotes).
11. Begin Phase 0: **hash-commit the G0 plausibility band first**, then assemble the 2008–09 archives (Wayback fee tables, DB1B, Form 41 acct 3906.2).

**September–October:**
12. Complete the retrospective + one historical re-bundling negative print; publish as the pre-registration note **on the site**; run gate G0.
13. Air-travel route panel live by October. (The panel's first fully in-sample annual link is **the 2027 link, Dec 2026 → Dec 2027, measured from the December 2027 wave** — 12 months of coverage attained October 2027; the Q1 2027 print is the archival-denominator exhibit under the pre-registered convention in §4, plus the exact streaming link.) ~~Freeze panel pre-registration only after G0 passes.~~ **G0 passed 2026-07-04; the pre-registration is DRAFTED and committed (2026-07-06): `docs/phase1-preregistration.md` + `docs/g1-band.md` (pass criteria GA–GD, committed first per the band-before-inputs ordering) + `data/phase1-inputs.md` + `pipeline/select_routes.py` (the frozen 18-route formula, pinned by `engine/test_select_routes.py`) + `pipeline/wave-prompts.md`. Binding on owner sign-off (checkboxes in the band and pre-registration files); wave 0 dry run Sept 2026; wave 1 = 2026-10-06. Owner-action queue before wave 0: T-100 CY2024 pull + SHA-256, DB1C product-name byte-verification, CE Table 1101 detail cells, FDIC SoD pull, WS-G counsel review of the fare-search carve-out + WN manual protocol, discussant outreach (Aug). Sandbox build queue before wave 0: the wave-worksheet generator + the Step-4 ingestion validator (pre-registration §6 Step 0).**

**Q1 2027:** first Restoration Gap print (archival-denominator air exhibit + streaming + controls), gated on G1.

---

## Appendix A — spec open items closed by this pass

| Spec §13 item | Status |
|---|---|
| 3 — Verify T-Mobile event | **Closed**: confirmed with detail (no opt-out, ~1,100 codes retired, crosswalk published); upgraded to Phase 2 flagship; pre-event archival added as the most urgent task |
| 5 — R-CPI-I March 2026 vintage | **Closed**: not released as of 2026-07-04; latest is Dec 2024 data; delay structurally likely (shutdowns) — weights pinned accordingly, and the comparator-continuity convention (P11) added for the Oct 2025 CPI hole |
| 6 — Eurostat/HICP unbundling rules | **Closed**: Reg 2020/1148 contains the principle (condition change = price change), no procedure; novelty claim reworded (P12) |
| 7 — Healthcare ruling + rental memo | **Closed**: healthcare OUT (§2.3, printable); rental memo superseded by full module ruling (§2.1) |

Items 1, 2, 4, 8 (NPRM comment, BLS re-quotes, CEX table refresh, incidence build-out) remain open and are scheduled in §9. Fold all closures into the spec at its next revision (v00.02.00).

## Appendix B — adversarial review disposition (v00.01.00 → v00.02.00)

An independent adversarial review of plan v00.01.00 returned 10 findings (3 blockers, 6 serious, 1 minor). All were accepted and applied: F1 first-print denominator convention + corrected in-sample dates (§4, §9); F2 phase-conditional product definition (§0, P2); F3 kill-criterion rewording with preservation exemption and at-risk cap (§0, §4, P3, P8); F4 comparator-continuity convention + vintage-aware G1 (§2.4, P11, §4); F5 coverage-map residual row, entertainment share corrected 0.6%→0.5%, mixed-vintage disclosure (§1); F6 two-number north star separating restoration-priced from monitored coverage (§0, §7); F7 WS-H funding, publish operationalized with DOI, discussant shortlist moved to August, redistribution rights in WS-G (§3, §9, P10); F8 rental audit budgeted/counsel-reviewed/piloted Q4 2026 (§2.1, §6, §9); F9 G2 made concrete (≥25%, named rerun, scheduled H1 2027 review), rent flagship H2 2027, T-Mobile link pre-registration (§4, §2.2); F10 incidence proxies scheduled, G0 band hash-committed before results, utilities revisit trigger (§9, §4, §1).

---

## Appendix C — Cloudflare deployment prompt (run after "go" on P13–P15)

Paste the following into Claude for Chrome while logged into the Cloudflare dashboard. It is written to stop at every irreversible step. Prerequisite met 2026-07-05: PR #2 merged the working branch to `main`, so `main` now contains `/site` (with the tagline) — the production branch is `main` with no fallback, and step 7 checks the tagline to confirm the latest build shipped.

```
You are operating my Cloudflare dashboard (dash.cloudflare.com — I am already
logged in). Task: register a domain and deploy a static site from my GitHub
repo. Work step by step, confirm each numbered step's success before moving to
the next, and STOP and report if anything deviates from what's described.

CONTEXT
- Domain to register: restorationgap.org (primary). Also register
  restorationgap.com ONLY if it costs ≤ $15/yr.
- GitHub repo: arthurculang/bpi. The site is plain static HTML in the /site
  directory. There is NO build step.
- Production branch: main (it already contains /site).

STEPS
1. REGISTER: Go to Domain Registration → Register Domains. Search
   "restorationgap.org". If it is NOT available, STOP and report what you
   found (including any suggested alternatives and their prices) — do not buy
   anything else. If available and ≤ $15/yr, register it for 1 year with
   auto-renew ON and WHOIS redaction/privacy ON (the default), using my
   existing payment method. Do NOT buy any add-ons or upsells.
2. Repeat for restorationgap.com under the same ≤ $15/yr cap. If it is taken
   or over the cap, skip it and note that — do not substitute another TLD.
3. PAGES PROJECT: Go to Workers & Pages → Create application → Pages →
   Connect to Git. Authorize GitHub if prompted (I will complete the OAuth
   popup — pause and ask me when it appears). Select the repository
   arthurculang/bpi.
4. CONFIGURE: project name "restorationgap"; production branch main;
   Framework preset: None; Build command: (leave empty); Build output
   directory: site. Save and deploy. Wait for the first deployment to finish,
   then open the *.pages.dev preview URL and confirm it renders a page titled
   "The Restoration Gap".
5. CUSTOM DOMAIN: In the Pages project → Custom domains → add
   restorationgap.org. Accept the DNS records Cloudflare proposes (it manages
   the zone, so this should be automatic). Then add www.restorationgap.org
   the same way.
6. REDIRECTS: Ensure www redirects to the apex. If Cloudflare did not create
   this automatically, add a Redirect Rule (or Bulk Redirect):
   https://www.restorationgap.org/* → https://restorationgap.org/$1, status
   301. If restorationgap.com was registered, add its zone the same way and
   301-redirect https://restorationgap.com/* and www.* to
   https://restorationgap.org/$1.
7. VERIFY: Load https://restorationgap.org in a new tab. Confirm ALL of:
   (a) the page renders with a valid certificate — no browser warnings;
   (b) the header reads "The Restoration Gap";
   (c) the tagline "what it costs to keep last year's life" appears under the
       brand in the header (this confirms the latest build shipped);
   (d) the nav links (Coverage, Inclusion Ledger, Exclusion Register, Methods,
       About) each load.
8. REPORT: Total charged and for which domains; the pages.dev URL; the
   production branch in use; and any step you skipped or that needs my
   follow-up.

CONSTRAINTS
- Do not modify any other zones, DNS records, Workers, or account settings.
- Do not enable any paid plan or add-on; everything here fits the free Pages
  tier plus at-cost domain registration.
- If any screen asks for something not covered above, STOP and ask me.
```

---

## Changelog

- **v00.03.08** (2026-07-06 19-52) — **Adversarial review of the Phase 1 package applied: 46 confirmed findings** (5 review lenses, 127 agents, every finding independently verified by two skeptics; 15 killed). Blockers fixed: (1) all "October 2027 link" language corrected to the 2027 link (Dec 2026 → Dec 2027, December-wave-measured) — links are December-to-December per codebook §6, so no October link exists; corrected here in §4 and §9 item 13 at the phrase's source, and in g1-band/pre-registration via their logged amendment mechanisms; (2) the archival-regime Gap composition pinned (EC over the matched-carrier scalar-fare comparator, never inserted into codebook §9's Σw[ρ − π^CPI]; predicted-residual-Gap machinery; executable worked number in `engine/test_phase1.py`); (3) the anti-promotion rule split by price type and made symmetric, with the annual link computing after the January confirmation wave and ULCC December = median of three sessions; (4) the pairing rule rewritten sequential leg-by-leg with per-leg verbatim fields. Also: honest wave-hours restated with all steps counted (~8.4 h from Dec 2026; de-scope trigger re-anchored to a committed wave-0 wall-clock vs 9.0 h with a deterministic tie-branch); wave-0 schedule-check protocol pinned and folded into G1-GD; streaming observation of record disambiguated (capture.py hash-grade; Prompt C fallback-only); Hulu incidence corrected to [0%,100%] per the register's rule 1 (register GAP row added); Gate G1 paragraph aligned to GA–GD; the §4 denominator sentence corrected to DB1B/DB1C under the per-event single-product rule; `select_routes.py` hardened (header validation, blank-distance and CLASS handling, mutation-safety) with 6 new tests incl. deficit-unit-semantics and WN-pax-ordering pins; `capture.py` now skips `needs-url` rows; wave prompts brought to §5 field parity (per-leg prices, promo detection, member-price labeling, times, codes). Suite: 38 tests green.

- **v00.03.07** (2026-07-06 16-09) — **Phase 1 kickoff: the panel pre-registration is drafted and committed.** Produced by a 3-design/3-judge adversarial synthesis (identification-first design won 2 of 3 judges; feasibility and critic grafts merged). New binding artifacts: `docs/g1-band.md` (G1 pass criteria GA–GD — discussant, grocery null two-stage, banking sign-only negative, independent rerun with disclosure parity; committed FIRST per the band-before-inputs ordering), `docs/phase1-preregistration.md` (18-route T-100 CY2024 panel by deterministic formula with hub-span/carrier-coverage constraints and logged relaxation; first-Tuesday paired-quote grid, 21/28-day Tuesday itinerary with frozen blackout windows; profiles AIR-P1–P4 with provenance-tagged incidence and the [0,100] carry-on interval; fixed-denominator T3 attribution; December-wave sole-link-observation rule with anti-promotion corroboration; provenance ladder with the December manual-save upgrade; missingness taxonomy and pre-registered de-scope order; streaming dictionary v1 freeze; grocery per-unit null with conservative-tilt framing; FDIC-formula banking negative; the three-regime denominator handoff with the published splice diagnostic; wave-0 dry run Sept, wave 1 = 2026-10-06), `data/phase1-inputs.md` (pinned inputs; T-100 SHA-256 pending owner pull), `pipeline/select_routes.py` + `engine/test_select_routes.py` (the formula as executable, deterministic, fully tested code — the route list is the freeze's output, not its input), `engine/test_phase1.py` (the §13 paired-quote worked example, executable per house rule), `pipeline/wave-prompts.md` (three monthly Chrome prompts with the stated fare-search safety carve-out), banking targets block, codebook §13 pointer. All 31 engine tests green. Both sign-off checkboxes open — collection may not start before owner sign-off. Also: **P14 .com registration SHELVED** by owner decision (revisit on traction); §9 item 13 updated with the owner-action queue (T-100 pull, DB1C byte-verification, Table 1101 cells, FDIC SoD, WS-G counsel review, August discussant outreach).

- **v00.03.06** (2026-07-06 14-48) — **Site is LIVE (P14/P15 done).** restorationgap.org deployed on Cloudflare Pages off `main` (output `site/`, valid cert); `www`→apex 301 redirect active (path + query preserved); Git integration reconnected — root cause was the Cloudflare Workers-and-Pages GitHub App being scoped to only `yamorseal`, resolved by adding `arthurculang/bpi`, so pushes to `main` now auto-deploy (confirmed by a successful test deployment). Homepage hero, `<title>`, and OG description aligned to the canonical "keep last year's life" tagline (they had read "live"); README opener aligned too. `.com` not yet registered (optional defensive buy, deferred). No methodology, gate, or numeric change.

- **v00.03.05** (2026-07-05 05-06) — Deploy handoff. PR #2 merged the working branch to `main` (merge commit 726ca9c), bringing `main` current: G0 PASS, the T-Mobile pre-migration captures, and the tagline site now live on the production branch. Appendix C finalized against production branch `main` (the "/site not yet on main" fallback removed since it now exists there) and its verify step extended to check the tagline "what it costs to keep last year's life" renders — a positive signal that the *latest* build shipped, not a stale commit. Execution-status note updated (P13–P15). No methodology, gate, or numeric change.

- **v00.03.04** (2026-07-04 22-47) — PR #1 merged to `main` (working branch restarted from it); G0 band signed off by owner and Phase 0 begun: retrospective conventions pinned pre-computation (commit da8f599 — event-contribution interpretation of band tests 2–3, incidence primary 45% grid 35–55%, prepaid-online purchase point, $250–400 anchor grid), harness built (`engine/retro_2008.py`), and the **dry run passes**: T1/T2/T4 everywhere, T3 at the primary point (+4.15pp, band [1.0, 6.0]) and across the grid interior with one extreme corner (55% × $250) honestly over the bound — official gate evaluation awaits fare-anchor byte-verification (inputs items 4/7). MIT + CC BY 4.0 licenses added; single-repo build-in-the-open posture adopted; discussant outreach drafts written (Fox / Greenlees / Jaravel).

- **v00.03.03** (2026-07-04 22-04) — Companion pointer updated to Spec v00.02.00 (P2 refined to menu-expansion monotonicity; engine v0 implements the spec's worked examples as 19 passing tests). Adversarial review of engine + P2 propagation applied in full: two engine blockers fixed (mixed-bundle route classification no longer launders tier upgrades through named fees; tier-gap interval re-baselined on today's menu per trigger rule T3), two serious (requirement-derived quantity bounds; fee-only route fall-through), plus consistency fixes to the codebook (§4 and governing-spec pointer), spec (§6 row 3, §11 row 1), G0 band wording (logged amendment, limits untouched), and the site. Root README and CLAUDE.md added.

- **v00.03.02** (2026-07-04 20-08) — Sprint 0 / August pull-forward executed in-repo: codebook v0; **G0 band pre-committed at 57581d6 before any retrospective inputs**; CE quintile weights byte-verified from mirror (anchors exact, residual closes within $1) with reproducible builder; 2008–09 chronology input file (negative-print episode designated: US Airways beverage repeal 3/1/2009; open items listed with tie-breaker source = Brueckner Table 1); incidence proxy register (bag-check ~34–39%, fee-paying ~16–19%, United BE 16%, Disney+ ads 37%, Netflix ads ~45%; carry-on = flagged gap); discussant shortlist (12 candidates, trio: Fox / Greenlees / Jaravel); WS-H budget memo template (~$4–11k year-one cash); site deploy hygiene (favicon, 404, robots, OG tags). Execution-status note added to §9.

- **v00.03.01** (2026-07-04 19-39) — Decisions P1–P15 recorded as adopted by owner; public brand confirmed as **The Restoration Gap** (restorationgap.org). Sprint 0 execution begun in-repo: snapshot pipeline v0 (`pipeline/`), Inclusion Ledger seed data (`data/ledger-events.json`), DOT NPRM comment draft (`docs/dot-nprm-comment-draft.md`).
- **v00.03.00** (2026-07-04 19-17) — Public-artifact pivot: added WS-I (public site & brand); scaffolded the full site in `site/` (home, Gap/releases hub, coverage, Inclusion Ledger seeded with verified events, Exclusion Register, methods, about — placeholders labeled); added decisions P13 (retire "Better Price Index/BPI" for public use — collision scan verdict: blocked by Bank Policy Institute, Bullish Percent Index, ESPN BPI, British Phonographic Industry, and the OECD "Better ___ Index" family — adopt **"The Restoration Gap"**, which scanned clear), P14 (restorationgap.org primary + .com redirect, availability probable but confirmed only at purchase — registry checks blocked from this environment), and P15 (Cloudflare Pages from the repo's `site/` directory, no build step); added Appendix C (Claude-for-Chrome Cloudflare prompt with stop-if-unavailable and price-cap checkpoints); renumbered §9 with the naming/domain/deploy steps in the this-week block.
- **v00.02.00** (2026-07-04 18-49) — Applied all 10 findings from the adversarial plan review (Appendix B): fixed the three blockers (first-print denominator, composite phasing vs product promise, kill-criterion consistency), added comparator-continuity convention for the Oct 2025 CPI hole, corrected coverage-map arithmetic and added the ≈23% residual row with disposition, split the north star into restoration-priced vs monitored coverage, added WS-H (funding) and data-redistribution rights, resourced and scheduled the rental audit, made G2 operational, and hardened G0 (band pre-committed, hash-timestamped).
- **v00.01.00** (2026-07-04 18-40) — Initial project plan. Reframed around the holistic goal: coverage map as spine (real CE Table 1101 quintile dollars), three-artifact product with the Exclusion Register first-class, capture-now-publish-later collection posture. Sector rulings: rental housing IN (Phase 2 flagship, panel starts immediately), telecom IN (T-Mobile 7/13/26 flagship, complementarity framing), healthcare OUT (printable ruling). April 2026 bag-fee wave fully verified; R-CPI-I pinned to Dec 2024 vintage; novelty claim reworded against EU Reg 2020/1148; competitor field verified clear. Built on a 5-agent verified research pass.
