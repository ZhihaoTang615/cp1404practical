"""
Emails
Estimate: 15 minutes
Actual:
"""

email_to_name = {}
email = input("Email: ")
while email != "":
    name = ' '.join(email.split('@')[0].split('.')).title()
    confirm = input(f"Is your name {name}? (Y/n) ").lower()
    if confirm != "" and confirm != "y":
        name = input("Name: ")
    email_to_name[email] = name
    email = input("Email: ")


print(email_to_name)