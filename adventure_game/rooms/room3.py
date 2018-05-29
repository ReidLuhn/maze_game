import adventure_game.my_utils as utils

# # # # #
# ROOM 3
#
# Serves as a good template for blank rooms


room3_inventory = {
    'sword': 1,
    'clue': 1
}

def run_room(player_inventory):
    # Let the user know what the room looks like
    # valid commands for this room
    room3_description = '''
        . . .  3rd room ... 
        You are in a room that feels very familiar. There is a door to the north.
        '''

    if room3_inventory['sword'] > 0:
        room3_description = room3_description + " There is a sword hanging on the wall."
    if room3_inventory['clue'] > 0:
        room3_description = room3_description + " There is a clue on the desk."
    print(room3_description)


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
            if direction == 'west':
                next_room = 1
                done_with_room = True
            if direction == 'north':
                next_room = 4
                done_with_room = True
            else:
                print("You cannot go", direction)
        elif the_command == 'take':
            take_what = response[1].lower()
            utils.take_item(player_inventory, room3_inventory, take_what)
        elif the_command == 'status':
            utils.room_status(room3_inventory)
            utils.player_status(player_inventory)
        elif the_command == 'drop':
            drop_what = response[1]
            utils.drop_item(player_inventory, room3_inventory, drop_what)
        elif the_command == 'examine':
            examine_what = response[1]
            if examine_what == 'clue':
                print("The clue reads: WITHIN THIS DUNGEON LIES A GREAT TREASURE. SEEK IT AT YOUR OWN RISK!!!")
            if examine_what == 'sword':
                print("The sword is made of polished steel.")
            if examine_what == 'map':
                utils.map(player_inventory)
        else:
            print("Bleh")

            # END of WHILE LOOP - done_room
            # TODO return next room
    return next_room