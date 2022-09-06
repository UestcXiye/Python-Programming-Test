foods = ('rice', 'egg', 'fish', 'beef', 'apple')
print("Original menu:")
for food in foods:
    print(food)

# foods[-1] = 'orange'

'''报错信息
Traceback (most recent call last):
  File "C:/Users/81228/Documents/Program/Python Program/chapter4/4-13_buffet.py", line 5, in <module>
    foods[-1] = 'orange'
TypeError: 'tuple' object does not support item assignment
'''

print("\nModified menu:")
foods = ('rice', 'egg', 'fish', 'milk', 'orange')
for food in foods:
    print(food)
