BASE_FAIR = 4

def cal_fare(distance):
    fare = BASE_FAIR + (distance/140) * 0.25
    return fare

distance = int(input('Enter distence in kilometres (km): '))
print(f'\nThe total fair is ${cal_fare(distance):.2f}')
