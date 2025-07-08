from guitar import Guitar


FILENAME = "guitars.csv"


def main():
    """Read and update guitar collection."""
    guitars = load_guitars(FILENAME)
    print("These are my guitars:")
    display_guitars(guitars)

    # Add new guitars from user input
    guitars.extend(add_new_guitars())

    # Sort guitars by year (requires __lt__ in Guitar class)
    guitars.sort()
    print("\nThese are my guitars sorted by year:")
    display_guitars(guitars)

    # Save updated list to file
    save_guitars(FILENAME, guitars)


def load_guitars(filename):
    """Load guitars from CSV file."""
    guitars = []
    with open(filename, 'r') as in_file:
        for line in in_file:
            name, year, cost = line.strip().split(',')
            guitar = Guitar(name, int(year), float(cost))
            guitars.append(guitar)
    return guitars


def display_guitars(guitars):
    """Print a list of guitars with index."""
    for i, guitar in enumerate(guitars, 1):
        print(f"Guitar {i}: {guitar}")


def add_new_guitars():
    """Ask user to input new guitars, return list of new Guitar objects."""
    new_guitars = []
    print("\nAdd new guitars (leave name blank to stop):")
    name = input("Name: ")
    while name:
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        new_guitar = Guitar(name, year, cost)
        new_guitars.append(new_guitar)
        print(f"{new_guitar} added.\n")
        name = input("Name: ")
    return new_guitars


def save_guitars(filename, guitars):
    """Save all guitars to the CSV file."""
    with open(filename, 'w') as out_file:
        for guitar in guitars:
            print(f"{guitar.name},{guitar.year},{guitar.cost}", file=out_file)


if __name__ == "__main__":
    main()
