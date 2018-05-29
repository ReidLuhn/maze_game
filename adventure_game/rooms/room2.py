import adventure_game.my_utils as utils

#
# Items currently in the room.
#



room2_inventory = {
    'key': 1,
    'cup': 1,
    'rock': 1
}


# # # # # # # # #
#   Room 2
#       This room can only be gotten too from Room 1
#       You can only go to room 1
#       You can take a key
#       There is nothing to use in this room
#
#   The player_inventory is expected to be a dictionary, and will be provided by the main game loop
def run_room(player_inventory):
    description = '''
    . . . Room 2 ...

    You are in a brightly lit room. 
    The room appears to be an office.
    There is desk in the room.
    '''
    if room2_inventory['key'] == 1:
        description = description + "There is a key on the desk."
    if room2_inventory['cup'] == 1:
        description = description + " There is a cup on the desk."
    if room2_inventory['rock'] == 1:
        description = description + " A massive boulder blocks the door to the east."
    print(description)

    # valid commands for this room
    commands = ["go", "take", "drop", "use", "drink", "examine", "status", "help"]
    no_args = ["examine", "status", "help"]

    # nonsense room number, we need to figure out which room they want in the loop
    next_room = -1

    done_with_room = False
    while not done_with_room:
        # Examine the response and decide what to do
        response = utils.ask_command("What do you want to do?", commands, no_args)
        response = utils.scrub_response(response)
        the_command = response[0].lower()

        if the_command == 'go':
            direction = response[1]
            # Use your hand drawn map to help you think about what is valid
            if direction == 'north':
                next_room = 1
                done_with_room = True
            if direction == 'east':
                if room2_inventory['rock'] == 1:
                    print("The boulder is till there.")
                else:
                    print("You move to the next room.")
                    next_room = 6
                    done_with_room = True
            if direction == 'west':
                print("There is no way to go,", direction)
        elif the_command == 'take':
            take_what = response[1]
            utils.take_item(player_inventory, room2_inventory, take_what)
        elif the_command == 'drop':
            drop_what = response[1]
            utils.drop_item(player_inventory, room2_inventory, drop_what)
        elif the_command == 'status':
            utils.room_status(room2_inventory)
            utils.player_status(player_inventory)
        elif the_command == 'use':
            use_what = response[1]
            if use_what == 'dynamite':
                print("Your stick of dynamite explodes the rock into millions of pieces")
                room2_inventory['dynamite'] = 0
                room2_inventory['rock'] = 0
        elif the_command == 'examine':
            examine_what = response[1]
            if examine_what == 'map':
                utils.map(player_inventory)
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


    # end of main while loop
    return next_room

