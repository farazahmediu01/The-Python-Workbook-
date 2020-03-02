def display_name_3_times(name, user_range):
    for i in range(1, user_range + 1):
        print(f"{i}){name.title()}")


def main():
    name = input("Enter your name: ")
    user_range = int(input("Enter number" +\
        "so that many times your name will print on screen: "))
    display_name_3_times(name, user_range)


main()
