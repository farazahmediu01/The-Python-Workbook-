print('\nEnter number to check weather the number is odd or even.')

value = int(input('Enter number: '))
divisor = int(input('Enter a divisor to divide by number: '))
print()

if value%4 == 0:
    message = f'{value} is even and Multiple of 4.'
    print(message)

elif value%2 == 0:
    message = f'{value} is even and Not multiple of 4.'
    print(message)

if divisor != 0 and value%divisor == 0: 
    message = f'The number you have entered {value} is evenly divided by {divisor}.'
    print(message)
    

  