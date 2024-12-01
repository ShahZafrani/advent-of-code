import re
from functools import reduce
isDebug = False

def debug(text):
    if isDebug is True:
        print(text)

def openFile(name):
    file1 = open(name, 'r') 
    return file1.readlines() 


def getPossibility(pull):
    debug(pull)
    patterns = [r'\d*.red', r'.\d*.green', r'.\d*.blue']
    max_cubes = [12, 13, 14]
    for color in zip(patterns, max_cubes):
        match = re.findall(color[0], pull)
        if match:
            debug(match)
            count = int(re.sub(r'\D', '', match[0]))
            debug(count)
            if count > color[1]:
                debug("IMPOSSIBLE!!!")
                return False
    return True

def getGamePossibility(line):
    # debug(line)
    inputSegments =  re.split(r':|;', line)
    # debug(inputSegments)
    gameId = int(re.sub(r'\D', '', inputSegments[0]))
    debug(gameId)
    for pull in inputSegments[1:]:
        possible = getPossibility(pull)
        if not possible:
            return 0
    return gameId

def getPower(pulls):
    debug(pulls)
    cubes = {}
    cubes['red'] = 1
    cubes['green'] = 1
    cubes['blue'] = 1
    patterns = [r'\d*.red', r'.\d*.green', r'.\d*.blue']
    for pull in pulls:
        for color in zip(patterns, cubes.keys()):
            match = re.findall(color[0], pull)
            if match:
                debug(match)
                count = int(re.sub(r'\D', '', match[0]))
                debug(count)
                if count > cubes[color[1]]:
                    cubes[color[1]] = count
    return reduce((lambda x, y: x * y), cubes.values())

def getTotalPower(line):
    inputSegments =  re.split(r':|;', line)
    power = getPower(inputSegments[1:])
    return power

if __name__=="__main__":
    print("day 1: trebuchet calibration")
    test = openFile("test.txt")
    print("test input is {} lines long".format(len(test)))
    
    # testSum = 0
    # for i in range(0, len(test)):
    #     testSum += getGamePossibility(test[i])
    # print("test sum should be 8. actually equals: {}".format(testSum))


    # input = open("input.txt").readlines()
    # print("actual input is {} lines long".format(len(input)))
    # inputSum = 0
    # for i in range(0, len(input)):
    #     inputSum += getGamePossibility(input[i])
    # print("part 1 equals: {}".format(inputSum))


    testSum = 0
    for i in range(0, len(test)):
        testSum += getTotalPower(test[i])
    print("test sum should be 2286. actually equals: {}".format(testSum))


    input = open("input.txt").readlines()
    print("actual input is {} lines long".format(len(input)))
    inputSum = 0
    for i in range(0, len(input)):
        inputSum += getTotalPower(input[i])
    print("part 1 equals: {}".format(inputSum))