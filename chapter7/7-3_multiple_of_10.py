number = input("Please input a number: ")
number = int(number)

if number % 10 == 0:
    print(str(number) + " is multiple of 10.")
else:
    print(str(number) + " is not multiple of 10.")