import adventure_game.my_utils as utils
import random
#
#  ROOM 4
#
room4_inventory = {
    'kobold': 1
}

def run_room(player_inventory):
    description = '''
    . . . 
    You open the door to the fourth room.'''

    if room4_inventory['kobold'] == 1:
        description = description + '\nImmediately you spot a well armed kobold! He lunges at you with his spear! It is kill or be killed!'


    commands = ["go", "take", "drop", "use", "drink", "examine", "status", "help"]
    no_args = ["examine", "status", "help"]

    # nonsense room number, we need to figure out which room they want in the loop
    next_room = -1
    print(description)

    done_with_room = False
    while not done_with_room:
        # Examine the response and decide what to do
        response = utils.ask_command("What do you do?", commands, no_args)
        response = utils.scrub_response(response)
        the_command = response[0].lower()
        if the_command == 'use':
            if room4_inventory['kobold'] > 0:
                if response[1].lower() == 'sword':
                    blah = True
                    while blah == True:
                        if random.randrange(21) > 5:
                            print("You have slain the kobold!!!")
                            blah = False
                            room4_inventory['kobold'] = 0
                        else:
                            print("You missed!")
                            player_inventory['health'] = player_inventory['health'] - 10
                            print("He attacks you for ten points of damage. Your health is now", player_inventory['health'])
                            if player_inventory['health'] <= 0:
                                print("You died! GAME OVER")
                                break
                            print("Keep fighting!")
                            response = utils.ask_command("What do you do?", commands, no_args)
                else:
                    print("This item cannot kill the kobold!")
            else:
                print("Nothing happens.")
        elif the_command == 'go':
            if room4_inventory['kobold'] == 1:
                print("You must kill the kobold first!")
            direction = response[1]
            # Use your hand drawn map to help you think about what is valid
            if direction == 'south':
                next_room = 3
                done_with_room = True
            elif direction == 'east':
                if room4_inventory['kobold'] == 0:
                    print("You move towards the next room.")
                    done_with_room = True
                    next_room = 7
                else:
                    print("You cannot pass to the next room without killing the kobold!")
            else:
                # In this room, there is nowhere else to go.
                print("There is no way to go,", direction)
        elif the_command == 'take':
            take_what = response[1].lower()
            if take_what == 'kobold':
                print("You cannot take the kobold.")
            else:
                utils.take_item(player_inventory, room4_inventory, take_what)
        elif the_command == 'drop':
            if room4_inventory['kobold'] == 1:
                print("You must kill the kobold first!")
            drop_what = response[1]
            utils.drop_item(player_inventory, room4_inventory, drop_what)
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