'''
Exercise 85: Compute the Hypotenuse

Write a function that takes the lengths of the two shorter sides of a right triangle as
its parameters. Return the hypotenuse of the triangle, computed using Pythagorean
theorem, as the function’s result. Include a main program that reads the lengths of
the shorter sides of a right triangle from the user, uses your function to compute the
length of the hypotenuse, and displays the result.

Pythagorean theorem = c2 = a2 + b2
'''
from math import sqrt

def calculate_hypotenuse(side_a,side_b):
    '''This function return the hypotenuse of a right angle triangle using Pythagorean theorem'''
    return sqrt(side_a ** 2 + side_b ** 2)

print("\n\nEnter two shorter sides of a right angle triangle in order to get its hypotenuse...\n")
side_a = float(input("Enter first side: "))
side_b = float(input("Enter second side: "))

hypotenuse = calculate_hypotenuse(side_a, side_b)
print(f'\nThe hypotenuse of given two sides is {hypotenuse:.2f}')


