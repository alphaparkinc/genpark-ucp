# Skill: genpark-trust-guardian
# Description: Reverse-engineered Trustpilot-style trust and verification engine. Orchestrates service/product reviews, automated sentiment analysis, and business unit trust scoring.

## Core Capabilities
1. **Business Trust Scoring**: Automatically calculates trust scores (1-5 stars) based on aggregated review distribution and volume.
2. **Verified Review Verification**: Logic to distinguish between "Verified" purchases and organic reviews using proof-of-transaction metadata.
3. **Automated Sentiment Summary**: Summarizes thousands of reviews into "Common Themes" (Pros/Cons) using LLM-based extraction.
4. **Competitor Trust Benchmarking**: Compares a target business unit against industry peers to identify market positioning.
5. **Transparency & Reporting**: Generates "Trust Reports" that flag unusual review patterns (Potential Bot Attacks or Review Bombing).

## Workflow Logic
- **Stage 1 (Data Fetch)**: Agent crawls/fetches reviews for a specific business unit via `web_search`.
- **Stage 2 (Distribution Analysis)**: Maps out the star-rating distribution (1 to 5 stars).
- **Stage 3 (Sentiment Extraction)**: Identifies key pain points (e.g., "Slow Shipping", "Great Support").
- **Stage 4 (Score Generation)**: Produces the "Guardian Score" to be displayed in the GenPark "ChatCanvas".
