import sys
import re

def open_file(name):
    file1 = open(name, 'r') 
    return file1.readlines() 

directional_vectors = [
    (1,0),
    (-1,0),
    (0,1),
    (1,1),
    (-1,1),
    (0,-1),
    (1,-1),
    (-1,-1)
    ]
diagonal_vectors = [
    (1,1),
    (-1,1),
    (1,-1),
    (-1,-1)
    ]

def checkRemainingVector(vector, pos, remaining_letters, grid):
    if len(remaining_letters) == 0:
        return 1
    new_y = pos[0] + vector[0]
    new_x = pos[1] + vector[1]
    # check bounds first
    if(new_y >= 0 and new_y < len(grid)):
        if (new_x >=0 and new_x < len(grid[0])):
            if remaining_letters[0] == grid[new_y][new_x]:
                remaining_letters.pop(0)
                return checkRemainingVector(vector, (new_y, new_x), remaining_letters, grid)
    return 0

def checkForX(grid):
    xmas_found = 0
    for row in range(len(grid)):
        for column in range(len(grid[row])):
            if grid[row][column] == "X":
                # check all vectors for remaining
                for vector in directional_vectors:
                    xmas_found += checkRemainingVector(vector, (row, column), ['M', 'A', 'S'], grid)
    return xmas_found

def get_letter(vector, pos, grid):
    new_y = pos[0] + vector[0]
    new_x = pos[1] + vector[1]
    # check bounds first
    if(new_y >= 0 and new_y < len(grid)):
        if (new_x >=0 and new_x < len(grid[0])):
            return grid[new_y][new_x]
    return "."

def checkForMasX(grid):
    masx_found = 0
    for row in range(len(grid)):
        for column in range(len(grid[row])):
            if grid[row][column] == "A":
                # check all vectors for remaining values
                found_letters = {}
                for vector in diagonal_vectors:
                    found_letters["{}:{}".format(vector[0], vector[1])] = get_letter(vector, (row, column), grid)
                # print(found_letters.values())
                # check all four possible X shapes
                if ((found_letters["1:1"] == "S" and found_letters["-1:-1"] == "M") and (found_letters["-1:1"] == "S" and found_letters["1:-1"] == "M")):
                    masx_found += 1
                elif ((found_letters["1:1"] == "S" and found_letters["-1:-1"] == "M") and (found_letters["-1:1"] == "M" and found_letters["1:-1"] == "S")):
                    masx_found += 1
                elif ((found_letters["1:1"] == "M" and found_letters["-1:-1"] == "S") and (found_letters["-1:1"] == "M" and found_letters["1:-1"] == "S")):
                    masx_found += 1
                elif ((found_letters["1:1"] == "M" and found_letters["-1:-1"] == "S") and (found_letters["-1:1"] == "S" and found_letters["1:-1"] == "M")):
                    masx_found += 1
    return masx_found

def loadGrid(file):
    grid = []
    for line in file:
        row = [letter for letter in line if letter != "\n"]
        grid.append(row)
    return grid

if __name__=="__main__":
    print(sys.argv)
    # add test after `python3 file.py` to run the test file
    if len(sys.argv) > 1:
        filename = "test_input.txt"
    else:
        filename = "input.txt"
    print("day 4: word search")
    file = open_file(filename)
    grid = loadGrid(file)
    # print(grid)
    print("part 1 test answer should be 18\n\tanswer={}".format(checkForX(grid)))

    print("part 2 test answer should be 9\n\tanswer={}".format(checkForMasX(grid)))