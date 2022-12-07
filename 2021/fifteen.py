from os import path
from lib.solver import Solver
from lib.utils import openFile, loadGrid, printGrid, getAllNeighborCoords
from collections import Counter
import sys
import random

def key(y, x):
    return f"{y}-{x}"

#djikstra
def getLengthOfShortestPath(grid):
    ylen = len(grid)
    xlen = len(grid[ylen-1])
    startingPos = key(0, 0) # top left
    visited = set() # filled with keyed y, x coords ("y-x")
    # initialize with max values
    nodeDistances = { key(y, x): sys.maxsize for x in range(xlen) for y in range(ylen)}
    nodeDistances[startingPos] = 0
    destination = key(ylen - 1, xlen - 1) # bottom right
    # printGrid(grid)
    # print(nodeDistances)
    for i in range(4): # this is ludicrous
        pathQueue = [(y, x) for x in range(xlen) for y in range(ylen)]
        pathQueue = sorted(pathQueue, key=lambda tup: tup[0] + tup[1], reverse=True)
        pathQueue.append((0, 0))
        while len(pathQueue) > 0:
            currentY, currentX = pathQueue.pop()
            currentKey = key(currentY, currentX)
            adjacentNodes = [(y, x) for y, x in getAllNeighborCoords(currentY, currentX, ylen, xlen, diagonals=False) if key(y, x) != "0-0"]
            for nodeY, nodeX in adjacentNodes:
                nodeKey = key(nodeY, nodeX)
                newDist = nodeDistances[currentKey] + grid[nodeY][nodeX]
                if nodeDistances[nodeKey] > newDist:
                    nodeDistances[nodeKey] = newDist
                if nodeKey not in visited:
                    pathQueue.append((nodeY, nodeX))
                    visited.add(nodeKey)

    return nodeDistances[destination]


def loadExpandedGrid(file):
    grid = loadGrid(file)
    numTiles = 5
    ylen = len(grid)
    xlen = len(grid[ylen-1])
    bigGrid = [[0 for _ in range(5*xlen)] for _ in range(5*ylen)]
    for i in range(numTiles):
        for j in range(numTiles):
            for y in range(ylen):
                for x in range(xlen):
                    newVal = (grid[y][x] + i + j)
                    while newVal > 9:
                        newVal = newVal - 9
                    bigGrid[y + ylen*i][x + xlen*j] = newVal
    # printGrid(bigGrid)
    return bigGrid

if __name__ == "__main__":
    # testInput = loadGrid(openFile("15/test.txt"))
    # input = loadGrid(openFile("15/input.txt"))
    # fifteen = Solver(testInput, input)
    # fifteen.solve(getLengthOfShortestPath, 40, testOnly=False)
    bigTest = loadExpandedGrid(openFile("15/test.txt"))
    bigInput = loadExpandedGrid(openFile("15/input.txt"))
    fifteenPart2 = Solver(bigTest, bigInput)
    fifteenPart2.solve(getLengthOfShortestPath, 315, testOnly=False)
    print("answer should be < 3068")
    print("answer should be < 3065")
    print("TODO: figure out why answer was 3063")
    



