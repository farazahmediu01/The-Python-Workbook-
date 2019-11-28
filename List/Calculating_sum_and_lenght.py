nums     = [100, 1, 3, 14, 2, 25, 177, 91, 5, 3, 11]
addition = 0
lenght   = 0
largest  = None
smallest = None

for num in nums:
    if (largest == None) and (smallest == None):
        largest  = nums[0]
        smallest = nums[0]
    
    elif largest < num:
        largest = num

    elif smallest > num:
        smallest = num
    
    addition = addition + num
    lenght   = lenght + 1
    


print(f'\naddition   = {addition}')
print(f'sum        = {sum(nums)}')

print(f'lenght     = {lenght}')
print(f'len        = {len(nums)}')

print(f'smallest   = {smallest}')
print(f'largest    = {largest}')
