def show_magicians(magicians):
    for magician in magicians:
        print(magician)


def make_great(magicians, great_magicians):
    while magicians:
        current_magician = magicians.pop()
        great_magicians.append('the Great ' + current_magician.title())
