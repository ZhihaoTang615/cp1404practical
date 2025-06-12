"""
CP1404/CP5632 Practical
Quick Pick Lottery Ticket Generator
"""

import random

NUMBERS_PER_PICK = 6
MIN_NUMBER = 1
MAX_NUMBER = 45

def main():
    number_of_picks = int(input("How many quick picks? "))
    for _ in range(number_of_picks):
        quick_pick = generate_quick_pick()
        # Format: print numbers right-aligned in 2-digit columns
        print(" ".join(f"{num:2}" for num in quick_pick))

def generate_quick_pick():
    """Generate one quick pick of non-repeating, sorted numbers."""
    numbers = []
    while len(numbers) < NUMBERS_PER_PICK:
        num = random.randint(MIN_NUMBER, MAX_NUMBER)
        if num not in numbers:
            numbers.append(num)
    numbers.sort()
    return numbers

main()
