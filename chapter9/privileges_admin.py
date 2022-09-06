from user import User


class Privileges:
    def __init__(self):
        self.privileges = ["can add post", "can delete post", "can ban user"]

    def show_privileges(self):
        print("\nYou have the following privileges:")
        for privilege in self.privileges:
            print("\t" + privilege.title())


class Admin(User):
    def __init__(self, first, last, age, location):
        super().__init__(first, last, age, location)
        self.privileges = Privileges()
