def openFile(name):
    file1 = open(name, 'r') 
    return file1.readlines() 

def moveSub_part1(pos, line):
    parts = line.split()
    if (parts[0] == "forward"):
        pos[1] += int(parts[1])
    elif(parts[0] == "down"):
        pos[0] += int(parts[1])
    elif(parts[0] == "up"):
        pos[0] -= int(parts[1])


def moveSub_part2(pos, aim, line):
    parts = line.split()
    if (parts[0] == "forward"):
        pos[1] += int(parts[1])
        pos[0] += (int(parts[1]) * aim)
    elif(parts[0] == "down"):
        aim += int(parts[1])
    elif(parts[0] == "up"):
        aim -= int(parts[1])
    return pos, aim

if __name__=="__main__":
    print("day 2: calc depth")
    test = openFile("test.txt") # 150
    print("test input is {} lines long".format(len(test)))
    pos = [0,0] # depth, horizontal
    for i in range(0, len(test)):
        moveSub_part1(pos, test[i])
    print("test product should be 150. actually equals: {}", pos[0] * pos[1])

    input = openFile("input.txt") 
    print("input is {} lines long".format(len(input)))
    pos = [0,0] # depth, horizontal
    for i in range(0, len(input)):
        moveSub_part1(pos, input[i])
    print("final horizontal position multiplied by vertical position equals:{}", pos[0] * pos[1])


    # test = openFile("test.txt") # 900
    pos = [0,0] # depth, horizontal
    aim = 0
    for i in range(0, len(test)):
        pos, aim = moveSub_part2(pos, aim,  test[i])
    print("pt2 test product should be 900. actually equals: {}", pos[0] * pos[1])


    # test = openFile("test.txt") # 900
    pos = [0,0] # depth, horizontal
    aim = 0
    for i in range(0, len(input)):
        pos, aim = moveSub_part2(pos, aim,  input[i])
    print("pt2 product: {}", pos[0] * pos[1])

