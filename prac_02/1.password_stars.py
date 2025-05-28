def get_password():
    """Prompt the user to enter a password and return it."""
    return input("Enter your password: ")

def print_asterisks(password):
    """Print a line of asterisks equal to the length of the password."""
    print("*" * len(password))

def main():
    password = get_password()
    print_asterisks(password)

main()
