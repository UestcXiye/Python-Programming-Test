import json


filename = 'favorite_number.json'
number = 6

with open(filename, 'w') as file_object:
    json.dump(number, file_object)
    print("We'll remember that " + str(number) + " is your favorite number.")
