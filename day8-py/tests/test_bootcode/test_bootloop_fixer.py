from bootcode.bootcode_parser import parse_bootcode
from bootcode.bootcode_interpeter import bootloop_finder, run_program
from bootcode.bootcode_fixer import fix_bootcode

def test_run_example_program():
    filename = "input_test"

    with open(filename) as f:
        bootcodes = parse_bootcode(f.readlines())
    
    acc = fix_bootcode(bootcodes)
    
    assert 8 == acc

