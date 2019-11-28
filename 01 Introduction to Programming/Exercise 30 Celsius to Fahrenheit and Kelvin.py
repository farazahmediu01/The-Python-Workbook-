print("\n\nProgram start now...\n")

#
# This program convert tempreature from Digree Celcious to Fehrenheit and Kelvin.
#

# User input the tempreature in Digree Celcious.
c = int(input("Enter tempreature in Celcious: "))

# Converting Celcious into Kelvin and Fahrenhiet.
k = c + 273.15
f = (c * 9 / 5) + 32          #    formula (1°C × 9/5) + 32 = 33.8°F

# Output of porgram.
print()
print("%d\tCelcious->Kelvin\t%.2f"%(c,k))
print("%d\tCelcious->Fahrenhiet\t%.2f"%(c,f))