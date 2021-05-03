from shuttlesearch.shuttlesearch import find_earliest_bus_id, parse_file

def test_single_bus():
    earliest_timestamp = 939
    list_of_bus_ids = [7]

    earliest_bus_id, _ = find_earliest_bus_id(earliest_timestamp, list_of_bus_ids)

    assert 7 == earliest_bus_id

def test_parse_file():
    f = 'input_example.txt'
    earliest_timestamp, list_of_bus_ids = parse_file(f)

    assert 939 == earliest_timestamp
    assert [7,13,59,31,19] == list_of_bus_ids

def test_example_file():
    earliest_timestamp, list_of_bus_ids = parse_file('input_example.txt')

    earliest_bus_id, _ = find_earliest_bus_id(earliest_timestamp, list_of_bus_ids)
    assert 59 == earliest_bus_id