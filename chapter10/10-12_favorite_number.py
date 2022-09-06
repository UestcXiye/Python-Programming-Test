import json


filename = 'my_favorite_number.json'

try:
    with open(filename) as file_object:
        favoriteNumber = json.load(file_object)
except FileNotFoundError:
    number = input("\nWhat's your favorite number? ")
    with open(filename, 'w') as file_object:
        json.dump(number, file_object)
        print("We'll remember that " + str(number) + " is your favorite number.")
else:
    print("I know your favorite number! It's " + str(favoriteNumber) + ".")
