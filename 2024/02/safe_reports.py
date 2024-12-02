import sys
def open_file(name):
    file1 = open(name, 'r') 
    return file1.readlines() 

# Part 1
def check_report_safety(lines):
    safe = 0
    for line in lines:
        vals = line.split()
        if int(vals[0]) < int(vals[1]):
            safe += check_grad_diffs(vals, -4, -1)
        elif int(vals[0]) > int(vals[1]):
            safe += check_grad_diffs(vals, 0, 3)
        else:
            pass
    return safe

def check_grad_diffs(line, lower_limit, upper_limit):
    for i in range(len(line) - 1):
        diff = int(line[i]) - int(line[i + 1])
        if diff > lower_limit and diff <= upper_limit:
            pass
        else: 
            return 0
    return 1

# Part 2

def check_report_safety_with_damper(lines):
    safe = 0
    for line in lines:
        vals = line.split()
        safe_decreasing = check_grad_diffs_with_damper(vals.copy(), 0, 3, list(range(len(vals))))
        # I wasted all that time removing values in case it was decreasing
        # but I haven't checked if it was increasing yet
        if safe_decreasing is 0:
            safe += check_grad_diffs_with_damper(vals.copy(), -4, -1, list(range(len(vals))))
        else:
            safe += safe_decreasing
    return safe

def check_grad_diffs_with_damper(input_line, lower_limit, upper_limit, indexes_left_to_remove):
    line = input_line.copy()
    line_len = len(line) - 1
    level_removed = False
    i = 0
    while i < line_len:
        diff = int(line[i]) - int(line[i + 1])
        if diff > lower_limit and diff <= upper_limit:
            i += 1
            pass
        # if I haven't tried removing any values here...
        elif level_removed is False and len(indexes_left_to_remove) > 0: 
            index_to_remove = indexes_left_to_remove.pop(0)
            print("removing {} from {}".format(line[index_to_remove], line))
            line.pop(index_to_remove)
            line_len -= 1
            level_removed = True
            i = 0
            pass
        # I've tried removing a value but there's other values I haven't tried removing.
        elif len(indexes_left_to_remove) > 0:
            return check_grad_diffs_with_damper(input_line, lower_limit, upper_limit, indexes_left_to_remove)
        # I've tried removing every value once and this still doesn't pass
        else:
            return 0
    print("line {} deemed safe".format(line))
    return 1


if __name__=="__main__":
    print(sys.argv)
    # add test after `python3 file.py` to run the test file
    if len(sys.argv) > 1:
        filename = "test_input.txt"
    else:
        filename = "input.txt"
    print("day 2: reactor safety reports")
    input = open_file(filename)
    num_safe = check_report_safety(input)
    print("test part 1 output should = 2")
    print("part 1 output: \n\t{}".format(num_safe))
    print("\npart 2\n")
    dampened_safe = check_report_safety_with_damper(input)
    print("part 2 test output should be 4")
    print("part 2 output: \n\t{}".format(dampened_safe))