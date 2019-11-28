print("\n\nProgarm start now...\n")

# This program implements the conversion from human years to dog years.
# Hint:
# Each of the First two human years = 10.5 dog years.
# after that one human yera = 4 dog years.

# Constants for this program.

fisrt_2_years = 10.5 # First two human years = 10.5 dog years.
after_2_years = 4    # After two human years = 4 dog years.

# Developing a function which does all our work.
def human_to_dog(inp):
    
    if inp <= 2 and inp > 0:
        inp = inp * fisrt_2_years
    
    elif inp > 2:
        inp = (inp - 2) * after_2_years + (fisrt_2_years * 2)
   
    return inp

# User input in string data type.
inp = input("Enter age > ")

# try funtion try to convert str into float
try:
    inp = float(inp)

# if try function convert str into float expect funtion skips, if try cannot convert str into float then interpreter skip try and run except.
except:
    inp = -1

# if user enter string contaning of non numeric charachters like "abc" so the if block runs and print error.
if inp <= 0 :
        print()
        print("You enter a bad input.")
        print("Please enter number only. ")
# if user enter the input grater than zero or the required input for this program then else part excutes the function which does all work.
else:
    print(human_to_dog(inp))
