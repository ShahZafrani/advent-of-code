public class Solver {
    private string day;
    private string expectedTestOutput;
    private string testFileName;
    private string inputFileName;
    public Solver(string day, string expectedTestOutput, string testFileName = "test.txt", string inputFileName = "input.txt") {
        this.day = day;
        this.expectedTestOutput = expectedTestOutput;
        this.testFileName = testFileName;
        this.inputFileName = inputFileName;
    }
    public void Run() {
        Console.WriteLine("Solving day {0}", this.day);
        Console.WriteLine("Test Output: {0}, expected: {1}", this.expectedTestOutput, Solve(this.testFileName));
        Console.WriteLine("\nSovled output: {0}", Solve(this.inputFileName));
    }
    public int Solve(string fileName) {
        return 0;
    }
}