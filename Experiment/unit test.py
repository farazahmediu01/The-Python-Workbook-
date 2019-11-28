print("\n\n")
import sys

print(sys.version)
print(sys.executable)




















'''

month  = input("Enter month : ")

f_pos = month.find(" ")
print(f_pos)
s_pos = month[f_pos+1:]
print(s_pos)
date  = int(s_pos)
print(date)
'''
'''
from math import ceil, floor

while True:
    n = float(input(">"))
    a = ceil(n) 
    b = floor(n)   

    print("ceil =",a)
    print("floor",b)
'''