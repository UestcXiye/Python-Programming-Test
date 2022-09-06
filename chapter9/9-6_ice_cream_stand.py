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


class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_name):
        super(IceCreamStand, self).__init__(restaurant_name, cuisine_name)
        self.flavors = ['chocolate', 'strawberry', 'vanilla']

    def show_flavors(self):
        print("\nDifferent flavors in " + self.restaurant_name.title() + ":")
        for flavor in self.flavors:
            print("\t" + flavor.title() + " IceCream")


icecreamStand = IceCreamStand('love live icecream', 'ice cuisine')
icecreamStand.show_flavors()
