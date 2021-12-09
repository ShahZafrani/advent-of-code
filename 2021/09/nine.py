def openFile(name):
    file1 = open(name, 'r') 
    return file1.readlines() 

def findLocalMinima(input):
    heatMap = []
    lowPoints = []
    for line in input:
        intput =[int(n) for n in line if n != "\n"]
        heatMap.append(intput)
    
    for y in range(len(heatMap)):
        for x in range(len(heatMap[y])):
            point = 0 + heatMap[y][x]
            if y == 0:
                if (x == 0):
                    if (point < heatMap[y][x+1] and point < heatMap[y+1][x]):
                        lowPoints.append((y, x))
                elif (x == len(heatMap[y]) - 1):
                    if (point < heatMap[y][x-1] and point < heatMap[y+1][x]):
                        lowPoints.append((y, x))
                else:
                    if (point < heatMap[y][x-1] and point < heatMap[y][x+1] and point < heatMap[y+1][x]):
                        lowPoints.append((y, x))
            elif y == len(heatMap) - 1:
                if (x == 0):
                    if (point < heatMap[y][x+1] and point < heatMap[y-1][x]):
                        lowPoints.append((y, x))
                elif (x == len(heatMap[y]) - 1):
                    if (point < heatMap[y][x-1] and point < heatMap[y-1][x]):
                        lowPoints.append((y, x))
                else:
                    if (point < heatMap[y][x-1] and point < heatMap[y][x+1] and point < heatMap[y-1][x]):
                        lowPoints.append((y, x))
            else:
                if (x == 0):
                    if (point < heatMap[y][x+1] and point < heatMap[y-1][x] and point < heatMap[y+1][x]):
                        lowPoints.append((y, x))
                elif (x == len(heatMap[y]) - 1):
                    if (point < heatMap[y][x-1] and point < heatMap[y-1][x] and point <heatMap[y+1][x]):
                        lowPoints.append((y, x))
                else:
                    if (point < heatMap[y][x-1] and point < heatMap[y][x+1] and point < heatMap[y-1][x] and point < heatMap[y+1][x]):
                        lowPoints.append((y, x))
    
    return lowPoints, heatMap



def findBasins(heatMap, lowPoints):
    basins = []
    heatMap.insert(0, [9 for i in range(len(heatMap[0]) + 2)] )
    for i in range(1, len(heatMap)):
        heatMap[i].insert(0, 9)
        heatMap[i].append(9)
    heatMap.append([9 for i in range(len(heatMap[0]))])
    # for line in heatMap:
    #     print(line)
    for y, x in lowPoints:
        y = y + 1
        x = x + 1
        visited = {}
        toVisit = []
        basin = []
        toVisit.append((y, x+1))
        toVisit.append((y+1, x))
        toVisit.append((y-1, x))
        toVisit.append((y, x-1))
        while len(toVisit) != 0:
            cy, cx = toVisit.pop()
            try:
                key = "{},{}".format(cy, cx)
                if (key not in visited.keys()):  
                    visited[key] = True
                    point = heatMap[cy][cx]
                    if (point != 9):
                        basin.append(point)
                        toVisit.append((cy, cx+1))
                        toVisit.append((cy+1, cx))
                        toVisit.append((cy-1, cx))
                        toVisit.append((cy, cx-1))
            except IndexError: 
                pass
        basins.append(basin)
    return basins

if __name__ == "__main__":
    test = openFile("test.txt")
    input = openFile("input.txt")
 
    testLowPoints, testHeatMap = findLocalMinima(test)

    lowPoints, heatMap = findLocalMinima(input)

    print("part 1 test should be 15 == {}".format(sum([ 1 + testHeatMap[y][x] for y, x in testLowPoints])))
    print("part 1 answer ---------")
    print(sum([ 1 + heatMap[y][x] for y, x in lowPoints]))
    print("solving part 2")
    testBasins = sorted([len(basin) for basin in findBasins(testHeatMap, testLowPoints)])
    testBasins.reverse()
    print("part 2 test should be 1134 == {}".format(reduce((lambda x, y: x * y), testBasins[0:3])))
    basins = sorted([len(basin) for basin in findBasins(heatMap, lowPoints)])
    basins.reverse()
    print(reduce((lambda x, y: x * y), basins[0:3]))