from binaryboarding.binaryspacepartition import getseatid, determine_row

# def test_valid_seatid():
#     boardingpass1 = "BFFFBBFRRR"
#     boardingpass2 = "FFFBBBFRRR"
#     boardingpass3 = "BBFFBBFRLL"

#     assert 567 == getseatid(boardingpass1)
#     assert 119 == getseatid(boardingpass2)
#     assert 820 == getseatid(boardingpass3)

def test_determine_row():
    boardingpass = "BFFFBBFRRR"
    assert 70 == determine_row(boardingpass)

def test_determine_row2():
    boardingpass = "FFFBBBFRRR"
    assert 14 == determine_row(boardingpass)

def test_determine_row3():
    boardingpass = "BBFFBBFRLL"
    assert 102 == determine_row(boardingpass)


     