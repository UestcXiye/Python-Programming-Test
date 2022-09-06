favorite_number = {'Bob': [1, 2, 3], 'Jack': [4, 5, 6], 'Alice': [7, 8, 9]}

for key, values in favorite_number.items():
    print("\n" + key + " like: ")
    for value in values:
        print("\t" + str(value))