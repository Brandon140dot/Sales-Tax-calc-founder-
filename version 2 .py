price = float(input("Enter the price of the item: "))

tax_rate = 0.06625  # New Jersey sales tax
tax = price * tax_rate
total = price + tax

print("Sales tax: $", round(tax, 2))
print("Total cost: $", round(total, 2))
prices = []

while True:
    item = input("Enter item price (or type 'done'): ")

    if item == "done":
        break

    prices.append(float(item))

subtotal = sum(prices)
tax_rate = 0.06625
tax = subtotal * tax_rate
total = subtotal + tax

print("Sales tax: $", round(tax, 2))
print("Total cost: $", round(total, 2))
