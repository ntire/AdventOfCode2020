from binaryboarding.binaryspacepartition import determine_seatid

def main():
    max_seatid = 0
    seats = list()
    with open('input') as f:
        for line in f.readlines():
            seatid = determine_seatid(line)
            seats.append(seatid)
            max_seatid = max(seatid, max_seatid)

    for seat in range(max_seatid):
        if seat not in seats:
            if seat + 1 in seats and seat - 1 in seats:
                print("My seat id: ", seat)
                return


if __name__ == "__main__":
    main()