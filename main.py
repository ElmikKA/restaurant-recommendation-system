#This is gonna be main file where the logic will be written
from data.location_choices import location_choices
from data.location_food_choices import location_food_choices
from functions.get_location import get_location
from functions.get_restaurant_menu import show_restaurant_menu
from functions.direction_indicator import direction_indicator

location_choices_string = ""
for key, location in location_choices.items(): 
    location_choices_string += "{0} - {1}\n".format(key, location)


def greeting(): 
    print("Hello and welcome to the Food For You!")
    print("In here you can find food for your taste and even have it located for you!!!!!")
    print("Please tell us where are you located:\n" + location_choices_string)



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
            show_restaurant_menu(location)
        else: 
            direction_indicator(location)

            
    show_food_types_of_city()







food_for_you()