print("\n\nProgram start now...\n")
#This program compute the Aera of Circle and Volume of Sphere.
from math import pi # import pi from math module.

# User input the Radious "r".
r = int(input("Enter radious: "))

# Compute the Area of Circle and Volume of Sphere.
area    = pi * r ** 2           # The formula of Aera of Circle is area = πr2. 
volume  = 4 / 3 * pi * r ** 3   # The formula of  volume = 4/3 πr3 .

# Output of program.
print()
print("The Aera of Circle   =",area)
print("The Volume of Sphere =",volume)
