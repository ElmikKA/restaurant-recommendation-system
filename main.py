#This is gonna be main file where the logic will be written
from functions.greeting_script import greeting
from functions.restaurants_in_city import restaurants_types_in_city


def food_for_you(): 
    
    greeting()
    restaurants_types_in_city()
    

food_for_you()