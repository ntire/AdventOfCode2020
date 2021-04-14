from bootcode.bootcode_parser import parse_bootcode
from bootcode.bootcode_interpeter import bootloop_finder, run_program

def test_run_example_program():
    filename = "input_test"

    with open(filename) as f:
        bootcodes = parse_bootcode(f.readlines())
    
    acc, _ = bootloop_finder(bootcodes)
    
    assert 5 == acc

def test_run_program_with_bootloop():
    filename = "input_test"

    with open(filename) as f:
        bootcodes = parse_bootcode(f.readlines())
    
    acc, _, is_bootloop = run_program(bootcodes)
    
    assert 5 == acc
    assert True == is_bootloop


def test_run_program_without_bootloop():
    filename = "input_test_fixed"

    with open(filename) as f:
        bootcodes = parse_bootcode(f.readlines())
    
    acc, _, is_bootloop = run_program(bootcodes)
    
    assert 8 == acc
    assert False == is_bootloop
