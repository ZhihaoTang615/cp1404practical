from guitar import Guitar
import csv

FILENAME = "guitars.csv"

def main():
    guitars = load_guitars(FILENAME)
    print("These are my guitars:")
    display_guitars(guitars)

    # Ask user for new guitars
    print("\nAdd new guitars:")
    while True:
        name = input("Name: ")
        if name == "":
            break
        year = int(input("Year: "))
        cost = float(input("Cost: "))
        new_guitar = Guitar(name, year, cost)
        guitars.append(new_guitar)

    # Display all guitars
    print("\nThese are all the guitars:")
    display_guitars(guitars)

    # Save updated list
    save_guitars(FILENAME, guitars)

def load_guitars(filename):
    """Load guitars from a CSV file."""
    guitars = []
    with open(filename, 'r') as in_file:
        for line in in_file:
            name, year, cost = line.strip().split(',')
            guitars.append(Guitar(name, int(year), float(cost)))
    return guitars

def save_guitars(filename, guitars):
    """Save the list of guitars to a CSV file."""
    with open(filename, 'w', newline='') as out_file:
        writer = csv.writer(out_file)
        for guitar in guitars:
            writer.writerow([guitar.name, guitar.year, guitar.cost])

def display_guitars(guitars):
    """Display all guitars nicely."""
    for i, guitar in enumerate(guitars, start=1):
        vintage_string = " (vintage)" if guitar.is_vintage() else ""
        print(f"Guitar {i}: {guitar}{vintage_string}")

main()
