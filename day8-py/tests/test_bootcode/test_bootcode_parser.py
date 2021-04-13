from bootcode.bootcode_parser import parse_bootcode

def test_simple_bootcode():
    lines = ["nop +0", 
            "acc +1",
            "jmp -11"]
    bootcode = parse_bootcode(lines)
    assert 3 == len(bootcode)

def test_simple_bootcode_command_with_positive_number():
    lines = ["nop +0"] 
    bootcode = parse_bootcode(lines)
    assert bootcode[0][0] == "nop"
    assert bootcode[0][1] == 0

def test_simple_bootcode_command_with_negative_number():
    lines = ["jmp -99"] 
    bootcode = parse_bootcode(lines)
    assert bootcode[0][0] == "jmp"
    assert bootcode[0][1] == -99
