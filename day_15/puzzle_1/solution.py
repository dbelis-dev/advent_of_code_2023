import sys
import os

def main():
    ## Set the variables/constants
    filepath = './input_file.txt'

    ## Check if the input file exists
    if not os.path.isfile(filepath):
        print("File path {} does not exist. Exiting...".format(filepath))
        sys.exit()

    ## Iterate over the file, lne_by_line
    with open(filepath) as fp:
        for line in fp.readlines():
            line = line.strip()
            ## Parse the input
            ### Tokenize on commas
            curr_seq = line.split(',')
            sum = 0
            for seq in curr_seq:
                curr_val = 0
                for ch in seq:
                    ascii = ord( ch )
                    curr_val += ascii
                    curr_val *= 17
                    curr_val = curr_val % 256
                sum += curr_val
            
        print(f"Total sum of the results: {sum}")


if __name__ == '__main__':
    main()