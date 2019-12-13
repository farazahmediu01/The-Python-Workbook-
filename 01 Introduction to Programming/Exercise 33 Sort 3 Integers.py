num_1 = int(input('Enter 1st number: '))
num_2 = int(input('Enter 2nd number: '))
num_3 = int(input('Enter 3rd number: '))

small_val    = min(num_1,num_2,num_3)
large_val    = max(num_1,num_2,num_3)
middle_val   = (num_1 + num_2 + num_3) - (large_val + small_val)

print(f'>{small_val}\n>{middle_val}\n>{large_val}')

