cart = []

def add_to_cart(product_name, price, quantity):
    cart.append({
        "name": product_name,
        "price": price,
        "quantity": quantity
    })

def view_cart():
    if not cart:
        print("\nCart is empty")
        return

    print("\nYour Cart:")
    for item in cart:
        print(f"{item['name']} - ₹{item['price']} x {item['quantity']}")

