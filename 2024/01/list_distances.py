import sys
def open_file(name):
    file1 = open(name, 'r') 
    return file1.readlines() 

def split_lists(lines):
    left, right = [], []
    for line in lines:
        split_line = line.split()
        left.append(int(split_line[0]))
        right.append(int(split_line[1]))
    return sorted(left), sorted(right)

def map_occurance_of_list_items(lines):
    left = []
    right = {}
    for line in lines:
        split_line = line.split()
        left.append(int(split_line[0]))
        if right.get(int(split_line[1])) is not None:
            right[int(split_line[1])] += 1
        else:
            right[int(split_line[1])] = 1
    return left, right

if __name__=="__main__":
    print(sys.argv)
    # add test after `python3 file.py` to run the test file
    if len(sys.argv) > 1:
        filename = "test_input.txt"
    else:
        filename = "input.txt"
    print("day 1: list distance calculation")
    input = open_file(filename)
    left, right = split_lists(input)
    print("part 1 puzzle output = \n\t{}".format(sum(map(lambda xy: abs(xy[0] - xy[1]), zip(left, right)))))
    print("\n\n\nPart 2\n")
    left_list, right_dict = map_occurance_of_list_items(input)
    print("part 2 puzzle output: {}".format(sum(map(lambda x: x * right_dict.get(x, 0), left_list))))