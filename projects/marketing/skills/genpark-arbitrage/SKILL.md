# GenPark Arbitrage Skill (HFT Procurement)

High-frequency procurement engine that monitors wholesale APIs to front-run retail listings and lock inventory via GenPark protocol.

## Commands

### `genpark-arbitrage scan <market_sector>`
Scans for price discrepancies between wholesale (upstream) and retail (downstream) markets.

### `genpark-arbitrage lock <sku_id> --quantity <n>`
Uses the GenPark protocol to instantly lock inventory at the lower price before it hits general retail.

## Guidelines
- Priority: Speed and precision.
- Use Case: Sourcing high-demand electronics and hardware at scale.
- Tone: Cold, efficient, and profit-driven.
