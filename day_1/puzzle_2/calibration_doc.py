import sys
import os

def main():
    ## Set the variables/constants
    filepath = './input_file'
    digits_found = {}
    total_cal_value = 0
    wordtodigit = {
            "one" : 1,
            "two" : 2,
            "three" : 3,
            "four" : 4,
            "five" : 5,
            "six" : 6,
            "seven" : 7,
            "eight" : 8,
            "nine" : 9,
            "1" : 1,
            "2" : 2,
            "3" : 3,
            "4" : 4,
            "5" : 5,
            "6" : 6,
            "7" : 7,
            "8" : 8,
            "9" : 9,
        }

    ## Check if the input file exists
    if not os.path.isfile(filepath):
        print("File path {} does not exist. Exiting...".format(filepath))
        sys.exit()

    ## Iterate over the file, lne-by-line
    with open(filepath) as fp:
        for line in fp.readlines():
            digits_found = {}
            line = line.strip()
            ## Iterate over the characters of the string
            for i in range(len(line)):
                for key, value in wordtodigit.items():
                    ## Check if any of lookup dictionary words exist in the string
                    ## moving the start index
                    if (line.find(key, i) == i):
                        ## once found, add it to the new dictionary
                        digits_found[i] = value
            ## Add the first and last entries of the dictionary to the total
            total_cal_value += list(digits_found.values())[0]*10 + list(digits_found.values())[-1]

    print(f"Total Calibration Value: {total_cal_value}")

if __name__ == '__main__':
    main()