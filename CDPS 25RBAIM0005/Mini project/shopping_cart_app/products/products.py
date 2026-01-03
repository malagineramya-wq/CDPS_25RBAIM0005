products = {
    1: {"name": "Milk", "price": 50},
    2: {"name": "Bread", "price": 30},
    3: {"name": "Rice (1kg)", "price": 60},
    4: {"name": "Wheat Flour (1kg)", "price": 55},
    5: {"name": "Eggs (1 piece)", "price": 6},
    6: {"name": "Sugar (1kg)", "price": 45},
    7: {"name": "Salt (1kg)", "price": 20},
    8: {"name": "Cooking Oil (1L)", "price": 160},
    9: {"name": "Tea Powder (250g)", "price": 120},
    10: {"name": "Coffee Powder (200g)", "price": 150},
    11: {"name": "Biscuits", "price": 25},
    12: {"name": "Chips Packet", "price": 20},
    13: {"name": "Soap", "price": 35},
    14: {"name": "Shampoo Sachet", "price": 5},
    15: {"name": "Toothpaste", "price": 90},
    16: {"name": "Toothbrush", "price": 40},
    17: {"name": "Detergent Powder (1kg)", "price": 110},
    18: {"name": "Notebook", "price": 50},
    19: {"name": "Pen", "price": 10},
    20: {"name": "Water Bottle (1L)", "price": 20}
}

def show_products():
    print("\nAvailable Products:")
    print("-" * 30)
    for pid, item in products.items():
        print(f"{pid}. {item['name']} - ₹{item['price']}")

