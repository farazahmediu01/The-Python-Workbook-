favorite_colors = {
    'sameer': 'orange',
    'ali': 'blue',
    'sarab': 'green',
    'saad': 'orange',
    'talha': 'blue',
    'faraz': 'black',
}
print(f"The list of fovorite colors:")
for color in set(favorite_colors.values()):
    print(color.title())

