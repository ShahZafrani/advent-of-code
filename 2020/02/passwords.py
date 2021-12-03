isDebug = False

def debug(text):
    if isDebug is True:
        print(text)

def openFile(name):
    file1 = open(name, 'r') 
    return file1.readlines() 

def getInputsFromLine(line):
    limits, char, password = line.split(" ")
    lower_limit, upper_limit = limits.split("-")
    char = char[0]
    password = password[:-1]
    return int(lower_limit), int(upper_limit), char, password

def isLineValidPart1(line):
    lower_limit, upper_limit, char, password = getInputsFromLine(line)
    count = password.count(char)
    debug("{} contains '{}' {} times".format(password, char, count))
    return (count >= lower_limit and count <= upper_limit)

def isLineValidPart2(line):
    index_one, index_two, char, password = getInputsFromLine(line)
    index_one -=1
    index_two -=1
    debug(index_one)
    debug(index_two)
    debug(line)
    debug(((password[index_one] == char) or (password[index_two] == char)))
    return ((password[index_one] == char) and (password[index_two] != char)) or ((password[index_one] != char) and (password[index_two] == char))

if __name__=="__main__":
    print("day 2: passwords")
    lines = openFile("input.txt")
    print("input is {} lines long".format(len(lines)))
    print("\t part 1 \n")
    mapLines = map(lambda x : isLineValidPart1(x)==True, lines)
    print(sum(mapLines))
    print("\t part 2 \n")
    mapLines = map(lambda x : isLineValidPart2(x)==True, lines)
    print(sum(mapLines))
    
