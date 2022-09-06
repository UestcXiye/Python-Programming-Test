def print_file(filename):
    try:
        with open(filename, 'r') as file_object:
            contents = file_object.read()
    except FileNotFoundError:
        pass
    else:
        print("\nContents in file " + filename + ":")
        print(contents)


file_names = ['cats.txt', 'dogs.txt']
for file_name in file_names:
    print_file(file_name)
