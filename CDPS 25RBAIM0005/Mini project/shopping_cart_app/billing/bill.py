def calculate_total(cart):
    total = 0
    for item in cart:
        total += item["price"] * item["quantity"]
    return total

def generate_bill(cart):
    print("\n------ BILL ------")
    for item in cart:
        print(f"{item['name']} - {item['quantity']} x ₹{item['price']}")
    total = calculate_total(cart)
    print("------------------")
    print(f"Total Amount: ₹{total}")# -*- coding: utf-8 -*-

