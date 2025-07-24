"""
CP1404/CP5632 Practical
Test program for UnreliableCar class
"""

from prac_09.unreliable_car import UnreliableCar


def main():
    """Test UnreliableCar with varying reliability."""

    # Create two cars: one very reliable, one unreliable
    reliable_car = UnreliableCar("Reliable", 100, reliability=90.0)
    unreliable_car = UnreliableCar("Unreliable", 100, reliability=10.0)

    print("Attempting to drive 10 times each...")

    print("\nReliableCar drives:")
    for i in range(10):
        distance = reliable_car.drive(10)
        print(f"Drive {i + 1}: {distance} km")

    print("\nUnreliableCar drives:")
    for i in range(10):
        distance = unreliable_car.drive(10)
        print(f"Drive {i + 1}: {distance} km")


main()
