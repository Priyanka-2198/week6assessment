def parse_transaction_line(line_text):
    """
    Parses a single transaction line and returns (description, amount).
    Returns None if the line is invalid.
    """
    line_text = line_text.strip()

    # Ignore empty lines
    if line_text == "":
        return None

    try:
        description, amount_text = line_text.split(",")
        amount = float(amount_text)
        return description, amount

    except ValueError:
        print(f"Skipping invalid line: {line_text}")
        return None


def load_transactions(filename):
    """
    Reads file and returns valid transactions + total amount.
    """
    transactions = []
    total_amount = 0  # 👉 NEW: total tracker

    try:
        with open(filename, "r") as file:
            for line_text in file:
                result = parse_transaction_line(line_text)

                if result is not None:
                    description, amount = result
                    transactions.append(result)

                    # 👉 Add to total
                    total_amount += amount

    except FileNotFoundError:
        print("File not found!")

    return transactions, total_amount


# Main program
file_name = "transactions.txt"

transactions, total = load_transactions(file_name)

print("\nValid Transactions:")
for description, amount in transactions:
    print(f"{description}: ${amount}")

print("\nTotal Balance:")
print(f"${total}")