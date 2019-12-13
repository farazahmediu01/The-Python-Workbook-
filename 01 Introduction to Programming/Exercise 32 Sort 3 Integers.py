print("\n\nProgram start now...\n")
#
# This program sort 3 intergers in Assending Order. 
#

# User input consit of three numbers.
print("Enter three numbers...")
a = float(input("Enter First number : "))
b = float(input("Enter Second number: "))
c = float(input("Enter Third number : "))

# Sorting integers in assending order.
smallest = min(a,b,c)                                # The smallest value in smallesr.
largest = max(a,b,c)                                 # The largest value in largest.
middle =  (a + b + c) - (smallest + largest)         # The middle value is calculated and stored in middle.
message = f'>{smallest}\n>{middle}\n>{largest}'      # A message composed to show the output.

# Output of program.
print(message)
