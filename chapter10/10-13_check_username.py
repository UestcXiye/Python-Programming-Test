import json


def get_stored_username():
    filename = 'username.json'
    try:
        with open(filename, 'r') as file_object:
            username = json.load(file_object)
    except FileNotFoundError:
        return None
    else:
        return username


def get_new_username():
    filename = 'username.json'
    username = input("What's your name? ")

    with open(filename, 'w') as file_object:
        json.dump(username, file_object)

    return username


def greet_user():
    username = get_stored_username()
    if username:
        check = input("Is " + username + " your name? (yes/no): ")
        if check == 'yes':
            print("Welcome back, " + username + "!")
        else:
            username = get_new_username()
            print("We'll remember you when you come back, " + username + "!")
    else:
        username = get_new_username()
        print("We'll remember you when you come back, " + username + "!")


greet_user()
