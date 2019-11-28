inp        = int(input("Enter num: "))
check      = int(input("Enter check: "))
check      = inp % check
multiple_2 = inp % 2
multiple_4 = inp % 4

if multiple_4 == 0:
        print("The number is even and multiple of 4.")
elif multiple_2 == 0:
        print("The number is even and not a multiple of 4.")
else:
    print("The number is odd.")

if check == 0:
    print("The number is evenly divided by check.")
else:
    print("The number is not evenly divided by check.")