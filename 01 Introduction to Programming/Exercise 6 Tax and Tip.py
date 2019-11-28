
#To determine the percent of a number do the following steps:
#1- Multiply the number by the percent (e.g. 87 * 68 = 5916).
#2- Divide the answer by 100 (Move decimal point two places to the left) (e.g. 5916/100 = 59.16).
#3- Round to the desired precision (e.g. 59.16 rounded to the nearest whole number = 59).
# for more detail visi https://www.aaamath.com/rat61ax2.htm.
print("\n\nProgram start from here...\n")


# Cost of a meal entered by user. Or simply user input.
user_meal_cost = float(input("Enter cost of meal you have ordered: "))


# Sales Tax Rate in Pakistan is expected to be 17.00 percent.
# Compute the tip as 18.00 percent of the meal amount (without the tax).
# So that 18 + 17 = 35 %.
tax             = (user_meal_cost * 17) / 100
tip             = (user_meal_cost * 18) / 100
total_tax       = tip + tax
over_all_cost   = user_meal_cost + total_tax


# Output of the program.
print("\n\nTax       = $%.2f."                               %(tax))
print("Tip       = $%.2f."                                   %(tip))
print("Tip + Tax = $%.2f."                              %(total_tax))
print("\nOver all cost including tip and tax is $%.2f." %(over_all_cost))