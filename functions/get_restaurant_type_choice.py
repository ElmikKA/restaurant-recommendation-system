from data.location_food_choices import location_food_choices


def get_restaurant_type_choice(location): 

    restaurant_type_choice_letter = input("In what kind of restaurant would you like to eat? Please enter a corresponding letter here: ")

    if restaurant_type_choice_letter in location_food_choices[location].keys(): 
        restaurant_type_choice = location_food_choices[location][restaurant_type_choice_letter]
        return restaurant_type_choice
    else: 
        print("Sorry thats not a restaurant we have data on. Let's try this again ...")
        get_restaurant_type_choice()