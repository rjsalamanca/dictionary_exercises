check_in_out = input('Type \'in\' to check-in and \'out\' to check out: ')
floor_num = input('Floor number: ')
room_num = input('Room number: ')

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

def checking_in_or_out(in_or_out,f_num,r_num):
    occupants = []
    end_of_check_in = False

    if(in_or_out == 'in'):
        occupant_num = int(input('Number of occupants: '))
        for i in range(occupant_num):
            occupants.append(input('Name of occupant %d: ' % (i+1)))        

    while end_of_check_in == False:
        if(in_or_out == 'out'):
            end_of_check_in = True

        if f_num in hotel:
            if r_num in hotel[f_num]:
                if len(hotel[f_num][r_num]) == 0 and in_or_out == 'in':
                    hotel[f_num][r_num] = occupants
                    print('Checking into room %s located on floor %s with %d occupant(s) named: %s' % (floor_num,room_num,len(hotel[floor_num][room_num]),', '.join(hotel[floor_num][room_num])))
                    end_of_check_in = True
                    print('Check in successful.')
                elif len(hotel[f_num][r_num]) != 0 and in_or_out == 'out':
                    print('Checking out of room %s located on floor %s with %d occupant(s)' % (floor_num,room_num,len(hotel[floor_num][room_num])))
                    hotel[floor_num][room_num] = []
                    print('Checked out successful.')
                elif in_or_out == 'in':
                    print('Room is already occupied')
                    end_of_check_in = True
                elif in_or_out == 'out':
                    print('Room isn\'t occupied.')
            elif in_or_out == 'in':
                hotel[f_num][r_num] = []
            else:
                print('Room isn\'t occupied.')
        elif in_or_out == 'in':
            hotel[f_num] = {}
        else:
            print('Room isn\'t occupied.')

    return 'Finished checking %s' % in_or_out

print(checking_in_or_out(check_in_out,floor_num,room_num))

# Display a menu asking whether to check in or check out. - DONE
# Prompt the user for a floor number, then a room number. - DONE
# If checking in, ask for the number of occupants and what their names are. - DONE
# If checking out, remove the occupants from that room.
# Do not allow anyone to check into a room that is already occupied. - DONE 
# Do not allow checking out of a room that isn't occupied.