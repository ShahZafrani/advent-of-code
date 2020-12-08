isDebug = False

def debug(text):
    if isDebug is True:
        print(text)

def openFile(name):
    file1 = open(name, 'r') 
    return file1.readlines() 

def getSeatId(row, col):
    return row*8 + col

def getRowAndCol(input):
    row = 0
    for r in range(1,8):
        if (input[r-1] == "B"):
            row += 2**(7-r)
    col = 0
    for c in range(1,4):
        if (input[c+6]=="R"):
            col += 2**(3-c)
    return row, col

def calSeatId(input):
    debug(input)
    row, col = getRowAndCol(input)
    return getSeatId(row, col)
# run with python -m cProfile trees.py 
if __name__=="__main__":
    print("day 5: boarding passes")
    # #  test data
    # BFFFBBFRRR: row 70, column 7, seat ID 567.
    # FFFBBBFRRR: row 14, column 7, seat ID 119.
    # BBFFBBFRLL: row 102, column 4, seat ID 820.
    testLines = openFile("testInput.txt")
    print("test lines:")
    for line in testLines:
        line = line.replace("\n", "")
        row, col = getRowAndCol(line)
        print("\t{}: row {}, column {}, seat ID {}".format(line, row, col, getSeatId(row, col)))
    lines = openFile("input.txt")
    seatIds = map(lambda x : calSeatId(x), lines)
    print("max seat id: {}".format(max(seatIds)))
    # sorted(seatIds)
    print(sorted(seatIds))




