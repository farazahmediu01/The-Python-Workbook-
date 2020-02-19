print("Enter a series of pizza toppings, press enter to quit.")

active = True

while active:
    user_input = input(">")
    message = f"\nYou have included {user_input.title()}."

    if user_input:
        print(message)
    else:
        active = False
    