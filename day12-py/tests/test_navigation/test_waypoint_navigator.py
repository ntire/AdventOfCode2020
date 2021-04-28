from navigation.waypoint_navigator import find_destination_via_waypoint

def test_move_towards_waypoint():
    instructions = [['F', 2]]
    x, y = find_destination_via_waypoint(instructions)
    
    assert x == 20
    assert y == 2

def test_change_waypoint_no_moving():
    instructions = [['N', 2]]
    x, y = find_destination_via_waypoint(instructions)
    
    assert x == 0
    assert y == 0

def test_move_waypoint_move_ship():
    instructions = [['N', 2], ['F', 2]]
    x, y = find_destination_via_waypoint(instructions)
    
    assert x == 20
    assert y == 6


def test_rotation_by_90_degrees_left():
    instructions = [['S', 1], ['W', 9], ['L', 90], ['F', 1]]
    x, y = find_destination_via_waypoint(instructions)
    
    assert x == 0
    assert y == 1

def test_rotate_right_90():
    instructions = [['S', 1], ['W', 9], ['R', 90], ['F', 1]]
    x, y = find_destination_via_waypoint(instructions)
    
    assert x == 0
    assert y == -1

def test_examples():
    with open('input_example') as f:
        instructions = [[line[:1], int(line[1:].rstrip())] for line in f.readlines()]
    x, y = find_destination_via_waypoint(instructions)

    assert x == 214
    assert y == -72