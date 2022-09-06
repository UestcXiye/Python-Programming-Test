from restaurant import Restaurant

restaurant = Restaurant('beijing restaurant', 'traditional food')
print(restaurant.restaurant_name + "," + restaurant.cuisine_name)
restaurant.describe_restaurant()
restaurant.open_restaurant()