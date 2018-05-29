import adventure_game.my_utils as utils

# # # # #
# ROOM 13
#
# Serves as a good template for blank rooms


room13_inventory = {
    'bowling ball': 1,
    'sapphire': 1,
    'rug': 1
}

def run_room(player_inventory):
    # Let the user know what the room looks like
    # valid commands for this room
    room13_description = '''
        . . .  13th room ... 
        This room smells a lot like someone had a piss in it. A large shelf stands in the corner.
        '''

    if room13_inventory['bowling ball'] > 0:
        room13_description = room13_description + " A huge bowling ball sits on the table. On the front there is a name: Jeff Lebowski."
    if room13_inventory['sapphire'] > 0:
        room13_description = room13_description + " A sapphire the size of 2/17 of a mini-fridge sits on a pillow in the center of the room."
    if room13_inventory['rug'] > 0:
        room13_description = room13_description + " A rug that really ties the room together sits on the floor. There is a pee stain on it."
    print(room13_description)


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
                next_room = 12
                done_with_room = True
            else:
                print("You cannot go", direction)
        elif the_command == 'take':
            take_what = response[1].lower()
            utils.take_item(player_inventory, room13_inventory, take_what)
        elif the_command == 'status':
            utils.room_status(room13_inventory)
            utils.player_status(player_inventory)
        elif the_command == 'drop':
            drop_what = response[1]
            utils.drop_item(player_inventory, room13_inventory, drop_what)
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
            if examine_what == 'map':
                utils.map(player_inventory)


            # END of WHILE LOOP - done_room
            # TODO return next room
    return next_room