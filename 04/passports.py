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
    # extra space at end is in case the passport id is the last field.
    return bool(p.match(line.replace("\n", " ") + " "))


# run with python -m cProfile trees.py 
if __name__=="__main__":
    print("day 4: passports")
    # lines = openFile("testInput.txt", "\n")
    lines = openFile("input.txt", "\n\n")
    pstring1 = "^(?=.*ecl)(?=.*eyr)(?=.*pid)(?=.*hcl)(?=.*byr)(?=.*hgt)(?=.*iyr).+$"
    pattern1 = re.compile(pstring1)
    eyeColor = "(?=.*ecl:(brn|gry|blu|amb|grn|hzl|oth))"
    expYear = "(?=.*eyr:((202[0-9])|(2030)))"
    passportId = "(?=.*pid:\d{9}\s)"
    hairColor = "(?=.*hcl:#[0-9,a-f]{6})"
    birthYear = "(?=.*byr:((19[2-9][0-9])|(200[0-2])))"
    issueYear = "(?=.*iyr:((201[0-9])|(2020)))"
    height = "(?=.*hgt:((1[5-8][0-9]cm)|(19[0-3]cm)|(59in)|(6[0-9]in)|(7[0-6]in)))"
    pstring2 = "^" + eyeColor + expYear + passportId + hairColor + birthYear + issueYear + height + ".+$"
    pattern2 = re.compile(pstring2)
    print("using pattern:\n{}\n for part 1\ncount: {}".format(pstring1, sum(map(lambda x : validatePassport(x, pattern1), lines))))
    print("using pattern:\n{}\n for part 2\ncount: {}".format(pstring2, sum(map(lambda x : validatePassport(x, pattern2), lines))))

    

