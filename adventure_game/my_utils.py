# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# prompt_question:
#   Ask a question of your user. The user must provide a response that is in
#   you list of valid options
#
#   prompt : A string that will be used to ask the user a question
#
#   valid_options : A list of string values you expect your user to respond with.
#
#   example usage:
#       a_topping = prompt_question("Would you like cheese on your pizza?", ['yes', 'no'])
def prompt_question(prompt, valid_options):
    response = input(prompt)
    while not response.lower() in valid_options:
        print("Sorry, I did not understand your choice.")
        response = input(prompt)
    return response.lower()


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# ask_command:
#   Ask your user for a command. The user must provide a response that is in
#   you list of valid options
#
#   prompt : A string that will be used to ask the user a question
#
#   valid_options : A list of string values you expect your user to respond with.
#
#   example usage:
#       a_topping = prompt_question("What do you want to do?", ['go', 'take', 'drop'])
def ask_command(prompt, valid_commands, no_arguments = ['status', 'help']):
    ask_again = True
    result = []
    while ask_again:
        # Get a response from the user and split the response into words
        response = input(prompt)
        words = response.split()

        # be safe against user accidents of just hitting the ENTER key
        if len(words) > 0:
            #check if the command is the list of valid commands
            if words[0].lower() not in valid_commands:
                print('\tSorry, I don\'t understand:"', response, '"')
                print('\t\t Your choices are:', valid_commands, "\n")
            else:
                #if the command is valid, but they forgot an argument, try again.
                if len(words) < 2:
                    # but check first if it was in the no argument list
                    if words[0].lower() in no_arguments:
                        result = words
                        ask_again = False
                    else:
                        print('\tThe command: "', words[0], '" requires an argument.\n')
                else:
                    # Otherwise we at least have two arguments! Now programmer gets to choose what to do.
                    ask_again = False
                    result = words
    # END WHILE LOOP

    #Return the command back to the user as a list (command will be index 0)
    # If the command was required then it will be in position 1
    return result
def has_a(player_inventory, item):
    if item in player_inventory.keys():
        current_count = player_inventory[item]
        if current_count > 0:
            return True
        else:
            return False
    else:
        return False

def drop_item(player_inventory, room_inventory, item):
    if has_a(player_inventory, item):
        current_count = player_inventory[item]
        player_inventory[item] = current_count - 1
        if player_inventory[item] == 0:
            del player_inventory[item]
        if has_a(room_inventory, item):
                room_count = room_inventory[item]
                room_inventory[item] = room_count + 1

        room_inventory[item] = 1
        print("You dropped the", item)
    else:
        print("You cannot drop that which you do not possess young grasshopper.")


def take_item(player_inventory, room_inventory, item):
    if has_a(room_inventory, item):
        room_count = room_inventory[item]
        room_inventory[item] = room_count - 1
        if has_a(player_inventory, item):
            player_count = player_inventory[item]
            player_inventory[item] = player_count + 1
        else:
            player_inventory[item] = 1
            print("You take the", item)
    else:
        print("You're out of your element Donny, you can't take this item!")


def room_status(room_inventory):
    print("In this room you see:")
    empty = True
    for key in room_inventory.keys():
        if room_inventory[key] > 0:
            print("\t\ta", key)
            empty = False
    if empty == True:
        print("\t\t....sadly it is empty.")


def player_status(player_inventory):
    print("\tYou are in possession of:")
    for key in player_inventory.keys():
        if player_inventory[key] > 0:
            print("\t\t", key, ' : ' ,player_inventory[key])


def scrub_response(sus_response):
    result = []
    result.append(sus_response[0])

    if len(sus_response) > 1:
        arg = sus_response[1]
        if arg == 'gory':
            result.append('gory simplicity')
        elif arg == 'happy':
            result.append('happy little accidents')
        elif arg == 'pick':
            result.append('pick axe')
        elif arg == 'healing':
            result.append('healing potion')
        elif arg == 'bowling':
            result.append('bowling ball')
        elif arg == 'magic':
            result.append('magic key')
        elif arg == 'minor':
            result.append('minor healing potion')
        elif arg == 'elven':
            result.append('elven greatsword')
        elif arg == 'gold':
            result.append('gold key')
        elif arg == 'holy':
            result.append('holy hand grenade')
        else:
            result.append(sus_response[1])
    return result

def map(player_inventory):
    if 'map' in player_inventory.keys():
        room_map = '''    
            10---8---9   4---7 
                 |       |   | 
                 5---1---3   11
                     |         
                     2---6     
                         |     
                    14---12---13
                    |          
                   15     

                I'm the map!
                '''
        print(room_map)
    else:
        print("You do not have the map right now.")

