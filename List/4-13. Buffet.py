foods = ('pizza fries', 'crisp roll', 'zinger burger', 'italian salad', 'twist potatto')

print('\nOriginal items:')
for food in foods:
    print(f'{food.title()}.')

foods = ('pizza fries', 'twist potatto', 'chiken burger', 'italian salad', 'crispy maya roll',)

print('*' * 20 + '\n\nModified items:')
for food in foods:
    print(food.title() + '.')

print('*' * 20 + '\n\nLabeled Items: ')
for number in range(len(foods)):
    message = f'{number}) {foods[number].title()}.'
    print(message)
