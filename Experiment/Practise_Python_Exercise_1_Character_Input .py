name    =  input("Enter Name: ")
age     =  input("Enter Age : ")
number  =  int(input("How many times message you want to print the message: "))
age     =  2019 - int(age) + 100
message =  f"\n{name.title()} you become 100 year old in {age}."

print(message * number)

