from seatingsystem.seating_optimization import find_stable_seating

with open('input.txt') as f:
    origin = [[seat for seat in row] for row in f.readlines()]

stable_setting = find_stable_seating(origin)

occupied_seat = 0

for row in range(len(stable_setting)):
    for col in range(len(stable_setting[0])):
        if stable_setting[row][col] == '#':
            occupied_seat += 1

print("Found {} occupied seats".format(occupied_seat))

