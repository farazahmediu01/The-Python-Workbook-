print("\n\nProgram start now...\n")

#
# This program reads the input of four digits and diaplay the sum of those four digits.
# For example, if the user enters 3141 then your program should display 3+1+4+1=9.
# 

inp = input("Enter a four digit number: ")

# Lets play with string (data type) to break each number seprate and make sum of all.
a = int(inp[0]) # we can break string into its parts with their index number.
b = int(inp[1]) # a = "1234" is a string and and b = a[0] is "1".
c = int(inp[2]) # we can convert string into integer with int() function.
d = int(inp[3])
e = a + b + c + d

# Output of the program.
print()
print("The sum of four digits you have entered is %d + %d + %d + %d = %d." % (a,b,c,d,e))