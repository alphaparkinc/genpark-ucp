# GenPark Inventory-Oracle Skill (Personal Asset Lifecycle Manager)

Monitors the real-time resale value and maintenance status of products in the user's GenPark database. Prevents asset depreciation by flagging optimal sell-by dates before market saturation.

## Commands

### `genpark-oracle audit <product_id>`
Fetches real-time secondary market data (eBay, Mercari, Xianyu) to provide a current "Liquid Value" for any physical asset.

### `genpark-oracle sell-alert <product_id>`
Monitors news cycles and product launch schedules. Automatically alerts the user to sell an item (e.g., "iPhone 15 Pro") 7-10 days before a new model announcement to maximize resale ROI.

## Guidelines
- Priority: Human financial health and asset liquidity.
- Focus: Consumer electronics, designer goods, and limited-edition hardware.
- Tone: Professional, advisory, and predictive.
