print("\n\nThis program tells you what is your Astrological Sign.\n")
print("Enter date of birth like: January-08")
#print("Enter your date of birth eg: 8")

month  = input("> : ")
print()

try:

    find_pos = month.find("-")
    slice_month = month[find_pos + 1: ]
    month       = month[ : find_pos]
    date  = int(slice_month)
except:
    date = -1


#date   = int(input("Enter date : "))

list_month = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

if month in list_month :
    

    if month == "January":
        
        if date >= 1 and date <=19:
            print("Capricorn.")
        
        elif date >= 20 and date <= 31:
            print("Aquarius.") 
    
    elif month == "February":

        if date >= 1 and date <= 18:
            print("Aquarius")
        
        elif date >= 19 and date <= 31:
            print("Pisces.")

    elif month == "March":

        if date >= 1 and date <= 20:
            print("Pisces.")
        
        elif date >= 21 and date <= 31:
            print("Aries.") 
    
    elif month == "April":

        if date >= 1 and date <= 19:
            print("Aries")
        
        elif date >= 20 and date <= 31:
            print("Taurus.") 
    
    elif month == "May":

        if date >= 1 and date <= 20:
            print("Taurus.")
        
        elif date >= 21 and date <= 31:
            print("Gemini.")
    
    elif month == "June":

        if date >= 1 and date <= 20:
            print("Gemini.")
        
        elif date >= 21 and date <= 31:
            print("Cancer.")

    elif month == "July":

        if date >= 1 and date <= 22:
            print("Cencer.")
        
        elif date >= 23 and date <= 31:
            print("Leo.")

    elif month == "August":

        if date >= 1 and date <= 22:
            print("Leo.")
        
        elif date >= 23 and date <= 31:
            print("Virgo.")
    
    elif month == "September":

        if date >= 1 and date <= 22:
            print("Virgo.")
        
        elif date >= 23 and date <= 31:
            print("Libra.")

    elif month == "October":

        if date >= 1 and date <= 22:
            print("Libra.")
        
        elif date >=23 and date <= 31:
            print("Scorpio.")
    
    elif month == "November":

        if date >= 1 and date <= 21:
            print("Scorpio.")
        
        elif date >=22 and date <= 31:
            print("Sagittarius.")

    elif month == "December":

        if date >= 1 and date <= 21:
            print("Aquarius")
        
        elif date >=22 and date <= 31:
            print("Capricorn.")
else:
    print("'Error'")