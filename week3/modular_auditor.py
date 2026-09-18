MAX_INVENTORY = 500
TAX_RATE = 0.10


def get_valid_input():
    stock_input = input(
        "Enter the stock count (or type 'quit' to quit): "
    ).strip()

    if stock_input.lower() == "quit":
        return "quit"

    try:
        stock_quantity = int(stock_input)
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
        return None

    if stock_quantity < 0:
        print("Invalid input. Please enter a non-negative integer.")
        return None

    return stock_quantity


def process_delivery(current_total, new_value):
    return current_total + new_value


def calculate_tax(amount):
    return amount * TAX_RATE


def generate_report(total_units, failed_attempts):
    print("\n" + "=" * 42)
    print("              AUDIT SUMMARY")
    print("=" * 42)
    print(f"Total Units Processed: {total_units}")
    print(f"Total Failed Entries: {failed_attempts}")
    print("=" * 42)
    print("Thank you for using Inventory Auditor!")


def main():
    inventory = 0
    failed_attempts = 0

    print("=" * 42)
    print("       WELCOME TO INVENTORY AUDITOR")
    print("=" * 42)
    print("Track stock quantities safely.")
    print(f"The maximum inventory limit is {MAX_INVENTORY} units.")
    print("Type 'quit' at any time to finish.\n")

    while True:
        delivery = get_valid_input()

        if delivery == "quit":
            generate_report(inventory, failed_attempts)
            return

        if delivery is None:
            failed_attempts += 1
            continue

        if inventory + delivery > MAX_INVENTORY:
            print("Inventory limit exceeded. Cannot add more stock.")
            failed_attempts += 1
            continue

        inventory = process_delivery(inventory, delivery)
        tax = calculate_tax(delivery)
        print(f"Delivery accepted. Tax for this delivery: {tax:.2f}")


if __name__ == "__main__":
    main()
