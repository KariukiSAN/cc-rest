#!/usr/bin/env python3
import ipdb
import importlib


Customer = importlib.import_module("lib.Customer").Customer
Restaurant = importlib.import_module("lib.Restaurant").Restaurant
Review = importlib.import_module("lib.Review").Review

if __name__ == '__main__':

    customer = Customer()
    restaurant = Restaurant()
    review = Review()


    customer.name = "John"
    customer.email = "john@example.com"
    customer.phone = "1234567890"
    customer.address = "123 Main St"
    customer.city = "San Francisco"
    customer.state = "CA"
    customer.zipcode = "94107"
    customer.save()  

    restaurant.name = "Sample Restaurant"
    restaurant.address = "456 Elm St"
    restaurant.city = "Los Angeles"
    restaurant.state = "CA"
    restaurant.zipcode = "90001"
    restaurant.save()  
    review.customer = customer
    review.restaurant = restaurant
    review.stars = 5
    review.comment = "Awesome!"
    review.save() 

 
    ipdb.set_trace()
