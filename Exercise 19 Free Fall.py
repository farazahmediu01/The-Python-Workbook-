#
# This program determines how quickly an object is travelling when it hits the ground.
#
print("\n\nThe program start now...\n")
from math import sqrt

# Contant values which we use in this program.
vi = 0
a  = 9.8

# User input the hight or distance in meters.
h = int(input("Enter hight in meters(m): "))


# Compute the final vilocity.
# Because the object is dropped its initial speed is 0m/s. Assume that the acceleration due to gravity is 9.8m/s2.
vf = sqrt(vi ** 2 + 2 * a * h)

# Output of program.
print()
print("The final speed of the object fall from the hight of %d miters is %.2f m/s." %(h, vf))

