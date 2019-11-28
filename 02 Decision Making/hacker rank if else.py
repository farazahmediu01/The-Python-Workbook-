'''
Given an integer, , perform the following conditional actions:

If  is odd, print Weird
If  is even and in the inclusive range of  to , print Not Weird
If  is even and in the inclusive range of  to , print Weird
If  is even and greater than , print Not Weird
'''
n = int(input())

n_1 = n % 2 # if n == 0 even otherwise odd.

if n_1 != 0:
    print("Weird")
elif n_1 == 0 and n in range(2,6):
    print("Not Weird")
elif n_1 == 0 and n in range(6,21):
    print("Weird")
elif n_1 == 0 and n > 20:
    print("Not Weird")

