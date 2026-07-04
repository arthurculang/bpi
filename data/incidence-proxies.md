# Incidence proxy register — v0

`v0 · 2026-07-04 · workstream C (codebook §8) · every figure carries provenance + a usable-as-weight vs sanity-only label`
`Method caveat: bts.gov, gao.gov, airlines.org, antenna.live figures were triangulated from search snippets (direct fetch blocked); re-pull primary tables from an unblocked connection before print`

## Air travel

| Quantity | Value | Vintage | Provenance | Status |
|---|---|---|---|---|
| Checked bags per enplaned passenger | ~0.55 (45.7M bags handled Dec 2024 ÷ 83.3M systemwide enplanements) | Dec 2024 | DOT Air Travel Consumer Report + BTS traffic release | **usable** with stated bags-per-checker assumption |
| Share checking ≥1 bag (derived) | ~34–39% (at 1.4–1.6 bags per checking passenger) | 2024 | derived from above | **usable** — publish the assumption; note numerator/denominator scope mismatch (marketing carriers vs systemwide) |
| Fee-paying incidence (derived) | ~16–19% of enplanements ($7.27B ÷ 982.3M = $7.40/enplanement ÷ ~$40–45 blended fee) | 2024; $7.62/enplanement for 2025 | BTS Schedule P-1.2 revenue ÷ BTS enplanements (2024 ≈ 982.3M reconstructed; 2025 = 971.6M summed from monthly releases) | **usable** with fee-level assumptions; the ~20pp wedge vs check-rate = fee-exempt checking (Southwest pre-5/2025 at ~2× check rates, elites, cardholders, premium cabins, military) |
| Southwest pre/post response | pre: ~2× industry bag volume (CEO, Mar 2025); post: bags/customer −~30%, revenue/passenger converged to Big-3, ~$1B annualized (Q3 2025 call) | 2025 | company statements/earnings | **usable** for WN profile shift; also the modern elasticity analog for the 2008–09 retrospective |
| Survey check-rate | ~55% "check some or all" | 2023 | Go Group via Forbes | sanity only (self-report, biased high) |
| Full-size carry-on incidence | **no defensible public number** | — | bin-capacity framing suggests a ~70–85% structural ceiling; Southwest's "modest increase in gate-checks" post-fees suggests bins near saturation | **GAP** — publish [0%,100%] bounds or the structural ceiling as an upper bound; pursue proprietary sources (airline ops, IATA cabin studies) |
| United Basic Economy take rate | ~16% of domestic passengers (up from ~12% YoY) | Q3 2024 | CCO Nocella, earnings call | **usable** as the BE-attribute weight, vintage-tagged |
| Delta BE buy-up | >50% buy up at warning; ~20% BE take of offered base | 2017–19 era | investor statements | sanity only (dated, offered-base concept) |

## Streaming

| Quantity | Value | Vintage | Provenance | Status |
|---|---|---|---|---|
| Disney+ ad-tier share of US subs | 37% (company); ~30% global | Aug 2024 | Iger/earnings | **usable** (stock mix); conflicting externals (Ampere 14%, survey ~20%) as bounds |
| Netflix ad-tier share | ~45% of US Netflix households (Comscore); ad tier ~50% of 2025 US gross signups, 54% Q1 2026 (Antenna) | 2025–Q1 2026 | Comscore/Antenna via trade press | **usable** with the household-vs-billing caveat; signup shares are flow, not stock |
| Market-wide ad-tier share | 46% of US premium SVOD subs (services offering ads); ad tiers = 57% of Q1 2025 gross adds | Q1 2025 | Antenna | envelope/sanity |

## Rules of use (binding, per codebook §8)

1. A line item is weighted only by a **usable**-tagged figure with its assumption
   stated in the release table; otherwise the published [0%, 100%] interval applies.
2. Provenance tags travel with the number into every release.
3. The carry-on gap is the known weak point of the air module: first print uses
   bounds or the structural ceiling, labeled, until a defensible source exists.
4. Enplanement reconstructions (2024 ≈ 982.3M; 2025 = 971.6M) must be replaced
   with the official BTS annual prints before publication (A4A's ~960M for 2024
   is a scope-difference conflict — use BTS).
