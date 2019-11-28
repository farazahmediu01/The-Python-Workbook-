# Initialize data and largest pos.
data        = [1.62, 1.41, 3.14, 2.71, 0.26, 4.46, 9.999, 10]
largest_pos = 0

'''
# Find the position of the largest element.
for value in data:    
    if largest_pos < value:
        largest_pos = value
'''

for index in range(1, len(data)):
    if data[index] > data[largest_pos]:
        largest_pos = index



# Display the result
print(f'The largest value is {data[largest_pos]} on index {largest_pos}.')
