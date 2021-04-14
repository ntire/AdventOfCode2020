from bootcode.bootcode_interpeter import run_program
from copy import deepcopy
def fix_bootcode(bootcodes):
    is_fixed = False
    i = 0
    acc = 0
    while not is_fixed:

        modify = bootcodes[i][0] in ["jmp", "nop"]

        if modify:
            modified_bootcodes = deepcopy(bootcodes)
            
            if bootcodes[i][0] == "nop" :
                modified_bootcodes[i][0] = "jmp"
            else:
                modified_bootcodes[i][0] = "nop"
                        
            acc, _, is_bootloop = run_program(modified_bootcodes)

            is_fixed = not is_bootloop 

        i += 1
    return acc
