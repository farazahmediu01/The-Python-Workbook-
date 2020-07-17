class User:
    """This Class define a user"""

    def __init__(self, first_name, last_name):
        """Initialzing attributes for a user """
        self.first_name = first_name
        self.last_name = last_name
        self.full_name = f"{first_name} {last_name}"

    def describe_user(self):
        """User discription"""
        print(f"Name: {self.full_name}")

    def greet_user(self):
        """This method greets user"""
        print(f"Hello {self.first_name}\n")


user_1 = User("Ali", "Khan")
user_2 = User("Sameer", "Ahmed")

user_1.describe_user()
user_1.greet_user()

user_2.describe_user()
user_2.greet_user()