"""
CP1404/CP5632 - Practical
Pseudocode for temperature conversion
"""

# MENU = """C - Convert Celsius to Fahrenheit
# F - Convert Fahrenheit to Celsius
# Q - Quit"""
# print(MENU)
# choice = input(">>> ").upper()
# while choice != "Q":
#     if choice == "C":
#         celsius = float(input("Celsius: "))
#         fahrenheit = celsius * 9.0 / 5 + 32
#         print(f"Result: {fahrenheit:.2f} F")
#     elif choice == "F":
#         fahrenheit = float(input("Fahrenheit: "))
#         celsius = 5 / 9 * (fahrenheit - 32)
#         print(f"Result: {celsius:.2f} C")
#     else:
#         print("Invalid option")
#     print(MENU)
#     choice = input(">>> ").upper()
# print("Thank you.")


def print_menu():
    print("C - Convert Celsius to Fahrenheit\nF - Convert Fahrenheit to Celsius\nQ - Quit")

def convert_celsius_to_fahrenheit():
    celsius = float(input("Celsius: "))
    fahrenheit = celsius * 9.0 / 5 + 32
    return fahrenheit

def convert_Fahrenheit_Celsius():
    fahrenheit = float(input("Fahrenheit: "))
    celsius = 5 / 9 * (fahrenheit - 32)
    return celsius

def main():
    print_menu()
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            fahrenheit = convert_celsius_to_fahrenheit()
            print(f"Result: {fahrenheit:.2f} F")
        elif choice == "F":
            celsius = convert_Fahrenheit_Celsius()
            print(f"Result: {celsius:.2f} C")
        else:
            print("Invalid option")
        print_menu()
        choice = input(">>> ").upper()
    print("Thank you.")
main()