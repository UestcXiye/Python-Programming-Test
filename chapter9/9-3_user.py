class User:
    def __init__(self, first, last, age, location):
        self.first_name = first
        self.last_name = last
        self.age = age
        self.location = location

    def describe_user(self):
        print("\nUser info:")
        name = self.last_name.title() + " " + self.first_name.title()
        print("\tName: " + name)
        print("\tAge: " + str(self.age))
        print("\tLocation: " + self.location.title())

    def greet_user(self):
        name = self.last_name.title() + " " + self.first_name.title()
        print("\nHi, " + name + "! Nice to see you again!")


zhangsan = User('san', 'zhang', 22, 'shanghai')
lisi = User('si', 'li', 33, 'beijing')
wangwu = User('wu', 'wang', 44, 'sichuan')

zhangsan.describe_user()
zhangsan.greet_user()
lisi.describe_user()
lisi.greet_user()
wangwu.describe_user()
wangwu.greet_user()