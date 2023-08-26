class Restaurant:
    def __init__(self, name):
        self.name = name
    def name(self):
        return self.name
    
class Customer:
    def __init__(self, given_name, family_name):
        self.given_name = given_name
        self.family_name = family_name

    def given_name(self):
        return self.given_name

    def family_name(self):
        return self.family_name

    def full_name(self):
        return f"{self.given_name} {self.family_name}"
    
class Review:
    def __init__(self, customer, restaurant, rating):
        self.customer = customer
        self.restaurant = restaurant
        self.rating = rating
    def rating(self):
        return self.rating
    