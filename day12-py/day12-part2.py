from navigation.waypoint_navigator import find_destination_via_waypoint

with open('input.txt') as f:
    instructions = [[line[:1], int(line[1:])] for line in f.readlines()]

x, y = find_destination_via_waypoint(instructions)

d = abs(x) + abs(y)
print("Manhattan distance:", d)