array = list(range(6))
box = 0
count_a = 0
count_b = 0
print(array)
array.reverse()
print(array)



for index in range(6):
    if array[index] > array[index + 1]:      # 5 > 4     
        for i in range(6):
            if array[i] > array[i + 1]:      # 5 > 4
                box = array[i]               # box = 5
                array[i] = array[i+1]        # array[0]   = 4
                array[i+1] = box             # array[0+1] = 5
                                             #[4,5,3,2,1]






'''def draw_box():
    print("**********")
    print("*        *")
    print("*        *")
    print("**********")

draw_box()
'''