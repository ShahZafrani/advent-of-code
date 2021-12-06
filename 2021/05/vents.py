import re

def openFile(name):
    file1 = open(name, 'r') 
    return file1.readlines() 

def isFortyFiveDegree(lineSegment):
    return (abs(lineSegment[0] - lineSegment[2]) == abs(lineSegment[1] - lineSegment[3]))

def buildMap(input, partTwo=False):
    graphMap = {}
    for line in input:
        lineSegment = [int(point) for point in re.split(",|\s|", line) if point != "->" and point !=""]
        # print(lineSegment)
        # print("\t{}".format(isFortyFiveDegree(lineSegment)))
        if (lineSegment[0] == lineSegment[2]): #vertical cause x vals are the same
            for i in range(min(lineSegment[1], lineSegment[3]), max(lineSegment[1], lineSegment[3]) + 1):
                key = "{},{}".format(lineSegment[0], i)
                if (key in graphMap):
                    graphMap[key] = True
                else:
                    graphMap[key] = False
        elif lineSegment[1] == lineSegment[3]: #horizonal cause y vals are the same
            for i in range(min(lineSegment[0], lineSegment[2]), max(lineSegment[0], lineSegment[2]) + 1):
                key = "{},{}".format(i, lineSegment[1])
                if (key in graphMap):
                    graphMap[key] = True
                else:
                    graphMap[key] = False
        if (partTwo and isFortyFiveDegree(lineSegment)):
            # negativeSlope = False
            # if (lineSegment[1] - lineSegment[3]) / (lineSegment[0] - lineSegment[2]) < 0:
            #     negativeSlope = True
            #     print("NEGATIVE SLOPE: {}".format(lineSegment))
            xrange = range(lineSegment[0], lineSegment[2])
            yrange = range(lineSegment[1], lineSegment[3])
            if lineSegment[0] > lineSegment[2]:
                xrange.append(int(lineSegment[2] -1))
            else: 
                xrange.append(int(lineSegment[2] +1))
            if lineSegment[1] > lineSegment[3]:
                yrange.append(int(lineSegment[3] -1))
            else: 
                yrange.append(int(lineSegment[3] +1))
            for x in xrange:
                for y in yrange:
                    key = "{},{}".format(x, y)
                    if (key in graphMap):
                        graphMap[key] = True
                    else:
                        graphMap[key] = False
    return graphMap
if __name__=="__main__":
    print("day 5: thermal vents")
    test = openFile("test.txt") # 5, 12 for part 2
    # input = openFile("input.txt") # 
    graphMap = buildMap(test, True)
    for key in graphMap.keys():
        if (graphMap[key] == True):
            print(key)
    print(sum(graphMap.values()))