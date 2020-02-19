'''
A prime number is an integer greater than one that is only divisible by one and itself.
Write a function that determines whether or not its parameter is prime, returning
True if it is, and False otherwise. Write a main program that reads an integer
from the user and displays a message indicating whether or not it is prime. Ensure
that the main program will not run if the file containing your solution is imported
into another program.
'''
user_inp=(int(input("Enter the integer value to indicate: ")))
a = user_inp/user_inp

def isprime(user_inp):
    if user_inp > 1 and user_inp = 