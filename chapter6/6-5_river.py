rivers = {'nile': 'egypt', 'amazon river': 'bizarre', 'yangtze river': 'china'}

for key, value in rivers.items():
    print("The " + key.title() + " runs through " + value.title() + ".")
print("\n")
for key in rivers.keys():
    print(key.title())
print("\n")
for value in rivers.values():
    print(value.title())