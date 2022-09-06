from random import randint


class Die:
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        x = randint(1, self.sides)
        print(x)


die_6 = Die()
print("\nThe results of a 6-sized die:")
for i in range(10):
    die_6.roll_die()

die_10 = Die(sides=10)
print("\nThe results of a 10-sized die:")
for i in range(10):
    die_10.roll_die()

die_20 = Die(sides=20)
print("\nThe results of a 20-sized die:")
for i in range(10):
    die_20.roll_die()