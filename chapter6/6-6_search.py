favorite_language = {'jen': 'python', 'sarah': 'c', 'edward': 'ruby', 'phil': 'python'}
names = ['jen', 'tim', 'phil', 'candy']

for name in names:
    if name in favorite_language.keys():
        print("Dear " + name.title() + ", Thank you for involving in this search!")
    else:
        print("Hi, " + name.title() + "! Would you want to participate in an interesting search?")