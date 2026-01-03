
from products.products import products, show_products


from cart.cart import add_to_cart, view_cart, cart
from billing.bill import generate_bill

while True:
    print("\n1. Show Products")
    print("2. Add to Cart")
    print("3. View Cart")
    print("4. Generate Bill")
    print("5. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        show_products()

    elif choice == 2:
        show_products()
        pid = int(input("Enter product id: "))
        qty = int(input("Enter quantity: "))

        product = products.get(pid)
        if product:
            add_to_cart(product["name"], product["price"], qty)
            print("Item added to cart")
        else:
            print("Invalid product id")

    elif choice == 3:
        view_cart()

    elif choice == 4:
        generate_bill(cart)

    elif choice == 5:
        print("Thank you for shopping 😊")
        break

    else:
        print("Invalid choice")# -*- coding: utf-8 -*-

