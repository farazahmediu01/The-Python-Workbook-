print("\n\nProgram start now...\n")
from math import sqrt

#
# This program compute the area of a triangle when the lengths of all three sides are known.
#

# User input for each side of the triangle.
print("Enter Lenght for each side of the triangle.") 
s1 = float(input("Enter first side : "))
s2 = float(input("Enter second side: "))
s3 = float(input("Enter third side : "))

# Lets compute the Area with all three sides.
# Let s = (s 1 + s 2 + s 3 )/2. Then the area of the trianglecan be calculated using the following formula:area = sqrt(s × (s − s 1 ) × (s − s 2 ) × (s − s 3 ))
s     = s1 + s2 + s3
area  = sqrt(s * (s - s1 ) * (s - s2 ) * (s - s3 ))

# Output of the program.
print()
print("The Area of Triangle is %.2f." %area)
