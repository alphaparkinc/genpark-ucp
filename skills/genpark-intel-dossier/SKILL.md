---
name: genpark-intel-dossier
description: Autonomous intelligence gathering and dossier generation for entities (people, companies, narratives). Reverse-engineered from Ventify.ai. Use when Chris needs deep, stateful, evidence-linked tracking of competitors, candidates, or investment targets.
---

# GenPark Intel Dossier 📂

Autonomous intelligence engine that constructs living dossiers from 100+ sources.

## Core Capabilities

- **Entity Resolution**: Cross-platform identity mapping (X, LinkedIn, GitHub, etc.)
- **Change Logs**: Automated tracking of what changed and when
- **Evidence Memory**: Every fact linked back to a source URL
- **Dossier Chapters**: Structured output covering Professional, Personal, Network, and Risk Assessment.

## Usage

### 1. Initialize Dossier
Trigger when starting a new research task on a person or company.
`scripts/intel_engine.py --target "Name/Company" --init`

### 2. Deep Search & Update
Run to refresh signals from social posts, hiring patterns, and regulatory filings.
`scripts/intel_engine.py --target "Name/Company" --deep-scan`

### 3. Generate Report
Exports a structured markdown dossier.
`scripts/intel_engine.py --target "Name/Company" --report`

## Reference Patterns
- See `references/dossier_structure.md` for chapter definitions.
- See `references/signal_logic.md` for "Weak-Signal" detection rules.
