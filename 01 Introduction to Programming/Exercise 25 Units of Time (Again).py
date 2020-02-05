# constants of the program.
SECONDS_PER_DAY = 24 * 60 * 60
SECONDS_PER_HOUR = 60 * 60
SECONDS_PER_MINUTE = 60 



# This program is the reverse of Exercise 24 in the python workbook.
print("\nThis program converts the number of seconds into equivalent number of days, hours, minutes and seconds.")
input_for_seconds = float(input("Enter number of seconds: "))

# The logic part.
number_of_days    = input_for_seconds / SECONDS_PER_DAY
input_for_seconds = input_for_seconds % SECONDS_PER_DAY
number_of_hours   = input_for_seconds / SECONDS_PER_HOUR
input_for_seconds = input_for_seconds % SECONDS_PER_HOUR
number_of_minutes = input_for_seconds / SECONDS_PER_MINUTE
input_for_seconds = input_for_seconds % SECONDS_PER_MINUTE
number_of_seconds = input_for_seconds

# The formated output in the form D:HH:MM:SS, where D,HH,MM, and SS represent days, hours, minutes and seconds respectively.
print("_" * 30)
print(f"{number_of_days:.0f}:{number_of_hours:.0f}:{number_of_minutes:.0f}:{number_of_seconds:.0f}")
print("_" * 30)