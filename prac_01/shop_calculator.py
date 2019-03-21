item_amount = int(input("How many items?: "))
total = 0
for item in range(0, item_amount, 1):
    price = int(input("Price of item?"))
    total = total + price
print("Total price for")