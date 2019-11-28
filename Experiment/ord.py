a = "abcdefghijklmnopqrstuvwxyz"
b = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
c = r"+*/ !@#$%^&()<>?""':?.,;\/"

for i in range(10):
    print(f"{i} = {ord(str(i))}")

for i in b:
    print(f"{i} = {ord(i)}")

for i in a:
    print(f"{i} = {ord(i)}")

for i in c:
    print(f"{i} = {ord(i)}")