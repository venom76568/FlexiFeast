"""
Swiggy MCP Adapter (Sandbox mode).
Wraps the mock Swiggy menu with a clean interface.
In production, this would communicate with the real Swiggy MCP server.
"""
MOCK_SWIGGY_CATALOG = [
    {"id": "sw_001", "name": "Chicken Sandwich", "price": 120, "category": "Snacks"},
    {"id": "sw_002", "name": "Paneer Wrap", "price": 150, "category": "Snacks"},
    {"id": "sw_003", "name": "Cold Coffee", "price": 80, "category": "Beverages"},
    {"id": "sw_004", "name": "Masala Dosa", "price": 90, "category": "Breakfast"},
    {"id": "sw_005", "name": "Veg Biryani", "price": 180, "category": "Meals"},
    {"id": "sw_006", "name": "Chicken Biryani", "price": 220, "category": "Meals"},
    {"id": "sw_007", "name": "Fruit Salad", "price": 70, "category": "Healthy"},
]


def get_catalog() -> list:
    """Returns full Swiggy menu catalog."""
    return MOCK_SWIGGY_CATALOG


def build_cart_deeplink(item_ids: list, coupon: str = "CORPORATE10") -> str:
    """Generates deep-link URL for Swiggy app with pre-filled cart and best coupon."""
    ids_param = ",".join(item_ids)
    return f"swiggy://cart?items={ids_param}&coupon={coupon}"


def search_items(query: str) -> list:
    """Search catalog by name (case-insensitive, multi-word)."""
    words = query.lower().split()
    return [
        item for item in MOCK_SWIGGY_CATALOG
        if any(w in item["name"].lower() for w in words)
    ]
