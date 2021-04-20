from seatingsystem.seating_optimization import find_stable_seating

def test_example_layout():
    with open('input_example') as f:
        layout = [[seat for seat in row] for row in f.readlines()]
    
    with open('result_example') as f:
        expected = [[seat for seat in row] for row in f.readlines()]

    result = find_stable_seating(layout)

    assert expected == result