#This is gonna be main file where the logic will be written
from data.location_choices import location_choices
from data.location_food_choices import location_food_choices
from functions.get_location import get_location
from functions.get_restaurant_menu import restauran_function
from functions.direction_indicator import direction_indicator

location_choices_string = ""
for key, location in location_choices.items(): 
    location_choices_string += "{0} - {1}\n".format(key, location)


def greeting(): 
    welcome_logo = """
 __      __       .__                                ___________      ___________               .___ ___________            _____.___.            ._. 
/  \    /  \ ____ |  |   ____  ____   _____   ____   \__    ___/___   \_   _____/___   ____   __| _/ \_   _____/__________  \__  |   | ____  __ __| | 
\   \/\/   // __ \|  | _/ ___\/  _ \ /     \_/ __ \    |    | /  _ \   |    __)/  _ \ /  _ \ / __ |   |    __)/  _ \_  __ \  /   |   |/  _ \|  |  \ | 
 \        /\  ___/|  |_\  \__(  <_> )  Y Y  \  ___/    |    |(  <_> )  |     \(  <_> |  <_> ) /_/ |   |     \(  <_> )  | \/  \____   (  <_> )  |  /\| 
  \__/\  /  \___  >____/\___  >____/|__|_|  /\___  >   |____| \____/   \___  / \____/ \____/\____ |   \___  / \____/|__|     / ______|\____/|____/ __ 
       \/       \/          \/            \/     \/                        \/                    \/       \/                 \/                    \/
        """
    print(welcome_logo)
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
            restaurant_type_input = input("Please pick a restaurant. Choose the corresponding letter: ")
            retsaurant_type = location_food_choices[location][restaurant_type_input]
            restauran_function(retsaurant_type)
        else: 
            direction_indicator(location)

            
    show_food_types_of_city()







food_for_you()