class User:
    """This Class define a user."""

    def __init__(self, first_name, last_name):
        """initializing user attributes."""
        self.first_name = first_name
        self.last_name = last_name
        self.full_name = f"{first_name} {last_name}"

    def describe_user(self):
        print("\nThis user belongs to User class.")
        print(f"Name: {self.full_name}")

    def greet_user(self):
        print(f"\nHello {self.first_name}, How are you!")


user_1 = User("Amir", "Khan")
user_2 = User("Ravi", "Kumar")

user_1.describe_user()
user_2.describe_user()

user_1.greet_user()
user_2.greet_user()

print(
user_2.full_name,
user_1.full_name
)