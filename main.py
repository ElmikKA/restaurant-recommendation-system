#This is gonna be main file where the logic will be written
from data.food_type_choices import food_type_choices
from data.location_choices import location_choices
from data.location_food_choices import location_food_choices
from data.restaurant_menus import restaurant_menus

food_type_string = ""
for key, food_type in food_type_choices.items():
    food_type_string += "{0} - {1}\n".format(key, food_type)

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
        
        show_restaurants_menu(location)    
        
    
    def show_restaurants_menu(location): 

        restaurant_type = get_restaurant_type_choice(location)

        if restaurant_type in restaurant_menus.keys():
            print("=====================================")
            for category, items in restaurant_menus[restaurant_type].items(): 
                print(category + ":")
                for item, price in items.items():
                    print("- {0} - {1}$".format(item, str(price)))
        else: 
            print("Something went wrong, please try again!")



    def get_location():

        location_letter = input("Where are you? Please enter a corresponding letter here: ")

        if location_letter in location_choices.keys(): 
            location = location_choices[location_letter]
            print(location)
            return location 
        else: 
            print("Sorry, that's not a location we have data on. Let's try this again ...")
            get_location()
         
         
    def get_restaurant_type_choice(location): 

        restaurant_type_choice_letter = input("In what kind of restaurant would you like to eat? Please enter a corresponding letter here: ")

        if restaurant_type_choice_letter in location_food_choices[location].keys(): 
            restaurant_type_choice = location_food_choices[location][restaurant_type_choice_letter]
            return restaurant_type_choice
        else: 
            print("Sorry thats not a restaurant we have data on. Let's try this again ...")
            get_restaurant_type_choice()

    
            
    show_food_types_of_city()







food_for_you()