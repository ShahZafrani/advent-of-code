using System.Text;

public class Solver {
    private string day;
    private string expectedTestOutput;
    private bool newModel;
    private string testFileName;
    private string inputFileName;
    public Solver(string day, string expectedTestOutput, bool newModel, string testFileName = "test.txt", string inputFileName = "input.txt") {
        this.day = day;
        this.expectedTestOutput = expectedTestOutput;
        this.newModel = newModel;
        this.testFileName = testFileName;
        this.inputFileName = inputFileName;
    }
    public void Run() {
        Console.WriteLine("Solving day {0}", this.day);
        Console.WriteLine("Test Output: {1}, expected: {0}", this.expectedTestOutput, Solve(this.testFileName, this.newModel));
        Console.WriteLine("\nSovled output: {0}", Solve(this.inputFileName, this.newModel));
    }
    public string Solve(string fileName, bool newModel) {
        CargoManifest manifest = loadCargoMap(fileName, newModel);
        StringBuilder stackPrinter = new StringBuilder();
        manifest.getFinalConfiguration();
        foreach (Stack<char> stack in manifest.cargo)
        {
            stackPrinter.Append(stack.Pop());
        }
        return stackPrinter.ToString();
    }

    private CargoManifest loadCargoMap(string fileName, bool newModel) {
        var lines = System.IO.File.ReadLines(@fileName);
        string first = lines.First();
        Stack<char>[] cargo = new Stack<char>[(first.Length / 4) + 1];
        for (int i = 0; i < cargo.Length; i ++) {
            cargo[i] = new Stack<char>();
        }
        Console.WriteLine("Number of crates for {0} is {1}", fileName, cargo.Length);
        string[] separatingStrings = {"move", "from", "to"};
        List<Instruction> instructions = new List<Instruction>();
        bool cargoLoaded = false;
        foreach (string line in lines) {
            if (cargoLoaded == false) {
                if (line.Length == 0) {
                    // reverse all the stacks 
                    for (int i = 0; i < cargo.Length; i ++) {
                    Stack<char> reversedCargo = new Stack<char>();
                        while (cargo[i].Count != 0) {
                            reversedCargo.Push(cargo[i].Pop());
                        }
                        cargo[i] = reversedCargo;
                    }
                    cargoLoaded = true;
                } else {
                    for (int i  = 0; i < line.Length; i++) {
                        if (System.Char.IsLetter(line[i])) {
                            // Console.WriteLine("{0}, in stack {1}", line[i], i/4);
                            cargo[i / 4].Push(line[i]);
                        }
                    }
                }
            } else {
                string[] pieces = line.Split(separatingStrings, System.StringSplitOptions.RemoveEmptyEntries);
                instructions.Add(new Instruction(Int32.Parse(pieces[0]), Int32.Parse(pieces[1]) -1, Int32.Parse(pieces[2])-1));
            }
        }
        return new CargoManifest(cargo, instructions, newModel);
    }
    class CargoManifest {
        public Stack<char>[] cargo;
        public List<Instruction> instructions;
        private bool newModel;
        public CargoManifest(Stack<char>[] cargo, List<Instruction> instructions, bool newModel) {
            this.cargo = cargo;
            this.instructions = instructions;
            this.newModel = newModel;
        }
        public void getFinalConfiguration() {
            foreach (Instruction i in this.instructions) {
                this.executeInstruction(i);
            }
        }
        private void executeInstruction(Instruction instruction) {
            if (this.newModel == false) {
                for (int i = 0; i < instruction.amount; i ++) {
                    this.cargo[instruction.to].Push(this.cargo[instruction.from].Pop()); 
                }
            } else {
                    Stack<char> intermediate = new Stack<char>();
                    for (int i = 0; i < instruction.amount; i ++) { 
                        intermediate.Push(this.cargo[instruction.from].Pop());
                    }
                    for (int i = 0; i < instruction.amount; i ++) { 
                        this.cargo[instruction.to].Push(intermediate.Pop());
                    }
            }
        }
    }
    class Instruction {
        public int amount, from, to;
        public Instruction(int amount, int from, int to) {
            this.amount = amount;
            this.from = from;
            this.to = to;
        }

    }
}