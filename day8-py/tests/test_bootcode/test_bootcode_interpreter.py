from bootcode.bootcode_interpeter import execute_command

# return delta of accumulator and new index pointer
def test_acc_command():
    command = ["acc", -2] 
    d_acc, d_index = execute_command(command)
    assert d_acc == -2
    assert d_index == 1

def test_jmp_command():
    command = ["jmp", 12] 
    d_acc, d_index = execute_command(command)
    assert d_acc == 0
    assert d_index == 12
    
def test_nop_command():
    command = ["nop", 1] 
    d_acc, d_index = execute_command(command)
    assert d_acc == 0
    assert d_index == 1