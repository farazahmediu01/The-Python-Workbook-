#!
print("\n\nEnter Three Sides of Triangle...\n")
# User input.
side_1 = input("Enter first side: ")
side_2 = input("Enter second side: ")
side_3 = input("Enter third side: ")

# try and except is for error handling.
try:
    side_1 = float(side_1)
    side_2 = float(side_2)
    side_3 = float(side_3)
except:
    side_1 = side_2 = side_3 = -1
if side_1 > 0 and side_2 > 0 and side_3 > 0 :
    
    if side_1 == side_2 and side_2 == side_3 and  side_1 > 0 : 
        print("\nThe triangle is Equilateral.") 
    elif side_1 != side_2 and side_2 != side_3  and side_3 != side_1 :
        print("\nThis triangle is Scalene.")
    elif side_1 == side_2 or side_2 == side_3 or side_3 == side_1 :
        print("\nThe triangle is Isosceles.") 
else:
    print("\nThe value you have entered is wrong input.")
    print("Please enter numbers only.") 