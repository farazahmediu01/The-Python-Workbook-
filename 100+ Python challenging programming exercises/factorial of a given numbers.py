
n = int(input("Enter number: "))
var     = 1
list_   = []

for i in range(1,n+1):
    list_.append("i = " + str(i))
    var *= i
    list_.append(var)

print("Factorial of %d = %d" %(n,var))     
print("list =",list_)
