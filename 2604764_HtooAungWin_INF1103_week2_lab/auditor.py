
inventory = 0
failed_entries = 0

print("=" * 42)
print("       WELCOME TO INVENTORY AUDITOR")
print("=" * 42)
print("Track stock quantities safely.")
print("The maximum inventory limit is 500 units.")
print("Type 'quit' at any time to finish.\n")

while True:
    stock_input = input(
        "Enter stock quantity: "
    ).strip()

    if stock_input.lower() == "quit":
        print("\n" + "=" * 42)
        print("              AUDIT SUMMARY")
        print("=" * 42)
        print(f"Total Units Processed: {inventory}")
        print(f"Total Failed Entries: {failed_entries}")
        print("=" * 42)
        print("Thank you for using Inventory Auditor!")
        break

    try:
        stock_quantity = int(stock_input)
    except ValueError:
        print("Invalid input. Please enter a valid stock quantity.")
        failed_entries += 1
        continue

    if stock_quantity < 0:
        print("Invalid input. Stock quantity cannot be negative.")
        failed_entries += 1
        continue

    if inventory + stock_quantity > 500:
        print("Inventory limit exceeded. Cannot add more stock.")
        failed_entries += 1
        continue

    inventory += stock_quantity
