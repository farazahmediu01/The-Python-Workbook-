aliens = []
for num in range(10):
    alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(alien)
#print("There are " + str(len(aliens)) + " in the list.")

for alien in aliens[:5]:
    alien['color'] = 'yellow'
    alien['points'] = 10
    alien['speed'] = 'medium'

for alien in aliens:
    print(alien)