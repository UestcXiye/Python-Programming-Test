class User:
    def __init__(self, first, last, age, location):
        self.first_name = first
        self.last_name = last
        self.age = age
        self.location = location
        self.login_attempts = 0

    def describe_user(self):
        print("\nUser info:")
        name = self.last_name.title() + " " + self.first_name.title()
        print("\tName: " + name)
        print("\tAge: " + str(self.age))
        print("\tLocation: " + self.location.title())

    def greet_user(self):
        name = self.last_name.title() + " " + self.first_name.title()
        print("\nHi, " + name + "! Nice to see you again!")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


user = User('san', 'zhang', 22, 'shanghai')
for i in range(10):
    user.increment_login_attempts()
print(user.login_attempts)
user.reset_login_attempts()
print(user.login_attempts)
