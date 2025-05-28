"""
Scores
File: score.py

Your main function should ask the user for their score and print the result.
Write a new function that takes in the user's score as a parameter and returns the result to be printed.
Follow SRP: The function should not print it.

Now add a new part to the bottom of your main function that generates a random score and prints the result.
You do NOT need to write a different function to determine the result for the random score.
If you've written your new function properly, you can use it.
If you've breached SRP, then you'll see that you can't.
"""


import random



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

def main():
    score = get_valid_score()
    result = result_score(score)
    print(f"Your score is {score}, it is {result}")

    random_score = random.randint(0, 100)
    result = result_score(random_score)
    print(f"Your random score is {random_score}, it is {result}")
main()