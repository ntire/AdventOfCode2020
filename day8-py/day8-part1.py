from bootcode.bootcode_parser import parse_bootcode
from bootcode.bootcode_interpeter import bootloop_finder

def main():
    filename = "input"

    with open(filename) as f:
        bootcodes = parse_bootcode(f.readlines())
    
    acc, _ = bootloop_finder(bootcodes)
    print ("Last value of acc before bootloop:", acc)

if __name__ == "__main__":
    main()