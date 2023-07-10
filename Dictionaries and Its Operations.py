Grocery = {
    "Cornflakes": {"quantity": 15, "price": 100},
    "Muesli": {"quantity": 14, "price": 150},
    "Oats": {"quantity": 10, "price": 80},
    "Wheat Flakes": {"quantity": 5, "price": 75},
    "Granola": {"quantity": 8, "price": 125}
}


print("Grocery:")
print(Grocery)


choice = int(input("Display what you want to do?\n1. Add the additional quantity of the cereals\n2. Update the price of the grocery\n3. Add new item\nEnter your choice: "))
if choice == 1:
    item_name = input("Enter the grocery item name: ")
    quantity_to_add = int(input("Enter the quantity of item to be added: "))
    if item_name in Grocery:
        Grocery[item_name]["quantity"] += quantity_to_add
    else:
        print("Item not found in the grocery dictionary.")
elif choice == 2:
    item_name = input("Enter the grocery item name: ")
    new_price = float(input("Enter the new price of the item: "))
    if item_name in Grocery:
        Grocery[item_name]["price"] = new_price
    else:
        print("Item not found in the grocery dictionary.")
elif choice == 3:
    item_name = input("Enter the new item name: ")
    quantity = int(input("Enter the quantity of the new item: "))
    price = float(input("Enter the price of the new item: "))
    Grocery[item_name] = {"quantity": quantity, "price": price}
else:
    print("Invalid choice.")


print("Item details after updating:")
print("Grocery:")
print(Grocery)