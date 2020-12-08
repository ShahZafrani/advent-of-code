import re 

isDebug = False

def debug(text):
    if isDebug is True:
        print(text)

def openFile(name, pattern):
    with open(name, 'r') as file:
        data = re.split(pattern, file.read())
    return data

if __name__=="__main__":
    print("day 6: customs")
    lines = openFile("input.txt", "\n\n")
    print(sum(map(lambda x : len(set(x.replace("\n", ""))), lines)))

    

