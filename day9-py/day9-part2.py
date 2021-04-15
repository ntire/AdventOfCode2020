from xmas.xmas_checker import find_encryption_weakness

def main():
    filename = "input"
    with open(filename) as f:
        data = [int(i) for i in f.readlines()]
    
    weakness = find_encryption_weakness(data, 25)
    print("Encryption weakness:", weakness)


if __name__ == "__main__":
    main()