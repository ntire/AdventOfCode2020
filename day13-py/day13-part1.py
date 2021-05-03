from shuttlesearch.shuttlesearch import find_earliest_bus_id, parse_file    
    
earliest_timestamp, list_of_bus_ids = parse_file('input.txt')
bus_id, departure_timestamp = find_earliest_bus_id(earliest_timestamp, list_of_bus_ids)

result = bus_id * (departure_timestamp - earliest_timestamp)

print(result)