'''
Fill in the blanks to make the factorial function return the factorial of n.
Then, print the first 10 factorials (from 0 to 9) with the corresponding number.
Remember that the factorial of a number is defined as the product
of an integer and all integers before it.
For example, the factorial of five (5!) is equal to 1*2*3*4*5=120.
Also recall that the factorial of zero (0!) is equal to 1.


def factorial(n):
    result = 1

    if n == 0:
        return 1
    
    else:
        for x in range(1,n):
            result *= x
    
    return result

print(factorial(0))
print(factorial(4))
print(factorial(5))
'''

def factorial(n):
    result = 1
    
    if (n != 0) and (n != 1):
        for x in range(1, n + 1):
    
            result = result * x 
        return result
    
    return 1

for n in range(6):
    print(n, factorial(n))