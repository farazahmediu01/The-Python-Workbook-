print("\n\nProgram start now...\n")
#
# This program sort 3 intergers in order of Minimum, Middle and Maximum. 
#

# User input consit of three numbers.
print("Enter three numbers...")
a = int(input("Enter First number : "))
b = int(input("Enter Second number: "))
c = int(input("Enter Third number : "))

# Sorting integers in assending order.
s = min(a,b,c)     # The smallest value in s.
l = max(a,b,c)     # The largest value in l.
m =  (a + b + c) - (s + l)   # The middle value is calculated and stored in m.

# Output of program.
print()
print(s)
print(m)
print(l)