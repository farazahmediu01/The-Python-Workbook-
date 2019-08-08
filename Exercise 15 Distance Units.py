print("\n\nThe program start now...\n")
# This program convert feet into inches, yards and miles.

# User input the distance in feet.
feet = int(input("Enter distance in feet: "))

# Conversion of feet into inches, yards and miles.
inch = feet * 12        # There are 12 inches in a foot.
yard = feet / 3         # There are 3 feet in a yard.
mile = feet / 5280      # There are 5280 feet in a mile.

# Output of the program.
print()
print(feet,"\tFeet --> Inch\t",inch)
print(feet,"\tFeet --> Yard\t",yard)
print(feet,"\tFeet --> Mile\t",mile)