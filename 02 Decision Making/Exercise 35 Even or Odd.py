print("Program start now...")
#
# By the name of this program you can eaisly understand the perpose of this program.
# In this program user input a number and program display a message indicating whether the integer is even or odd.
#
# getting input and setting variables.

print("Enter a number to verify whether it is even or odd.")
inp = int(input("Enter number: "))

# Computation
print()
inp = inp % 2

if inp == 0:
    print("The number you have entered is even.")

else:
    print("The number you have entered is odd.")



