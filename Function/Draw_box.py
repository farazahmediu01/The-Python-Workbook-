array = list(range(6))
box = 0
count_a = 0
big_b = 0
print(array)
array.reverse()
print(array)

for index in range(6):
    if array[index] > array[index + 1]:      # 5 > 4     
        for i in range(1, len(array)):
            if array[i] > array[big_b]:      # 5 > 4

                box = array[i]                 # box = 5
                array[i] = array[big_b]      # array[0]   = 4
                array[big_b] = box           # array[0+1] = 5
                                               #[4,5,3,2,1]


'''def draw_box():
    print("**********")
    print("*        *")
    print("*        *")
    print("**********")

draw_box()
'''