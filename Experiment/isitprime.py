'''
A prime number is an integer greater than one that is only divisible by one and itself.
Write a function that determines whether or not its parameter is prime, returning
True if it is, and False otherwise. Write a main program that reads an integer
from the user and displays a message indicating whether or not it is prime. Ensure
that the main program will not run if the file containing your solution is imported
into another program.
'''
#user_inp=(int(input("Enter the integer value to indicate: ")))
#a = user_inp/user_inp
varification_array = []


def is_prime(user_inp):
    if user_inp > 1:
        for i in range(2, user_inp):
            #if i == user_inp:
            #    continue
            elif user_inp % i != 0:
                varification_array.append(0)
            else:
                varification_array.append(1)

    if 1 in varification_array:
        return False
    if 1 not in varification_array and user_inp > 1:
        return True


def main():
    print("\nEnter number to check whether it is prime or not.")

    user_inp = int(input(">"))
    answer = is_prime(user_inp)
    message = str(user_inp) + " is " + "a prime number."\
        if answer else "not a prime number."

    print(message)


if __name__ == "__main__":
    main()
