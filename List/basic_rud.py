def press_validation(n):
    if n.isnumeric():
        return True
    else:
        return False


def number_validation(n, message):
    # This function is used in the '1' and '2' part where the user enter number for add or delete names.
    if n.isnumeric():
        return int(n)
    else:
        print(message)
        while True:
            print("Enter number only.")
            n = input(">")
            try:
                return int(n)
            except:
                continue


def input_loop(n):
    # This funtion start a loop for user input the range is defined by user and loops ends with an empty string.
    count = 0
    inp = None
    input_array.clear()
    print(f"\nEnter {n} names, (press enter to skip)")

    while (count < n) and (inp != ""):
        inp = input(">")
        if inp:
            input_array.append(inp)
        count += 1
    return input_array


def sorted_names(n):
    # This function print names in a sorted form if user ented yes otherwise names printed as they were sorted.
    if n.lower() == 'y':
        for name in sorted(storage):
            print(name.title())
    else:
        for name in storage:
            print(name)


def delete_names(n):
    while n in storage:
        storage.remove(n)


# Initialzing main variables
message_1 = "\nEnter name of your friends you want to invite in your party."
storage = []        # Main storage variable.
input_array = []    # Partial storage variable.
inp = None          # Defaul input variable.
validation = None
print(message_1)

# Main loop.
while True:

    # First impression.
    if inp == None:
        # This block runs only first time where user enter first 5 or less then 5 names.
        input_array = input_loop(5)
        print(f"You have entered {len(input_array)} names.")

    print("\nPress '1' to add names.")
    print("Press '2' to delete names.")
    print("Press '3' to see all names.")
    print("Type 'quit' to exit.\n")

    inp = input(">")
    if press_validation(inp) or inp == 'quit' or inp == 'exit':
        pass
    else:
        print("Error")
        continue

    # Add names.
    if inp == '1':
        print("How many names you want to enter?")
        inp = input("Enter number: ")
        num = number_validation(inp)
        input_array = input_loop(num)
        print(f"{len(input_array)} names entered.")
        # input_array.clear

    # Delete names
    elif inp == '2':
        message = "\nYou are trying to delete names."
        message += "\nHow many names you want to delete,"
        message += " enter a number."

        print("How many names you want to delete?")
        inp = input("Enter number: ")

        # if number_validation_1(inp,message):
        #    num = int(num)
        # else:
        #    while

        num = number_validation(inp, message)
        input_array = input_loop(num)

    # sort and print all names in title case.
    elif inp == '3':
        print("\nPress 'y' to print formated names, otherwise press enter.")
        inp = input(">")

        sorted_names(inp)

    # Exit
    elif inp.lower() == 'exit' or 'quit':
        print("_" * 30)
        print("\nHave a nice day see you soon.")
        print("_" * 30)
        break


'''
copied code from first impression.
#inp = input(">").lower()
    # input_array.append(inp)
    # count += 1
    # storage.extend(input_array)
    # if input_array:
    # print(f"\nYou have enterd {len(input_array)} names.")
    # else:
    # print("You don't invite any of your friend.")
    # input_array.clear()
    #print("\nPress Enter to skip.")

'''
