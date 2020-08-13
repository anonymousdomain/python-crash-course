class Restaurant:
    def __init__(self, restaurant_name, cuisine_ytpe):
        self.restaurant_name = restaurant_name
        self.cuisine_ytpe = cuisine_ytpe

    def describe_restaurant(self):
        print(f"name of the restaurant is {self.restaurant_name} its is {self.cuisine_ytpe}")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is opend")


restaurant = Restaurant('harmony hotel', '5 starts hotel')
restaurant.describe_restaurant()
restaurant.open_restaurant()
