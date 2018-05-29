import adventure_game.my_utils as utils
import random
# # # # #
# ROOM 7
#
# Serves as a good template for blank rooms
room7_inventory = {
    'meat': 1,
    'armor': 1,
    'trap': 1
}

def run_room(player_inventory):
    # Let the user know what the room looks like
    room7_description = '''
        . . .  7th room ... 
        You find yourself in an almost pitch black room.'''

    if room7_inventory['meat'] == 1:
        room7_description = room7_description + '\nYou see some meat on a plate.'
    if room7_inventory['armor'] == 1:
        room7_description = room7_description + '\nThere is also a set a of armor hanging on the wall.'
    if room7_inventory['trap'] == 1:
        room7_description = room7_description + '\nSuddenly you hear the tell tale signs of a triggered pit trap! You should try jumping!'

    print(room7_description)




    # valid commands for this room
    commands = ["go", "take", "drop", "use", "jump", "drink", "examine", "status", "help"]
    no_args = ["examine", "status", "help", "jump"]

    # nonsense room number,
    # In the loop below the user should eventually ask to "go" somewhere.
    # If they give you a valid direction then set next_room to that value
    next_room = -1

    done_with_room = False
    while not done_with_room:
        # Examine the response and decide what to do
        response = utils.ask_command("What do you want to do?", commands, no_args)
        response = utils.scrub_response(response)
        the_command = response[0]

        # now deal with the command
        if the_command == 'jump':
            if room7_inventory['trap'] == 1:
                if random.randrange(21) > 10:
                    print("You narrowly avoid the trap! It is now disabled and will not bother you again.")
                    room7_inventory['trap'] = 0
                else:
                    player_inventory['health'] = player_inventory['health'] - 10
                    if player_inventory['health'] <= 0:
                        print("You died! GAME OVER")
                        break
                    print("You could not jump far enough and fall into the pit! You take ten points of damage. You are now at", player_inventory['health'], "health.")
                    print("After some time, you manage to climb out. The trap is now disabled and will not bother you again.")
                    room7_inventory['trap'] = 0
            else:
                print("You jump up and hit your head. Nothing happens.")
        elif the_command == 'go':
            if room7_inventory['trap'] == 1:
                print("You must try to avoid the trap first!")
            else:
                direction = response[1].lower()
                if direction == 'west':
                    next_room = 4
                    done_with_room = True
                elif direction == 'south':
                    next_room = 11
                    done_with_room = True
                else:
                    print("You cannot go", direction)
        elif the_command == 'take':
            if room7_inventory['trap'] == 1:
                print("You must try to avoid the trap first!")
            else:
                take_what = response[1]
                utils.take_item(player_inventory, room7_inventory, take_what)
        elif the_command == 'drop':
            if room7_inventory['trap'] == 1:
                print("You must try to avoid the trap first!")
            else:
                drop_what = response[1]
                utils.drop_item(player_inventory, room7_inventory, drop_what)
        elif the_command == 'status':
            if room7_inventory['trap'] == 1:
                print("You must try to avoid the trap first!")
            else:
                utils.room_status(room7_inventory)
                utils.player_status(player_inventory)
        elif the_command == 'drink':
            potion = response[1]
            if room7_inventory['trap'] > 0:
                print("You must try to avoid the trap first!")
            else:
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