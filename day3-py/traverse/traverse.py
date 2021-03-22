def traverse_slope(input_file, step_x, step_y):
    # Per definition each step goes X+3 and Y+1

    grid = list()    
    with open(input_file) as f:
        for line in f.readlines():
            grid.append(line)

    pos_x, pos_y = 0, 0
    
    MAX_Y = len(grid)
    MAX_X = len(grid[0]) - 1 # starting index at 0

    tree_counter = 0
    while pos_y <= (MAX_Y - step_y): # FIXME: consider MAX_Y
        symbol = grid[pos_y][pos_x]
        
        if symbol == '#':
            tree_counter += 1
        
        pos_x += step_x
        if pos_x >= (MAX_X):
            pos_x -= MAX_X # HINT: Remember the index starts at 0
        
        pos_y += step_y

    return tree_counter