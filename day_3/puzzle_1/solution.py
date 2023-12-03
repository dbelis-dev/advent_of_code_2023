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
    find_parts()

def find_parts():
    part_digit = ""
    is_part = False
    total = 0
    for i in range(rows):
        for j in range(cols):
            if input_array[i][j].isnumeric():
                part_digit += input_array[i][j]
                if not is_part:
                    is_part = calculate_window(i,j)
            else:
                if is_part and part_digit:
                    total += int(part_digit)
                part_digit = ""
                is_part = False
    print(f"Total: {total}")

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
    return scan_for_symbol(top, bottom, left, right)

def scan_for_symbol(top, bottom, left, right):
    for i in range(top, bottom+1):
        for j in range(left, right+1):
            if input_array[i][j] == '.':
                continue
            elif input_array[i][j].isnumeric():
                continue
            else:
                return True
    return False


if __name__ == '__main__':
    main()