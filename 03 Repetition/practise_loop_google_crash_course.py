'''Fill in the blanks to make the print_prime_factors function 
print all the prime factors of a number."
A prime factor is a number that is prime and divides another without a remainder.'''




def print_prime_factors(number):
    # Start with two, which is the first prime
    factor = 2

    # Keep going until the factor is larger than the number
    while factor <= number:

        # Check if factor is a divisor of number
        if number % factor == 0:

            # If it is, print it and divide the original number
            print("ok",factor)
            number = number / factor # 100, 50, 25, 5, 1
            
        
        else:
            # If it's not, increment the factor by one
            print("factor not ok",factor)
            factor += 1 # 2,3,4,5
    return "Done"


a = print_prime_factors(100)
# Should print 2,2,5,5
print(a)