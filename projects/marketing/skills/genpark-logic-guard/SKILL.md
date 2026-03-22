# GenPark Logic-Guard Skill (Anti-Impulse Marketing Filter)

Real-time analysis of marketing psychological triggers (e.g., FOMO, price anchoring, misleading comparisons) and "dark patterns" used by retailers to force impulse purchases.

## Commands

### `genpark-guard filter <marketing_page_url>`
Analyzes a product page's text and identifies "psychological anchoring" techniques (e.g., "Original Price $999 -> Now $199" where the $999 is fake).

### `genpark-guard utility-score <product_name>`
Cross-references the product with the user's historical habits to provide a "Utility Likelihood" score (e.g., "92% chance of 6-month abandonment based on your similar unused purchases").

## Guidelines
- Priority: Protecting the user's mental and financial boundaries.
- Focus: Influencer-driven marketing, live-stream "flash sales," and subscription traps.
- Tone: Cold, analytical, and protective.
