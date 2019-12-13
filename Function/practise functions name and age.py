def get_old(name,age=23):
    '''This function teels you when you get 100 year old'''
    year = 2019 - age + 100
    message = f'{name.title()}, you get 100 year old in year {year}.'
    print(message)

get_old(age=12,name='faraz')
