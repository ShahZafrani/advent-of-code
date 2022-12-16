# 2022 AoC Journal

## Days 1 and 2:
I started these a week late and decided to use dotnet 7 as a means to help get more comfortable with the tech I'm supposed to use at MSFT.

## Day 3:
I have decided to a class based approach.

## Day 4:
I am creating a template to use in the dotnet cli so that I can generate a Solver Implementation with methods already in place to read in puzzle input and solve parts 1 and 2. The goal is to have a Solver Interface with methods that need to be implemented. 

tutorial followed: https://learn.microsoft.com/en-us/dotnet/core/tutorials/cli-templates-create-item-template 
The /test and /working folders are used for the extensions. 

-- Giving up on interface for now since I have no wifi to look things up. 

Had trouble with Part 1 where my answer was too low but my test was passing. The undetected overlap was "3-76,3-3" and the that failed to pick it up was:
```
    public int Solve(string fileName) {
        int fullOverlap = 0;
        foreach (string line in System.IO.File.ReadLines(@fileName))
        {
            string[] elfAssignments = line.Split(',');
            string[] elfOne = elfAssignments[0].Split('-');
            string[] elfTwo = elfAssignments[1].Split('-');

            //3-76,3-3
            // Console.WriteLine(line);
            if (Int32.Parse(elfOne[0]) >= Int32.Parse(elfTwo[0])) {
                if (Int32.Parse(elfOne[1]) <= Int32.Parse(elfTwo[1])) {
                    fullOverlap +=1;
                    // Console.WriteLine("Overlap ^^^");
                }
            } else if (Int32.Parse(elfOne[0]) <= Int32.Parse(elfTwo[0])) {
                if (Int32.Parse(elfOne[1]) >= Int32.Parse(elfTwo[1])) {
                    fullOverlap +=1;
                    // Console.WriteLine("Overlap ^^^");
                }
            }
        }  
        return fullOverlap;
    }
```

Because of the "else if" clause my logic was able to detect an overlap for "6-6,4-6" but not "3-76,3-3". I added the new input to my test case and verified the bug was fixed before checking if it was correct. Currently I'm on a plane in taxi waiting to take off so I had to submit the answer via my cell phone to see if it was correct. 



