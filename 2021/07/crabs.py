def openFile(name):
    file1 = open(name, 'r') 
    return file1.readlines() 


def oilyCrabs(num): #euler
    return (num*(num+1))/2

if __name__ == "__main__":
    input = [int(val) for val in openFile("test.txt")[0].split(",")]
    print(input)

    fuelDict = {}

    minPos = min(input)
    maxPos = max(input)

    for i in range(minPos, maxPos +1):
        fuelDict[i] = sum([oilyCrabs(abs(crabMove - i)) for crabMove in input])
    print(min(fuelDict.values()))

