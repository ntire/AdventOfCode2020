from seatingsystem.seating_optimization_part2 import find_stable_seating, count_first_adjacent_seat_in_each_direction

def test_example_eight_occupied_seats():
    with open('input_example_part2') as f:
        origin = [[seat for seat in row.rstrip()] for row in f.readlines()]
    
    assert 8 == count_first_adjacent_seat_in_each_direction(origin, 4, 3)


def test_example_layout_part2():
    with open('input_example') as f:
        layout = [[seat for seat in row.rstrip()] for row in f.readlines()]
    
    with open('result_example_part2') as f:
        expected = [[seat for seat in row.rstrip()] for row in f.readlines()]

    result = find_stable_seating(layout)

    assert expected == result