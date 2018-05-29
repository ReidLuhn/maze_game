import adventure_game.my_utils as utils
import random
# # # # #
# ROOM 11
#
# Serves as a good template for blank rooms


room11_inventory = {
    'dynamite': 1,
    'caltrops': 1,
    'healing potion': 1,
    'spider': 1
}


def run_room(player_inventory):
    # Let the user know what the room looks like
    # valid commands for this room
    room11_description = '''
        . . .  11th room ... 
       You enter a brightly lit room with a large chandelier.'''

    if room11_inventory['dynamite'] == 1:
        room11_description = room11_description + " You see a stick of dynamite."
    if room11_inventory['caltrops'] == 1:
        room11_description = room11_description + " A small bag of caltrops sits in the corner."
    if room11_inventory['healing potion'] == 1:
        room11_description = room11_description + " A healing potion sits on a shelf."
    print(room11_description)

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
            if direction == 'north':
                next_room = 7
                done_with_room = True
            else:
                print("You cannot go", direction)
        elif the_command == 'take':
            take_what = response[1].lower()
            utils.take_item(player_inventory, room11_inventory, take_what)
            if take_what == 'dynamite':
                if room11_inventory['spider'] == 1:
                    print("You hear a soft click, and an enormous spider pops out of a trap door. It jumps and tries to attack you!")
                    blah = True
                    while blah == True:
                        response = utils.ask_command("What do you do?", commands, no_args)
                        the_command = response[0]
                        if the_command != 'use':
                            print("You must use something to kill the spider first!")
                        if the_command == 'use':
                            if response[1].lower() == 'sword':
                                if room11_inventory['spider'] > 0:
                                    r = random.randrange(21)
                                    if r > 10:
                                        print("You have slain the spider!!!")
                                        blah = False
                                        room11_inventory['spider'] = 0
                                    else:
                                        print("You missed!")
                                        player_inventory['health'] = player_inventory['health'] - 10
                                        print("He attacks you for ten points of damage. Your health is now", player_inventory['health'])
                                        if player_inventory['health'] <= 0:
                                            print("You died! GAME OVER")
                                            break
                                        print("Keep fighting!")
                                else:
                                    print("You stab the spider corpse again.")
                            elif response[1].lower() != 'sword':
                                print("You must use your sword to fight!")
                        elif the_command != 'use':
                            print("You must use something to kill the spider first!")
                else:
                    print("There is only one stick of it, so use it wisely.")
        elif the_command == 'status':
            utils.room_status(room11_inventory)
            utils.player_status(player_inventory)
        elif the_command == 'drop':
            drop_what = response[1]
            utils.drop_item(player_inventory, room11_inventory, drop_what)
        elif the_command == 'drink':
            potion = response[1]
            if potion == 'healing potion':
                if player_inventory['healing potion'] == 1:
                    print("You drink a healing potion. You gain 20 hit points.")
                    player_inventory['health'] = player_inventory['health'] + 20
                    print("Your health is now:", player_inventory['health'])
                else:
                    print("You don't have a healing potion.")
            elif potion == 'minor healing potion':
                if 'minor healing potion' in player_inventory.keys():
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