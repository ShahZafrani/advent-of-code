isDebug = False

def debug(text):
    if isDebug is True:
        print(text)

def openFile(name):
    file1 = open(name, 'r') 
    return file1.readlines() 

def getNextLocation(down, right, ypos, xpos, grid, gridWidth):
    ypos += down
    # stop processing when you hit the bottom of the grid
    # if ypos >= gridHeight:
    #     ypos -= gridHeight
    # elif ypos == -1:
    #     ypos +=gridHeight
    xpos += right 
    if xpos >= gridWidth:
        xpos -= gridWidth
    return ypos, xpos


def countTreesInPath(count, down, right, ypos, xpos, grid, gridHeight, gridWidth):
    if isDebug == True:
        rowstr = "" + grid[ypos]
        if rowstr[xpos] == "#":
            print(rowstr[:xpos] + "X" + rowstr[xpos + 1:] + "\t y={}, x={}".format(ypos, xpos))
        else:
            print(rowstr[:xpos] + "O" + rowstr[xpos + 1:] + "\t y={}, x={}".format(ypos, xpos))
    if ypos >= gridHeight - 1:
        return 0
    else: 
        ypos, xpos = getNextLocation(down, right, ypos, xpos, grid, gridWidth)
        hit = grid[ypos][xpos] == True
        return hit + countTreesInPath(count, down, right, ypos, xpos, grid, gridHeight, gridWidth)

# run with python -m cProfile trees.py 
if __name__=="__main__":
    print("day 3: trees")
    # lines = openFile("testInput.txt")
    lines = openFile("input.txt")
    down = [1, 1, 1, 1, 2]
    right = [1, 3, 5, 7, 1]
    print("input is {} by {}".format(len(lines[0][:-1]), len(lines)))
    grid = []
    # create 2d array (this will be accessed by [y][x] instead of standard xy)
    for line in lines:
        strtoarr = []
        strtoarr[:0] = line[:-1]
        grid.append([i == "#" for i in strtoarr])
    print("Part 1")
    print("\t{} trees encountered with slope ({}, {})".format(countTreesInPath(0, down[1], right[1], 0, 0, grid, len(grid), len(grid[0])), right[1], down[1]))
    print("\nPart 2")
    count = 1
    for i in range(len(right)):
        run = countTreesInPath(count, down[i], right[i], 0, 0, grid, len(grid), len(grid[0]))
        print("\t{} trees encountered with slope ({}, {})".format(run, right[i], down[i]))
        count *= run
    print("total: {}".format(count))

