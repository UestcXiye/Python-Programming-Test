person1 = {'first_name': 'San', 'last_name': 'Zhang', 'age': 22, 'city': "Shenzhen"}
person2 = {'first_name': 'Si', 'last_name': 'Li', 'age': 68, 'city': "Beijing"}
person3 = {'first_name': 'Wu', 'last_name': 'Wang', 'age': 6, 'city': "Shanghai"}
people = [person1, person2, person3]

for person in people:
    name = person['last_name'] + person['first_name']
    print("\nName: " + name)
    print("Age: " + str(person['age']))
    print("City: " + person['city'])
