resort = {}
active = True
while active:
    name = input("\nWhat is your name?")
    place = input("If you could visit one place in the world, where would you go?")

    resort[name] = place

    repeat = input("Would you like to let another one respond? (yes/no) ")
    if repeat == 'no':
        active = False

print("\n--- Results ---")
for name, place in resort.items():
    print(name + "'s dream resort is " + place)