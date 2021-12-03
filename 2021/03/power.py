def openFile(name):
    file1 = open(name, 'r') 
    return file1.readlines() 

def calcPower(input):
    width = len(input[0])
    height = len(input)
    input2d = [[int(char) for char in line if char != '\n'] for line in input]
    gamma = [int(count >= height/2) for count in map(sum,zip(*input2d))]
    epsilon = [val ^ 1 for val in gamma]
    print("gamma: {}".format(gamma))
    print("epsilon: {}".format(epsilon))
    int_gamma = int("".join(str(byte) for byte in gamma), 2)
    int_epsilon = int("".join(str(byte) for byte in epsilon), 2)
    return int_gamma * int_epsilon

def getCarbonVal(input, bit, position):
    # print("position: {}, remianing: {}".format(position, len(input)))
    if (position == len(input[0]) or len(input) == 1):
        return int("".join(str(byte) for byte in input[0]), 2)
    split = [val for val in input if val[position] == bit]
    if (len(split) > float(len(input)) / 2):
        split = [val for val in input if val[position] == (bit^ 1)]
    # print(split)
    return getCarbonVal(split, bit, position+1)

def getOxygenVal(input, bit, position):
    # print("position: {}, remianing: {}".format(position, len(input)))
    if (position == len(input[0]) or len(input) == 1):
        return int("".join(str(byte) for byte in input[0]), 2)
    split = [val for val in input if val[position] == bit]
    if (len(split) < float(len(input)) / 2):
        bit = bit ^ 1
        split = [val for val in input if val[position] == (bit)]
        bit = bit ^ 1
    # print(split)
    return getOxygenVal(split, bit, position+1)

if __name__=="__main__":
    print("day 3: binary stuff")
    test = openFile("test.txt") # 198
    print("test 198 should equal {}".format(calcPower(test)))
    input = openFile("input.txt") # 198
    print("answer: {}".format(calcPower(input)))


    # part2 230 (10 * 23)
    test2d = [[int(char) for char in line if char != '\n'] for line in test]
    print(getCarbonVal(test2d, 0, 0))
    print(getOxygenVal(test2d, 1, 0))


    input2d = [[int(char) for char in line if char != '\n'] for line in input]

    print("life support rating is : {}".format(getCarbonVal(input2d, 0, 0) * getOxygenVal(input2d, 1, 0)))