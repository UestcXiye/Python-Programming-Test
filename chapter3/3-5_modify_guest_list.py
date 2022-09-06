names = ['Bob', 'Jack', 'Alice', "John", "Tom"]

for i in range(len(names)):
    invite_message = "Hi, " + names[i] + "! Would you like to have a dinner with me?"
    print(invite_message)

print("Sorry to hear that Alice do not have spare time.")

new_guest = "Amy"
names[2] = new_guest
# print(names)
print("Let's send the message again!")

for i in range(len(names)):
    invite_message = "Hi, " + names[i] + "! Would you like to have a dinner with me?"
    print(invite_message)
