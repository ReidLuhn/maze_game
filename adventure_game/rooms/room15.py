import adventure_game.my_utils as utils
import random
# # # # #
# ROOM 15
#
# Serves as a good template for blank rooms


room15_inventory = {
    'magic key': 1,
    'minor healing potion': 1,
    'death mage' : 1
}

def run_room(player_inventory):
    # Let the user know what the room looks like
    # valid commands for this room
    room15_description = '''
        . . .  15th room ... 
        You find yourself in a dead end room. 
        '''

    if room15_inventory['death mage'] > 0:
        room15_description = room15_description + " A robed death mage floats in front of you. He seems to be guarding something."
    if room15_inventory['magic key'] > 0:
        room15_description = room15_description + " A magic key sits on a pedestal. It is embellished with jewels and gold."
    if room15_inventory['minor healing potion'] > 0:
        room15_description = room15_description + " A minor healing potion sits in a corner."
    print(room15_description)


    commands = ["go", "take", "drop", "use", "drink", "examine", "status", "help"]
    no_args = ["examine", "status", "help"]

    # nonsense room number,
    # In the loop below the user should eventually ask to "go" somewhere.
    # If they give you a valid direction then set next_room to that value
    next_room = -1
    mage_health = 30
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
                next_room = 14
                done_with_room = True
            else:
                print("You cannot go", direction)
        elif the_command == 'take':
            take_what = response[1].lower()
            if take_what == 'magic key':
                if room15_inventory['death mage'] > 0:
                    print("The death mage is still in your way. It begins to move forward.")
                else:
                    utils.take_item(player_inventory, room15_inventory, take_what)

            if take_what != 'magic key':
                if room15_inventory['death mage'] > 0:
                    print("The Death Mage is still in your way. It begins to move forward.")
                else:
                    utils.take_item(player_inventory, room15_inventory, take_what)
        elif the_command == 'use':
            use_what = response[1].lower()
            if use_what == 'sword':
                if 'sword' in player_inventory.keys():
                    if room15_inventory['death mage'] > 0:
                        blah = True
                        while blah == True:
                            r = random.randrange(21)
                            if r > 11:
                                if mage_health > 10:
                                    print("You slice across the mage's chest.")
                                    mage_health = mage_health - 10
                                    print("The death mage's health is now: ", mage_health)
                                    response = utils.ask_command("What do you want to do?", commands, no_args)
                                if mage_health == 10:
                                    blah = False
                                    room15_inventory['death mage'] = 0
                                    print("You stab the mage in the heart and it dies in a pile of ashes.")
                                if mage_health == 0:
                                    print("The mage is dead Donny.")
                            else:
                                print("You missed!")
                                player_inventory['health'] = player_inventory['health'] - 20
                                print("He attacks you with a flame spell for twenty points of damage. Your health is now", player_inventory['health'])
                                if player_inventory['health'] <= 0:
                                    print("The death mage engulfs you in a final cloud of flames, and you fall down dead. GAME OVER!")
                                    blah = False
                                    break
                                else:
                                    print("Keep fighting!")
                                    response = utils.ask_command("What do you want to do?", commands, no_args)
                    else:
                        print("You swing at nothing.")
                else:
                    print("You don't have a weapon DONNY!!!")
            elif use_what == 'bowling ball':
                if 'bowling ball' in player_inventory.keys():
                    print("The bowling ball sails through the air, and hits the mage in the chest. The death mage is thrown against the wall, and dies instantly.")
                    room15_inventory['death mage'] = 0
                    mage_health = 0
                else:
                    print("You don't have a bowling ball stupid.")
            else:
                print("This item cannot kill the death mage!")
        elif the_command == 'status':
            utils.room_status(room15_inventory)
            utils.player_status(player_inventory)
        elif the_command == 'drop':
            drop_what = response[1]
            utils.drop_item(player_inventory, room15_inventory, drop_what)
        elif the_command == 'examine':
            examine_what = response[1]
            if examine_what == 'map':
                utils.map(player_inventory)
        elif the_command == 'drink':
            if room15_inventory['death mage'] > 0:
                print("The death mage prevents you from doing this.")
            else:
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

            # END of WHILE LOOP - done_room
            # TODO return next room
    return next_room