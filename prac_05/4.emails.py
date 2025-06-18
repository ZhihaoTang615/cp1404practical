"""
Emails
Estimate: 15 minutes
Actual: 12 minutes
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

for email, name in email_to_name.items():
    print(f"{name} ({email})")


