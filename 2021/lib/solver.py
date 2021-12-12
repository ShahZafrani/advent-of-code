class Solver:
    def __init__(self, testInput, input):
        self.testInput = testInput
        self.input = input 
        self.problemPart = 0


    def solve(self, solution : callable, testAnswer):
        self.problemPart += 1
        print("-----Solving Part: {}".format(self.problemPart))
        testOutput = solution(self.testInput)
        print("test pass: \t {} \n \t expected: {} \n \t got: {}".format(testAnswer == testOutput, testAnswer, testOutput))
        output  = solution(self.input)
        print("answer:\n \t {}".format(output))

