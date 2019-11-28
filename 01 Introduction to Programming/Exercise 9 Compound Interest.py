print("\n\nProgram start now...\n")

# User enter the amount desposited into the account.
amount = int(input("Enter amount deposited into your account: "))


# Compute the four persent (4 %) interest of all amount and add it into the total amount.
interest          = amount * 0.04           # Four persent (4 %) interest on all over amount.
interest_1        = interest + amount       # Interest after one year.
interest_2        = interest * 2 + amount   # Interest after two years.
interest_3        = interest * 3 + amount   # Interest after three years.
err               = "%"
# Output of the program.
print("\n\nThe four persent (4%s) interest on all all over amount is %.2f.\n" %(err,interest))
print("The amount in your savings account after 1 year is %.2f."              %(interest_1))
print("The amount in your savings account after 2 year is %.2f."              %(interest_2))
print("The amount in your savings account after 3 year is %.2f."              %(interest_3))