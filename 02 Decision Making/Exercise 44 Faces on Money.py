print("\n\nProgram start now...\n")
#This program display the name of the individual that appears on the banknote of the entered amount. 
print("Please enter the amount of dollar to see the name of individual appers on the back note.")
a = input("> ")

if a == "1" or a == "2" or a == "5" or a == "10" or a == "20" or a == "50" or a == '100' :
 if a == "1" :
        print("George Washington.")
 elif a == "2" :
        print("Thomas Jefferson.")
 elif a == "5" :
        print("Abraham Lincoln.")
 elif a == "10" :
        print("Alexander Hamilton.")
 elif a == "20" :
        print("Andrew Jackson.")
 elif a == "50" :
        print("Ulysses S. Grant.")
 elif a == "100" :
        print("Benjamin Franklin.")
else:
    print("'Individual not found'".title())   