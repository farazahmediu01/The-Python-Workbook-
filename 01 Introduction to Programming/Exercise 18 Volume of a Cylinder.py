print("\n\nProgram start now...\n")
#
# This program compute the Volume of Cylinder.
#

# User input the radious and hight of the cylinder.
print("To find the volume of cylinder do following steps.")
r = float(input("Enter radious: "))
h = float(input("Enter hight  : "))

# Compute the Volume of Cylinder.
# Volume of cylinder can be computed by multiplying Cylinder's Hight with its Radious.
volume = r * h  # Radious x Hight.

# Output of program.
# The result display is rounded to one decimal place.
print()
print("The volume of cylinder is %.1f." %volume) 