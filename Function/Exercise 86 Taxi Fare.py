BASE_FAIR = 4
METER_TO_KILOMETER = 140 / 1000

def cal_fare(distance):
    distance *= 1000
    fare = BASE_FAIR + (distance / 140) * 0.25
    return fare

distance = float(input('Enter distence in kilometres (km): '))
fare = cal_fare(distance)

print(f'\nThe total fair is ${fare:.2f}')
