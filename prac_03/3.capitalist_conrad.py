"""
CP1404/CP5632 - Practical
Capitalist Conrad wants a stock price simulator for a volatile stock.
The price starts off at $10.00, and, at the end of every day there is
a 50% chance it increases by 0 to 17.5%, and
a 50% chance that it decreases by 0 to 5%.
If the price rises above $100 or falls below $1, the program should end.
The price should be displayed to the nearest cent.
The output is written to a file.
"""

import random

# Constants
MAX_INCREASE = 0.175  # 17.5%
MAX_DECREASE = 0.05   # 5%
MIN_PRICE = 1.0
MAX_PRICE = 100.0
INITIAL_PRICE = 10.0
FILENAME = "output.txt"

# Initial values
price = INITIAL_PRICE
number_of_days = 0

# Open output file
out_file = open(FILENAME, 'w')

# Write starting price
print(f"Starting price: ${price:,.2f}", file=out_file)

# Price simulation loop
while MIN_PRICE <= price <= MAX_PRICE:
    price_change = 0

    if random.randint(1, 2) == 1:
        # Price increases
        price_change = random.uniform(0, MAX_INCREASE)
    else:
        # Price decreases
        price_change = random.uniform(-MAX_DECREASE, 0)

    price *= (1 + price_change)
    number_of_days += 1




    print(f"On day {number_of_days} price is: ${price:,.2f}", file=out_file)

# Close the file after writing
out_file.close()
