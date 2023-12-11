import sys
import os
import pprint
import numpy as np

def main():
    ## Set the variables/constants
    filepath = './input_file'
    pp = pprint.PrettyPrinter(indent=4)
    ## Set the size of the arrays
    orig_arr = []
    row_to_expand = []
    col_to_expand = []

    ## Check if the input file exists
    if not os.path.isfile(filepath):
        print("File path {} does not exist. Exiting...".format(filepath))
        sys.exit()
    
    ## Iterate over the file, lne_by_line
    with open(filepath) as fp:
        for line in fp.readlines():
            line = line.strip()
            ## Parse the input
            orig_arr.append([c for c in line])
    ## Find lines with no galaxies
    for i in range(len(orig_arr)):
        if '#' not in orig_arr[i]:
            row_to_expand.append(i)
    for j in range(len(orig_arr[0])):
            col = []
            for i in range(len(orig_arr)):
                col.append(orig_arr[i][j])
            if '#' not in col:
                col_to_expand.append(j)

    ## Expand the original board with the above findings
    new_row = ['.' for i in range(len(orig_arr))]
    orig_arr = np.insert(orig_arr, row_to_expand, new_row, axis=0)
    new_col = ['.' for i in range(len(orig_arr))]
    _new_col = np.array(new_col).reshape((len(orig_arr), 1))
    orig_arr = np.insert(orig_arr, col_to_expand, _new_col, axis=1)
    ## Identify the galaxies
    galaxy = 1
    galaxies_dict = {}
    for i in range(len(orig_arr)):
        tup = []
        f = np.where(orig_arr[i] == '#')
        ## If a galaxy is found, add its indices
        for x in f[0]:
            tup.append((i,x))
        if tup:
            ## Add the indices for each galaxy
            for g in tup:
                galaxies_dict[galaxy] = g
                galaxy += 1
    ## Calculate all pairs
    dist = 0
    for gal, pos in galaxies_dict.items():
        gal_rng = range(gal + 1, len(galaxies_dict) + 1)
        for next_gal in gal_rng:
            next_pos = galaxies_dict[next_gal]
            dist += calculate_distance(pos, next_pos)
    # pp.pprint(galaxies_dict)
    print(f"The sum of the lengths: {dist}")

def calculate_distance(pos, next_pos):
    dist = 0
    pos_i, pos_j = pos
    next_pos_i, next_pos_j = next_pos
    ## Check if they are in the same row
    if pos_i == next_pos_i:
        dist = abs(next_pos_j - pos_j)
        return dist
    ## Check if they are in the same column
    if pos_j == next_pos_j:
        dist = abs(next_pos_i - pos_i)
        return dist
    ## Calculate diagonals
    dist = abs(next_pos_j - pos_j) + abs(next_pos_i - pos_i) 
    return dist
    

if __name__ == '__main__':
    main()