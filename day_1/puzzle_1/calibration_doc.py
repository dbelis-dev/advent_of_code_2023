import sys
import os

def main():
    ## Set the variables/constants
    filepath = './input_file'
    total_cal_value = 0

    ## Check if the input file exists
    if not os.path.isfile(filepath):
        print("File path {} does not exist. Exiting...".format(filepath))
        sys.exit()

    ## Iterate over the file, lne-by-line
    with open(filepath) as fp:
        for line in fp.readlines():
            line = line.strip()
            found_first = False
            first_digit = 0
            found_last = False
            last_digit = 0
            ## Iterate over the characters of the string
            for i in range(len(line)):
                ## If it's numeric and not the first
                if ( line[i].isnumeric() and not found_first):
                    first_digit = int(line[i])
                    found_first = True
                ## If it's numeric and not the last
                if ( line[len(line) -1 -i].isnumeric() and not found_last):
                    last_digit = int(line[len(line) -1 -i])
                    found_last = True
            ## Add the first and last values to the total
            total_cal_value += (first_digit*10 + last_digit)
    print(f"Total Calibration Value: {total_cal_value}")

if __name__ == '__main__':
    main()