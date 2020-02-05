# Constants of this program.
SECONDS_PER_DAY = 24 * 60 * 60
SECONDS_PER_HOUR = 60 * 60
SECOND_PER_MINUTE = 60
 
# Program's introduction.
print("\nThis program converts the days, hours, minutes, and seconds into equivalent number of seconds.")

# User input for number of days, hours, minutes, and seconds.
number_of_days = float(input("Enter number of days: "))
number_of_hours = float(input("Enter number of hours: "))
number_of_minutes = float(input("Enter number of minutes: "))
number_of_seconds = float(input("Enter number of seconds: "))

# The logic part.
conversion = number_of_days * SECONDS_PER_DAY + \
    number_of_hours * SECONDS_PER_HOUR + \
    number_of_minutes * SECOND_PER_MINUTE +\
    number_of_seconds

# Showing the formated output.
print(f"\nDays = {number_of_days} \nHours = {number_of_hours} \nMinutes = {number_of_minutes} \nSeconds = {number_of_seconds}\n{'_' * 50}\nTotal seconds = {conversion:.2f}")
