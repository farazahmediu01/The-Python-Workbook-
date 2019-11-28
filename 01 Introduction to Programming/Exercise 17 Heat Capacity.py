print("\n\nProgram start now...\n")

# This program compute the amount of energy needed to heat a volume of water and the amount of cost for same.
C           = 4.186     # Specific heat capacity of water.
J_TO_KWH    = 2.777e-7  # 1 jule = 2.777x10-7 .This is a contanat for the enhanced program.
E_UNIT      = 8.9       # A Unit of Electricity is 8.9 cents.


# User input the mass and tempreature.
mass   = int(input("Enter mass in milliliters: "))
del_t  = int(input("Enter tempreature in digree celcious: "))


#  The total amount of energy q required to raise m grams of a material by ΔT degrees Celsius can be computed using the formula: q = mCΔT
q    = mass * C * del_t
cost = E_UNIT * J_TO_KWH * q


# Output of program.
print()
print("The total amount of enery required q =",q,"jules.")
print("The total cost on this process is",cost,"cent.")
