# starting with empty list.
aliens = []

for number in range(10):
    green_alien = {'color': 'green', 'point': 5, 'speed': 'slow'}
    aliens.append(green_alien)
#aliens = [green_alien for number in range(10)]

for alien in aliens[:5]:
    alien['color'] = 'yellow'
    alien['point'] = 10
    alien['speed'] = 'medium'

for alien in aliens:
    print(alien)























'''
for number in range(10):
    green_alien = {'color': 'green', 'point': 5, 'speed': 'slow'}
    aliens.append(green_alien)

print(len(aliens))


for alien in ballu_party[:3]:
    alien['color'] = 'yellow'
    alien['point'] = 10
    alien['speed'] = 'medium'

for alien in ballu_party[:5]:
    print(alien)
'''