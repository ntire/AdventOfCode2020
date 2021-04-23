
#    -1, 1     0, 1    1, 1
#           \   |   /
#    -1, 0  --- x ---  + 1,0
#           /   |   \
#    -1, -1   0, -1    1, -1
def find_destination(instructions):
    position = [0 , 0]
    rotation_vector = [1, 0] # east, per initialization
    for instruction in instructions:
        action = instruction[0]
        value = int(instruction[1])
        
        if action == 'F':
            position[0] = position[0] + rotation_vector[0] * value
            position[1] += rotation_vector[1] * value
        elif action in ['N', 'S', 'E', 'W']:
            switcher = {
                'N': [ 0,  1],
                'S': [ 0, -1],
                'E': [ 1,  0],
                'W': [-1,  0],
            }
            move_vector = switcher.get(action, [0, 0])
            position[0] += move_vector[0] * value
            position[1] += move_vector[1] * value
        elif action in ['R', 'L']:
            rotation_vector = turn_rotation_vector(rotation_vector, action, value)
        else:
            raise ValueError("Action '{}' not implemented".format(action))
    
    return position

# The idea is to rotate thru a array of possible rotation vectors, since I do not know the math of cos and sin :-(
def turn_rotation_vector(current_rotation_vector, action, angle):
    vectors = [[0,1], [1,1], [1,0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]

    index = 0
    for i in range(len(vectors)):
        if current_rotation_vector == vectors[i]:
            index = i
            break
    
    direction = 0
    if action == 'R': direction = 1
    elif action == 'L': direction = -1

    steps = int(angle / 45)
    while steps > 0:
        index += direction
        
        if index == len(vectors): 
            index = 0
        elif index == -1: 
            index = len(vectors) - 1
        
        print("Step {} Index {} makes {}".format(steps, index, vectors[index]))
        steps -= 1
    return vectors[index]