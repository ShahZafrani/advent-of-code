from lib.solver import Solver
from lib.utils import openFile
from typing import List

def getProductCode(input):
    grid = input[0]
    folds = input[1]
    for instruction in folds:
        grid = fold(grid, *instruction)

    printGrid(grid)
    return sum(map(lambda x : sum(x), grid))


def fold(grid, axis, foldLine):
    
    outputGrid = []
    if axis == "x":
        for line in grid:
            lineA = line[0:foldLine]
            lineB = line[(foldLine + 1):]
            lineB.reverse()
            newLine = [a or b for (a, b) in zip(lineA, lineB)]
            outputGrid.append(newLine)
    elif axis == "y":
        gridA = grid[0: foldLine]
        gridB = grid[(foldLine + 1):]
        gridB.reverse()
        for lineA, lineB in zip(gridA, gridB):
            newLine = [a or b for (a, b) in zip(lineA, lineB)]
            outputGrid.append(newLine)
    return outputGrid

def createDotGrid(rawInput : List[str]): # 0 represents no dot, 1 represents dot
    grid = []
    initialDots = [] #list containing y, x coords (flipped from original input to make 2d array traversal easier)
    folds = []
    dotsFinished = False
    for line in rawInput: 
        if len(line) == 1:
            dotsFinished = True
            pass
        if not dotsFinished:
            dotLoc = [int(val) for val in line.split(',')]
            dotLoc.reverse()
            initialDots.append(dotLoc)
        elif line != '\n': 
            foldText = line.split('=')
            folds.append([foldText[0][-1], int(foldText[1])]) # append [axis, line]

    maxX = max([loc[1] for loc in initialDots])
    maxY = max([loc[0] for loc in initialDots])

    for i in range(maxY + 1):
        grid.append([0 for x in range(maxX + 1)])

    for loc in initialDots:
        grid[loc[0]][loc[1]] = 1

    return grid, folds

def printGrid(grid):
    print(['-' for i in range(len(grid[0]))])
    for line in grid:
        print("\t{}".format(line))

if __name__ == "__main__":
    testInput = createDotGrid(openFile("13/test.txt"))
    input = createDotGrid(openFile("13/input.txt"))

    twelve = Solver(testInput, input)


    twelve.solve(getProductCode, 17)
    



