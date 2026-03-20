import json
import random

# Mock GenPark Product Database
PRODUCTS = [
    {"id": "p1", "name": "Keychron K2 V2", "category": "Keyboard", "price": 79.99, "stock": 42, "variants": ["Red Switch", "Blue Switch", "Brown Switch"]},
    {"id": "p2", "name": "Logitech MX Master 3S", "category": "Mouse", "price": 99.00, "stock": 15, "variants": ["Pale Gray", "Graphite"]},
    {"id": "p3", "name": "Nanoleaf Shapes Triangles", "category": "Lighting", "price": 199.99, "stock": 8, "variants": ["7-pack", "15-pack"]},
    {"id": "p4", "name": "Steelcase Gesture Chair", "category": "Furniture", "price": 1200.00, "stock": 3, "variants": ["Licorice", "Blueberry"]},
    {"id": "p5", "name": "Sony WH-1000XM5", "category": "Audio", "price": 348.00, "stock": 25, "variants": ["Black", "Silver", "Midnight Blue"]}
]

# Mock Loyalty Benefits
LOYALTY_DISCOUNTS = {
    "google": 0.05, # 5% off
    "metamask": 0.10, # 10% off for web3 OGs
    "base": 0.08, # 8% off for Base users
    "discord": 0.03 # 3% off for community members
}

def genpark_ucp_search(query, include_inventory=True):
    results = [p for p in PRODUCTS if query.lower() in p['name'].lower() or query.lower() in p['category'].lower()]
    if include_inventory:
        return results
    return [{k: v for k, v in p.items() if k != 'stock'} for p in results]

def genpark_ucp_batch_add(item_ids, store_id="genpark-flagship"):
    selected = [p for p in PRODUCTS if p['id'] in item_ids]
    total = sum(p['price'] for p in selected)
    print(f"[*] UCP Batch Add: Added {len(selected)} items to cart at {store_id}.")
    print(f"[*] Total items: {', '.join([p['name'] for p in selected])}")
    print(f"[*] Subtotal: ${total:.2f}")
    return {"status": "success", "items_added": len(selected), "total": total}

def genpark_ucp_loyalty_apply(provider):
    discount = LOYALTY_DISCOUNTS.get(provider.lower(), 0)
    if discount > 0:
        return {"status": "success", "provider": provider, "discount_percentage": discount * 100, "msg": f"Applied {discount*100}% discount via {provider} Identity Linking."}
    return {"status": "error", "msg": "No loyalty benefits found for this provider."}

if __name__ == "__main__":
    # Test
    print(json.dumps(genpark_ucp_search("Keyboard"), indent=2))
    print(json.dumps(genpark_ucp_batch_add(["p1", "p2"]), indent=2))
    print(json.dumps(genpark_ucp_loyalty_apply("metamask"), indent=2))
