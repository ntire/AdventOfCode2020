
# return delta of accumulator and detta of index
def execute_command(bootcode):
    d_acc = 0
    d_index = 0
    instruction = bootcode[0]
    param = bootcode[1]

    if instruction == "acc":
        d_acc = param
        d_index = 1
    elif instruction == "jmp":
        d_acc = 0
        d_index = param
    elif instruction == "nop":
        d_acc = 0
        d_index = 1
    
    return d_acc, d_index

def bootloop_finder(bootcodes):
    acc = 0
    index = 0
    is_bootloop = False

    visited_registers = set()
    
    while not is_bootloop:
        d_acc, d_index = execute_command(bootcodes[index])
        index += d_index
        
        if index in visited_registers:
            is_bootloop = True
        else:
            acc += d_acc
            visited_registers.add(index)

    return acc, index