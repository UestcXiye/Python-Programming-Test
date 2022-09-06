file_name = 'reasons.txt'
prompt = "\nPlease tell me why you love coding(Enter 'quit' to end the program): "

while True:
    reason = input(prompt)
    if reason == 'quit':
        break

    with open(file_name, 'a') as file_object:
        file_object.write(reason + '\n')
