from car import Car

def main():
    """Test Car class with a Limo example."""
    # Create a new Car object named "Limo" with 100 units of fuel
    limo = Car("Limo", 100)

    # Add 20 more units of fuel
    limo.add_fuel(20)

    # Print the current amount of fuel
    print(f"Fuel in limo: {limo.fuel}")

    # Attempt to drive 115 km
    distance_driven = limo.drive(115)
    print(f"Limo drove {distance_driven} km")

    # Print the car object (uses __str__ method)
    print(limo)

if __name__ == '__main__':
    main()



