def openFile(name):
    file1 = open(name, 'r') 
    return file1.readlines() 

if __name__=="__main__":
    print("day 1: sonar sweep")
    test = openFile("test.txt")
    print("test input is {} lines long".format(len(test)))
    # solve with sliding window of size 2
    testSum = 0
    for i in range(1, len(test)):
        testSum += (int(test[i- 1]) <int(test[i]))
    print("test sum should be 7. actually equals: {}", testSum)


    input = open("input.txt").readlines()
    print("actual input is {} lines long".format(len(input)))
    # solve with sliding window of size 2
    inputSum = 0
    for i in range(1, len(input)):
        inputSum = inputSum + (int(input[i -1]) < int(input[i]))
    print("part 1 equals: {}", inputSum)

    # input = test
    p2sum = 0
    for i in range(3,len(input)):
        if (int(input[i-3]) + int(input[i-2]) + int(input[i-1]) < int(input[i-2]) + int(input[i-1]) + int(input[i])):
            p2sum = p2sum + 1
    print("part 2 equals: {}", p2sum)

    
