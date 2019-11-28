data = [1.62, 1.41, 3.14, 2.71, 0.26, 4.46, 9.999, 10]

data.sort()
print(data[-1])
index = data.index(data[-1])
print(index)


'''
i = 0
max_position = 0
while i < len(data):
    if data[i] > data[max_position]:
        max_position = i

    i += 1
print(max_position)
'''



'''
box = data[0]
data[0] = data[2]
data[2] = box
'''