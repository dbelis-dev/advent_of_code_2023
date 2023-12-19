import sys
import os
import pprint
import numpy as np
import csv

def main():
    ## Set the variables/constants
    filepath = './input_file.txt'
    pp = pprint.PrettyPrinter(indent=4)
    moves_arr = []
    rows, cols = (500, 500)
    board = [[0 for i in range(cols)] for j in range(rows)]

    ## Check if the input file exists
    if not os.path.isfile(filepath):
        print("File path {} does not exist. Exiting...".format(filepath))
        sys.exit()

    ## Iterate over the file, lne_by_line
    with open(filepath) as fp:
        for line in fp.readlines():
            line = line.strip()
            ## Parse the input
            ### Tokenize on spaces
            dir, moves, colour = line.split(' ')
            colour = colour[2:len(colour)-1]
            moves_arr.append([dir, int(moves), colour])
        ## Iterate over each dig in the arrary
        x, y = (int(rows/2), int(rows/2))
        for step in moves_arr:
            if step[0] == 'U':
                ## keep y, decrease x
                for i in range(step[1] + 1):
                    board[x - i][y] = 1
                x -= i
            if step[0] == 'D':
                ## keep y, increase x
                for i in range(step[1] + 1):
                    board[x + i][y] = 1
                x += i
            if step[0] == 'L':
                ## keep x, decrease y
                for j in range(step[1] + 1):
                    board[x][y - j] = 1
                y -= j
            if step[0] == 'R':
                ## keep yx increase y
                for j in range(step[1] + 1):
                    board[x][y + j] = 1
                y += j

    board_np = np.array(board)
    ones = np.where(board_np == 1)
    pp.pprint(board_np)
    print(ones)
    print(len(ones[0]))
    with open('board_all.csv', 'w', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
        spamwriter.writerows(board)


if __name__ == '__main__':
    main()