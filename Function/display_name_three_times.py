def display_name(name, user_range):
    for i in range(1, user_range + 3):
        print(f"{i}){name.title()}")

def main(name, user_range):
    name = input("Enter your name: ")
    user_range = int(input("Enter number \
    so that many times your name will print"))

display_name(name, user_range)
main(name,user_range)