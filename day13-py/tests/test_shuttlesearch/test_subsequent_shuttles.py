
from shuttlesearch.subsequent_shuttlesearch import find_earliest_timestamp_for_subsequent_departures


def test_find_first_subsequent_departure_of_two_shuttles():
    list_of_bus_id = ['2', '3', '5']
    earliest_timestamp = find_earliest_timestamp_for_subsequent_departures(list_of_bus_id)

    assert 77 == earliest_timestamp

def test_find_first_subsequent_departure_of_two_shuttles():
    list_of_bus_id = ['67','7','59','61']
    earliest_timestamp = find_earliest_timestamp_for_subsequent_departures(list_of_bus_id)

    assert 754018 == earliest_timestamp

def test_example_file():
    with open('input_example.txt') as f:
        list_of_bus_ids = f.readlines()[1].split(',')
    
    earliest_timestamp = find_earliest_timestamp_for_subsequent_departures(list_of_bus_ids)
    assert 1068781 == earliest_timestamp