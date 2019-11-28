a = "banax"
b = "banana"
c = "bun"


if a in b:
    print("a == b")
if a > b :
    print("1) a is greater then b.")
if b > c :
    print("2) b is greater then c.")
if c < a and c < b :
    print("3) c is smaller then both a and b.")
if a > b and a > c:
    print("4) a is grater then both b and c.")
if b < a and b > c :
    print("5) b is smaller then a and b is grater then c.")