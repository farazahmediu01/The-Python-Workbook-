# I THINK I HAVE TO USE NESTED LOOP TO CATCH VALUES LIKE 000.




key     = "000"
#count  = 0

for i in range(999):
    
    i = str(i)
    if i == key:
        print("Found")
        break
print(i)