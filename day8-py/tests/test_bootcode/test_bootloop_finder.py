from bootcode.bootcode_parser import parse_bootcode
from bootcode.bootcode_interpeter import bootloop_finder

def test_run_example_program():
    filename = "input_test"

    with open(filename) as f:
        bootcodes = parse_bootcode(f.readlines())
    
    acc, _ = bootloop_finder(bootcodes)
    
    assert 5 == acc
