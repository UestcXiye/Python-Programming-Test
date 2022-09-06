names = ['Bob', 'Jack', 'Alice', "John", "Tom"]
for i in range(len(names)):
    invite_message = "Hi, " + names[i] + "! Would you like to have a dinner with me?"
    print(invite_message)

print("I find a bigger table, so I can invite 3 guests additionally.")

new_guest = ['ZhangSan', 'LiSi', 'WangWu']

names.insert(0, new_guest[0])
names.insert(3, new_guest[1])
names.append(new_guest[2])
# print(names)
print("Let's send the message again!")

for i in range(len(names)):
    invite_message = "Hi, " + names[i] + "! Would you like to have a dinner with me?"
    print(invite_message)

print("Oh no! I just learned that the newly purchased table could not be delivered in time, so I can only invite 2 "
      "guests.")

while len(names) > 2:
    popped_guest = names.pop()
    notice_message = "I'm sorry, " + popped_guest + ". I can't invite you to dinner."
    print(notice_message)
# print(names)
while len(names):
    del names[0]

print(names)
