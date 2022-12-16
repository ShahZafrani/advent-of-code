using System;
  
class Solver {
  
    // Main Method
    static public void Main(String[] args)
    {
        Console.WriteLine("Test sum of the priorities is {0}, expected: 157", SearchRucksacks("test.txt"));  
        Console.WriteLine("sum of the priorities for the puzzle input is {0}", SearchRucksacks("input.txt")); 
        Console.WriteLine("Part 2 --- \n\n\n");
        Console.WriteLine("Test sum of the priorities is {0}, expected: 70", RucksackThrees("test.txt"));  
        Console.WriteLine("sum of the priorities for the puzzle input for Part 2 is {0}", RucksackThrees("input.txt"));  
    }

    // A= ascii 65, Z = ascii 90
    // a = ascii 97, z = ascii 122

    private static int SearchRucksacks(string fileName) {
        int prioritySum = 0;

        foreach (string line in System.IO.File.ReadLines(@fileName))
        {
            byte[] asciiBytes = System.Text.Encoding.ASCII.GetBytes(line);
            var common = 0;
            var secondArray = asciiBytes.Skip(asciiBytes.Length / 2).ToHashSet();
            for (int i = 0; i < asciiBytes.Length / 2; i++) {
                if (secondArray.Contains(asciiBytes[i])) {
                    common = asciiBytes[i];
                    break;
                }
            }
            prioritySum += translateBytesToElfNumber(common);
        }  
        return prioritySum;
    }

    private static int RucksackThrees(string fileName) {
        int prioritySum = 0;
        List<string> elfGroup = new List<string>();

        foreach (string line in System.IO.File.ReadLines(@fileName))
        {
            elfGroup.Add(line);
            if (elfGroup.Count() == 3) {
            prioritySum += getCommon(elfGroup);
            elfGroup.Clear();
            }
        }  
        return prioritySum;
    }

    private static int getCommon(List<string> group) {
        byte[] asciiBytesFirst = System.Text.Encoding.ASCII.GetBytes(group[0]);
        HashSet<byte> asciiBytesSecond = System.Text.Encoding.ASCII.GetBytes(group[1]).ToHashSet();
        HashSet<byte> asciiBytesThird = System.Text.Encoding.ASCII.GetBytes(group[2]).ToHashSet();
        var common = 0;
        List<byte> candidates = new List<byte>();
        for (int i = 0; i < asciiBytesFirst.Length; i++) {
            if (asciiBytesSecond.Contains(asciiBytesFirst[i])) {
                candidates.Add(asciiBytesFirst[i]);
            }
        }        
        for (int i = 0; i < candidates.Count; i++) {
            if (asciiBytesThird.Contains(candidates[i])) {
                common = candidates[i];
                break;
            }
        }
        return translateBytesToElfNumber(common);
    }

    private static int translateBytesToElfNumber(int common) {
        if (common < 91) {
            common -= 38;
        } else {
            common -= 96;
        }
        return common;
    }
    
}