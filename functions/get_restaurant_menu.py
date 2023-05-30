from data.restaurant_menus import restaurant_menus
#If the import is from the same folder then you have to but "." infront of the file name 
from .get_restaurant_type_choice import get_restaurant_type_choice

def show_restaurant_menu(location): 

    restaurant_type = get_restaurant_type_choice(location)

    if restaurant_type in restaurant_menus.keys():
        print("=====================================")
        for category, items in restaurant_menus[restaurant_type].items(): 
            print(category + ":")
            for item, price in items.items():
                print("- {0} - {1}$".format(item, str(price)))
    else: 
        print("Something went wrong, please try again!")