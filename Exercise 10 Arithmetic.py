print("The program start now...")
from math import log10

# User input a and b.
a = int(input("Enter a: "))
b = int(input("Enter b: "))

# Compute the sum, difference, product, quotient, remainder, log(a) and exponential of a and b.
add = a + b
sub = a - b
pro = a * b
quo = a / b
rem = a % b
log = log10(a)
exp = a ** b

# Output of program.
print("\n\n")
print("a    +    b  =",add)
print("a    -    b  =",sub)
print("a    *    b  =",pro)
print("a    /    b  =",quo)
print("a    **   b  =",exp)
print("a    %    b  =",rem)
print("log10(a)     =",log)
