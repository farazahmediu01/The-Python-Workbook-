num_1 = int(input('Enter 1st number: '))
num_2 = int(input('Enter 2nd number: '))
num_3 = int(input('Enter 3rd number: '))

smallest_value = min(num_1,num_2,num_3)
largest_value  = max(num_1,num_2,num_3)
middle_value   = (num_1 + num_2 + num_3) - (largest_value + smallest_value)

print(f'>{smallest_value}')  
print(f'>{middle_value}')
print(f'>{largest_value}')

