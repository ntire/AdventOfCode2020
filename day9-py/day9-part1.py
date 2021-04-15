from xmas.xmas_checker import find_xmas_mismatch

def main():
    filename = "input"
    with open(filename) as f:
        data = [int(i) for i in f.readlines()]
    
    first_mismatch = find_xmas_mismatch(data, 25)
    print("First mismatch:", first_mismatch)


if __name__ == "__main__":
    main()