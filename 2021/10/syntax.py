def openFile(name):
    file1 = open(name, 'r') 
    return file1.readlines() 

def findFirstIllegal(line):
    openers = ["[", "{", "<", "("]
    closers = ["]", "}", ">", ")"]
    expectedQueue = []
    odict = {}
    for c, o in zip(closers, openers):
        odict[o] = c
    for c in [ c for c in line if c !="\n"]:
        if (c in openers):
            expectedQueue.append(odict[c])
        elif (c in closers):
            if expectedQueue[-1] == c:
                expectedQueue.pop()
            else:
                return c
        else:
            print("found: {}".format(c))

def findFirstIncompleteFix(line):
    openers = ["[", "{", "<", "("]
    closers = ["]", "}", ">", ")"]
    expectedQueue = []
    odict = {}
    for c, o in zip(closers, openers):
        odict[o] = c
    for c in [ c for c in line if c !="\n"]:
        if (c in openers):
            expectedQueue.append(odict[c])
        elif (c in closers):
            if expectedQueue[-1] == c:
                expectedQueue.pop()
            else:
                return []
        else:
            print("found: {}".format(c))
    expectedQueue.reverse()
    return expectedQueue

def scoreFix(fix):
    closers = ["]", ")", "}", ">"]
    scores = [2, 1, 3, 4]
    scoreDict = {}
    for c, s in zip(closers, scores):
        scoreDict[c] = s
    score = 0
    for i in range(0, len(fix)):
        score = score * 5
        score += scoreDict[fix[i]]
    return score


if __name__ == "__main__":
    test = openFile("test.txt")
    input = openFile("input.txt")

    closers = ["]", "}", ">", ")"]
    scores = [57, 1197, 25137, 3]
    scoreDict = {}
    for c, s in zip(closers, scores):
        scoreDict[c] = s
    testIllegals = []
    for line in test:
        testIllegals.append(findFirstIllegal(line))
    illegals = []
    for line in input:
        illegals.append(findFirstIllegal(line))
 
    print("part 1 test should be 26397 == {}".format(sum([scoreDict[c] for c in testIllegals if c != None])))
    print("part 1 answer: \n \t {}".format(sum([scoreDict[c] for c in illegals if c != None])))

    # PART 2
    testFixes = []
    for line in test:
        fix = findFirstIncompleteFix(line)
        if fix != []:
            testFixes.append(fix)
    fixes = []
    for line in input:
        fix = findFirstIncompleteFix(line)
        if fix != []:
            fixes.append(fix)
    testScores = sorted([scoreFix(fix) for fix in testFixes])
    print("part 2 test should be 288957 == {}".format(testScores[len(testScores)/2]))
    scores = sorted([scoreFix(fix) for fix in fixes])
    print("part 2 answer \n \t {}".format(scores[len(scores)/2]))
