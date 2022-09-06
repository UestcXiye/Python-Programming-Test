def make_sandwich(*ingredients):
    print("\nMaking a sandwich with the following ingredients:")
    for ingredient in ingredients:
        print("- " + ingredient)


make_sandwich('mushrooms', 'green peppers', 'cheese')
make_sandwich('eggs')
make_sandwich('bacon', 'apples')
