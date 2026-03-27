---
name: openclaw-moa-core
description: Mixture-of-Agents (MoA) orchestration for parallel search and structured synthesis. Use when Chris needs a deep-dive research report where multiple specialized agents research sub-topics in parallel and merge into one evidence-linked "Dossier-style" report.
---

# OpenClaw MoA Core ⚡️

A high-performance orchestration engine for parallel intelligence gathering.

## Core Architecture

1.  **Parallel Intent Decomposition**: A master agent breaks a single high-level query into 4-6 specialized sub-tasks.
2.  **Mixture-of-Agents (MoA) Execution**: Specialized sub-agents (Search, Analyst, Validator, Narrator) execute sub-tasks concurrently.
3.  **Synthesis Layer**: Merges multi-source evidence into a structured markdown page with a Table of Contents and Source Linking.

## Usage

### 1. Trigger MoA Research
Command: `scripts/moa_engine.py --query "Target Topic"`

### 2. Generate Report
Generates the final structured synthesis.
Command: `scripts/moa_engine.py --query "Target Topic" --synthesis --output report.md`

## Research Patterns
- **Parallel Search**: Executes 5 concurrent searches to bypass single-threaded context limits.
- **Deduplication**: Filters conflicting or low-authority sources during the merge phase.
