# Skill: genpark-arteditor-engine
# Description: Advanced design agent based on ArtEditor architecture. Orchestrates multi-agent workflows for brand systems, visual assets, and editable design layers.

## Core Capabilities
1. **Brand System Generation**: Unified color, layout, and voice into a cohesive brand world.
2. **Multi-Agent Asset Generation**: Coordinated production of hero images, product close-ups, and campaign videos.
3. **Layered "Touch Edit"**: Precision editing by preserving base context while swapping specific elements (logos, objects).
4. **Editable Typography**: Separates text layers from imagery to allow copy refinement without re-rendering.
5. **Real-time Design Reference**: Live web search for design trends and competitive visual benchmarking.

## Workflow Orchestration
- **Agent A (Researcher)**: Fetches real-time design references via `web_search`.
- **Agent B (Visualizer)**: Generates initial high-fidelity assets.
- **Agent C (Editor)**: Handles "Touch Edit" via In-painting and Layer extraction.
- **Agent D (Synthesizer)**: Merges brand voice and typography into the final "ChatCanvas".
