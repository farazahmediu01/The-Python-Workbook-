print("\n\nProgram start now...\n")
#
# This program sort 3 intergers in order of Minimum, Middle and Maximum. 
#

# User input consit of three numbers.
print("Enter three numbers...")
a = float(input("Enter First number : "))
b = float(input("Enter Second number: "))
c = float(input("Enter Third number : "))

# Sorting integers in assending order.
smallest = min(a,b,c)     # The smallest value in s.
largest = max(a,b,c)     # The largest value in l.
middle =  (a + b + c) - (smallest + largest)   # The middle value is calculated and stored in m.
message = f'largest = {smallest}'

# Output of program.
print()
print(smallest)
print(middle)
print(largest)