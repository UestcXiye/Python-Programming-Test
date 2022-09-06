class Restaurant:
    def __init__(self, restaurant_name, cuisine_name):
        self.restaurant_name = restaurant_name
        self.cuisine_name = cuisine_name

    def describe_restaurant(self):
        print("\nRestaurant name: " + self.restaurant_name.title())
        print("Cuisine name: " + self.cuisine_name.title())

    def open_restaurant(self):
        print("\n" + self.restaurant_name.title() + " is opening")


beijing_restaurant = Restaurant('beijing restaurant', 'beijing food')
lanzhou_restaurant = Restaurant('lanzhou restaurant', 'lanzhou food')
sichuan_restaurant = Restaurant('sichuan restaurant', 'sichuan food')

beijing_restaurant.describe_restaurant()
lanzhou_restaurant.describe_restaurant()
sichuan_restaurant.describe_restaurant()
