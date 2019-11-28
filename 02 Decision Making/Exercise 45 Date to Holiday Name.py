
month = input("Enter month: ")
date  = input("Enter date: ")

if date == "1" and month == "january"   or   date == "1" and month == "july"    or   date == "25" and month == "december" :
    
    if date == "1" and month == "january" :
        print("New Year’s Day")
    
    elif date == "1" and month == "july" :
        print("Canada Day")
    
    elif date == "25" and month == "december" :
        print("Christmas Day")
else:
    print("The entered month and day do not correspond to a fixed-date holiday.")
