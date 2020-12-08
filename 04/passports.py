import re 

isDebug = False

def debug(text):
    if isDebug is True:
        print(text)

def openFile(name, pattern):
    with open(name, 'r') as file:
        data = re.split(pattern, file.read())
    return data

def validatePassport(line, p):
    return bool(p.match(line.replace("\n", " ")))


# run with python -m cProfile trees.py 
if __name__=="__main__":
    print("day 4: passports")
    # lines = openFile("testInput.txt", "\n\n")
    lines = openFile("input.txt", "\n\n")
    pattern = re.compile("^(?=.*ecl)(?=.*eyr)(?=.*pid)(?=.*hcl)(?=.*byr)(?=.*hgt)(?=.*iyr).+$")
    remap = map(lambda x : validatePassport(x, pattern), lines)
    print(sum(remap))

    

