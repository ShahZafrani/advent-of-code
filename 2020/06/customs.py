import re 

isDebug = False

def debug(text):
    if isDebug is True:
        print(text)

def openFile(name, pattern):
    with open(name, 'r') as file:
        data = re.split(pattern, file.read())
    return data

def anyoneAnsweredYes(lines):
    debug("----------")
    debug(lines)
    answers = lines.split("\n")
    debug(answers)
    firstResponse = []
    firstResponse[:0] = answers[0]
    answerSet = set(firstResponse)
    for answer in answers[1:]:
        debug(answerSet)
        for a in firstResponse:
            if (a not in answer) and (a in answerSet):
                answerSet.remove(a)

    debug(len(answerSet))
    return len(answerSet)

if __name__=="__main__":
    print("day 6: customs")
    # lines = openFile("test_input.txt", "\n\n")
    lines = openFile("input.txt", "\n\n")
    print("input is {} large".format(len(lines)))
    print("part 1: {}".format(sum(map(lambda x : len(set(x.replace("\n", ""))), lines))))
    print("part 2: {}".format(sum(map(lambda x : anyoneAnsweredYes(x), lines))))
