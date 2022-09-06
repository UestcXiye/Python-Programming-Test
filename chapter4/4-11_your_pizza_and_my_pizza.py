pizzas = ['romano', 'ricotta', 'pepperoni']
friend_pizzas = pizzas[:]

pizzas.append('fruit')
friend_pizzas.append('meet')

print("My favorite pizzas are:")
for pizza in pizzas:
    print(pizza + " ")

print("My friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza + " ")
print("\n")

