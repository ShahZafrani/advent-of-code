from lib.solver import Solver
from lib.utils import openFile
from typing import List

def getProductCode(input):
    grid, folds = input
    for idx, instruction in enumerate(folds):
        grid = fold(grid, *instruction)
        if not idx:
            print(f"part 1: {sum(map(lambda x : sum(x), grid))}") # for part 1
    printGrid(grid) # for part 2


def fold(grid, axis, foldLine):
    if axis == "x":
        return [[a or b for (a, b) in zip(line[0:foldLine], reversed(line[(foldLine + 1):]))] for line in grid]
    elif axis == "y":
        return [[a or b for (a, b) in zip(lineA, lineB)] for lineA, lineB in zip(grid[0: foldLine], reversed(grid[(foldLine + 1):]))]

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

    grid = [[0 for _ in range(maxX + 1)] for _ in range(maxY + 1)]
    for loc in initialDots:
        grid[loc[0]][loc[1]] = 1
    return grid, folds

def printGrid(grid):
    print("\nprinting grid\n")
    for line in grid:
        print(f"\t{line}")

if __name__ == "__main__":
    testInput = createDotGrid(openFile("13/test.txt"))
    input = createDotGrid(openFile("13/input.txt"))
    twelve = Solver(testInput, input)
    twelve.solve(getProductCode, 17)
    



