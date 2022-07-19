
num_a = 2
num_z = 100
numbers = list(range(num_a, num_z + 1))
counter = 0

while counter < len(numbers) - 1:
    
    for x in range(2, len(numbers) + 1):
        not_a_prime_number = num_a * x
        if not_a_prime_number in numbers:
            numbers.remove(not_a_prime_number)

    counter += 1
    num_a = numbers[counter]

print(numbers)
