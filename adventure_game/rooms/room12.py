import adventure_game.my_utils as utils

# # # # #
# ROOM 12
#
# Serves as a good template for blank rooms
room_state = {
    'door_locked': True
}

room12_inventory = {
    'map': 1,
    'healing potion': 1
}

def run_room(player_inventory):
    # Let the user know what the room looks like
    # valid commands for this room
    room12_description = '''
        . . .  12rd room ... 
        You find yourself in a sort of corridor. There are doors to the EAST and WEST.
        '''

    if room_state['door_locked'] == True:
        room12_description = room12_description + " The door to the WEST is locked. It seems like you need a special gem to unlock it."
    if room12_inventory['map'] == 1:
        room12_description = room12_description + " There is a map hanging on the wall."
    if room12_inventory['healing potion'] == 1:
        room12_description = room12_description + " A healing potion sits on the desk."
    print(room12_description)


    commands = ["go", "take", "drop", "use", "drink", "examine", "status", "help"]
    no_args = ["examine", "status", "help"]

    # nonsense room number,
    # In the loop below the user should eventually ask to "go" somewhere.
    # If they give you a valid direction then set next_room to that value
    next_room = -1

    done_with_room = False
    while not done_with_room:
        # Examine the response and decide what to do
        response = utils.ask_command("What do you want to do?", commands, no_args)
        response = utils.scrub_response(response)
        the_command = response[0].lower()

        # now deal with the command
        if the_command == 'go':
            direction = response[1].lower()
            if direction == 'east':
                next_room = 13
                done_with_room = True
            elif direction == 'west':
                is_locked = room_state['door_locked']
                if not is_locked:
                    next_room = 14
                    done_with_room = True
                elif 'sapphire' in player_inventory.keys():
                    print("You should use the sapphire")
                else:
                    print("You do not have a gem.")
            elif direction == 'north':
                next_room = 6
                done_with_room = True
            else:
                print("You cannot go", direction)
        elif the_command == 'take':
            take_what = response[1].lower()
            utils.take_item(player_inventory, room12_inventory, take_what)
        elif the_command == 'use':
            if response[1] == 'sapphire':
                if 'sapphire' not in player_inventory.keys():
                    print("You do not have a gem.")
                else:
                    door_locked = room_state["door_locked"]
                    if door_locked:
                        room_state["door_locked"] = False
                        print("You place the sapphire in the center of the door. It glows for a moment,"
                              " and then winks out. You hear some clicking, and now the door to the WEST is unlocked!")
                        del player_inventory['sapphire']
                    else:
                        print("The door was already unlocked!")
        elif the_command == 'status':
            utils.room_status(room12_inventory)
            utils.player_status(player_inventory)
        elif the_command == 'drink':
            potion = response[1]
            if potion == 'healing potion':
                if player_inventory['healing potion'] == 1:
                    print("You drink a healing potion. You gain 20 hit points.")
                    player_inventory['health'] = player_inventory['health'] + 20
                    print("Your health is now:", player_inventory['health'])
            elif potion == 'minor healing potion':
                if player_inventory['minor healing potion']:
                    print("You drink the minor healing potion. You gain 10 hit points.")
                    player_inventory['health'] = player_inventory['health'] + 10
                    print("Your health is now:", player_inventory['health'])
            else:
                print("You do not have a healing potion Donny.")
        elif the_command == 'drop':
            drop_what = response[1]
            utils.drop_item(player_inventory, room12_inventory, drop_what)
        elif the_command == 'examine':
            examine_what = response[1]
            if examine_what == 'healing potion':
                print("Nothing special about it, it's just a healing potion Donny.")
            if examine_what == 'map':
                print("It is a map of the dungeon. You are in room 12, and the map looks like this: ")
                map = '''    
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
                print(map)

            # END of WHILE LOOP - done_room
            # TODO return next room
    return next_room