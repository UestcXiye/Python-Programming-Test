current_users = ['Bob', 'Jack', 'Alice', "John", "Tom", 'admin']
new_users = ['Amy', 'Candy', 'Tim', 'Jinx', 'Admin']

for i in range(len(current_users)):
    current_users[i] = current_users[i].lower()

for new_user in new_users:
    if new_user.lower() in current_users:
        print("Hi, " + new_user + "! This user name already exists. Please change your user name.")
    else:
        print("Hi, " + new_user + "! This user name is not in use.")
