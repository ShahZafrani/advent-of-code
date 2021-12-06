import re

def openFile(name):
    file1 = open(name, 'r') 
    return file1.readlines() 



if __name__=="__main__":
    print("day 6: something's fishy")
    # input = openFile("test.txt") # 5934
    input = openFile("input.txt") # 
    numDays = 256
    startingFish = [int(f) for f in input[0].split(",")]
    fishDict = {}
    for i in range(-1, 10):
        fishDict[i] = 0
    print(startingFish)
    for fish in startingFish:
        fishDict[fish] += 1
    for day in range(numDays):
        for i in range(0, 10):
            val = fishDict[i]
            fishDict[i-1] = val
        newbirths = fishDict[-1]
        fishDict[6] += newbirths
        fishDict[8] += newbirths
        fishDict[-1] = 0

    print(sum(fishDict.values()))