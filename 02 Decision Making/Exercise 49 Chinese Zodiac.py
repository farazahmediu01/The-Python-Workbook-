print("\n\nProgram start now...\n")
year = int(input("Enter year: "))
print()

year = year % 12


if year == 8:
    print("Dragon")
elif year == 9:
    print("Snake")
elif year == 10:
    print("Horse")
elif year == 11:
    print("Sheep")
elif year == 0:
    print("Monkey")
elif year == 1:
    print("Rooster")
elif year == 2:
    print("Dog")
elif year == 3:
    print("Pig")
elif year == 4:
    print("Rat")
elif year == 5:
    print("Ox")
elif year == 6:
    print("Tiger")
elif year == 7:
    print("Hare")
else:
    print("Value not found")








