print("\n\nProgram start now...\n")
#
# This program computes the amount of gas in moles when the user supplies pressure, volume and temperature.
#
R = 8.314   # R is the ideal gas constant, equal to 8.314 J/molK.

# User input for Pressure in Pascals, Volume in Liters and Tempreature in Kelvin.
P = float(input("Enter Pressure in (Pascals): "))
V = float(input("Enter Volume in (Liters)   : "))
T = float(input("Enter Tempreature in (Celcious): "))

# Computaion for Ideal gass law as per the requirement of program.
# Formula = PV = nRT but we have to find "n".

T_Kelvin = T + 273.15   # Converting tempreature in Kelvin.
n  = P * V / R * T_Kelvin

# Output of the program.
print()
print("The number of moles =",n)