"""
Emails
Estimate: 15 minutes
Actual:
"""

email_to_name = {}

email = input("Email: ")
while email != "":
    email_to_name[email] = ""
    email = input("Email: ")

print(email_to_name)