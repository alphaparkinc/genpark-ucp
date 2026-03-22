# GenPark Group-Buy Syndicator Skill (Aggregated Demand Lock)

Identifies clusters of intent for specific products and uses the aggregated volume to force high-discount wholesale contracts via the GenPark protocol.

## Commands

### `genpark-syndicate pool <product_name> --min-users <n>`
Scans the GenPark user base for active intent for the same product and creates a time-limited "syndicate" to pool purchasing power.

### `genpark-syndicate strike <syndicate_id>`
Once the user count is met, the skill automatically submits a bulk purchase order to the direct supplier, bypassing all retail channels.

## Guidelines
- Priority: Leveraging volume to crash price.
- Use Case: Group-buys for expensive electronics, peripherals, and high-demand tech.
- Tone: Collective, tactical, and powerful.
