BASE_FAIR = 4
METER_TO_KILOMETER = 140 / 1000

def cal_fare(distance):
    fare = BASE_FAIR + (distance/METER_TO_KILOMETER) * 0.25
    return fare

distance = float(input('Enter distence in kilometres (km): '))
fare = cal_fare(distance)

print(f'\nThe total fair is ${fare:.2f}')
