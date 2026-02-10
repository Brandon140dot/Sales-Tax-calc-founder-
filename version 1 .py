price = float(input("Enter the price of the item: "))

tax_rate = 0.06625  # New Jersey sales tax
tax = price * tax_rate
total = price + tax

print("Sales tax: $", round(tax, 2))
print("Total cost: $", round(total, 2))
