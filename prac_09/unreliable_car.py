"""
CP1404/CP5632 Practical
UnreliableCar class - inherits from Car
"""

import random
from prac_09.car import Car  # Adjust this if needed based on your project structure


class UnreliableCar(Car):
    """A Car that might not drive when asked, depending on reliability."""

    def __init__(self, name, fuel, reliability):
        """Initialise an UnreliableCar."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """
        Drive the car if it's reliable enough.
        Return the distance driven (0 if the car fails to drive).
        """
        random_chance = random.uniform(0, 100)
        if random_chance < self.reliability:
            return super().drive(distance)
        else:
            return 0
