print("This program tell you the season associated with the date and month.\n")

# user input
month = input("Enter starting 3 letters of a month (eg: jan): ")
date = int(input("\nEnter Date (eg: 31): "))
print()

# logic and decision
if (month == 'dec' and date >= 21 and date <= 31) or \
    (month == 'jan' and date >= 1 and date <= 31) or \
    (month == 'feb' and date >= 1 and date <= 31) or \
        (month == 'mar' and date >= 1 and date <= 19):
    print('Winter')


elif (month == 'mar' and date >= 20 and date <= 31) or \
    (month == 'apr' and date >= 1 and date <= 31) or \
    (month == 'may' and date >= 1 and date <= 31) or \
        (month == 'jun' and date >= 1 and date <= 20):
    print('Spring')


elif (month == 'jun' and date >= 21 and date <= 31) or \
    (month == 'jul' and date >= 1 and date <= 31) or \
    (month == 'aug' and date >= 1 and date <= 31) or \
        (month == 'sep' and date >= 1 and date <= 21):
    print('Summer')


elif (month == 'sep' and date >= 22 and date <= 31) or \
    (month == 'oct' and date >= 1 and date <= 31) or \
    (month == 'nov' and date >= 1 and date <= 31) or \
        (month == 'dec' and date >= 1 and date <= 20):
    print('Fall')


else:
    print("Invalid date or month")
