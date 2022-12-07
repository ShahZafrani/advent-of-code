from lib.solver import Solver
from lib.utils import openFile
from typing import List

#dfs
def findPaths(caveMap, currentCave="start", visitedSmall=["start"], pathTaken = ["start"], count=0):
    if currentCave == "end":
        # print(pathTaken)
        count = count + 1
  
    remainingPaths = [ exit for exit in caveMap.get(currentCave) if exit not in visitedSmall and exit != currentCave]
    for exit in remainingPaths:
        pathCopy = []
        pathCopy.append(exit)
        pathCopy.extend(pathTaken)
        if exit.isupper():
            # print("found upper: {}".format(exit))
            count = findPaths(caveMap, exit, visitedSmall, pathCopy, count)
        else:
            visitedCopy = []
            visitedCopy.append(exit)
            visitedCopy.extend(visitedSmall)
            count = findPaths(caveMap, exit, visitedCopy, pathCopy, count)
    # print(pathTaken)
    return count

#dfs 
def findPathsAllowSingleDoubleVisit(caveMap, currentCave="start", visitedSmall=["start"], pathTaken = ["start"], count=0, doubleVisited=False):
    if currentCave == "end":
        return count + 1 
    if doubleVisited is False:
        remainingPaths = [ exit for exit in caveMap.get(currentCave) if (exit != currentCave) and (exit != "start")]
    else:
        remainingPaths = [ exit for exit in caveMap.get(currentCave) if exit not in visitedSmall and (exit != currentCave) and (exit != "start")]
    for exit in remainingPaths:
        pathCopy = []
        pathCopy.append(exit)
        pathCopy.extend(pathTaken)
        if exit.isupper():
            count = findPathsAllowSingleDoubleVisit(caveMap, exit, visitedSmall, pathCopy, count, doubleVisited)
        else:
            visitedCopy = []
            visitedCopy.append(exit)
            visitedCopy.extend(visitedSmall)
            count = findPathsAllowSingleDoubleVisit(caveMap, exit, visitedCopy, pathCopy, count, doubleVisited or (exit in visitedSmall))
    return count

    # pun intended
def createCaveMap(rawInput : List[str]): # expecting list of strings like "a-b"
    caveMap = {} # gonna be str (caveEntrance) --> List[str] (connectingCaves)
    for entrance, exit in [line.replace('\n', '').split('-')  for line in rawInput]:
        # sanity check early in dev
        # print("{} ---> {}".format(entrance, exit))
        if entrance in caveMap:
            caveMap[entrance].append(exit)
        else:
            caveMap[entrance] = [entrance, exit]
        if exit in caveMap:
            caveMap[exit].append(entrance)
        else:
            caveMap[exit] = [exit, entrance]
    return caveMap


if __name__ == "__main__":
    testInput = createCaveMap(openFile("12/test.txt"))
    input = createCaveMap(openFile("12/input.txt"))

    twelve = Solver(testInput, input)

    # print(testInput)

    twelve.solve(findPaths, 10)
    twelve.solve(findPathsAllowSingleDoubleVisit, 36)
    



