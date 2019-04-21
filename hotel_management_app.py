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

    # Checks to see if we're checking in, if we are we will ask for number of occupants and their names
    if(in_or_out == 'in'):
        occupant_num = int(input('Number of occupants: '))
        # loops through the amount of occupants and adds them to the occupants list
        for i in range(occupant_num):
            occupants.append(input('Name of occupant %d: ' % (i+1)))        

    while end_of_check_in == False:
        # If were checking out we only want to do this while loop once
        # If we were checking in, we need to loop to see if we were missing any floors or rooms 
        # (we wouldnt normally do this since there are supposed to be a set of floors and rooms),
        # but we'll add them just for practice
        if(in_or_out == 'out'):
            end_of_check_in = True

        if f_num in hotel:
            if r_num in hotel[f_num]:
                if len(hotel[f_num][r_num]) == 0 and in_or_out == 'in':
                    # We place the occupants in the room
                    hotel[f_num][r_num] = occupants
                    print('Checking into room %s located on floor %s with %d occupant(s) named: %s' % (floor_num,room_num,len(hotel[floor_num][room_num]),', '.join(hotel[floor_num][room_num])))
                    end_of_check_in = True
                    print('Check in successful.')
                elif len(hotel[f_num][r_num]) != 0 and in_or_out == 'out':
                    print('Checking out of room %s located on floor %s with %d occupant(s)' % (floor_num,room_num,len(hotel[floor_num][room_num])))
                    # when we're checking out we set the array to empty so that we remove the occupants.
                    hotel[floor_num][room_num] = []
                    print('Checked out successful.')
                elif in_or_out == 'in':
                    print('Room is already occupied')
                    end_of_check_in = True
                elif in_or_out == 'out':
                    print('Room isn\'t occupied.')
            elif in_or_out == 'in':
                # If we find a floor but cant find a room we create it and give it an empty array for occupants
                hotel[f_num][r_num] = []
            else:
                print('Room isn\'t occupied.')
        elif in_or_out == 'in':
            # if we're checking in and cant find the floor, we create it and give it an empty list
            hotel[f_num] = {}
        else:
            print('Room isn\'t occupied.')

    return print('Finished checking %s' % in_or_out)

checking_in_or_out(check_in_out,floor_num,room_num)