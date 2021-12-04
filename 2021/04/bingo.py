def openFile(name):
    file1 = open(name, 'r') 
    return file1.readlines() 

def setupBingoBoard(input):
    numSequence = [int(num) for num in input[0].split(",")]
    print(numSequence)
    boards = [[]]
    numDict = {} # key is num -- val is [boardIndex, boardRow, boardCol]
    numBoards = 0
    boardRow = 0
    for i in range(1, len(input)):
        # print(i)
        row = [int(num) for num in input[i].split()]
        if (boardRow == 5):
            board = []
            boards.append(board)
            numBoards +=1
            boardRow = 0
        elif (len(row) > 1):
            boards[numBoards].append(row)
            # print(boards[numBoards -1])
            for i in (range(len(row))):
                if row[i] in numDict:
                    numDict[row[i]].append([numBoards, boardRow, int(i)])
                else:
                    numDict[row[i]] = [[numBoards, boardRow, int(i)]]
            boardRow +=1
    boards = [board for board in boards if len(board) != 0]
    # print(numDict)
    # print(boards[0])
    return numSequence, boards, numDict

def drawNumber(numDict, boards, number):
    if number in numDict:
        for match in numDict[number]:
            # print("match {}, {}".format(number, match))
            # print(boards[match[0]])
            boards[match[0]][match[1]][match[2]] = -1
    return boards

def checkVictory(numDict, boards, number, yetToWin):
        # row victory
    if number in numDict:
        for match in numDict[number]:
            columnSums = map(sum,zip(*boards[match[0]]))
            if (sum(boards[match[0]][match[1]]) == -5):
                if (sum(yetToWin.values()) == 1 and yetToWin[match[0]] == True):
                    return boards[match[0]]
                else:
                    yetToWin[match[0]] = False
            # column victory
            elif (columnSums[match[2]] == -5):
                if (sum(yetToWin.values()) == 1 and yetToWin[match[0]] == True):
                    return boards[match[0]]
                else: 
                     yetToWin[match[0]] = False

if __name__=="__main__":
    print("day 4: bingo")
    # test = openFile("test.txt") 
    
    input = openFile("input.txt") 
    numSequence, boards, numDict = setupBingoBoard(input)
    print(boards)

    winningBoard = 0
    currentDraw = 0
    yetToWin = {}
    for i in range(len(boards)):
        yetToWin[i] = True

    while winningBoard == 0:
        # print(currentDraw)
        boards = drawNumber(numDict, boards, numSequence[currentDraw])
        board = checkVictory(numDict, boards, numSequence[currentDraw], yetToWin)
        if board is not None:
            print("winning num: {}".format(numSequence[currentDraw]))
            winningBoard = board
            break
        # print(boards)
        currentDraw += 1
    # print(winningBoard)
    winningBoardZeroed = [[val for val in row if val != -1] for row in winningBoard]
    sumOfUncalled = sum(map( lambda y : sum(map(lambda x: x, y)), winningBoardZeroed))
    print(sumOfUncalled)
    print(numSequence[currentDraw] * sumOfUncalled)




