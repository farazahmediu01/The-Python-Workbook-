
limit = 1000
p = 2
numbers = list(range(p,limit+1))
counter = 0

while counter < len(numbers) - 1:
    
    for x in range(2, len(numbers) + 1):
        not_a_prime_number = p * x
        if not_a_prime_number in numbers:
            numbers.remove(not_a_prime_number)

    counter += 1
    p = numbers[counter]

print(numbers)
