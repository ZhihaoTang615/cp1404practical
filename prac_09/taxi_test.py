"""
CP1404/CP5632 Practical
Test program for the Taxi class
"""

from prac_09.taxi import Taxi



def main():
    """Test Taxi class functionality."""
    # Step 1: Create a new Taxi object
    my_taxi = Taxi("Prius 1", 100)

    # Step 2: Drive the taxi 40 km
    my_taxi.drive(40)

    # Step 3: Print the taxi's details and fare
    print(my_taxi)
    print(f"Current fare: ${my_taxi.get_fare():.2f}")

    # Step 4: Restart the fare and drive again
    my_taxi.start_fare()
    my_taxi.drive(100)

    # Step 5: Print details and new fare
    print(my_taxi)
    print(f"Current fare: ${my_taxi.get_fare():.2f}")


main()
