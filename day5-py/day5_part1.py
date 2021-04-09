from binaryboarding.binaryspacepartition import determine_seatid

def main():
    seatid = 0
    with open('input') as f:
        for line in f.readlines():
            seatid = max(seatid, determine_seatid(line))
    print("Max seat id: {}".format(seatid))


if __name__ == "__main__":
    main()