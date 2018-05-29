import adventure_game.my_utils as utils

# # # # #
# ROOM 9
#
# Serves as a good template for blank rooms


room9_inventory = {
    'gold key': 1,
    'holy hand grenade': 1
}

def run_room(player_inventory):
    # Let the user know what the room looks like
    # valid commands for this room
    room9_description = '''
        . . .  9th room ... 
        This room is brightly lit with candles, and the granite walls are slick with dew.
        '''

    if room9_inventory['gold key'] > 0:
        room9_description = room9_description + " The gold key hangs from a hook."
    if room9_inventory['holy hand grenade'] > 0:
        room9_description = room9_description + " A holy hand grenade rests on a golden pillow."
    print(room9_description)


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
        the_command = response[0]

        # now deal with the command
        if the_command == 'go':
            direction = response[1].lower()
            if direction == 'west':
                next_room = 8
                done_with_room = True
            else:
                print("You cannot go", direction)
        elif the_command == 'take':
            take_what = response[1].lower()
            utils.take_item(player_inventory, room9_inventory, take_what)
        elif the_command == 'status':
            utils.room_status(room9_inventory)
            utils.player_status(player_inventory)
        elif the_command == 'drop':
            drop_what = response[1]
            utils.drop_item(player_inventory, room9_inventory, drop_what)
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
            if examine_what == 'holy hand grenade':
                print("The grenade has directions that read:")
                phoo = '''
                
                And the Lord spake, saying, First shalt
               thou take out the Holy Pin.

               Then, shalt thou count to three, no more,
               no less.

              Three shalt be the number thou shalt
              count, and the number of the counting
              shalt be three.

              Four shalt thou not count,
              nor either count thou two, excepting that
              thou then proceed to three.

              Five is right out. 

              Once the number three,
              being the third number, be reached, then
              lobbest thou thy Holy Hand Grenade of
              Antioch towards thy foe, who being
              naughty in my sight, shall snuf it.
              '''
                print(phoo)
            if examine_what == 'map':
                utils.map(player_inventory)

            # END of WHILE LOOP - done_room
            # TODO return next room
    return next_room