
import math

# Expects a 10character-string as parameter, e.g. BFFFBBFRRR
def getseatid(boardingpass):
    row_floor = 0
    row_ceiling = 127

    # determine row
    for i in range(7):
        pass

def determine_row(boardingpass):
    boardingpass_row_part = boardingpass[:7]
    floor = 0
    ceiling = 127

    for s in (boardingpass_row_part):
        if s == "F":
            ceiling = math.floor(ceiling - (ceiling - floor) / 2)
        elif s == "B":
            floor = math.ceil(floor + (ceiling - floor) / 2)
    return floor # should be similiar to ceiling

def determine_column(boardingpass):
    boardingpass_column_part = boardingpass[7:]
    
    floor = 0
    ceiling = 7

    for s in (boardingpass_column_part):
        if s == "L":
            ceiling = math.floor(ceiling - (ceiling - floor) / 2)
        elif s == "R":
            floor = math.ceil(floor + (ceiling - floor) / 2)
    return floor # should be similiar to ceiling

def determine_seatid(boardingpass):
    row = determine_row(boardingpass)
    column = determine_column(boardingpass)
    seatid = row * 8 + column
    return seatid