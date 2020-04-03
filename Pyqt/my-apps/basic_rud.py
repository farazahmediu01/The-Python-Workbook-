from functionality import press_validation, input_loop, delete_names, sorted_names


names = ['sameer', 'faraz', 'sarab', 'ali', 'faiq', 'rameez']
names = sorted_names(names)
print(names)






# global variables
message = ""
storage = []        # Main storage variable.
input_array = []    # Partial storage variable.
inp = None          # Defaul input variable.


def main(message="", storage=[], input_array=[], inp=None):
    # global inp, storage, input_array, message
    # Initialzing main variables
    message = "\nEnter name of your friends you want to invite in your party."
    # storage = []        # Main storage variable.
    # input_array = []    # Partial storage variable.
    # inp = None          # Defaul input variable.
    #validation = None
    print(message)

    # Main loop.
    while True:

        # First block to be run.
        if inp == None:
            # This block runs only first time where user enter first 5 or less then 5 names.
            input_array = input_loop()
            storage.extend(input_array)
            print(f"You have entered {len(input_array)} names.")

        print("\nPress 'a' to Add names.")
        print("Press 'd' to Delete names.")
        print("Press 'r' to Read all names.")
        print("Press 'e' to Exit.\n")

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
            # message = "add"
            # print("How many names you want to 'Add'?")
            # inp = input("Enter number: ")
            # num = number_validation(inp, message)
            input_array = input_loop()
            storage.extend(input_array)
            print(f"You have entered {len(input_array)} names.")

        # Delete names
        elif inp == 'd':
            # message = "delete"
            # print("How many names you want to delete?")
            # inp = input("Enter number: ")
            # num = number_validation(inp, message)
            input_array = input_loop()
            delete_names(input_array)
            # print(f"You have delete {len(input_array)} names.")

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


# if __name__ == "__main__":
#     main()

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
