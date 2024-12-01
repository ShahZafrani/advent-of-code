import re
import os
isDebug = False

def debug(text):
    if isDebug is True:
        print(text)

def openFile(name):
    file1 = open(os.getcwd() + "/2023/03/" + name, 'r') 
    return file1.readlines() 

def getAllNeighbors(y, x, ylen, xlen):
    neighbors = []
    neighbors.append((y - 1, x))
    neighbors.append((y - 1, x + 1))
    neighbors.append((y - 1, x - 1))
    neighbors.append((y + 1, x))
    neighbors.append((y + 1, x + 1))
    neighbors.append((y + 1, x - 1))
    neighbors.append((y, x + 1))
    neighbors.append((y, x - 1))
    return [neighbor for neighbor in neighbors if 0 <= neighbor[0] < ylen and 0 <= neighbor[1] < xlen]
    

def hasAdjacentSymbol(digitPositions, ylen, xlen, grid):
    # this will involve checking duplicate spaces. not an optimization I'm in the mood to consider atm
    positionsToCheck = []
    for x, y in digitPositions: 
        positionsToCheck.extend(getAllNeighbors(x, y, ylen, xlen))
    syms = ""
    positionsToCheck = list(dict.fromkeys(positionsToCheck))
    debug(positionsToCheck)
    for x, y in positionsToCheck:
        syms += grid[x][y]
    debug(syms)
    match = re.search(r'[@_!#$%^&*()+<\->?/|}{~:=]', syms)
    debug(match)
    # if match is not None:
        # print(match, end="")
    return True if match != None else False

def getRatio(firstGear, digitPositions, ylen, xlen, grid, pastDigitPositions): 
    # this will involve checking duplicate spaces. not an optimization I'm in the mood to consider atm
    positionsToCheck = []
    for x, y in digitPositions: 
        positionsToCheck.extend(getAllNeighbors(x, y, ylen, xlen))
    syms = ""
    positionsToCheck = list(dict.fromkeys(positionsToCheck))
    debug(positionsToCheck)
    for x, y in positionsToCheck:
        if grid[x][y] == "*":
            # cog found
            # from here pass in digitPositions as a do-not-check parameter to a function that looks for another number
            otherGear = getOtherGear(pastDigitPositions, x, y, ylen, xlen, grid)
            print("cog found: {} x {}".format(firstGear, otherGear))
            return firstGear * otherGear
    return 0

def getOtherGear(pastDigitPositions, x, y, ylen, xlen, grid):
    positionsToCheck = []
    for pos in getAllNeighbors(x, y, ylen, xlen):
        if pos not in pastDigitPositions: 
            positionsToCheck.append(pos)
    for posx, posy in positionsToCheck:
        if (grid[posx][posy].isdigit()):
            return getNumber(posx, posy, ylen, grid)
    return 0

def getNumber(x, y, ylen, grid):
    currentGrid = grid[x][y]
    while(grid[x][y].isdigit()):
        y-=1
        currentGrid = grid[x][y]
    y +=1
    digits = ""
    while(grid[x][y].isdigit()):
        digits += grid[x][y]
        y +=1
        if y is ylen:
            break
    # print("other digit found! {}".format(digits))
    return int(digits)

def loadGrid(file):
    grid = []
    for line in file:
        row = [char for char in line if char != "\n"]
        grid.append(row)
    return grid

def solve(input):
    grid = loadGrid(input)
    parts = []
    digitFound = False
    digitPositions = []
    possiblePartNum = ""
    for x in range(len(grid)):
        if digitFound:
                debug(possiblePartNum)
                # part number ended. check for symbols here and reset afterwards
                if (hasAdjacentSymbol(digitPositions, len(grid), len(grid[0]), grid) == True):
                    debug("part found")
                    parts.append(int(possiblePartNum))
                    # print(":    {}".format(possiblePartNum))
                digitPositions = []
                digitFound = False
                possiblePartNum = ""
        for y in range(len(grid[0])):
            if (grid[x][y].isdigit()):
                # first or subsequent digit in a potential part number
                digitPositions.append((x, y))
                possiblePartNum += grid[x][y]
                digitFound = True
            elif digitFound:
                debug(possiblePartNum)
                # part number ended. check for symbols here and reset afterwards
                if (hasAdjacentSymbol(digitPositions, len(grid), len(grid[0]), grid) == True):
                    debug("part found")
                    parts.append(int(possiblePartNum))
                    # print(":    {}".format(possiblePartNum))
                digitPositions = []
                digitFound = False
                possiblePartNum = ""
    return sum(parts)


def solveGearRatios(input):
    grid = loadGrid(input)
    parts = []
    pastDigitPositions = []
    digitFound = False
    digitPositions = []
    possiblePartNum = ""
    for x in range(len(grid)):
        if digitFound:
                debug(possiblePartNum)
                # part number ended. check for symbols here and reset afterwards
                if (hasAdjacentSymbol(digitPositions, len(grid), len(grid[0]), grid) == True):
                    debug("part found")
                    pastDigitPositions.extend(digitPositions)
                    parts.append(getRatio(int(possiblePartNum), digitPositions, len(grid), len(grid[0]), grid, pastDigitPositions))
                    # print(":    {}".format(possiblePartNum))
                digitPositions = []
                digitFound = False
                possiblePartNum = ""
        for y in range(len(grid[0])):
            if (grid[x][y].isdigit()):
                # first or subsequent digit in a potential part number
                digitPositions.append((x, y))
                possiblePartNum += grid[x][y]
                digitFound = True
            elif digitFound:
                debug(possiblePartNum)
                # part number ended. check for symbols here and reset afterwards
                pastDigitPositions.extend(digitPositions)
                parts.append(getRatio(int(possiblePartNum), digitPositions, len(grid), len(grid[0]), grid, pastDigitPositions))
                # print(":    {}".format(possiblePartNum))
                digitPositions = []
                digitFound = False
                possiblePartNum = ""
    return sum(parts)

if __name__ == "__main__":
    test = openFile("test.txt")
    input = openFile("input.txt")
    testAnswer = solve(test)
    inputAnswer = solve(input)
    
    print("Day 3, part 1")
    print("test answer supposed 4361, test parts sum = {}".format(testAnswer))
    print("\n\n Part 1 Answer: {} \n\n".format(inputAnswer))

    print("\n\n\n Part 2: Gear Ratios")
    print("test answer should be 467835, but is actually {}".format(solveGearRatios(test)))
    print("\n\n Part 2 Answer: {} \n\n".format(solveGearRatios(input)))
    #  69361715 too low
    #  83792339 too low 
    #  83894237 incorrect = above + 459x222 (101898)
    #  84190276 incorrect
    #  84900926
    #  84289137 -- currently multiplying by self
    # 109750642 too high

                

