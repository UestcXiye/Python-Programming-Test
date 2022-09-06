class Restaurant():
    def __init__(self, restaurant_name, cuisine_name):
        self.restaurant_name = restaurant_name
        self.cuisine_name = cuisine_name

    def describe_restaurant(self):
        print("\nRestaurant name: " + self.restaurant_name.title())
        print("Cuisine name: " + self.cuisine_name.title())

    def open_restaurant(self):
        print("\n" + self.restaurant_name.title() + " is opening")


restaurant = Restaurant('beijing restaurant', 'traditional food')
print(restaurant.restaurant_name + "," + restaurant.cuisine_name)
restaurant.describe_restaurant()
restaurant.open_restaurant()
