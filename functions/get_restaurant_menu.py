from data.restaurant_menus import restaurant_menus
#If the import is from the same folder then you have to but "." infront of the file name 
from .goodbye_script import goodbye_script
from data.restaurant_logos import restaurant_logos

def restauran_function(restaurant_type): 
    
    show_restaurants_logo(restaurant_type)
    show_restaurant_menu(restaurant_type)
    user_input_for_yes_or_no = input("Do you see anything you would like to eat? Please type y/n: ")
    food_picking(restaurant_type,  user_input_for_yes_or_no)


def show_restaurant_menu(restaurant_type): 

    print("Hello and welcome to {0} restaurant. Please look at the menu and let us know when you are ready to order.".format(restaurant_type))
    if restaurant_type in restaurant_menus.keys():
        print("=====================================")
        for category, items in restaurant_menus[restaurant_type].items(): 
            print(category + ":")
            for item, price in items.items():
                print("- {0} - {1}$".format(item, str(price)))

    else: 
        print("Something went wrong, please try again!")



def food_picking(restaurant_type, user_input_for_yes_or_no, price = 0,): 

    if user_input_for_yes_or_no == "y": 
        user_pick_of_food = input("Please write what would you like to eat: ")
        user_pick_of_food_list = []
        for items in restaurant_menus[restaurant_type].values():
            for item in items.keys():
                if item in user_pick_of_food: 
                    user_pick_of_food_list.append(item)
                    price += items[item]
        does_user_want_more_food_to_order = input("Would you like to order more? Please type y/n: ")
        if does_user_want_more_food_to_order == "y": 
            price = food_picking(restaurant_type, user_input_for_yes_or_no, price)
            print("Price: " + str(price))
        else: 
            print("You have chosen {0}".format(user_pick_of_food_list))
            print("You have to pay us {0}".format(str(price)))

    else: 
        if_user_picks_no = input("Would you like to see other restaurant choices again? Please type y/n: ")
        if if_user_picks_no == "Y": 
            #direction_indicator(location)
            pass
        else: 
            goodbye_script()


    return price

def show_restaurants_logo(restaurant_type):

    for restaurant_logo in restaurant_logos.keys(): 
        if restaurant_type in restaurant_logo:
            logo = restaurant_logos[restaurant_type]
            print(logo)            
