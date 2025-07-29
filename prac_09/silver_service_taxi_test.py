"""
CP1404/CP5632 Practical
Test program for SilverServiceTaxi class
"""

from prac_09.silver_service_taxi import SilverServiceTaxi


def main():
    """Test the SilverServiceTaxi class with a sample trip."""

    # Create a SilverServiceTaxi with fanciness 2 (i.e., double price per km)
    fancy_taxi = SilverServiceTaxi("Limo", 100, fanciness=2)

    # Start a new fare and drive 18 km
    fancy_taxi.start_fare()
    fancy_taxi.drive(18)

    # Print taxi details and calculated fare
    print(fancy_taxi)
    print(f"Fare for 18km trip: ${fancy_taxi.get_fare():.2f}")


main()
