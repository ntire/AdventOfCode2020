from binaryboarding.binaryspacepartition import determine_seatid

def test_determine_row():
    boardingpass = "BFFFBBFRRR"
    assert 567 == determine_seatid(boardingpass)

def test_determine_row2():
    boardingpass = "FFFBBBFRRR"
    assert 119 == determine_seatid(boardingpass)

def test_determine_row3():
    boardingpass = "BBFFBBFRLL"
    assert 820 == determine_seatid(boardingpass)


     