class Dog:
    """A simple attempt to Model a Dog"""

    def __init__(self, name, age):
        """Initializing Dog's attributes"""
        self.name = name
        self.age = age

    def sit(self):
        print(f"{self.name} is sitting.")

    def roll_over(self):
        print(f"{self.name} is rolling.")


dog_1 = Dog("Tyson", 2)
dog_2 = Dog("Jack", 5)

dog_1.sit()
dog_1.roll_over()

dog_2.sit()
dog_2.roll_over()
