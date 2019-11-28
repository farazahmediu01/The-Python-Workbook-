print("\nEnter ages of all people in the group:")
cost = 0
inp = None

while inp != "" :    
    
    inp = input("> ")
    
    try:
        inp = int(inp)
    except:
        if inp == "":
             continue 
        else:
            print("Error")
            continue
    
    if   inp<= 2 :
            cost += 0
    elif inp<=12 :
            cost += 14
    elif inp>=65 :
            cost += 18
    else:
        cost += 23
    

print("cost =",cost)