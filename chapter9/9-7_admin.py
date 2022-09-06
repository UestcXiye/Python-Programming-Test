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


class Admin(User):
    def __init__(self, first, last, age, location):
        super().__init__(first, last, age, location)
        self.privileges = ["can add post", "can delete post", "can ban user"]

    def show_privileges(self):
        name = self.last_name.title() + " " + self.first_name.title()
        print("\nHello, " + name + "! You have the following privileges:")
        for privilege in self.privileges:
            print("\t" + privilege.title())


admin = Admin('liu', 'zhao', '18', 'chengdu')
admin.show_privileges()