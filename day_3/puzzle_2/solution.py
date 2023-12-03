import sys
import os
import pprint

def main():
    ## Set the variables/constants
    filepath = './input_file'
    global pp, rows, cols, input_array
    pp = pprint.PrettyPrinter(indent=4)
    rows = 140
    cols = 140
    input_array = [[0 for j in range(cols)] for i in range(rows)]

    ## Check if the input file exists
    if not os.path.isfile(filepath):
        print("File path {} does not exist. Exiting...".format(filepath))
        sys.exit()
    
    ### Read the input into an array of integers
    read_array_in(filepath, cols, input_array)
    # pp.pprint(input_array)
    find_gears()

def find_gears():
    total = 0
    for i in range(rows):
        for j in range(cols):
            if input_array[i][j] == '*':
                parts = calculate_window(i, j)
                total += int(list(parts)[0]) * int(list(parts)[1])
    
    print(f"Total: {total}")

def calculate_window(row, col):
    global top, bottom, left, right
    top = 0
    bottom = rows-1
    left = 0
    right = cols-1
    ## Check if above is out of limits
    if row > 0:
        top = row - 1
    ## Check if below is out of limits
    if row+1 < rows:
        bottom = row + 1
    ## Check if previous is out of limits
    if col > 0:
        left = col - 1
    ## Check if next is out of limits
    if col+1 < cols:
        right = col + 1
    return scan_for_gears(top, bottom, left, right)

def scan_for_gears(top, bottom, left, right):
    parts_set = set()
    for i in range(top, bottom+1):
        for j in range(left, right+1):
            if input_array[i][j].isnumeric():
                find_part_number(i, j, parts_set)
    # pp.pprint(parts_set)
    if (len(parts_set) == 1):
        parts_set.add("0")
    return parts_set

def find_part_number(row, col, array):
    part_digit = ""
    part_digit += input_array[row][col]
    k = col+1
    while input_array[row][k].isnumeric():
        ## add digit to the left
        part_digit += input_array[row][k]
        k += 1
        if k == cols:
            break

    k = col-1
    while input_array[row][k].isnumeric():
        ## add digit to the left
        part_digit = input_array[row][k] + part_digit
        k -= 1
    array.add(part_digit)

### Iterate over the lines in the file
def read_array_in(filepath, cols, array):
    row = 0
    with open(filepath, 'r') as fp:
        for line in fp.readlines():
            fill_array(cols, row, line, array)
            row += 1

### Read each char and add it to the array
def fill_array(cols, row, line, array):
    for col in range(cols):
        char_in = line[col]
        if char_in == '\n':
            # print("End of line")
            return
        array[row][col] = char_in


if __name__ == '__main__':
    main()