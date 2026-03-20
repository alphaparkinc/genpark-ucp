# genpark-ucp (Google Universal Commerce Protocol Agent)

Use this skill when the user wants to experience "Agentic Commerce" on GenPark, specifically leveraging Google's Universal Commerce Protocol (UCP) features.

## Capabilities

1.  **Batch Shopping Cart (`genpark_ucp_batch_cart`)**: 
    - Agents can add multiple items to the cart at once from a single prompt (e.g., "Add the entire 'Cyberpunk Setup' to my cart").
    - Mimics the UCP standard for "single-action multi-item" transactions.

2.  **Real-time Product Details (`genpark_ucp_product_sync`)**:
    - Retrieves real-time variants, inventory, and pricing directly from GenPark/Retailer APIs.
    - Ensures the agent never recommends an out-of-stock item.

3.  **Identity Linking & Loyalty (`genpark_ucp_loyalty_apply`)**:
    - Connects GenPark accounts with Google/MetaMask/Discord identities.
    - Automatically applies member benefits, discounts, and loyalty points.

## Tools

### `genpark_ucp_search`
Search for products using UCP-enhanced queries.
- `query`: Search string (e.g., "blue mechanical keyboard with red switches")
- `include_inventory`: Boolean (fetch real-time stock)

### `genpark_ucp_batch_add`
Add multiple items to cart.
- `item_ids`: List of product IDs.
- `store_id`: ID of the merchant.

### `genpark_ucp_link`
Link external identity for rewards.
- `provider`: "google", "metamask", "base", etc.

## Best Practices
- **Vibe-based shopping**: Instead of adding one by one, suggest "kits" or "bundles" that can be added in one go.
- **Inventory Awareness**: Always check stock before confirming a recommendation.
- **Loyalty First**: Mention applied discounts to reinforce value.

## Implementation (Python/Node)
The underlying logic is handled via the `projects/marketing/ucp_agent.py` script and GenPark's internal API.
