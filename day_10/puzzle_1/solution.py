import sys
import os
import pprint

def main():
    ## Set the variables/constants
    filepath = './input_file'
    ## Increase the recursion limit
    sys.setrecursionlimit(15000)
    global pp, board, start_i, start_j, count_tiles, max_step, steps, first_pass
    pp = pprint.PrettyPrinter(indent=4)
    ## Set the size of the arrays
    rows, cols = (140, 140)
    board = [[0 for i in range(cols)] for j in range(rows)]
    steps = [[0 for i in range(cols)] for j in range(rows)]
    ## Initialize the variables
    start_i, start_j, i, j = (0, 0, 0, 0)
    count_tiles = 0
    max_step = 0
    first_pass = False

    ## Check if the input file exists
    if not os.path.isfile(filepath):
        print("File path {} does not exist. Exiting...".format(filepath))
        sys.exit()
    
    ## Iterate over the file, lne_by_line
    with open(filepath) as fp:
        i = 0
        for line in fp.readlines():
            j = 0
            line = line.strip()
            ## Parse the input
            for ch in line:
                ## Translate the symbols to
                ### incoming/outgoing directions
                match ch:
                    case ".":
                        board[i][j] = ""
                    case "|":
                        board[i][j] = "ns"
                    case "-":
                        board[i][j] = "ew"
                    case "F":
                        board[i][j] = "es"
                    case "7":
                        board[i][j] = "ws"
                    case "L":
                        board[i][j] = "en"
                    case "J":
                        board[i][j] = "wn"
                    ## If an exact match is not confirmed, this last case will be used
                    case _:
                        ## Manually set the starting point symbol
                        ### could be done by code, but not bothered
                        board[i][j] = "ns"
                        start_i = i
                        start_j = j
                j += 1
            i += 1

    ## Pick the two directions of the starting point
    ### and move forward to the next tile
    for dir in board[start_i][start_j]:
        count_tiles = 0
        max_step = 0
        i, j = (start_i, start_j)
        first_pass = not first_pass
        ## Recursive function
        follow_dir(i, j, dir)
        
    # pp.pprint(steps)
    max_step = max(max(steps, key=max))
    print(f"Max tiles: {max_step}")

## Update the steps array, calculate the next move
### and repeat
def follow_dir(i, j, dir):
    global count_tiles
    if not first_pass:
        ## If the tile is already visited, update with the lower value
        if count_tiles < steps[i][j]:
            steps[i][j] = count_tiles
    else:
        ## Update the tile with the current step counter
        steps[i][j] = count_tiles
    count_tiles += 1
    ## Calculate which index need to increase/decrease
    if dir == 'n':
        i -= 1
        rpl = 's'
    if dir == 's':
        i += 1
        rpl = 'n'
    if dir == 'w':
        j -= 1
        rpl = 'e'
    if dir == 'e':
        j += 1
        rpl = 'w'
    ## If the next tile is a dot (.), stop
    if board[i][j] == "":
        return
    ## If the next tile is the starting tile, stop
    if i == start_i and j == start_j:
        return
    ## Remove from the next tile the incoming direction
    next_dir = board[i][j].replace(rpl, '')
    ## Repeat the above with the next tile
    follow_dir(i, j, next_dir)


if __name__ == '__main__':
    main()