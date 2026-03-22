# GenPark Sub-Killer Skill (Subscription Auditor)

Identifies vampire subscriptions from transaction metadata and auto-executes non-reversible cancellations via GenPark automated legal notices.

## Commands

### `genpark-sub-killer audit <transaction_log>`
Identifies recurring charges that have low usage or high price volatility.

### `genpark-sub-killer terminate <sub_id>`
Generates and sends an automated legal notice to the provider via GenPark API to cancel the subscription instantly.

## Guidelines
- Priority: Human financial health.
- Use Case: Saving users $50-200/mo on hidden SaaS and digital service fees.
- Tone: Protective, firm, and efficient.
