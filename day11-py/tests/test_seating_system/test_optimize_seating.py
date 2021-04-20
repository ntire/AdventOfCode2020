from seatingsystem.seating_optimization import run_simple_seating_simulation

def test_occupied_seat_rule_instable():
    layout =\
        [['#', '#', '#'],\
        ['#', '#', '#'],\
        ['#', '#', '#']]

    expected_result =\
        [['#', 'L', '#'],\
         ['L', 'L', 'L'],\
         ['#', 'L', '#']]


    occupied_layout = run_simple_seating_simulation(layout)
    assert occupied_layout == expected_result


def test_occupied_seat_rule_stable():
    layout =\
        [['#', '.'],\
        ['.', '.']]

    expected_result =\
        [['#', '.'],\
        ['.', '.']]

    occupied_layout = run_simple_seating_simulation(layout)
    assert occupied_layout == expected_result


def test_empty_seat_rule_with_no_occupied_adjacent_seats():
    layout =\
        [['L']]

    expected_result =\
        [['#']]

    occupied_layout = run_simple_seating_simulation(layout)
    assert occupied_layout == expected_result


def test_empty_seat_rule_with_no_occupied_adjacent_seats_for_square():
    layout =\
        [['L', 'L'],\
        ['L', 'L']]

    expected_result =\
        [['#', '#'],\
        ['#', '#']]

    occupied_layout = run_simple_seating_simulation(layout)
    assert occupied_layout == expected_result


def test_empty_seat_rule_with_one_floor():
    layout =\
        [['L', '.'],\
        ['L', 'L']]

    expected_result =\
        [['#', '.'],\
        ['#', '#']]

    occupied_layout = run_simple_seating_simulation(layout)
    assert occupied_layout == expected_result


def test_skip_floor():
    layout =\
        [['.']]

    expected_result =\
        [['.']]

    occupied_layout = run_simple_seating_simulation(layout)
    assert occupied_layout == expected_result

