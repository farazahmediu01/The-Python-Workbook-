from math import radians, sin, cos


print("\n\nProgram start now...\n")
# This program program should display the distance between two points, following the surface of the earth, in kilometers.

# User input four points of earth.
t1 = radians(float(input("Enter the latitude  of one point of earth:    ")))
g1 = radians(float(input("Enter the longitude of one point of earth:    ")))
t2 = radians(float(input("Enter the latitude  of second point of earth: ")))
g2 = radians(float(input("Enter the longitude of second point of earth: ")))


# Computation.
fromula =  6371.01 * cos(sin(t1) * sin(t2) + cos(t1) * cos(t2) * cos(g1 - g2))


# Output
print("\nThe distance of earth between two points you have entered is %.2f kilometrs." %fromula)