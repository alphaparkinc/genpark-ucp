# GenPark TrustGuardian Discovery & Verification Skill Integration

This repository contains the reverse-engineered logic for **Trustpilot.com**, integrated as a GenPark Skill.

## Features
- **Business Trust Scoring**: Automated star-distribution (1-5) and trust score calculation for service/product units.
- **Verified Review Verification**: Distinguishing between verified purchases and organic reviews using proof-of-transaction patterns.
- **Automated Sentiment Summary**: LLM-driven extraction of common review themes (Pros/Cons) for thousands of data points.
- **Competitor Trust Benchmarking**: Comparative analysis of business trust scores against industry peers.
- **Trust Integrity Reporting**: Flags unusual review patterns (e.g., bot attacks or review bombing).

## Repository Structure
- `skills/genpark-trust-guardian/SKILL.md`: Detailed documentation of the trust and verification agent.
- `skills/genpark-trust-guardian/scripts/guardian_engine.py`: Core logic for trust score calculation and sentiment extraction.

## Integration with GenPark
TrustGuardian provides GenPark users with a "Trust Layer" for their digital shopping and service interactions, ensuring they can verify business credibility instantly.

---
*Developed for Chris P. by Genius.*
