import adventure_game.my_utils as utils

# # # # #
# ROOM 6
#
# Serves as a good template for blank rooms


room6_inventory = {
    'gory simplicity': 1,
    'pick axe': 1,
    'happy little accidents': 1,
    'pointless': 1
}



room_state = {
    'door_locked': True
}

def run_room(player_inventory):
    # Let the user know what the room looks like
    # valid commands for this room
    room6_description = '''
        . . .  6th room . . . 
        This room seems to have almost no purpose. Nothing but pictures hang on the wall. One of a mountain landscape with titled 'happy little accidents',
        one with a great battle scene between ancient men and a mammoth titled 'gory simplicity', and one of a wooden bowl of fruit titled 'pointless'.
        There is a door to the South, but it has no door knob, and no key hole. Just a thick layer of clay a soft stone cakes the front of the door.
        '''

    commands = ["go", "take", "drop", "use", "drink", "examine", "status", "help"]
    no_args = ["examine", "status", "help"]

    print(room6_description)

    # nonsense room number,
    # In the loop below the user should eventually ask to "go" somewhere.
    # If they give you a valid direction then set next_room to that value
    next_room = -1
    door_writings = 0
    done_with_room = False
    while not done_with_room:
        # Examine the response and decide what to do
        response = utils.ask_command("What do you want to do?", commands, no_args)
        response = utils.scrub_response(response)
        the_command = response[0]

        # now deal with the command
        if the_command == 'go':
            direction = response[1].lower()
            if direction == 'west':
                next_room = 2
                done_with_room = True
            if direction == 'south':
                is_locked = room_state['door_locked']
                if not is_locked:
                    next_room = 12
                    done_with_room = True
                else:
                    print("The door is locked.")
            else:
                print("You cannot go", direction)
        elif the_command == 'take':
            take_what = response[1].lower()
            utils.take_item(player_inventory, room6_inventory, take_what)
        elif the_command == 'use':
            use_what = response[1]
            if use_what == 'pick axe':
                if room6_inventory['pick axe'] == 0:
                    print("You hack away the loose rock and clay to reveal a small bit of writing. It says: Answer this riddle correctly, and you may pass "
                          "through this door. (clears throat), thirty white horses on a red hill. First they champ, then they stamp, and then they "
                          "stand still. What is it?")
                    correct = False
                    while correct == False:
                        response = input("What is the answer?:")
                        if response != 'teeth':
                            print("Incorrect! Try Again!")
                        elif response == 'teeth':
                            print("Correct!")
                            door_locked = room_state["door_locked"]
                            correct = True
                            if door_locked:
                                room_state["door_locked"] = False
                                print("The door to the SOUTH is unlocked!")
                            else:
                                print("The door was already unlocked!")

        elif the_command == 'status':
            utils.room_status(room6_inventory)
            utils.player_status(player_inventory)
        elif the_command == 'drop':
            drop_what = response[1]
            utils.drop_item(player_inventory, room6_inventory, drop_what)
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
            if examine_what == 'door':
                print("You notice some small cave paintings depicting the hunting of some kind of large animal.")
                door_writings = door_writings + 1
            if examine_what == 'gory simplicity':
                if door_writings == 1:
                    print("You notice the painting hides a secret alcove. Within the alcove lies a pick axe")
            if examine_what == 'happy little accidents':
                print("The painting is quite striking, and it seems to made by a strange man named Bob Ross.")
            if examine_what == 'pointless':
                print("It looks just like the title says it does: pointless.")
            if examine_what == 'map':
                utils.map(player_inventory)



            # END of WHILE LOOP - done_room
            # TODO return next room
    return next_room