print("\n\nProgram start now...\n")
# This proram is for making change.

# User input or the amount which have been entered for making change.
rupees = int(input("Enter amount in Rupees: "))

# Setting variables, all possible amount of change.
one_rup             = 1
two_rup             = 2
five_rup            = 5
ten_rup             = 10
twenty_rup          = 20
fifty_rup           = 50
hundred_rup         = 100
five_hundered_rup   = 500
thousand_rup        = 1000

# Output of the program.
print("Thousand Rupees     =",            (rupees // thousand_rup))
rupees = rupees % thousand_rup

print("Five Hundred Rupees =",            (rupees // five_hundered_rup))
rupees = rupees % five_hundered_rup

print("Hundred Rupees      =",            (rupees // hundred_rup))
rupees = rupees % hundred_rup

print("Fifty Ruppes        =",            (rupees // fifty_rup))
rupees = rupees % fifty_rup

print("Twenty Rupees       =",            (rupees // twenty_rup))
rupees = rupees % twenty_rup

print("Ten Rupees          =",            (rupees // ten_rup))
rupees = rupees % ten_rup

print("Five Ruppes         =",            (rupees // five_rup))
rupees = rupees % five_rup

print("Two Rupees          =",            (rupees // two_rup))
rupees = rupees % two_rup

print("One Ruppes          =",            (rupees // one_rup))
rupees = rupees % one_rup