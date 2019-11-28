# $4.95, $9.95, $14.95, $19.95 and $24.

print("\n\nDiscount is 60%.\n")

for i in [4.95, 9.95, 14.95, 19.95, 24.95]:
    
    print("\nOriginal price",i)
    
    i *= 0.60

    print("Discounted price = %.2f" %(i))
    print()
    print("*" * 20)
 