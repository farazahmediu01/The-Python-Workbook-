print("\n\nThe program start now...\n")

# User input number of cents.
cents       = int(input("Enter number of cents:   "))

# calculation of how many coines in cents given by user.
pennies     = 4 
nickels     = 8
dimes       = 10
quarters    = 50
loonies     = 100
toonies     = 200

# Output of program.

print("In change the total toonies  =",     cents // toonies)
cents = cents % toonies

print("In change the total loonies  =",     cents // loonies)
cents = cents % loonies

print("In change the total quarters =",     cents // quarters)
cents = cents % quarters  

print("In change the total dimes    =",     cents // dimes)
cents =  cents  % nickels

print("In change the total nickels  =",     cents // nickels)
cents = cents % pennies  

print("In change the total pennies  =",     cents // pennies)