# GenPark Flash-Return Skill (Instant Refund Execution)

Automates the high-friction refund process by generating non-negotiable legal demand letters based on consumer protection laws and delivering them via the GenPark protocol.

## Commands

### `genpark-refund scan <order_id>`
Analyzes purchase metadata (terms of service, return policy) and identifies the strongest legal ground for a refund (e.g., "not as described," "delayed shipping").

### `genpark-refund trigger <order_id>`
Generates a formal demand letter and sends it to the merchant's support API and legal department simultaneously to force an instant refund or credit.

## Guidelines
- Target: Merchants with complex, "vampire" return policies.
- Priority: Human liquidity and consumer rights.
- Tone: Cold, legalistic, and uncompromising.
