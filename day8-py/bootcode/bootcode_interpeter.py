
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



def run_program(bootcodes):
    acc = 0
    index = 0
    is_bootloop = False
    is_terminated = False
    termination_index = len(bootcodes)
    
    visited_registers = set()
    
    while not is_bootloop and not is_terminated:
        d_acc, d_index = execute_command(bootcodes[index])
        index += d_index

        if index == termination_index:
            is_bootloop = False
            is_terminated = True
            acc += d_acc
        elif index in visited_registers:
            is_bootloop = True
        else:
            acc += d_acc
            visited_registers.add(index)

    return acc, index, is_bootloop