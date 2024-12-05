import sys
import functools

def open_file(name):
    file1 = open(name, 'r') 
    return file1.readlines() 

def parse_input(lines):
    maps = {}
    updates = []
    for line in lines:
        if "|" in line:
            pages = line.strip().split("|")
            if maps.get(pages[1]):
                maps[pages[1]].append(pages[0])
            else:
                maps[pages[1]] = [pages[0]]
        elif len(line) < 2:
            pass
        else:
            updates.append(line.strip().split(","))
    return maps, updates

def get_valid_manual(maps, update):
    for i, val in enumerate(update):
        for num in update[:i]:
            if val in maps[num]:
                return False
    return True

def sort_by_precedence(x, y, maps):
    if x in maps[y]:
        return -1
    return 1

if __name__=="__main__":
    # add test after `python3 file.py` to run the test file
    filename = "test_input.txt" if len(sys.argv) > 1 else "input.txt"
    print("day 5: trees or maps?")
    maps, updates = parse_input(open_file(filename))
    valid_manuals = sum([int(manual[int(len(manual)/2)]) for manual in updates if get_valid_manual(maps, manual) == True])
    print("test output should be 143\n\toutput: {}".format(valid_manuals))
    repaired = [sorted(manual, key=functools.cmp_to_key(lambda x, y: sort_by_precedence(x, y, maps))) for manual in updates if get_valid_manual(maps, manual) == False]
    print("part 2\n\n\ntest output should be 123\n\t{}".format(sum([int(manual[int(len(manual)/2)]) for manual in repaired])))