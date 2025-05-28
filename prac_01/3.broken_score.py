"""
2. Debugging:
File: broken_score.py

Someone was trying to write a program to tell the user if their score is invalid, bad, passable or excellent, but their code doesn't work.

Rewrite the following program using the most efficient if, elif, else structure you can. The code is available here at: broken_score.py
Remember to click Raw before copying and pasting so that you get proper formatting!

The intention is that the score must be between 0 and 100 inclusive; 90 or more is excellent; 50 or more is a pass; below 50 is bad. There is no intention to do any repetition.

Be very careful of your boundary conditions... and test systematically.
"""


"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""


score = float(input("Enter score: "))
while score < 0 or score > 100:
    print("Invalid score")
    score = float(input("Score must be between 0 and 100 inclusive:"))

if score >= 90:
    print(f"Your score is {score}, that's Excellent")
elif score >= 50:
    print(f"Your score is {score}, that's Passable")
else:
    print(f"Your score is {score}, that's Bad")
