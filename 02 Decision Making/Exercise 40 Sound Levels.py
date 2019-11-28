print("\n\nProgram start now...\n")

db = input("Enter sound level in decibels: ")
try:
    db = float(db)
except:
    db = -1
# if block runs only when the value given is greater than or equals to 40 and smaller than or equals to 30.
if db >= 40 and db <= 130 :
    # first nested if block runs only when the values are 40, 70, 106 or 130.
    if db == 130 or db == 106 or db == 70 or db == 40 :
        if db == 130 :
            print("Jackhammer")
        elif db >= 106 :
            print("Gas Lawnmower")
        elif db == 70 :
            print("Alarm Colck")
        elif db == 40 :
            print("Quiet Room")
    # This nested elif block runs only when the values are between 40 and 130 to determine the value which is between two names eg Quiet room and Alarm clock.
    elif db > 40 and db < 130 :
        if db > 40 and db < 70 :
            print("The value you have enter is between the sound of Quiet Room and Alarm Clock.")
        elif db > 70 and db < 106 :
            print("The value you have enter is between the sound of Alarm Clock and Gas Lawnmower.")
        elif db > 106 and db < 130 :
            print("The value you have enter is between the sound of Gas Lawnmower and Jackhammer.")
# This block runs only when the value is greater than 0 and blow 40 or greater than 130.
elif db > 0 and db < 40 or db > 130 :
    
    if db < 40 :
        print("The value you have entered is lower then the sound of a Quiet Room.") 
    elif db > 130 :
        print("The value you have entered is higher then the sound of a Jackhammer.")
# else block runs when the value is blow 0.
else:
    print("You have ented wrong input.")
    print("Please enter numbers only.")