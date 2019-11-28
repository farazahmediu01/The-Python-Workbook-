print("\n\nProgram start now...\n")
#  This program determine the name of a shape from its number of sides.
def name_that_shape(side):
    
    if side == 3:
        side = "Triangle"
    
    elif side == 4:
        side = "Square"
    
    elif side == 5:
        side = "Pentagon"
    
    elif side == 6:
        side = "Hexagon"
    
    elif side == 7:
        side = "Heptagon"

    elif side == 8:
        side = "Octagon"
    
    elif side == 9:
        side = "Nonagon"

    elif side == 10:
        side = "Decagon"
    
    return side

print("Enter sides of shape to determine its name.")
side = input("Enter number of sides: ")

try:
    side = float(side)

except:
    side = -1

if side <= 0:
    print()
    print("You entered wrong input.")
    print("Please enter numbers only.")

elif side == 1 or side == 2 or side > 10:
    if side == 1:
        print("There is no shape with only one side.")
        print("I think you ask for a circle.")
    
    elif side == 2:
        print("There is no shape with two sides.")
    
    elif side > 10:
        side = int(side)
        print("There is no shape with %d sides."%side)

else:
    
    print()
    print(str(name_that_shape(side)) + " is the shape which have " + str(int(side)) + " sides.")



