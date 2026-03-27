---
name: openclaw-moa-spark-engine
description: Mixture-of-Agents (MoA) orchestration for parallel search and structured synthesis. Reverse-engineered from Genspark's Sparkpage logic. Use when Chris needs a "Sparkpage-style" deep dive where multiple specialized agents research sub-topics in parallel and merge into one evidence-linked report.
---

# OpenClaw MoA Spark Engine ⚡️

A high-performance orchestration engine that mimics the Genspark "Sparkpage" logic within the OpenClaw environment.

## Core Architecture (Reverse Engineered)

1.  **Parallel Intent Decomposition**: A master agent breaks a single high-level query into 4-6 specialized sub-tasks.
2.  **Mixture-of-Agents (MoA) Execution**: Specialized sub-agents (Search, Analyst, Validator, Narrator) execute sub-tasks concurrently.
3.  **Synthesis Layer**: Merges multi-source evidence into a structured markdown page with a Table of Contents and Source Linking.

## Usage

### 1. Trigger MoA Research
Command: `scripts/moa_spark.py --query "Target Topic"`

### 2. Generate Sparkpage
Generates the final structured synthesis.
Command: `scripts/moa_spark.py --query "Target Topic" --synthesis --output report.md`

## Research Patterns
- **Parallel Search**: Executes 5 concurrent searches to bypass single-threaded context limits.
- **Deduplication**: Filters conflicting or low-authority sources during the merge phase.
