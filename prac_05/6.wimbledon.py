"""
CP1404/CP5632 Practical
Wimbledon
Estimate: 30 minutes
Actual: 35 minutes
"""

FILENAME = "wimbledon.csv"


def main():
    data = load_wimbledon_data(FILENAME)
    champions_to_wins = count_champion_wins(data)
    countries = extract_countries(data)

    print("Wimbledon Champions:")
    for champion, wins in sorted(champions_to_wins.items()):
        print(f"{champion:20} {wins}")

    print(f"\nThese {len(countries)} countries have won Wimbledon:")
    print(", ".join(sorted(countries)))


def load_wimbledon_data(filename):
    """Load Wimbledon data from CSV and return a list of rows."""
    with open(filename, encoding="utf-8-sig") as in_file:
        next(in_file)  # skip header
        return [line.strip().split(",") for line in in_file]


def count_champion_wins(data):
    """Count how many times each champion has won."""
    champions_to_wins = {}
    for row in data:
        champion = row[2]
        champions_to_wins[champion] = champions_to_wins.get(champion, 0) + 1
    return champions_to_wins


def extract_countries(data):
    """Extract a set of unique champion countries."""
    return {row[1] for row in data}


if __name__ == '__main__':
    main()
