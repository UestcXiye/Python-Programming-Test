class Restaurant:
    def __init__(self, restaurant_name, cuisine_name):
        self.restaurant_name = restaurant_name
        self.cuisine_name = cuisine_name
        self.number_served = 0

    def describe_restaurant(self):
        print("\nRestaurant name: " + self.restaurant_name.title())
        print("Cuisine name: " + self.cuisine_name.title())
        print("Number served: " + str(self.number_served))

    def open_restaurant(self):
        print("\n" + self.restaurant_name.title() + " is opening")

    def set_number_served(self, number):
        self.number_served = number


restaurant = Restaurant('beijing restaurant', 'traditional food')
print(restaurant.number_served)
restaurant.number_served = 10
print(restaurant.number_served)

restaurant.set_number_served(20)
print(restaurant.number_served)
