import json


filename = 'favorite_number.json'

with open(filename, 'r') as file_object:
    number = json.load(file_object)

print("I know your favorite number! It's " + str(number) + ".")
