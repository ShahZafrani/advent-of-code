List<int> elves = new List<int>();
// Read the file and display it line by line.  
int current = 0;
int max = 0;
int second = 0;
int third  = 0;
foreach (string line in System.IO.File.ReadLines(@"input.txt"))
{
    var trimmedLine = line.Trim();
    if (trimmedLine == "") {
        if (current > max) {
            max = current;
        } else if (current > second) {
            second = current;
        } else if (current > third) {
            third = current;
        }
        current = 0;
        continue;   
    } else {
        current += Int32.Parse(trimmedLine);
    }
}  
  
System.Console.WriteLine("The greediest elves have {0} calories", max + second + third);  
