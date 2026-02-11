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

tax_rates = {
    "Alabama": 4.00,
    "Alaska": 1.82,
    "Arizona": 5.60,
    "Arkansas": 6.50,
    "California": 7.25,
    "Colorado": 2.90,
    "Connecticut": 6.35,
    "Delaware": 0.00,
    "Florida": 6.00,
    "Georgia": 4.00,
    "Hawaii": 4.00,
    "Idaho": 6.00,
    "Illinois": 6.25,
    "Indiana": 7.00,
    "Iowa": 6.00,
    "Kansas": 6.50,
    "Kentucky": 6.00,
    "Louisiana": 5.00,
    "Maine": 5.50,
    "Maryland": 6.00,
    "Massachusetts": 6.25,
    "Michigan": 6.00,
    "Minnesota": 6.88,
    "Mississippi": 7.00,
    "Missouri": 4.23,
    "Montana": 0.00,
    "Nebraska": 5.50,
    "Nevada": 6.85,
    "New Hampshire": 0.00,
    "New Jersey": 6.63,
    "New Mexico": 4.88,
    "New York": 4.00,
    "North Carolina": 4.75,
    "North Dakota": 5.00,
    "Ohio": 5.75,
    "Oklahoma": 4.50,
    "Oregon": 0.00,
    "Pennsylvania": 6.00,
    "Rhode Island": 7.00,
    "South Carolina": 6.00,
    "South Dakota": 4.20,
    "Tennessee": 7.00,
    "Texas": 6.25,
    "Utah": 6.10,
    "Vermont": 6.00,
    "Virginia": 5.30,
    "Washington": 6.50,
    "West Virginia": 6.00,
    "Wisconsin": 5.00,
    "Wyoming": 4.00
}

state = input("Enter your state name: ")

prices = []

while True:
    item = input("Enter item price (or type 'done'): ")

    if item == "done":
        break

    prices.append(float(item))

subtotal = sum(prices)
tax = subtotal * (tax_rates[state] / 100)
total = subtotal + tax

print("Sales tax: $", round(tax, 2))
print("Total cost: $", round(total, 2))
