class Computer:
    def make_shirt(self):
        print(f'Object Oriented Programming')


comp_1 = Computer()
comp_2 = Computer()

Computer.make_shirt(comp_1)
Computer.make_shirt(comp_2)

comp_1.make_shirt()
comp_2.make_shirt()
