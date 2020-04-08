import functionality as ft

names = ['sameer', 'faraz', 'sarab', 'ali', 'faiq', 'rameez', 'sameer', 'sameer', 'faraz', 'haseeb', 'munir','qadeer', 'naseer']
names_to_delete = ['sameer','faraz', 'naseer']

print('names =',names)
print('names_to_delete =', names_to_delete)
# inputy_list = ft.input_loop()

deleted_names = ft.delete_names(names_to_delete, names)

print('\nAfter')
print('names =',names)
print('names_to_delete =', names_to_delete)
print('deleted_names =', deleted_names)