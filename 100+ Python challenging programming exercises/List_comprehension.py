# result = [nest for nest in [var for var in range(2,11,2)]]
# result = [lis ]
# print(result)

# sub_list = []
complete_list = []
# for i in range(5):
#     lis.append(result)

# print(result)
# print(lis)

x = int(input())
y = int(input())
n = int(input())


print ([ [ i, j] for i in range( x + 1) for j in range( y + 1) if ( ( i + j ) != n )])

for i in range(x+1):
    for j in range(y+1):
        if ( ( i + j ) != n ):
           complete_list.append([i,j])

print(complete_list)