array = [111, 222, 333, 444, 123]
for i in array[:]:
    print(i)

print("Enter number a three-digit number (ie: 123).")
user_inp = int(input(">"))

if user_inp in array:
    print(f"The number {user_inp} is at position {array.index(user_inp)} in the list.")
else:
    print(f"The number {user_inp} is not in the list.")
