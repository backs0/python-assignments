inventory = {
    1001: {"name": "Laptop", "quantity": 10, "price": 1000},
    1002: {"name": "Monitor", "quantity": 5, "price": 200},
}

def add_item():
    item_id = input("Enter item ID (unique integer): ").strip()
    if item_id in inventory:
        print("Error: Item ID already exists.")
        return

    while True:
        try:
            item_value = int(input("Enter new values (press Enter to keep existing values): ").strip())
            break
        except ValueError:
            print("Invalid input! Please enter a whole number.")

    inventory[item_id] = [item_value]
    print("Item added successfully!")

def update_item():
    pass

def remove_item():
    item_id = input("Enter the ID of the item to remove: ").strip()
    if name in students:
        del students[name]
        print("Item removed successfully!")
    else:
        print("Error: Item not found.")

def view_inventory():
    pass

def check_total_value():
    pass

def find_low_stock():
    pass

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
            print("Exit Program")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 7.")

if __name__ == "__main__":
    main()