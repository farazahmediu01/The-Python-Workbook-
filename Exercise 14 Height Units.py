print("\n\nThe program starts now...\n")
# This program take input of hight in feet and inches and convert the equivalent value in centimeters.

# User input.
print("Enter your height.")
hight_in_feet    = int(input("Enter number of feet: "))
hight_in_inch    = int(input("Enter number of inch: "))


# Computation of hoght in feet and inches to centimeters.
hight_in_centimeters = (hight_in_inch + hight_in_feet * 10) * 2.54


# Output.
print("\nYour height in centimeters =",hight_in_centimeters)