from guitar import Guitar

FILENAME = "guitars.csv"

def main():
    """Load guitars from file, allow user to add more, then save to file."""
    guitars = load_guitars(FILENAME)
    print("These are my guitars:")
    display_guitars(guitars)

    # Let user add new guitars
    guitars.extend(get_new_guitars())

    # Sort guitars by year
    guitars.sort()
    print("\nSorted guitars:")
    display_guitars(guitars)

    # Save updated list back to file
    save_guitars(FILENAME, guitars)


def load_guitars(filename):
    """Read guitars from a CSV file and return a list of Guitar objects."""
    guitars = []
    with open(filename, "r") as file:
        for line in file:
            name, year, cost = line.strip().split(",")
            guitars.append(Guitar(name, int(year), float(cost)))
    return guitars


def display_guitars(guitars):
    """Display a list of guitars."""
    for i, guitar in enumerate(guitars, 1):
        print(f"Guitar {i}: {guitar}")


def get_new_guitars():
    """Prompt user for new guitars and return a list of Guitar objects."""
    new_guitars = []
    print("\nAdd new guitars (leave name blank to stop):")
    name = input("Name: ")
    while name:
        year = int(input("Year: "))
        cost = float(input("Cost: "))
        new_guitar = Guitar(name, year, cost)
        new_guitars.append(new_guitar)
        name = input("Name: ")
    return new_guitars


def save_guitars(filename, guitars):
    """Write the list of Guitar objects to a CSV file."""
    with open(filename, "w") as file:
        for guitar in guitars:
            file.write(f"{guitar.name},{guitar.year},{guitar.cost}\n")


main()
