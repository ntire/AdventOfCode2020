import sys, functools

def find_earliest_timestamp_for_subsequent_departures(list_of_bus_ids, start_counter = -1):
    counter = start_counter
    stepper = 1
    found_earliest_departure = False
    while not found_earliest_departure:
        counter += stepper
        new_stepper = 1
        for i in range(len(list_of_bus_ids)):
            if list_of_bus_ids[i] != 'x':
                bus_id = int(list_of_bus_ids[i])
                if (counter + i) %  bus_id == 0:
                    new_stepper = new_stepper * bus_id
                    stepper = new_stepper
                    found_earliest_departure = True
                else:
                    found_earliest_departure = False
                    break

    return counter
