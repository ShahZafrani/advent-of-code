from lib.solver import Solver
from lib.utils import openFile
from typing import List
from collections import Counter
import gc

def getPolymerChain(input):
    polymer, pairs = input
    pairQueue = getPairQueue(polymer)
    for i in range(40):
        print(i)
        newQueue = []
        for idx, pair in enumerate(pairQueue):
            newQueue.append(f"{pair[0]}{pairs[pair]}")
            newQueue.append(f"{pairs[pair]}{pair[1]}")
        pairQueue = newQueue
    chars = [pair[0] for pair in pairQueue]
    chars.append(pairQueue[-1][1])
    counts = Counter(chars)
    mostCommon = counts.most_common()[0]
    leastCommon = counts.most_common()[-1]
    print(f"{mostCommon} - {leastCommon} = {mostCommon[1] - leastCommon[1]}")
    return mostCommon[1] - leastCommon[1]


def smartPolymerChain(input):
    polymer, pairs = input
    pairQueue = getPairQueue(polymer)
    pairsDict = {}
    for pair in pairQueue:
        if pair in pairsDict:
            pairsDict[pair] = pairsDict[pair] + 1
        else:
            pairsDict[pair] = 1
    for i in range(40):
        newPairsDict = {}
        print(i)
        for key in pairsDict:
            newKeys = [f"{key[0]}{pairs[key]}", f"{pairs[key]}{key[1]}"]
            for newKey in newKeys:
                if newKey in newPairsDict:
                    newPairsDict[newKey] = newPairsDict[newKey] + pairsDict[key]
                else:
                    newPairsDict[newKey] = pairsDict[key]
        pairsDict = newPairsDict
    countsDict = {}
    for key in pairsDict:
        for char in key:
            if char in countsDict:
                countsDict[char] = pairsDict[key] + countsDict[char]
            else:
                countsDict[char] = pairsDict[key]
    counts = sorted([int(val/2) for val in countsDict.values()])
    print(countsDict)
    return counts[-1] - counts[0]
    # print(pairsDict)
    # return 0

def getPairQueue(sequence):
    pairQueue = []
    for i in range(1, len(sequence)):
        pairQueue.append(f"{sequence[i - 1]}{sequence[i]}")
    return pairQueue

def extractPairs(rawInput : List[str]): # 0 represents no dot, 1 represents dot
    pairs = {}
    for idx, line in enumerate(rawInput):
        if not idx:
            inputSequence = line.replace("\n","")
        else:
            inPair, out = line.split(" -> ")
            pairs[inPair] = out[0]
    return inputSequence, pairs

if __name__ == "__main__":
    testInput = extractPairs(openFile("14/test.txt"))
    input = extractPairs(openFile("14/input.txt"))
    fourteen = Solver(testInput, input)
    # TODO: this has the potential to be off by one. Got the star for now, but you should fix this later
    fourteen.solve(smartPolymerChain, 1588, testOnly=False)
    



