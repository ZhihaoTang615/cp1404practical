"""
CP1404/CP5632 Practical
Refactored cumulative total income program
"""

def main():
    """Display income report for incomes over a given number of months."""
    incomes = []
    number_of_months = int(input("How many months? "))  # ✅ renamed for clarity

    for month in range(1, number_of_months + 1):
        income = float(input(f"Enter income for month {month}: "))  # ✅ use f-string
        incomes.append(income)

    print_income_report(incomes)


def print_income_report(incomes):
    """Print formatted income report from the given income list."""
    print("\nIncome Report\n-------------")
    total = 0
    for month in range(1, len(incomes) + 1):
        income = incomes[month - 1]
        total += income
        print(f"Month {month:2} - Income: ${income:10.2f} Total: ${total:10.2f}")
