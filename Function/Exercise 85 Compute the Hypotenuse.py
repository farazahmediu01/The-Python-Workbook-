from math import sqrt

def cal_hypo(Len_1,Len_2):
    '''This function calculate the Hypotenuse using Pythagorean theorem.'''
    return sqrt(Len_1**2 + Len_2**2)
     

print('Enter two short sides of triangle to get its hypotenuse.')
Len_1 = int(input('Enter 1st lenght: '))
Len_2 = int(input('Enter 2nd lenght: '))

print(f'\nHypotenuse = {cal_hypo(Len_1,Len_2)}')