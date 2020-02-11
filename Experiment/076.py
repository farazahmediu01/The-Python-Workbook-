# intialzing the list of Members.
members = list()

def input_loop(limit=5):
    '''This function append each member into the list of members
    with default limit 5 or user can skip prompt by pressing enter.
    There are two conditions for loop to stop. First one is lenght
    of members list is smaller then 5 and second one if user enter
    empty string loop will stop working.'''
  
    user_input = None
    while (len(members) < limit) and (user_input != ''):
        user_input = input(">")
        if user_input:
            members.append(user_input)

# start with taking user input.
print("\nEnter 5 names of your friends which you want to invite in your party, \
(press enter to skip).")
input_loop()

# formatting output.
if members:
    print(F"\nYou have invited {len(members)} members.")
    for member in sorted(members):
        print(member.title())
else:
    print("\nSorry, You have not invited any person.")

# Asking for more information 
print("\nDo you want to invite more friends? press 'y' to contineu and 'n' to exit.")
verification = input(">")

# if user say yes the loop runs otherwise it says bye to user.
if verification.lower() == "y":
    print("\nHow many friends you want to invite?")
    limit = int(input("Enter number only: "))
    print(f"Please enter {limit} names, (press enter to skip).")
    limit += len(members)    
    input_loop(limit)

    print("\nList of all members you have invited:")
    for member in sorted(members):
        print(member.title())
else:
    print("\nThank you, See you later!")