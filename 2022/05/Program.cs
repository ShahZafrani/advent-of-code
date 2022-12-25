class Advent {
    static public void Main(String[] args)
    {
        Solver Part1 = new Solver("5, CrateMover 9000", "CMZ", false);
        Part1.Run();
        Solver Part2 = new Solver("5, CrateMover 9001", "MCD", true);
        Part2.Run();
    }
}
