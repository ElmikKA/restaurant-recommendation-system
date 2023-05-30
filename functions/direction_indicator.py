from data.food_type_choices import restaurant_type_choices
from data.location_food_choices import location_food_choices




def direction_indicator(location): 

    restaurant_types_string = ""
    for key, restaurant_types in restaurant_type_choices.items(): 
        restaurant_types_string += "{0} - {1}\n".format(key, restaurant_types) 
    
    print("So here are all the restaurant types that we have in Estonia, please choose what kind of restaurant you would like to visit and we will direct you to the nearest restaurant of your choice:\n" + restaurant_types_string)

    restaurant_type_for_directions = get_restaurant_type_choice_for_directions()

    print(citys_that_have_restaurant_of_users_choice(restaurant_type_for_directions))


    


    


def get_restaurant_type_choice_for_directions(): 

    restaurant_choice_letter = input("In here please enter a corresponging letter for your restaurant: ")

    if restaurant_choice_letter in restaurant_type_choices.keys(): 
        restaurant_choice = restaurant_type_choices[restaurant_choice_letter]
        return restaurant_choice
    else: 
        print("We dont have this kind of letter in our system. Please try again ...")
        get_restaurant_type_choice_for_directions()


def citys_that_have_restaurant_of_users_choice(restaurant_type_for_directions): 

    list_of_citys = []

    for city, restaurants in location_food_choices.items():
        for restaurant in restaurants.values(): 
            if restaurant_type_for_directions == restaurant: 
                list_of_citys.append(city)
    
    return list_of_citys


def get_route()