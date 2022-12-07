def openFile(name):
    file1 = open(name, 'r') 
    return file1.readlines() 

# for loading input that looks like:
# 01234
# 56789
# into:
# [[0, 1, 2, 3, 4],
# [5, 6, 7, 8, 9]]

def loadGrid(file):
    grid = []
    for line in file:
        row = [int(row) for row in line if row != "\n"]
        grid.append(row)
    return grid

def printGrid(grid):
    print("\nprinting grid\n")
    [print(f"\t{line}") for line in grid]


# returns a list of (y, x) tuples that border the provided point
def getAllNeighborCoords(y, x, ylen, xlen, diagonals=True):
    neighbors = []
    neighbors.append((y - 1, x))
    neighbors.append((y + 1, x))
    neighbors.append((y, x + 1))
    neighbors.append((y, x - 1))
    if (diagonals is True):
        neighbors.append((y + 1, x + 1))
        neighbors.append((y + 1, x - 1))
        neighbors.append((y - 1, x + 1))
        neighbors.append((y - 1, x - 1))
    return [neighbor for neighbor in neighbors if 0 <= neighbor[0] < ylen and 0 <= neighbor[1] < xlen]
