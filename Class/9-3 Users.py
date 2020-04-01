class User:

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 0

    def describe_user(self):
        message = f"{self.first_name} {self.last_name}"
        return message.title()

    def greet_user(self):
        greeting = f"Hello {self.first_name.title()}, How are you?"
        return greeting

    def print_user_info(self):
        '''This method print the outcome of describe_user() and greet_user()'''
        information = f"\n{self.describe_user()}\n{self.greet_user()}\n"
        information += f"Login attempts = {self.login_attempts}"
        print(information)

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


class Privileges:
    def __init__(self, *privileges):
        self.privileges = ('can edit post', 'can delete post', 'can ban user')
        self.privileges += privileges

    def set_priviliges(self, *privileges):
        print(f"before{self.privileges}")
        for p in privileges:
            self.privileges += p
        print('after', self.privileges)

    def show_privileges(self):
        for text in self.privileges:
            # print(f"{admin_1.first_name} {text}.")
            print(text)


class Admin(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.privileges = Privileges()


admin_1 = Admin('imran', 'khan')
Privileges.privileges = ("hello", "python")















# tupi = ("can go outside","can jump", 'can eat')

# admin_1.privileges.set_priviliges(tupi)
# Privileges.show_priviliges(admin_1)
# admin_1.privileges.show_privileges()


'''
# User_1
user_1.increment_login_attempts()
user_1.increment_login_attempts()
user_1.print_user_info()


# User_2
for i in range(10):
    user_2.increment_login_attempts()
user_2.print_user_info()

# User_3
for i in range(20):
    user_3.increment_login_attempts()
user_3.print_user_info()

# User_4
for i in range(30):
    user_4.increment_login_attempts()
user_4.print_user_info()

# Reset login attempts and print information of all instances.
for user in (user_1, user_2, user_3, user_4):
    user.reset_login_attempts()
    user.print_user_info()
'''
