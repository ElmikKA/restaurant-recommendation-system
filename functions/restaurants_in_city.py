from .get_location import get_location
from data.location_food_choices import location_food_choices
from .get_restaurant_menu import restauran_function
from .direction_indicator import direction_indicator

def restaurants_types_in_city():

    location = get_location()

    restaurant_types = print_restaurant_types(location)

    print("In {0} we have such food restaurants:\n{1}".format(location, restaurant_types))

    does_user_like_restaurants_what_that_city_offers(location)

def print_restaurant_types(location):
    
    restaurant_types_string = ""
    for keys, restaurant_type in location_food_choices[location].items(): 
        restaurant_types_string += "{0} - {1}\n".format(keys, restaurant_type)

    return restaurant_types_string

def does_user_like_restaurants_what_that_city_offers(location): 

    user_input = input("Do you see where would you like to eat? Enter y/n: ")    

    if user_input == "y": 
        resturant_type_input = input("Please pick a restaurant. Choose a corresponding letter: ")
        restaurant_type = location_food_choices[location][resturant_type_input]
        restauran_function(restaurant_type)
    elif user_input == "n": 
        direction_indicator(location)
    else: 
        print("Something went wrong, please try again and try to input a correct letter!")
        does_user_like_restaurants_what_that_city_offers(location)
        