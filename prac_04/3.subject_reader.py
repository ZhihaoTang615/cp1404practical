"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    data = load_data()
    display_subjects(data)


def load_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    subject_data = []
    input_file = open(FILENAME)
    for line in input_file:
        line = line.strip()
        parts = line.split(',')
        parts[2] = int(parts[2])
        subject_data.append(parts)
    input_file.close()
    return subject_data


def display_subjects(data):
    """Display subject details in formatted output."""
    for subject_code, lecturer, students in data:
        print(f"{subject_code} is taught by {lecturer} and has {students} students")


main()
