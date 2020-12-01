def openFile(name):
    file1 = open(name, 'r') 
    return file1.readlines() 

def getProductOfNumsThatMakeSum(sumNum, lines):
    notFound = True
    while(notFound):
        for i in range(len(lines)):
            for j in range(len(lines)):
                for k in range(len(lines)):
                    a = int(lines[i])
                    b = int(lines[j])
                    c = int(lines[k])
                    sum1 = a + b + c
                    if  sum1 == sumNum:
                        print("{} + {} + {} = {}".format(a, b, c, sumNum))
                        print("{} * {} * {} = {}".format(a,b,c, a*b*c))
                        notFound=False
                        return

if __name__=="__main__":
    print("day 1: expense reports")
    lines = openFile("input.txt")
    print("input is {} lines long".format(len(lines)))
    getProductOfNumsThatMakeSum(2020, lines)