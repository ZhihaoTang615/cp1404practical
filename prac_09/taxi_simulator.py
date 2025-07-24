"""
CP1404/CP5632 Practical
Taxi simulator using Taxi and SilverServiceTaxi classes
"""

from prac_09.taxi import Taxi
from prac_09.silver_service_taxi import SilverServiceTaxi


def main():
    """Run the taxi simulator program."""
    taxis = [
        Taxi("Prius", 100),
        SilverServiceTaxi("Limo", 100, fanciness=2),
        SilverServiceTaxi("Hummer", 200, fanciness=4)
    ]

    current_taxi = None
    total_bill = 0.0

    print("Let's drive!")
    menu = "q)uit, c)hoose taxi, d)rive"
    print(menu)
    choice = input(">>> ").lower()

    while choice != "q":
        if choice == "c":
            # Display available taxis with index
            print("Taxis available:")
            for i, taxi in enumerate(taxis):
                print(f"{i} - {taxi}")
            try:
                taxi_choice = int(input("Choose taxi: "))
                current_taxi = taxis[taxi_choice]
            except (IndexError, ValueError):
                print("Invalid taxi choice")
        elif choice == "d":
            if current_taxi is None:
                print("You need to choose a taxi before you can drive")
            else:
                current_taxi.start_fare()
                try:
                    distance = float(input("Drive how far? "))
                except ValueError:
                    print("Invalid distance")
                    distance = 0
                current_taxi.drive(distance)
                trip_cost = current_taxi.get_fare()
                print(f"Your {current_taxi.name} trip cost you ${trip_cost:.2f}")
                total_bill += trip_cost
        else:
            print("Invalid option")

        print(f"Bill to date: ${total_bill:.2f}")
        print(menu)
        choice = input(">>> ").lower()

    # End of simulation
    print(f"Total trip cost: ${total_bill:.2f}")
    print("Taxis are now:")
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")


main()
