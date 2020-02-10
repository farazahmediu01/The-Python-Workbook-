# constants of the program.
SECONDS_PER_DAY = 24 * 60 * 60
SECONDS_PER_HOUR = 60 * 60
SECONDS_PER_MINUTE = 60 

# This program is the reverse of Exercise 24 in the python workbook.
print("\nThis program converts the number of seconds into equivalent number of days, hours, minutes and seconds.")
seconds = float(input("Enter number of seconds: "))

# The logic part.
days    = seconds / SECONDS_PER_DAY
seconds = seconds % SECONDS_PER_DAY
hours   = seconds / SECONDS_PER_HOUR
seconds = seconds % SECONDS_PER_HOUR
minutes = seconds / SECONDS_PER_MINUTE
seconds = seconds % SECONDS_PER_MINUTE
seconds = seconds

# The formated output in the form D:HH:MM:SS, where D,HH,MM, and SS represent days, hours, minutes and seconds respectively.
print("_" * 30)
print(f"{days:.0f}:{hours:.0f}:{minutes:.0f}:{seconds:.0f}")
print("_" * 30)