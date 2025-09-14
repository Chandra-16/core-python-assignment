def calc_cart_price(cart):
    if len(cart) == 0:
        return 0
    
    total = sum(cart.values())
    if len(cart) > 5:
        total *= 0.9
    return total

n = int(input("Enter no. of cart items"))
cart = {}
for _ in range(n):
    item = input("Enter item name: ")
    price = int(input("Enter price of %s: " %item))
    cart[item] = price

total = calc_cart_price(cart)
print("Total Price:", int(total))