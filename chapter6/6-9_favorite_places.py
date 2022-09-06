favorite_places = {'alice': ['Beijing', 'Shenzhen'], 'bob': [], 'candy': ['Shanghai']}

for name, places in favorite_places.items():
    if len(places) == 1:
        print("\n" + name.title() + "'s favorite place is: ")
        for place in places:
            print("\t" + place.title())
    elif len(places) > 1:
        print("\n" + name.title() + "'s favorite places are: ")
        for place in places:
            print("\t" + place.title())
    else:
        print("\n" + name.title() + " does not have a favorite place.")
