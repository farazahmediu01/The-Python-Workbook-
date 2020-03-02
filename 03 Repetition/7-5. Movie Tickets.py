print("This program is tell you the price of ticket according to your age.")
UNDER_3 = 0
BETWEEN_3_TO_12 = 10
OVER_12 = 15
PRICE = None
active = True

while active:
    
    user_input = input("Enter your age in numbers only: ")
    
    try:
        user_input = int(user_input)
    except:
        print("Please enter numbers only, (ie: 18)")
        continue

    if user_input <= 3:
        PRICE = UNDER_3
    
    elif user_input <= 12:
        
        