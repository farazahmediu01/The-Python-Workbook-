print("\n\nEnter values to find Average...\n")
print("Enter value to")

avg   = 0
index = 0

while True:
    inp = int(input("Enter Number: "))
    
    if index == 0 and inp == 0:
        print("Error")
        continue 
    elif index != 0 and inp == 0:
        break
    
    avg += inp
    index += 1
    
print("Average =",avg/index)
    