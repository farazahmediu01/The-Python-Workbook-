
message = ""
storage = []        # Main storage variable.
input_array = []    # Partial storage variable.
inp = 1          # Defaul input variable.


def press_validation(press):
    # This block verify that user input must be a number 'a' 'd' and 'r'.
    # User can only 'Add' 'Delete' and 'Read' data if this fuction returns True.
    if press == 'a' or press == 'd' or press == 'r':
        return True
    else:
        return False


def number_validation(number, message):
    # This block is skip due to complexity and non user friendly key mappings.
    # This function is used in the '1' and '2' part where the user enter number for add or delete names.
    if number.isnumeric():
        return int(number)
    else:
        print(f"\nYou are trying to '{message.title()}' names.")
        print(
            f"Enter a number so that system can determine how many names you want to {message}.")
        while True:
            print("\nEnter number only.")
            number = input(">")
            try:
                return int(number)
            except:
                continue


def input_loop(number):
    # This funtion start a loop for user input the range is defined by user and loops ends with an empty string.
    #count = 0
    inp = None
    input_array.clear()
    #print(f"\nEnter {number} names, (press enter to skip).")
    print(f"\nEnter names, (press enter to skip).")

    while (count < number) and (inp != ""):
        inp = input(">")
        if inp:
            input_array.append(inp)
        count += 1
    return input_array


def delete_names(names):
    #for x in names:
    #    while x in storage:
    #        storage.remove(x)

    


def sorted_names(n):

    # This function print names in a sorted form if user ented yes otherwise names printed as they were sorted.
    print()
    if n.lower() == 'y':
        for name in sorted(storage):
            print(name.title())
    else:
        for name in storage:
            print(name)


def main():
    global inp
    # Initialzing main variables
    message = "\nEnter name of your friends you want to invite in your party."
    #storage = []        # Main storage variable.
    #input_array = []    # Partial storage variable.
    #inp = None          # Defaul input variable.
    #validation = None
    print(message)

    # Main loop.
    while True:

        # First block to be run.
        if inp == 1:
            # This block runs only first time where user enter first 5 or less then 5 names.
            input_array = input_loop(5)
            storage.extend(input_array)
            print(f"You have entered {len(input_array)} names.")

        print("\nPress 'a' to add names.")
        print("Press 'd' to delete names.")
        print("Press 'r' to read all names.")
        print("Type 'quit' to exit.\n")

        # This is second conditonal block which handles the wrong input.
        inp = input(">").lower()
        if press_validation(inp) or inp == 'quit':
            # This block only execute when the inp is a number between 1 to 3  or 'quit'
            pass
        else:
            print("Error")
            print("You can only press the instructions blow.")
            continue

        # Add names
        if inp == 'a':
            message = "add"
            print("How many names you want to 'Add'?")
            inp = input("Enter number: ")
            num = number_validation(inp, message)
            input_array = input_loop(num)
            storage.extend(input_array)
            print(f"{len(input_array)} names entered.")

        # Delete names
        elif inp == 'd':
            message = "delete"
            print("How many names you want to delete?")
            inp = input("Enter number: ")
            num = number_validation(inp, message)
            input_array = input_loop(num)
            delete_names(input_array)
            print(f"{len(input_array)} names deleted.")

        # Sort names
        elif inp == 'r':
            print("Read name in a sorted way [y/n]?")
            #print("\nPress 'y' to print formated names, otherwise press enter.")
            inp = input(">")
            sorted_names(inp)
            print(f"Total {len(storage)} names")

        # Exit
        elif inp == 'e':
            print("_" * 30)
            print("\nHave a nice day see you soon.")
            print("_" * 30)
            break


if __name__ == "__main__":
    main()

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


    delete:
    # if number_validation_1(inp,message):
        #    num = int(num)
        # else:
        #    while


'''
