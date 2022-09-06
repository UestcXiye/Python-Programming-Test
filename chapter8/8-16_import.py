# 1
import make_car
car = make_car.make_car('subaru', 'outback', color='blue', tow_package=True)
print(car)

# 2
'''
from make_car import make_car
car = make_car('subaru', 'outback', color='blue', tow_package=True)
print(car)
'''

# 3
'''
from make_car import make_car as mc
car = mc('subaru', 'outback', color='blue', tow_package=True)
print(car)
'''

# 4
'''
import make_car as mc
car = mc.make_car('subaru', 'outback', color='blue', tow_package=True)
print(car)
'''

# 5
'''
from make_car import *
car = make_car('subaru', 'outback', color='blue', tow_package=True)
print(car)
'''