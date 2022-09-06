# file_path = '../chapter10/pi_digits.txt'
# file_path = r'C:\Users\81228\Documents\Program\Python Program\chapter10\pi_digits.txt'
file_path = 'C:\\Users\\81228\\Documents\\Program\\Python Program\\chapter10\\pi_digits.txt'

with open(file_path) as file_object:
    contents = file_object.read()
    print(contents.rstrip())
