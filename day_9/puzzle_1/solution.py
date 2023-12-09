import sys
import os
import pprint

def main():
    ## Set the variables/constants
    filepath = './input_file'
    global pp
    pp = pprint.PrettyPrinter(indent=4)
    histories = []

    ## Check if the input file exists
    if not os.path.isfile(filepath):
        print("File path {} does not exist. Exiting...".format(filepath))
        sys.exit()
    
    ## Iterate over the file, lne_by_line
    with open(filepath) as fp:
        for line in fp.readlines():
            line = line.strip()
            ## Parse the input, convert to int
            histories.append([int(x) for x in line.split(' ')])
    total = 0
    # Iterate over each history
    for hist in histories:
        ## Calculate all subsequent iterations
        ### and return the top-most value
        last_hist = calculate_next(hist)
        ## Add the top-most value to the last element
        total += hist[-1] + last_hist

    print(f"The sum of extrapolated values: {total}")

def calculate_next(history):
    sum = 0
    all_equal = False
    cur_hist = history
    ## Iterate until all values are 0
    while not all_equal:
        next_iter = []
        ## Iterate for all the values in history line
        for i in range(len(cur_hist) - 1):
            ## Calculate the difference
            calc_value = cur_hist[i + 1] - cur_hist[i]
            ## Add the value to next line
            next_iter.append( calc_value )
            ## If all values are 0, set flag
            if calc_value == 0:
                all_equal = True
            else:
                all_equal = False
        ## Add the last element to the total
        sum += next_iter[-1]
        ## Swap arrays: current is next line, and repeat
        cur_hist = next_iter
    ## Return the total of all last elements per history line
    return sum


if __name__ == '__main__':
    main()