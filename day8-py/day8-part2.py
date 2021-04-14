from bootcode.bootcode_parser import parse_bootcode
from bootcode.bootcode_fixer import fix_bootcode

def main():
    filename = "input"

    with open(filename) as f:
        bootcodes = parse_bootcode(f.readlines())
    
    acc = fix_bootcode(bootcodes)
    
    print ("Last value of acc before program termination:", acc)

if __name__ == "__main__":
    main()