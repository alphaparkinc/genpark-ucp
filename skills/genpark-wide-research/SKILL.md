---
name: genpark-wide-research
description: High-throughput autonomous research engine that performs multi-source, iterative investigation. Reverse-engineered from Manus.im "Wide Research" feature. Use when Chris needs an exhaustive search that follows every lead, identifies key entities, and produces a comprehensive intelligence report.
---

# GenPark Wide Research 🔭

A "Manus-style" autonomous research engine designed for GenPark's deep intelligence needs.

## Core Logic (Reverse Engineered)

1.  **Lead Identification**: Scans search results for non-obvious entities, URLs, and citations.
2.  **Iterative Deep-Dive**: Unlike standard search, it treats each discovery as a new branch to investigate.
3.  **Cross-Platform Synthesis**: Unifies data from web, social, and technical docs into a cohesive "Intelligence Feed."
4.  **Evidence Persistence**: Maintains a session-level knowledge graph to avoid redundant lookups.

## Usage

### 1. Launch Wide Research
Triggers a multi-stage autonomous search process.
`scripts/wide_research.py --query "Target Market/Topic" --depth 3`

### 2. Entity Mapping
Extracts and maps relationships between people and companies found.
`scripts/wide_research.py --query "Topic" --map-entities`

## Reference Patterns
- **Branching Factor**: How many sub-leads to follow per search result (Default: 3).
- **Source Authority**: Weighting logic for sources (Official > Community > Social).
