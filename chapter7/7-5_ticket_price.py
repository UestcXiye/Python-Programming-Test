active = True
prompt = "Please tell me your age(enter 'quit' to end): "
while active:
    age = input(prompt)

    if age == 'quit':
        active = False
    else:
        age = int(age)
        if age < 3:
            print("Your ticket price is 0.")
        elif age < 12:
            print("Your ticket price is $10.")
        else:
            print("Your ticket price is $15.")