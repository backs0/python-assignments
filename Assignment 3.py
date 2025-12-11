inventory = {}

def add_item():
    while True:
        print("Adding a New Item")
        item_id = input("Enter item ID (unique integer): ").strip()
        try:
            item_id =int(item_id)
        except ValueError:
            print("Invalid input! Please enter a valid integer for the item ID.")
            continue
        if item_id in inventory:
            print("Error: Item ID already exists. Try a different ID.")
            continue

        item_name = input("Enter item name: ").strip()
        item_quantity = int(input("Enter quantity: ")).strip()
        if item_quantity < 0:
            print("Quantity cannot be negative.")
            continue
        except ValueError:
            print("Invalid input! Please enter a whole number.")
        item_price = int(input("Enter price per unit: ")).strip()
        try:
            item_price = float(item_price)
        except ValueError:
            print("Invalid input! Please enter a valid number for the price.")
            continue
        Inventory[item_id] = {
            "name": name,
            "quantity" = quantity,
            "price" = price,
        }
        print(f"Item '{item_name}' added successfully!")
        print()
        return inventory

def update_item():
    print("Updating Item Details")
    item_id = input("Enter item ID to update: ").strip()
    if item_id not in inventory:
        print("Error: Item not found.")
        return

    while True:
        try:
            item_id = int(item_id)
        except ValueError:
            print("Invalid input! Please enter a valid integer for the item ID.")
            continue
        item_id_old = inventory[item_id]
        print("Enter new values (press Enter to keep existing values): ")
        new_name = input(f'Current Name: {item_id_old["name"]} | New Name: ').strip()
        if not new_name:
            new_name = item_id_old["name"]
        new_quantity = input(f'Current Quantity: {item_id_old["quantity"]} | New Quantity: ').strip()
        if not new_quantity:
            new_quantity = item_id_old["quantity"]
        if not new_quantity.isdigit():
            print("Invalid input! Enter a valid integer for quantity.")
            continue
        new_quantity = int(new_quantity)
        new_price = input(f'Current Price: {item_id_old["price"]} | New Quantity: ').strip()
        try:
            new_price = float(new_price)
        except ValueError:
            print("Invalid input! Please enter a valid number for the price.")
            continue
        if not new_price:
            new_price = item_id_old["price"]
        inventory[item_id] = {
            "name": new_name,
            "quantity": new_quantity,
            "price": new_price
        }
        print("Item updated successfully!")
        return inventory


def remove_item():
    item_id = input("Enter the ID of the item to remove: ").strip()
    if item_id in inventory:
        del inventory[item_id]
        print("Item removed successfully!")
    else:
        print("Error: Item not found.")

def view_inventory():
    if not inventory:
        print("No items in inventory.")
        return

    print("Current Inventory:")
    print("-" * 60)
    print(f"{'ID':<6}{'Name':<12}{'Quantity':>10}{'Price':>14}{'Total Value':>16}")
    print("-" * 60)
    for item_id, content in inventory.items():
        name = content["name"]
        quantity = content["quantity"]
        price = content["price"]
        value = quantity * price
        print(f"{item_id:<6}{name:<12}{quantity:>10}{price:>14}{value:>16}")
    print("-" * 60)

def check_total_value():
    total = 0
    for item_id, content in inventory.items():
        quantity = content["quantity"]
        price = content["price"]
        value = quantity * price
        total += value
    print(f"Total Inventory value: {total: .2f}")

def find_low_stock():
    print("Checking for Low Stock Items")
    num = input("Enter the low stock threshold: ")
    try:
        num = int(num)
    except ValueError:
        print("Invalid input! Please enter a valid integer.")
    else:
        for item_id, content in inventory.items():
            name = content["name"]
            quantity = content["quantity"]
            if quantity <= num:
                print("Items with Low Stock: ")
                print(f"- Name: {name}, ID: {item_id}, Quantity: {quantity}")
            elif quantity > num:
                print("No items with low stock.")

def main():
    while True:
        print("Inventory Management System")
        print("1. Add a new item")
        print("2. Update an item")
        print("3. Remove an item")
        print("4. Display all inventory")
        print("5. Check inventory value")
        print("6. Find items with low stock")
        print("7. Exit Program")

        choice = input("Choose an option (1-7): ").strip()

        if choice == "1":
            add_item()
        elif choice == "2":
            update_item()
        elif choice == "3":
            remove_item()
        elif choice == "4":
            view_inventory()
        elif choice == "5":
            check_total_value()
        elif choice == "6":
            find_low_stock()
        elif choice == "7":
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 7.")

if __name__ == "__main__":
    main()