def openFile(name):
    file1 = open(name, 'r') 
    return file1.readlines() 

    #  0000
    # 1    2
    # 1    2
    #  3333
    # 4    5
    # 4    5
    #  6666

# using 7 and we can find out what 3 is.
# there should be 2 chars that exist in 7  don't in 3
# whereas the other 5 char candidates, 2 and 5 have 3 missing chars

# using 3 and 4 we can find out what 5 is.
# out of the two remaining 5 char candidates, only 5 will be encompassed by 3 and 4
# 2 is the final remaining candidate
def decodeFiveChars(seven, four, candidates):
    two = ""
    three = ""
    five = ""
    for candidate in candidates:
        missingCount = 0
        for char in candidate:
            if (char not in seven):
                missingCount +=1
        if missingCount == 2:
            three = candidate 
            candidates.remove(three)
    for candidate in candidates:
        threeFour = set(three + four)
        missingCount = 0
        for char in candidate:
            if (char not in threeFour):
                missingCount +=1
        if missingCount == 0:
            five = candidate
            candidates.remove(five)
    two = candidates[0]
    return two, three, five
    
    #  0000
    # 1    2
    # 1    2
    #  3333
    # 4    5
    # 4    5
    #  6666

    # chars in eight minus chars in nine = seg4
    # chars in eight minus chars in zero = seg3
    # chars in eight minus chars in six = seg2
    # seg2 is in zero and nine but not in five
    # six is the only candidate without seg2
    # nine is the set of 1 + 5
    # zero is the final remaining candidate

def decodeSixChars(keys, candidates):
    zero = ""
    six = ""
    nine = ""
    seg2 = ""
    for c in keys[1]:
        if (c not in keys[5]):
            seg2 = c 
    for candidate in candidates:
        if (seg2 not in candidate):
            six = candidate
            candidates.remove(six)
    for candidate in candidates:
        missingCount = 0
        for c in set(keys[1] + keys[5]):
            if c not in candidate:
                missingCount += 1
        if (missingCount == 0):
            nine = candidate
            candidates.remove(nine)
    zero = candidates[0]
    return zero, six, nine

def buildDigitDict(lineInput):
    keys = ["" for i in range(0,10)]
    fiveChars = []
    sixChars = []
    # print(lineInput)
    for item in [ item for item in lineInput.split(" ") if item != ""]:
        # print(item)
        chars = len(item)
        # get the easy ones first
        if chars == 2:
            keys[1] = item
        elif chars == 4:
            keys[4] = item
        elif chars == 3:
            keys[7] = item
        elif chars == 7:
            keys[8] = item
        elif chars == 5:
            fiveChars.append(item)
        elif chars == 6:
            sixChars.append(item)
        else:
            print("something very wrong with: {}".format(item))
    keys[2], keys[3], keys[5] = decodeFiveChars(keys[7], keys[4], fiveChars)
    keys[0], keys[6], keys[9] = decodeSixChars(keys, sixChars)
    digitDict = {}
    error = False
    for i in range(0, 10):
        if (keys[i] != ""):
            key = ""
            for c in sorted(keys[i]):
                key += c
            digitDict[key] = i
        else:
            error = True
    if error:
        print(digitDict)
    return digitDict

def getDecodedDigit(digitDict, chars):
    
    return digitDict[chars]

def sumOutputs(input):
    counts = [0 for i in range(9)]
    total= 0
    for line in input:
        halves = line.split("|")
        outputString = ""
        digitDict = buildDigitDict(halves[0])
        print(digitDict)
        for num in halves[1].split():
            key = ""
            for c in sorted(num):
                key += c
            outputString += str(getDecodedDigit(digitDict, key))
            print(num)
            print(len(num))
            counts[len(num)] += 1
        total += int(outputString)
    return total

if __name__ == "__main__":
    test = openFile("test.txt")
    input = openFile("input.txt")
 
    testAnswer = sumOutputs(test)
    answer = sumOutputs(input)

    print("test case: does 61229 == {}?".format(testAnswer))
    print("answer ---------")
    print(answer)
