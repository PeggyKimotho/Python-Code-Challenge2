# Python-Code-Challenge2

This challenge defines a basic restaurant review system that allows users to create customers, restaurants, and reviews.

This system allows users to create customers, restaurants, and reviews, facilitating the management and retrieval of customer feedback and restaurant information. The code is organized into three classes: Review, Customer, and Restaurant, each serving a specific role in the system.

## Classes

### Review

The Review class captures essential information about the review, including the customer, the restaurant being reviewed, and the assigned rating. 
#### Methods:

- **__init__(self, customer, restaurant, rating):** Constructor method initializes a new review object with the provided customer, restaurant, and rating. The review is then automatically added to the all_reviews list.
- **get_rating(self):** Returns the rating given in the review.
- **get_customer(self):** Returns the customer who authored the review.
- **get_restaurant(self):** Returns the restaurant being reviewed.

### Customer

The Customer class represents an individual who can write reviews for restaurants. It stores customer-related data and actions. 

#### Methods:

- **__init__(self, given_name, family_name):** Constructor method creates a new customer with the provided given name and family name. The customer is then added to the all_customers list.
- **get_given_name(self):** Returns the given name of the customer.
- **get_family_name(self):** Returns the family name of the customer.
- **full_name(self):** Generates and returns the full name of the customer by combining the given and family names.
- **reviewed_restaurants(self):** Retrieves a list of restaurants that the customer has reviewed.
- **add_review(self, restaurant, rating):** Allows the customer to create a new review for a restaurant with a given rating.

### Restaurant
The Restaurant class models a restaurant and its associated data, such as reviews and customers. 

#### Methods:

- **__init__(self, name):** Constructor method initializes a new restaurant with the provided name.
- **get_name(self):** Returns the name of the restaurant.
- **__str__(self):** Provides a custom string representation of the restaurant by returning its name.
- **reviews(self):** Retrieves a list of reviews associated with the restaurant.
- **customers(self):** Retrieves a list of customers who have reviewed the restaurant.
- **average_star_rating(self):** Calculates and returns the average star rating for the restaurant based on its reviews.
- **find_by_name(cls, name):** Class method to search for a restaurant by its name.

### Usage/Sample

To utilize the Restaurant Review System, follow these steps:

- Instantiate Customer and Restaurant objects using the provided constructors.
- Use the customer's add_review method to add reviews for specific restaurants.
- Employ various methods to extract information, such as retrieving a customer's reviewed restaurants, finding a restaurant by name, and calculating average ratings.

#### Sample instances for testing

customer1 = Customer("John", "Doe")

restaurant1 = Restaurant("Burger King")

review1 = Review(customer1, restaurant1, 4)

##### Print
print(customer1.full_name())

print(review1.get_rating())

print(restaurant1)
