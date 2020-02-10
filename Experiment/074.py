colors = list()

print("Enter ten colors: ")
while len(colors) < 10:
    user_inp = input(">")
    colors.append(user_inp.lower())

for color in sorted(colors):
    print(color.title())

user_str = int(input("Enter number between 0 - 4: "))
user_end = int(input("Enter number between 5 - 9: "))

for color in sorted(colors[user_str:user_end]):
    print(color.title())
