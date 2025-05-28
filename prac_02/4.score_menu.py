"""
File: score_menu.py

In the lecture there was a "do this now" activity similar to this, so you can use what we did there to help with this program.

Write a complete Python program following the standard structure that uses a main and other functions.
Use a main menu following the standard menu pattern.

The menu should have four separate options:

(G)et a valid score (must be 0-100 inclusive)
(P)rint result (copy or import your function to determine the result from score.py)
(S)how stars (this should print as many stars as the score)
(Q)uit
Handle each of these (except quit) separately, and consider how you can reuse your functions.

In main(), before the menu loop, get a valid score using your function.
When the user quits, say some kind of "farewell".



display menu
get choice
while choice != <quit option>
    if choice == <first option>
        <do first task>
    else if choice == <second option>
        <do second task>
    ...
    else if choice == <n-th option>
        <do n-th task>
    else
        display invalid input error message
    display menu
    get choice
<do final thing, if needed>
"""





def display_menu():
    print("\nMenu:")
    print("(G)et a valid score")
    print("(P)rint result")
    print("(S)how stars")
    print("(Q)uit")

def get_valid_score():
    score = float(input("Enter score: "))
    while score < 0 or score > 100:
        print("Invalid score")
        score = float(input("Score must be between 0 and 100 inclusive:"))
    return score


def result_score(score):
    if score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


def show_stars(score):
    print("*" * int(score))

def main():

    display_menu()
    choice = str(input(">>>: ")).upper()
    while choice != "Q":

        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            print(f"Result: {result_score(score)}")
        elif choice == "S":
            show_stars(score)
        else:
            print("Invalid input")

        display_menu()
        choice = input(">>>: ").upper()

    print("Farewell!")
main()