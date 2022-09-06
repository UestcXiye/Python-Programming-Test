pet1 = {'name': 'Alice', 'variety': 'cat', 'owner_name': 'Amy'}
pet2 = {'name': 'Bob', 'variety': 'dog', 'owner_name': 'John'}
pet3 = {'name': 'Candy', 'variety': 'bird', 'owner_name': 'Mike'}
pets = [pet1, pet2, pet3]

for pet in pets:
    print("\nName: " + pet['name'])
    print("Variety: " + pet['variety'])
    print("Owner name: " + pet['owner_name'])
