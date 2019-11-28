'''
Jan-1,mar-3,may-5,july-7,aug-8,oct-9,dec-12 = 31
April-4,june6,sep9,nov11 = 30
if month == "April-04" or month == "June-06" or \
month == "September-09" or month == "November-11":
days = 30
elif month == "February":
days = "28 or 29" 
'''
print("\n\nDate formate is Year-Month-Date eg: 2000-01-01\n")

month_a = [1,3,5,7,8,9]       # Month with 30 days
month_b = [4,6,10,11]         # Month with 31 days
month_c = [2,12]              # Month with 28 days

while True:
    n     = input("Enter date: ")

    if n == "quit":
            break

    try:
        year = int(n[:4])
        month = int(n[5:7])
        date = int(n[8:])
    
    except:
        print("Enter wrong value")
        print("Type 'quit' for exit\n")
        continue

    if month in month_a and date in range(1,31):
        if date < 30:
            date = date + 1
        elif date == 30:
            date = 1
            month = month + 1 

    elif month in month_b and date in range(1,32):
        if date < 31 :
            date = date + 1
        elif date == 31 :
            date = 1
            month = month + 1

    elif month in month_c :
        if month == 2 and date in range (1,28):
            date = date + 1
        elif month == 2 and date in range(28,30):
            date = 1
            month = month + 1
        elif month == 12 and date in range(1,31):
            date = date + 1
        elif month == 12 and date == 31:
            date = 1
            month = 1
            year = year + 1
    elif month > 12 or date > 31:
        if month > 12:
            print("There are only 12 months in a year")
        elif date > 31:
            print("There are maximum 31 days in a month")

# output formate.
    if month < 10 and date < 10:
        print(str(year) + "-0" + str(month) + "-0" + str(date))    
    elif month < 10 and date >= 10 and date <= 31:
        print(str(year) + "-0" + str(month) + "-" + str(date))
    elif month >= 10 and month <= 12 and date < 10:
        print(str(year) + "-" + str(month) + "-0" + str(date))
    elif month < 13 and date < 32:
        print(str(year) + "-" + str(month) + "-" + str(date))

    #print(str(year) + "-" + str(month) + "-" + str(date))
    print("." * 20)
