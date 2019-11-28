##
# Compute the total due when several items are purchased. The amount payable for cash
# transactions is rounded to the closest nickel because pennies have been phased out in Canada.
#
PENNIES_PER_NICKEL = 5
NICKEL             = 0.05
#While it is highly unlikely that the number of pennies in a nickel will ever change, it is
#possible (even likely) that we will need to update our program at some point in the future so
#that it rounds to the closest dime. Using constants will make it easier to perform that update
#when it is needed.

# Track the total cost for all of the items
total = 0.00
# Read the price of the first item as a string
line = input("Enter the price of the item (blank to quit): ")
# Continue reading items until a blank line is entered
while line != "":
# Add the cost of the item to the total (after converting it to a floating-point number)
    total = total + float(line)
# Read the cost of the next item
    line = input("Enter the price of the item (blank to quit): ")
# Display the exact total payable
print("The exact amount payable is %.02f" % total)
# Compute the number of pennies that would be left if the total was paid using nickels

rounding_indicator = total * 100 % PENNIES_PER_NICKEL

'''
© Springer Nature Switzerland AG 2019
B. Stephenson, The Python Workbook, Texts in Computer Science,
https://doi.org/10.1007/978-3-030-18873-3_11
161
162 11 Solutions to the Repetition Exercises '''

if rounding_indicator < PENNIES_PER_NICKEL / 2:
# If the number of pennies left is less than 2.5 then we round down by subtracting that
# number of pennies from the total
    cash_total = total - rounding_indicator / 100
else:
# Otherwise we add a nickel and then subtract that number of pennies
    cash_total = total + NICKEL - rounding_indicator / 100
# Display amount due when paying with cash
print("The cash amount payable is %.02f" % cash_total)