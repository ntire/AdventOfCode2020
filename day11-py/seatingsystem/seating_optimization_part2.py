def find_stable_seating(layout):
    previous_layout = run_simple_seating_simulation(layout)
    new_layout = list()
    is_stable = False
    while not is_stable:
        new_layout = run_simple_seating_simulation(previous_layout)
        is_stable = previous_layout == new_layout
        previous_layout = new_layout

    return new_layout


def run_simple_seating_simulation(layout):
    optimized_layout = list()

    for row in range (len(layout)):
        new_row = list()
        for col in range (len(layout[0])):
            cell = layout[row][col]
            
            occupied_adjacent_seat_counter = count_first_adjacent_seat_in_each_direction(layout, row, col)
            # print("(Row, Col) {},{} with {} occupied adjacent".format(row, col, occupied_adjacent_seat_counter))
            has_no_adjacent_occupied_seat = occupied_adjacent_seat_counter == 0
            has_more_than_four_occupied_adjacent_seats = occupied_adjacent_seat_counter > 4
            
            if cell == 'L':
                if has_no_adjacent_occupied_seat:
                    cell = '#'
            
            elif cell == '#':
                if has_more_than_four_occupied_adjacent_seats:
                    cell = 'L'
            
            new_row.append(cell)
        optimized_layout.append(new_row)
    
    return optimized_layout


def count_first_adjacent_seat_in_each_direction(layout, row, col):
    counter = 0

    search_vectors = [[row, col] for col in range(-1, 2) for row in range(-1, 2)]

    #DEBUG
    # print(search_vectors)
    search_vectors.remove([0, 0])
    max_row = len(layout) 
    max_col = len(layout[0]) 

    # for i in range(len(layout)):
    #     print(layout[i])

    multiplier = 1
    skip_vectors = list()
    while len(search_vectors) > len(skip_vectors):
        # print("Running multiplier:", multiplier)

        for vector in search_vectors:
            if not vector in skip_vectors:
                # print("Vector ", vector)
                trow = row + multiplier * vector[0]
                tcol = col + multiplier * vector[1]

                if 0 <= trow < max_row and\
                    0 <= tcol < max_col:
                    if layout[trow][tcol] == '#':
                        counter += 1
                        skip_vectors.append(vector)
                    elif layout[trow][tcol] == 'L':
                        skip_vectors.append(vector)
                    #DEBUG
                    # layout[trow][tcol] = '+'
                else:
                    skip_vectors.append(vector)
        #DEBUG
        # for i in range(len(layout)):
        #     print(layout[i])

        multiplier += 1

    return counter