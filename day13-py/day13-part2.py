from shuttlesearch.subsequent_shuttlesearch import find_earliest_timestamp_for_subsequent_departures

with open('input.txt') as f:
    list_of_bus_ids = f.readlines()[1].split(',')

earliest_timestamp = find_earliest_timestamp_for_subsequent_departures(list_of_bus_ids, 100000000000000)
print(earliest_timestamp)