mylist = ['alpha-romeo','toyota','bmw','ferrari','audi']
friend_list = mylist
friend_lists = mylist[:]

print(id(mylist))
print(id(friend_list))
print(id(friend_lists))


'''if 'alpha-romeo' in mylist:
    print('True1')

if mylist[2].upper() == 'BMW':
     print('True2')

if 'alian' not in mylist:
    print('True3')

if not 'alian' in mylist:
    print('True5')

print('mylist:      ', mylist)
print('friend_list: ', friend_list)

friend_list.append('home_economics')
del friend_list[-2]

mylist.append('home_food')
del mylist[-3]

print('mylist:    ', mylist)
print('friend_list', friend_list)
'''