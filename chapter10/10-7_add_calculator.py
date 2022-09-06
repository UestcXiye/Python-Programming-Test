print("Give me two numbers, and I will add them.")
print("Enter 'quit' to end the program.")

while True:
    first_number = input("\nFirst number: ")
    if first_number == 'quit':
        break

    second_number = input("Second number: ")
    if second_number == 'quit':
        break

    try:
        answer = int(first_number) + int(second_number)
    except ValueError:
        print("\nError! Make sure you enter two digits.")
    else:
        print('\n' + first_number + ' + ' + second_number + ' = ' + str(answer))
