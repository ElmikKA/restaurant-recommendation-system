from data.food_type_choices import restaurant_type_choices
from data.location_food_choices import location_food_choices
from data.route_to_city import route_to_city
from algorithms.graph_search import breath_first_search




def direction_indicator(location): 

    restaurant_types_string = ""
    for key, restaurant_types in restaurant_type_choices.items(): 
        restaurant_types_string += "{0} - {1}\n".format(key, restaurant_types) 
    
    print("So here are all the restaurant types that we have in Estonia, please choose what kind of restaurant you would like to visit and we will direct you to the nearest restaurant of your choice:\n" + restaurant_types_string)

    restaurant_type_for_directions = get_restaurant_type_choice_for_directions()

    nearest_citys_that_have_restaurant = citys_that_have_restaurant_of_users_choice(restaurant_type_for_directions)
    

    citys_names = ""
    for city_name in nearest_citys_that_have_restaurant: 
        
        citys_names += "# - {0}\n".format(city_name)
    
    print("So we found " + str(len(nearest_citys_that_have_restaurant)) + " citys near you, that have {0} restaurants!\n{1}".format(restaurant_type_for_directions, citys_names))
    choice_of_city = input("So tell us, which city would you like to go for a good {0} meal? Please enter a corresponding Citys Name: ".format(restaurant_type_for_directions))
    
    if choice_of_city in route_to_city.keys():
        print("You have chosen {0}".format(choice_of_city))
        shortest_route = get_route(location, choice_of_city)
        shortest_route_string = " -> ".join(shortest_route)
        print("Here is the shortest route from {0} to {1} city: {2}".format(location, choice_of_city, shortest_route_string))


    


    


def get_restaurant_type_choice_for_directions(): 

    restaurant_choice_letter = input("In here please enter a corresponging letter for your restaurant: ")
    print("=====================")

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


def get_route(start_point, end_point):

    start_citys = route_to_city[start_point]
    end_citys = route_to_city[end_point]
    routes = []

    for start_city in start_citys: 
        
        for end_city in end_citys: 
            
            city_system = route_to_city
            route = breath_first_search(city_system, start_city, end_city)
            print(route)
            if route is not None: 
                routes.append(route)
                print("Inside if statement" + str(routes))
    
    shortest_route = min(routes, key=len)
    print(shortest_route)
    return shortest_route


