total = 0
item_number = int(input("Number of items: "))
while item_number < 0:
    print("Invalid number of items!")
    item_number = int(input("Please reenter number of items: "))
for i in range(1, item_number + 1):
    item_price = float(input("Price of item: "))
    total+=item_price
if total > 100:
    total = total * 0.9
print(f"Total price for {item_number} items is ${total:3,.2f}")
