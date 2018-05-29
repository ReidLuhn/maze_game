import adventure_game.my_utils as utils

# # # # #
# ROOM 5
#
# Serves as a good template for blank rooms
room5_description = '''
    . . .  5th room ... 
    This room has an erie feeling about it. Moss hangs from the walls, and a steady drip of viscus water stains the floor.
    There is a door to the north with yet another riddle.
    '''
room5_inventory = {

}

room_state = {
    'door_locked': True
}

def run_room(player_inventory):
    # Let the user know what the room looks like



    print(room5_description)




    # valid commands for this room
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
                next_room = 1
                done_with_room = True
            if direction == 'north':
                is_locked = room_state['door_locked']
                if not is_locked:
                    next_room = 8
                    done_with_room = True
                else:
                    print("The door is locked.")
            else:
                print("You cannot go", direction)
        elif the_command == 'status':
            utils.room_status(room5_inventory)
            utils.player_status(player_inventory)
        elif the_command == 'drop':
            drop_what = response[1]
            utils.drop_item(player_inventory, room5_inventory, drop_what)
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
            examine_what = response[1].lower()
            if examine_what == 'riddle' or examine_what == 'door':
                print("The riddle reads: 'My chores I no longer refuse because I got this new tool that I use. "
                      "I'm just walking around with a weird sucking sound. There's a vacuum built into my...")
                correct = False
                while correct == False:
                    response = input("What is the answer?:")
                    if response != 'shoes':
                        print("Incorrect! Try Again!")
                    elif response == 'shoes':
                        print("Correct!")
                        door_locked = room_state["door_locked"]
                        correct = True
                        if door_locked:
                            room_state["door_locked"] = False
                            print("The door to the NORTH is unlocked!")
                        else:
                            print("The door was already unlocked!")


            # END of WHILE LOOP - done_room
            # TODO return next room
    return next_room