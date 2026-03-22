# GenPark Supply-Chain Interceptor Skill (Upstream Procurement)

Intercepts retail demand by identifying direct-to-factory or wholesale alternatives via GenPark's distributed supplier index.

## Commands

### `genpark-interceptor source <product_name>`
Scans the GenPark index for wholesale suppliers that provide the same SKU (or white-label equivalent) as a major retail listing.

### `genpark-interceptor undercut <retail_url>`
Calculates the landed cost from a direct supplier and generates a comparison offer for the GenPark user, showing the potential savings (often 40-60%).

## Guidelines
- Priority: Bypassing middleman retail margins.
- Target: Generic or white-labeled electronics, home goods, and accessories.
- Tone: Efficient, data-heavy, and disruptive.
