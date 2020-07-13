class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(f"The {self.name} is sitting.")

    def roll(self):
        print(f"The {self.name} is rolling.")


dog_1 = Dog("Dolly", 6)
dog_2 = Dog("Joji", 8)

# print(dog_1.age) 
# print(dog_2.age)

# dog_1.roll()
# dog_2.sit()
print(dir(dog_1))