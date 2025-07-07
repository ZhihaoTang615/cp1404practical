from guitar import Guitar

def main():
    """Test get_age() and is_vintage() methods of the Guitar class."""

    # Test guitars
    guitar1 = Guitar("Gibson L-5 CES", 1922, 16035.40)
    guitar2 = Guitar("Another Guitar", 2013, 1000.00)

    # Expected values may change based on current year
    current_year = 2022  # Adjust if needed
    expected_age1 = current_year - guitar1.year
    expected_age2 = current_year - guitar2.year

    print(f"{guitar1.name} get_age() - Expected {expected_age1}. Got {guitar1.get_age()}")
    print(f"{guitar2.name} get_age() - Expected {expected_age2}. Got {guitar2.get_age()}")

    print(f"{guitar1.name} is_vintage() - Expected True. Got {guitar1.is_vintage()}")
    print(f"{guitar2.name} is_vintage() - Expected False. Got {guitar2.is_vintage()}")

if __name__ == '__main__':
    main()
