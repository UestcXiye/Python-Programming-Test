print("Give me two numbers, and I will add them.")

first_number = input("\nFirst number: ")
second_number = input("Second number: ")

try:
    answer = int(first_number) + int(second_number)
except ValueError:
    print("\nError! Make sure you enter two digits.")
else:
    print('\n' + first_number + ' + ' + second_number + ' = ' + str(answer))
