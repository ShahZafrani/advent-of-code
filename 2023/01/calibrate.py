import re

def openFile(name):
    file1 = open(name, 'r') 
    return file1.readlines() 


def getCalibration(line):
    # print(line)
    line =  re.sub(r'\D', '', line)
    # print(line)
    return int("{}{}".format(line[0], line[-1]))

wordsToNum = {}
wordsToNum["zero"] = 0
wordsToNum["one"] = 1
wordsToNum["two"] = 2
wordsToNum["three"] = 3
wordsToNum["four"] = 4
wordsToNum["five"] = 5
wordsToNum["six"] = 6
wordsToNum["seven"] = 7
wordsToNum["eight"] = 8
wordsToNum["nine"] = 9

def getCalibrationWithWords(line):
    # print(line)
    nums = re.findall(r"(?=(\d|one|two|three|four|five|six|seven|eight|nine))", line)
    # nums = re.findall(r'\d|one|two|three|four|five|six|seven|eight|nine', line)
    # print(nums)
    firstDigit = wordsToNum[nums[0]] if nums[0] in wordsToNum  else int(nums[0])
    secondDigit = wordsToNum[nums[-1]] if nums[-1] in wordsToNum else int(nums[-1]) 
    # print("{}-{}".format(firstDigit, secondDigit))
    # print(int("{}{}".format(firstDigit, secondDigit)))
    return int("{}{}".format(firstDigit, secondDigit))

if __name__=="__main__":
    # print("day 1: trebuchet calibration")
    # test = openFile("test.txt")
    # print("test input is {} lines long".format(len(test)))
    
    # testSum = 0
    # for i in range(0, len(test)):
    #     testSum += getCalibration(test[i])
    # print("test sum should be 142. actually equals: {}", testSum)


    # input = open("input.txt").readlines()
    # print("actual input is {} lines long".format(len(input)))
    # inputSum = 0
    # for i in range(0, len(input)):
    #     inputSum += getCalibration(input[i])
    # print("part 1 equals: {}", inputSum)


    print("\nPart 2\n")
    test2 = openFile("test2.txt")
    print("test input is {} lines long".format(len(test2)))
    
    testSum = 0
    for i in range(0, len(test2)):
        testSum += getCalibrationWithWords(test2[i])
    print("test sum should be 281. actually equals: {}".format(testSum))


    input = openFile("input.txt")
    print("actual input is {} lines long".format(len(input)))
    inputSum = 0
    for i in range(0, len(input)):
        inputSum = inputSum + getCalibrationWithWords(input[i])
    print("part 2 equals: {}".format(inputSum))
