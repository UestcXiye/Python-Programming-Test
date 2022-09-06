active = True
prompt = "Please tell me a series of pizza ingredients(enter 'quit' to end): "
while active:
    message = input(prompt)

    if message == 'quit':
        active = False
        # print("That's all! Please wait ten minutes.")
    else:
        print("We'll add " + message + " into your pizza.")