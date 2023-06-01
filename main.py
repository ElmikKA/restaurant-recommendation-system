#This is gonna be main file where the logic will be written
from data.location_choices import location_choices
from data.location_food_choices import location_food_choices
from functions.get_location import get_location
from functions.get_restaurant_menu import restauran_function
from functions.direction_indicator import direction_indicator
from functions.greeting_script import greeting


def food_for_you(): 
    greeting()
    

    def show_food_types_of_city():
         
        location = get_location()

        food_types_string = ""
        for keys, food_types in location_food_choices[location].items(): 
                food_types_string += "{0} - {1}\n".format(keys, food_types)
        
        print("In {0} we have such food restaurants:\n{1}".format(location, food_types_string))
        print("================")
        user_input = input("Do you see where would you like to eat? Enter y/n: ")



        if user_input == "y": 
            restaurant_type_input = input("Please pick a restaurant. Choose the corresponding letter: ")
            retsaurant_type = location_food_choices[location][restaurant_type_input]
            restauran_function(retsaurant_type)
        elif user_input == "n": 
            direction_indicator(location)
        else: 
             print("Something went wrong, please try again and try to input a correct letter!")

            
    show_food_types_of_city()







food_for_you()