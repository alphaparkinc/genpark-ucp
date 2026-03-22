# GenPark Adaptive-Subscription Skill (Dynamic SaaS Optimizer)

Automatically manages and optimizes a user's digital subscription portfolio by monitoring actual usage patterns and switching between plans (Individual vs. Family) or pausing billing during low-usage periods via GenPark automated service adapters.

## Commands

### `genpark-sub audit <account_link>`
Scans usage logs for a specific subscription (e.g., Netflix, Midjourney, Adobe) and identifies "idle periods" where the user is paying but not using.

### `genpark-sub optimize <account_link>`
Triggers an automated request to the provider's billing API to downgrade or pause the subscription based on predicted usage for the next 30 days.

## Guidelines
- Priority: Human financial liquidity.
- Focus: "Vampire" subscriptions with auto-renewal and opaque cancellation flows.
- Tone: Cold, efficient, and user-centric.
