check_in_out = input('Type \'in\' to check-in and \'out\' to check out: ')
floor_num = input('Floor number: ')
room_num = input('Room number: ')
occupants = []
hotel = {
  '1': {
    '101': ['George Jefferson', 'Wheezy Jefferson'],
  },
  '2': {
    '237': ['Jack Torrance', 'Wendy Torrance'],
  },
  '3': {
    '333': ['Neo', 'Trinity', 'Morpheus']
  }
}

if check_in_out == 'in':

    occupant_num = int(input('Number of occupants: '))
    for i in range(occupant_num):
        occupants.append(input('Name of occupant %d: ' % (i+1)))

    if floor_num in hotel:
        if room_num in hotel[floor_num]:
            if len(hotel[floor_num][room_num]) == 0:
                # add occupants
                print()
            else:
                print('Room is already occupied')
        # add occupants
    # add occupants

elif check_in_out == 'out':
    if floor_num in hotel:
        if room_num in hotel[floor_num]:
            if len(hotel[floor_num][room_num]) != 0:
                print(hotel)
                hotel[floor_num][room_num] = []
                print(hotel)
            else:
                print('Room isn\'t occupied.')
        else:
            print('Room isn\'t occupied.')
    else:
        print('Room isn\'t occupied.')


# Display a menu asking whether to check in or check out. - DONE
# Prompt the user for a floor number, then a room number. - DONE
# If checking in, ask for the number of occupants and what their names are. - DONE
# If checking out, remove the occupants from that room.
# Do not allow anyone to check into a room that is already occupied. - DONE 
# Do not allow checking out of a room that isn't occupied.