# GenPark Scalp-Guard Skill (Anti-Reseller Procurement)

Automatically scans and locks high-demand items (GPUs, concert tickets, limited drops) at MSRP by simulating human-like, multi-session purchasing flows to bypass bot-detection and reseller hoarding.

## Commands

### `genpark-guard lock <product_url> --msrp <price>`
Monitors stock levels 24/7. When restock occurs, it executes a multi-node purchase attempt to secure the item for the user at the original price.

### `genpark-guard verify-msrp <product_name>`
Scans historical pricing data to alert the user if a current "deal" is actually a reseller's inflated price.

## Guidelines
- Priority: Fairness and MSRP-enforcement.
- Target: Items plagued by professional scalping bots.
- Tone: Protective, anti-establishment, and tactical.
