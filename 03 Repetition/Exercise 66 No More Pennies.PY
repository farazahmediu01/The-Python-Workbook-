from math import ceil, floor

total_cost = 0

while True:
    price = input("Enter price: ")

    if price == "":
        break
    
    try:
        total_cost += float(price)
    except:
        print("Wrong input\n")
        continue
    
print("Total Pennies =",total_cost)

if total_cost % 5  < 2.5:
    print("Total nickles = %.2f" % floor(total_cost))
else:
    print("Total Nickles = %.2f" % ceil(total_cost))



