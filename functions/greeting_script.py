from data.location_choices import location_choices


def greeting(): 

    location_choices_string = ""
    for key, location in location_choices.items(): 
        location_choices_string += "{0} - {1}\n".format(key, location)
    
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