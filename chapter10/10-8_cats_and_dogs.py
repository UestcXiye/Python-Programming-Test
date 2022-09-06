def print_file(filename):
    try:
        with open(filename) as file_object:
            lines = file_object.readlines()
    except FileNotFoundError:
        print("\nSorry, the file " + filename + " doesn't exist.")
    else:
        print("\nContents in file " + filename + ":")
        for line in lines:
            print("\t" + line.rstrip())


file_names = ['cats.txt', 'dogs.txt']
for file_name in file_names:
    print_file(file_name)
