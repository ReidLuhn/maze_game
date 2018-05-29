import adventure_game.my_utils as utils

# # # # #
# ROOM 14
#
# Serves as a good template for blank rooms


room14_inventory = {
    'wolf': 1,
}

def run_room(player_inventory):
    # Let the user know what the room looks like
    # valid commands for this room
    room14_description = '''
        . . .  14th room ... 
        You find yourself in a dimly lit room.
        '''

    if room14_inventory['wolf'] > 0:
        room14_description = room14_description + " A wolf sits in front of the only other door to the SOUTH. It is incredibly thin and desperate for food. " \
                                                  "You are starting to look pretty tasty."
    print(room14_description)


    commands = ["go", "take", "drop", "use", "examine", "status", "help"]
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
                next_room = 12
                done_with_room = True
            if direction == 'south':
                if room14_inventory['wolf'] == 0:
                    next_room = 15
                    done_with_room = True
                else:
                    print("The wolf is still in the way.")
            else:
                print("You cannot go", direction)
        elif the_command == 'take':
            take_what = response[1].lower()
            if take_what != 'wolf':
                utils.take_item(player_inventory, room14_inventory, take_what)
            else:
                print("The wolf is chained to the wall. You cannot take her with you.")
        elif the_command == 'status':
            utils.room_status(room14_inventory)
            utils.player_status(player_inventory)
        elif the_command == 'drop':
            drop_what = response[1]
            if drop_what == 'meat':
                if 'meat' in player_inventory.keys():
                    utils.drop_item(player_inventory, room14_inventory, drop_what)
                    print("The wolf tears into it. It seems like she is very happy with you now and moves out of the way.")
                    room14_inventory['wolf'] = 0
            else:
                utils.drop_item(player_inventory, room14_inventory, drop_what)
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
        elif the_command == 'use':
            use_what = response[1]
            if use_what == 'sword':
                print("The second you reach for your sword, the wolf grows at you. There must be another way.")
            elif use_what == 'meat':
                if 'meat' in player_inventory.keys():
                    print("The wolf doesn't want to eat it while you are holding it.")
                else:
                    print("You don't have any.")
            else:
                print("Nothing happens.")


            # END of WHILE LOOP - done_room
            # TODO return next room
    return next_room