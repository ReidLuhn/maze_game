import adventure_game.my_utils as utils

# # # # #
# ROOM 10
#
# Serves as a good template for blank rooms


room10_inventory = {
    'rabbit': 1
}

def run_room(player_inventory):
    # Let the user know what the room looks like
    # valid commands for this room
    room10_description = '''
        . . .  10th room ... 
        You find yourself in a darkly lit small room.
        '''

    if room10_inventory['rabbit'] > 0:
        room10_description = room10_description + "  A small rabbit sits on top of a large treasure chest."
    print(room10_description)


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
                next_room = 8
                done_with_room = True
            else:
                print("You cannot go", direction)
        elif the_command == 'take':
            take_what = response[1].lower()
            if take_what != 'rabbit':
                if take_what == 'treasure':
                    if room10_inventory['rabbit'] == 0:
                        utils.take_item(player_inventory, room10_inventory, take_what)
                        print("You find a tortoise named Maynard, and you get to keep him forever! THE END")
                        break
                    else:
                        print("The bunny still guards the treasure!")
                else:
                    utils.take_item(player_inventory, room10_inventory, take_what)
            else:
                print("You cannot take the rabbit.")
        elif the_command == 'status':
            utils.room_status(room10_inventory)
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
            utils.drop_item(player_inventory, room10_inventory, drop_what)
        elif the_command == 'use':
            use_what = response[1]
            if use_what != 'holy hand grenade':
                if room10_inventory['rabbit'] > 0:
                    print("The rabbit seems to be immune to such attacks!")
                    print("The rabbit lunges and bites you for 10 points of damage!")
                    player_inventory['health'] = player_inventory['health'] - 10
                    print("Your health is now: ", player_inventory['health'])
                    if player_inventory['health'] <= 0:
                        print("You died! GAME OVER")
                        break
                else:
                    print("It does nothing.")
            if use_what == 'holy hand grenade':
                if room10_inventory['rabbit'] > 0:
                    blah = '''
                        After thoroughly reading the instructions, you count 'one......two.......five!, shit, three!!!"
                        the holy hand grenade sails through the air......... and hits the bunny on the head, killing him instantly. The holy hand grenade rolls
                        away and does nothing.
                        '''
                    print(blah)
                    room10_inventory['rabbit'] = 0
                else:
                    print("It does nothing.")
        elif the_command == 'examine':
            examine_what = response[1]
            if examine_what == 'map':
                utils.map(player_inventory)

            # END of WHILE LOOP - done_room
            # TODO return next room
    return next_room