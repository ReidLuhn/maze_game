import adventure_game.my_utils as utils
import time
from colorama import Fore, Style

room1_inventory = {

}

room_state = {
    'door_locked': True,
    'door_locked2': True
}


# # # # # # # # # # # # # # #
#  This is the main room you will start in.
#
#  GO: From this room you can get to Room 2 (SOUTH) and Room 1 (East)
#  Take: There is nothing to take in this room
#  Use: There is nothing to use in this room
#
def run_room(player_inventory):
    description = '''
    . . . Main Room . . .

    You open your eyes. The room you see is unfamiliar. You see a brightly lit
    doorway to the SOUTH. To the EAST and WEST you see a closed doors.

    '''
    print( Fore.BLUE + Style.BRIGHT + description + Style.RESET_ALL)

    # valid commands for this room
    commands = ["go", "take", "drop", "use", "drink", "master", "examine", "status", "help"]
    no_args = ["examine", "status", "help"]

    # nonsense room number, we need to figure out which room they want in the loop
    next_room = -1

    done_with_room = False
    while not done_with_room:
        # Examine the response and decide what to do
        response = utils.ask_command("What do you want to do?", commands, no_args)
        response = utils.scrub_response(response)
        the_command = response[0]
        if the_command == 'go':
            direction = response[1]
            # Use your hand drawn map to help you think about what is valid
            if direction == 'south':
                next_room = 2
                done_with_room = True
            elif direction == 'east':
                is_locked = room_state['door_locked']
                if not is_locked:
                    next_room = 3
                    done_with_room = True
                else:
                    print("The door is locked.")
            elif direction == 'west':
                is_locked2 = room_state['door_locked2']
                if not is_locked2:
                    next_room = 5
                    done_with_room = True
                else:
                    print("The door is locked. You need a magic key.")
            else:
                # In this room, there is nowhere else to go.
                print("There is no way to go,", direction)
        elif the_command == 'take':
            print("There is nothing to take here.")
        elif the_command == 'drop':
            drop_what = response[1]
            utils.drop_item(player_inventory, room1_inventory, drop_what)
        elif the_command == 'use':
            use_what = response[1]
            if use_what == 'key':
                if 'key' not in player_inventory.keys():
                    print("You don't have a key!")
                else:
                    door_locked = room_state["door_locked"]
                    if door_locked:
                        room_state["door_locked"] = False
                        print("The door to the EAST is unlocked!")
                    else:
                        print("The door was already unlocked!")
            elif use_what == 'magic key':
                if player_inventory['magic key'] == 0:
                    print("You don't have the magic key!")
                else:
                    door_locked2 = room_state["door_locked2"]
                    if door_locked2:
                        room_state["door_locked2"] = False
                        print("The door to the WEST is unlocked!")
                    else:
                        print("The door was already unlocked!")
            else:
                print("Gabe is a genius.")
        elif the_command == 'status':
            utils.room_status(room1_inventory)
            utils.player_status(player_inventory)
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
        elif the_command == 'master':
            phoo = response[1]
            if phoo == 'key':
                next_room = 15
                done_with_room = True

    # end of while loop
    return next_room
