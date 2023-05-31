from data.location_choices import location_choices

def get_location():

    location_letter = input("Where are you? Please enter a corresponding letter here: ")

    if location_letter in location_choices.keys(): 
        location = location_choices[location_letter]
        return location 
    else: 
        print("Sorry, that's not a location we have data on. Let's try this again ...")
        get_location()