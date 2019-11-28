print("\n\nProgram start now...\n")

#
# A polygon is regular if its sides are all the same length and the angles between all of the adjacent sides are equal.
# This program compute the Area of a Regular Polygon.
#
    
from math import pi, tan

# Reads input as "s" and "n" from the user.
s = float(input("Enter the size of all sides of Polygon: "))
n = int(input("Enter the number of sides of Polygon  : "))

# Area of polygon can be computed by the formula below.
area = n * s ** 2 / 4 * tan(pi / n)

# Output of the program.
print()
print("The Area of Regular Polygon = %.3f. " %area)