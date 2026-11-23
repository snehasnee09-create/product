
import sys

def product_details(pid, name, quantity, price):
    return (
        f"Product ID: {pid}\n"
        f"Product Name: {name}\n"
        f"Quantity: {quantity}\n"
        f"Price: {price}"
    )

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python product.py <pid> <name> <quantity> <price>")
        sys.exit(1)

    pid = sys.argv[1]
    name = sys.argv[2]

    try:
        quantity = int(sys.argv[3])
        price = float(sys.argv[4])
    except ValueError:
        print("Error: Quantity must be an integer and price must be a number.")
        sys.exit(1)

    print("\nProduct Details")
    print("---------------------")
    print(product_details(pid, name, quantity, price))
