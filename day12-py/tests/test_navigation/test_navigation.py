from navigation.navigator import find_destination

def test_moving_forward():
    instructions = [['F', 10]]
    x, y = find_destination(instructions)

    assert x == 10
    assert y == 0


def test_moving_north_without_turning():
    instructions = [['N', 2], ['F', 3]]

    x, y = find_destination(instructions)

    assert x == 3
    assert y == 2

def test_turning_180():
    instructions = [['R', 180], ['F', '5']]

    x, y = find_destination(instructions)

    assert x == -5
    assert y == 0
