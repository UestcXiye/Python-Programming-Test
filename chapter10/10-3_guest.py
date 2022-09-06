file_name = 'guest.txt'

name = input("Please input your name: ")
with open(file_name, 'a') as file_object:
    file_object.write(name + '\n')
