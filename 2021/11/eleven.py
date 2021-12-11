def openFile(name):
    file1 = open(name, 'r') 
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

def checkFlashes(octoGrid, flashes, flashQueue):
    if len(flashQueue) == 0:
        return octoGrid, flashes
    # we're operating under the assumption that this grid has all rows of the same length
    for i in range(len(flashQueue)):
        row, column = flashQueue.pop()
        if octoGrid[row][column] > 0:
            octoGrid[row][column] += 1

    ylen = len(octoGrid)
    xlen = len(octoGrid[0])
    for row in range(ylen):
        for column in range(xlen):
            if octoGrid[row][column] > 9:
                flashes += 1
                octoGrid[row][column] = 0
                flashQueue.extend(getAllNeighbors(row, column, ylen, xlen))

    return checkFlashes(octoGrid, flashes, flashQueue)



def step(octoGrid):
    flashQueue = []
    currentFlashes = 0
    for row in range(len(octoGrid)):
        for column in range(len(octoGrid[row])):
            octoGrid[row][column] += 1
            if octoGrid[row][column] > 9:
                flashQueue.append((row, column))
    
    octoGrid, currentFlashes = checkFlashes(octoGrid, currentFlashes, flashQueue)
    return octoGrid, currentFlashes

def loadGrid(file):
    grid = []
    for line in file:
        octorow = [int(octopus) for octopus in line if octopus != "\n"]
        grid.append(octorow)
    return grid

if __name__ == "__main__":
    test = openFile("test.txt")
    input = openFile("input.txt")

    testGrid = loadGrid(test)
    testFlashes = 0
    firstSync = 0
    steps = 1
    while firstSync == 0:
        testGrid, currentFlashes = step(testGrid)
        testFlashes = testFlashes + currentFlashes
        if (steps == 100):
            print("hundred steps test answer should be 1656: {}".format(testFlashes))
        if (currentFlashes == 100):
            print("all flashes happened at step test answer should be 195: {}".format(steps))
            firstSync = steps
        steps = steps + 1
            

    grid = loadGrid(input)
    flashes = 0
    firstSync = 0
    steps = 1
    while firstSync == 0:
        grid, currentFlashes = step(grid)
        flashes = flashes + currentFlashes
        if (steps == 100):
            print("hundred steps flashes part 1 answer \n \t: {}".format(testFlashes))
        if (currentFlashes == 100):
            print("all flashes happened at step: {}".format(steps))
            firstSync = steps

        steps = steps + 1

