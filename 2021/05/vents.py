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
            xrange = []
            yrange = []
            if lineSegment[0] > lineSegment[2]:
                xrange = range(lineSegment[2], lineSegment[0])
                xrange.append(lineSegment[0])
                xrange.reverse()
            else: 
                xrange = range(lineSegment[0], lineSegment[2])
                xrange.append(lineSegment[2])
            if lineSegment[1] > lineSegment[3]:
                yrange = range(lineSegment[3], lineSegment[1])
                yrange.append(lineSegment[1])
                yrange.reverse()
            else: 
                yrange = range(lineSegment[1], lineSegment[3])
                yrange.append(lineSegment[3])
            for x, y in zip(xrange, yrange):
                    key = "{},{}".format(x, y)
                    if (key in graphMap):
                        graphMap[key] = True
                    else:
                        graphMap[key] = False
    return graphMap
if __name__=="__main__":
    print("day 5: thermal vents")
    # input = openFile("test.txt") # 5, 12 for part 2
    input = openFile("input.txt") # 
    graphMap = buildMap(input, True)
    for key in graphMap.keys():
        if (graphMap[key] == True):
            print(key)
    print(sum(graphMap.values()))