from binaryboarding.binaryspacepartition import determine_column

def test_determine_row():
    boardingpass = "BFFFBBFRRR"
    assert 7 == determine_column(boardingpass)

def test_determine_row2():
    boardingpass = "FFFBBBFRRR"
    assert 7 == determine_column(boardingpass)

def test_determine_row3():
    boardingpass = "BBFFBBFRLL"
    assert 4 == determine_column(boardingpass)


     