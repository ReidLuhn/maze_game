import adventure_game.my_utils as utils

# # # # #
# ROOM 8
#
# Serves as a good template for blank rooms


room8_inventory = {
    'elven greatsword': 1,
    'book': 1
}

room_state = {
    'door_locked': True,
}

def run_room(player_inventory):
    # Let the user know what the room looks like
    # valid commands for this room
    room8_description = '''
        . . .  8th room ... 
        You are standing in a hallway. There is a door to the EAST and a locked door to the WEST. 
        '''

    if room8_inventory['elven greatsword'] > 0:
        room8_description = room8_description + " There is an elven greatsword hanging on the wall."
    if room8_inventory['book'] > 0:
        room8_description = room8_description + " There is a book on a desk."
    print(room8_description)


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
            if direction == 'west':
                is_locked = room_state['door_locked']
                if not is_locked:
                    next_room = 10
                    done_with_room = True
                else:
                    print("The door is locked.")
            if direction == 'east':
                next_room = 9
                done_with_room = True
            if direction == 'south':
                next_room = 5
                done_with_room = True
            else:
                print("You cannot go", direction)
        elif the_command == 'take':
            take_what = response[1].lower()
            utils.take_item(player_inventory, room8_inventory, take_what)
        elif the_command == 'status':
            utils.room_status(room8_inventory)
            utils.player_status(player_inventory)
        elif the_command == 'drop':
            drop_what = response[1]
            utils.drop_item(player_inventory, room8_inventory, drop_what)
        elif the_command == 'use':
            use_what = response[1]
            if use_what == 'gold key':
                if 'gold key' not in player_inventory.keys():
                    print("You don't have a gold key!")
                else:
                    door_locked = room_state["door_locked"]
                    if door_locked:
                        room_state["door_locked"] = False
                        print("The door to the WEST is unlocked!")
                    else:
                        print("The door was already unlocked!")
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
        elif the_command == 'examine':
            examine_what = response[1]
            if examine_what == 'book':
                print("The book has no writing in it.")
            if examine_what == 'map':
                utils.map(player_inventory)

            # END of WHILE LOOP - done_room
            # TODO return next room
    return next_room