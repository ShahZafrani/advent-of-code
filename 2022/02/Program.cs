var scoreguide = new Dictionary<string, int>
{
    { "A X", 4 }, 
    { "A Y", 8 }, 
    { "A Z", 3 }, 
    { "B X", 1 }, 
    { "B Y", 5 }, 
    { "B Z", 9 }, 
    { "C X", 7 }, 
    { "C Y", 2 }, 
    { "C Z", 6 }
};
// (1 for Rock, 2 for Paper, and 3 for Scissors) plus the score for the outcome of the round (0 if you lost, 3 if the round was a draw, and 6 if you won).
//  A for Rock, B for Paper, and C for Scissors.
//  X for Rock, Y for Paper, and Z for Scissors.



// The Elf finishes helping with the tent and sneaks back over to you. "Anyway, the second column says how the round needs to end:
// X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win. Good luck!"
var part2ScoreGuide = new Dictionary<string, int>
{
    { "A X", 3 },  
    { "A Y", 4 }, 
    { "A Z", 8 }, 
    { "B X", 1 }, 
    { "B Y", 5 }, 
    { "B Z", 9 }, 
    { "C X", 2 }, 
    { "C Y", 6 }, 
    { "C Z", 7 }
};
int score = 0;
foreach (string line in System.IO.File.ReadLines(@"input.txt"))
{
    score += part2ScoreGuide[line];
}  
  
System.Console.WriteLine("your Rock Paper Scissors Score would be {0}", score);  
