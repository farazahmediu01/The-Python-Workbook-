# user input for year.
year = int(input("Enter year: "))

# setting up all the variables according to the requirements.
a = year % 19       # '%'  operator for remaindre
b = year // 100     # '//' operator for floor
c = year % 100
d = b // 4
e = b % 4
f = (b + 8) // 25
g = (b - f + 1) // 3
h = (19 * a + b - d - g + 15) % 30
i = c // 4
k = c % 4
l = (32 + 2 * e + 2 * i - h - k) % 7
m = (a + 11 * h + 22 * l) // 451
month = (h + l - 7 * m + 114) // 31
day = (h + l - 7 * m + 114) % 31 + 1

# Output

print(f"The Eater in year {year}, is held on month {month} and date {day}.")
