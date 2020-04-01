def add_to_list(item, lst=None, string=''):
    lst = []
    lst.append(item)
    string += item
    print(lst)
    print(item)

# add_to_list('a')
# add_to_list('b')
# add_to_list('c')


class MyClass:
    log = list()

    # def __init__(self):
    #     self.log = []
    
    def writing_log(self, item):
        self.log.append(item)

usr1 = MyClass()
usr2 = MyClass()

usr1.writing_log('hello')

usr2.log = []
usr2.writing_log('world')
print(id(usr1.log))
print(id(usr2.log))
