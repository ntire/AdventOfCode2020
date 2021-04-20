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
            
            occupied_adjacent_seat_counter = count_adjacent_occupied_seat(layout, row, col)
            #print("(Row, Col) {},{} with {} occupied adjacent".format(row, col, occupied_adjacent_seat_counter))
            has_no_adjacent_occupied_seat = occupied_adjacent_seat_counter == 0
            has_more_than_tree_occupied_adjacent_seats = occupied_adjacent_seat_counter > 3
            
            if cell == 'L':
                if has_no_adjacent_occupied_seat:
                    cell = '#'
            
            elif cell == '#':
                if has_more_than_tree_occupied_adjacent_seats:
                    cell = 'L'
                # do magic:
            
            new_row.append(cell)
        optimized_layout.append(new_row)
    
    return optimized_layout

def count_adjacent_occupied_seat(layout, row, col):
    max_width = len(layout[0]) - 1
    max_height = len(layout) - 1
    
    occupied_adjacent_seat_counter = 0

    for r in range(max(0, row-1), min(row + 1, max_height) + 1):
        for c in range(max(0, col - 1), min(col + 1, max_width) + 1):
            if r == row and c == col:
                pass
            elif layout[r][c] == '#':
                occupied_adjacent_seat_counter += 1
    return occupied_adjacent_seat_counter
    

