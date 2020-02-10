index = 0
favorite_fruites = dict()

print("\nPlease Enter your five favorite foods: ")
while len(favorite_fruites) < 6:
    index += 1
    inp = input('>')
    favorite_fruites[index] = inp.lower()

print("\nYour favorite fruits are shown blow:")
for key, value in favorite_fruites.items():
    print(f"{key}) {value.title()}")

inp = int(
    input("Enter number of fruit which you think will be removed from the list: "))
del favorite_fruites[inp]

for value in sorted(favorite_fruites.values()):
    print(value.title())