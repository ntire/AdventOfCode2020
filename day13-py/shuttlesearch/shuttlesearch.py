import math
import sys

def find_earliest_bus_id(earliest_timestamp, list_of_bus_ids):
    earliest_bus_id = None
    earliest_departure_timestamp = sys.maxsize
    
    for current_bus_id in list_of_bus_ids:
        next_bus_departure_timestamp = current_bus_id * math.ceil(earliest_timestamp / current_bus_id)
        
        if next_bus_departure_timestamp < earliest_departure_timestamp:
            earliest_bus_id = current_bus_id
            earliest_departure_timestamp = next_bus_departure_timestamp  

        #print(bus_id, earliest_departure_timestamp)
    
    return earliest_bus_id, earliest_departure_timestamp

def parse_file(filename):
    with open(filename) as f:
        earliest_timestamp = int(f.readline().rstrip())
        list_of_bus_ids = list(map(int, list(filter(lambda x: x != 'x', f.readline().split(",")))))
    return earliest_timestamp, list_of_bus_ids