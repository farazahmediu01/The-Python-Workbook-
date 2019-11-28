print("\n\nProgram start noe...\n")
#To determine the percent of a number do the following steps:
#1- Multiply the number by the percent (e.g. 87 * 68 = 5916).
#2- Divide the answer by 100 (Move decimal point two places to the left) (e.g. 5916/100 = 59.16).
#3- Round to the desired precision (e.g. 59.16 rounded to the nearest whole number = 59).
# for more detail visi https://www.aaamath.com/rat61ax2.htm.

# Useful Constants.
regular  = 3.49        # price of a loave of bread. 
day_old  = regular * 0.40  # price of a day old loave of bread with 60 percent discount.

# User input the number of purchased day old bread.
inp = int(input("Enter the number of day old bread you have purchased: "))

# Calculation.
regular = regular * inp
day_old = day_old * inp 
disc    = regular - day_old

# Output of the program.
print()
print("The total cost of day old bread you have purchased = $ %.2f" %day_old)
print("The total cost if you purchased regular bread      = $ %.2f" %regular)
print("Total discount you got on purchase a day old bread = $ %.2f" %disc)

