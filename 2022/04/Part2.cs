public class Part2 {
    private string day;
    private string expectedTestOutput;
    private string testFileName;
    private string inputFileName;
    public Part2(string day, string expectedTestOutput, string testFileName = "test.txt", string inputFileName = "input.txt") {
        this.day = day;
        this.expectedTestOutput = expectedTestOutput;
        this.testFileName = testFileName;
        this.inputFileName = inputFileName;
    }
    public void Run() {
        Console.WriteLine("Solving day {0}", this.day);
        Console.WriteLine("Test Output: {0}, expected: {1}", Solve(this.testFileName), this.expectedTestOutput);
        Console.WriteLine("\nSovled output: {0}", Solve(this.inputFileName));
    }
    public int Solve(string fileName) {
        int fullOverlap = 0;
        foreach (string line in System.IO.File.ReadLines(@fileName))
        {
            int overlap = 0;
            string[] elfAssignments = line.Split(',');
            string[] elfOne = elfAssignments[0].Split('-');
            string[] elfTwo = elfAssignments[1].Split('-');

            //2-6,4-8
            //3-76,3-3
            //6-6,4-6
            //5-6,2-5
            //2-5,5-9
            //10,11-8,9
            // Console.WriteLine(line);
            if (Int32.Parse(elfOne[0]) >= Int32.Parse(elfTwo[0])) {
                if (Int32.Parse(elfOne[1]) <= Int32.Parse(elfTwo[0]) || Int32.Parse(elfOne[1]) <= Int32.Parse(elfTwo[1])) {
                    overlap = 1;
                    // Console.WriteLine("Overlap ^^^");
                }
                if (Int32.Parse(elfOne[0]) <= Int32.Parse(elfTwo[1])) {
                    overlap = 1;
                    // Console.WriteLine("Overlap ^^^");
                }
            }
            if (Int32.Parse(elfOne[0]) <= Int32.Parse(elfTwo[0])) {
                if (Int32.Parse(elfOne[1]) >= Int32.Parse(elfTwo[0])  || Int32.Parse(elfOne[1]) >= Int32.Parse(elfTwo[1])) {
                    overlap = 1;
                    // Console.WriteLine("Overlap ^^^");
                }
                // if (Int32.Parse(elfOne[0]) >= Int32.Parse(elfTwo[1])) {
                //     overlap = 1;
                //     // Console.WriteLine("Overlap ^^^");
                // }
            }
            fullOverlap += overlap;
        }  
        return fullOverlap;
    }
}