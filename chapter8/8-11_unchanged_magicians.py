def show_magicians(magicians):
    for magician in magicians:
        print("\t" + magician)


def make_great(magicians, great_magicians):
    while magicians:
        current_magician = magicians.pop()
        great_magicians.append('the Great ' + current_magician.title())


magicians = ['simon', 'jesse', 'lucy']
great_magicians = []

make_great(magicians[:], great_magicians)
# print(magicians)
# print(great_magicians)
print("Original magicians:")
show_magicians(magicians)
print("\nGreat magicians:")
show_magicians(great_magicians)
