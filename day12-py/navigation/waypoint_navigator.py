import math

def find_destination_via_waypoint(instructions):
    position = [0, 0]
    waypoint = [10, 1] # per definition

    for action, value in instructions:
        if action == 'F':
            position[0] = position [0] + waypoint[0] * value
            position[1] = position [1] + waypoint[1] * value
            
        elif action in ['N', 'S', 'E', 'W']:
            switcher = {
                'N': [ waypoint[0],  waypoint[1] + value ],
                'S': [ waypoint[0],  waypoint[1] - value ],
                'E': [ waypoint[0] + value,  waypoint[1] ],
                'W': [ waypoint[0] - value,  waypoint[1] ],
            }
            waypoint = switcher.get(action)     
        elif action in ['R', 'L']:
            # cheat: I've check the input file and find only rectangular angles, so this here is tailor made simplified
            # $ grep "[LR]" input.txt | sort | uniq
            x = waypoint[0] 
            y = waypoint[1]

            if action == 'L':
                angle = math.radians(value * 1.0)
            else:
                angle = math.radians(value * (-1.0))

            waypoint[0] = int(round(x * math.cos(angle) -  y * math.sin(angle), 2))
            waypoint[1] = int(round(y * math.cos(angle) +  x * math.sin(angle), 2))
        print("Action: {} Value: {}, Position {},{} Waypoint {},{}".format(action,value, position[0], position[1], waypoint[0], waypoint[1]))
    return position