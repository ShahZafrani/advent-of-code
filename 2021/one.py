from lib.solver import Solver
from lib.utils import openFile
from typing import List


def getOccurancesOfIncrease(values : List[int]):
    total = 0
    for i in range(1, len(values)):
        total += values[i - 1] < values[i]
    return total

def getSumsLargerThanPreviousSum(values : List[int]):
    total = 0
    for i in range(3, len(values)):
        if (int(values[i-3]) + int(values[i-2]) + int(values[i-1]) < int(values[i-2]) + int(values[i-1]) + int(values[i])):
            total = total + 1
    return total


if __name__ == "__main__":
    testInput = [int(line) for line in openFile("lib/test.txt")]
    input = [int(line) for line in openFile("01/input.txt")]

    sonar = Solver(testInput, input)

    sonar.solve(getOccurancesOfIncrease, 7)
    sonar.solve(getSumsLargerThanPreviousSum, 5)



