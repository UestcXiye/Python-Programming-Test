import time


file_name = 'guest_book.txt'
prompt = "\nPlease input your name(Enter 'quit' to end the program): "

while True:
    name = input(prompt)
    if name == 'quit':
        break

    print("\nHi, " + name + "! Nice to see you again!")
    log_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

    with open(file_name, 'a') as file_object:
        file_object.write(name + " logged in in " + log_time + ".\n")
