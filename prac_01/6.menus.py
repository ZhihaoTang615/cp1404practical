"""
get name
display menu
get choice
while choice != Q
   if choice == H
       display "hello" name
   else if choice == G
       display "goodbye" name
   else
       display invalid message
   display menu
   get choice
display finished message
"""

user_name = input("Enter your name: ")
menu = str("(H)ello\n(G)oodbye\n(Q)uit" )
print(menu)

choice = str(input(">>>")).upper()
while choice != "Q":
    if choice == "H":
        print("Hello " + user_name)
    elif choice == "G":
        print("Goodbye " + user_name)
    else:
        print("Invalid choice")
    print(menu)
    choice = str(input(">>>")).upper()
print("Finished.")

