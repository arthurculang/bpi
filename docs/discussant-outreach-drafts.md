# Discussant outreach — email drafts

`v1 · 2026-07-12 · workstream F · DRAFTS for owner to personalize and send (August, plan §9 item 8) · honorarium per WS-H memo line 7`
`Common attachments: the packet cover memo (docs/discussant-packet-memo.md — the reading guide, one order per seat) + spec v00.02.00, codebook v0, the pre-committed G0 band AND its PASSED result, the signed Phase 1 pre-registration; RX-100 proposal flagged as forward-looking/under-review. The self-imposed constraints — and the logged self-corrections — are the pitch`

---

## 1 — Kevin Fox (UNSW; index-number theory seat)

Subject: Methods review request — a conditional replication-cost price index (pre-registered, pre-committed validation gate)

Dear Professor Fox,

I'm building a research price measure — working name "The Restoration Gap" — and
am seeking a formal methods discussant before its first publication. The object
is a conditional replication-cost index in characteristics space: freeze the
attribute vector of what a household actually bought last year (including
formerly-included features — airline carry-on rights, ad-free tiers), and price
the cheapest same-seller bundle on today's menu that weakly dominates it. It is
published only as a spread over the matching official CPI series, with explicit
Konüs upper-bound language in every release.

Two design features may interest you specifically: the min-cost operator permits
procurement substitution while forbidding attribute substitution (a Leontief-in-
characteristics conditional cost function), and the validation was pre-committed —
a retrospective of the 2008–09 US checked-bag unbundling was required to land
inside a numeric band hash-committed to the repository before any inputs or
results existed. It did (gate passed July 2026; all four band tests hold at a
byte-verified fare anchor), and the live collection design is now signed and
frozen ahead of an October start. The methodology, engine (worked examples run as unit tests),
and all decision records are public in a single repository.

Would you consider a paid formal review (written comments, roughly a referee
report's depth) in the September–October window, ahead of the pre-registration
note? I'd be glad to send the two core documents — they total about 25 pages.

[NAME / contact / link]

---

## 2 — John Greenlees (ex-BLS; adversarial seat)

Subject: Request for a hostile review — a measure that claims CPI answers a different question, not a wrong one

Dear Dr. Greenlees,

I'm seeking the most skeptical qualified reviewer I can find for a research
price measure before it publishes anything. Your "Addressing Misconceptions
About the CPI" is the canonical statement of the position my project is most
likely to be accused of ignoring — which is exactly why I'd value your review.

The measure prices the reproduction cost of last year's consumption experience
(the fee-and-tier unbundling margin: carry-on rights, ad-free tiers, rental fee
stacks) and publishes only a spread over the matching CPI series. It explicitly
does not claim CPI error: the spec documents what CPI already captures (per-unit
shrinkflation, first-checked-bag fees on designated quotes) and expects
near-zero gaps there, with groceries and banking shipped as null and negative
controls. The claim under review is narrower: that no worked procedure exists
for pricing unbundling transitions — CPI's own airline-fares factsheet places
carry-on fees outside the quote specification, and the PPI's 2009 fee adjustment
is my strongest precedent.

The validation design may appeal to your skepticism: a 2008–09 bag-fee
retrospective was required to land inside a numeric plausibility band committed
publicly before any inputs were assembled — the commit history is the evidence,
and the gate has since passed at a byte-verified fare anchor. The project has
also already corrected three of its own published coverage hypotheses downward,
with logged amendments; the cover memo leads with that trail because it is the
behavior we are asking you to stress-test. I'd ask you to attack precisely that
benchmark logic, as someone who knows how CPI and PPI actually handled it from
the inside. Paid, written, and your criticisms would be published with the
methods note (with your permission) whether or not they're favorable.

[NAME / contact / link]

---

## 3 — Xavier Jaravel (LSE; distributional seat)

Subject: Review request — replication-cost index weighted to the bottom two income quintiles (R-CPI-I recipe)

Dear Professor Jaravel,

Your inflation-inequality work — and the D-CPI in particular — is the empirical
foundation for a measure I'm preparing for first publication, and I'd value your
formal review of its distributional design before it ships.

The measure prices the reproduction cost of last year's consumption experience
(unbundling and tier-stripping: the fees that restore what used to be included)
for bottom-two-quintile households, weighted by BLS's own R-CPI-I recipe
(equivalized imputed income, pooled CE shares), and published as a spread over
the matching CPI series with a mandatory decomposition into pricing-concept vs
basket effects — so the distributional choice is always shown, never smuggled.
Where your D-CPI holds prices common and varies baskets, this varies the price
concept itself; I think of them as complements and would welcome your view on
whether that framing holds.

Specific questions I'd put to you: whether the coping margin your and
Argente–Lee's work documents is fairly represented by incidence-weighted
experience profiles, and whether the bottom-40 weighting survives the CE
ranking critiques given the R-CPI-I inheritance. Paid formal review,
September–October, ahead of a pre-registration note; methodology and code are
public in a single repository.

[NAME / contact / link]

---

*Sending notes: personalize the openers with one line on their specific recent
work; attach or link rather than paste documents; Sichel is the alternate for
seat 2 if Greenlees is unreachable (shortlist has contact surfaces). All three
can be approached in parallel — the seats are complementary, not exclusive.*

- v1 (2026-07-12): tenses updated for the G0 pass and Phase 1 sign-off; packet cover memo added as the lead attachment; corrections-trail framing added to the Greenlees letter.
