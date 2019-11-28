# 4.6 Write a program to prompt the user for hours and rate per hour using input to compute gross pay. 

# Pay should be the normal rate for hours up to 40 and time-and-a-half for the hourly rate for all hours worked above 40 hours.

# Put the logic to do the computation of pay in a function called computepay() and use the function to do the computation.

# The function should return a value. 

# Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75).

# You should use input to read a string and float() to convert the string to a number.

# Do not worry about error checking the user input unless you want to - you can assume the user types numbers properly.

# Do not name your variable sum or use the sum() function.


def compute_pay(h,rph):
    if h > 40 :
        h_1 = h - 40           # values above 40 stored in h_1.
        h   = h - h_1          # now h can hold only 40 because h_1 which is above 40 is minus from h.
        h_1 = h_1 * 1.5 * rph  # hours more then 40 multiply by 1.5 of rate per hour.
        pay = h * rph + h_1
    
    else:
        pay = h * rph
        
    return pay


h   = float(input("Enter Hour: "))
rph = float(input("Enter Rate per Hour: "))

print(compute_pay(h,rph))

