from navigation.navigator import turn_rotation_vector

def test_180_degree_from_east():
    current = [1, 0] # ( x y ) = ( 1 0 )
    expect = [ -1, 0]

    result = turn_rotation_vector(current, 'R', 180)
    assert expect == result

def test_180_degree_from_east_to_left():
    current = [1, 0] # ( x y ) = ( 1 0 )
    expect = [ -1, 0]

    result = turn_rotation_vector(current, 'L', 180)
    assert expect == result

def test_90_degree_from_east_to_left():
    current = [1, 0] # ( x y ) = ( 1 0 )
    expect = [0, 1]

    result = turn_rotation_vector(current, 'L', 90)
    assert expect == result

def test_135_degree_from_east_to_right():
    current = [1, 0] # ( x y ) = ( 1 0 )
    expect = [-1, -1]

    result = turn_rotation_vector(current, 'R', 135)
    assert expect == result