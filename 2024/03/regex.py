import sys
import re

def openFile(name, pattern):
    with open(name, 'r') as file:
        data = re.findall(pattern, file.read())
    return data

# Part 1
def mul(cmd):
    # ex: mul(8,5) -- remove mul( and end parentheses
    # print(cmd)
    nums = cmd[4:-1].split(",")
    return int(nums[0]) * int(nums[1])

# Part 2
def remove_donts(cmds):
    do_these = []
    is_do = True
    for cmd in cmds:
        # print("isdo: {}, cmd: {}".format(is_do, cmd))
        if is_do is True:
            if cmd[0:3] == "mul":
                do_these.append(cmd)
            elif cmd[0:5] == "don't":
                is_do = False
            # else:
                # print("edge case!!! \n\t{}".format(cmd))
        else:
            if cmd[0:3] == "do(":
                is_do = True
    return do_these


if __name__=="__main__":
    print(sys.argv)
    # add test after `python3 file.py` to run the test file
    if len(sys.argv) > 1:
        filename = "test_input.txt"
    else:
        filename = "input.txt"
    print("day 3: multiplying regex matches")
    part_1_pattern = re.compile("mul\(\d+,\d+\)")
    part_1_cmds = openFile(filename, part_1_pattern)
    # print(part_1_cmds)
    multiplied_instructions = sum(map(lambda x: mul(x), part_1_cmds))
    print("test part 1 output should = 161")
    print("part 1 output: \n\t{}".format(multiplied_instructions))
    if len(sys.argv) > 1:
        filename = "test_input_2.txt"
    else:
        filename = "input.txt"
    part_2_pattern = re.compile("do\(\)|mul\(\d+,\d+\)|don't\(\)")
    part_2_cmds = openFile(filename, part_2_pattern)
    multiplied_validated_instructions = sum(map(lambda x: mul(x), remove_donts(part_2_cmds)))
    print("part 2 output: \n\t{}".format(multiplied_validated_instructions))