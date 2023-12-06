import dis
import sys
import os
import pprint
import re

def main():
    ## Set the variables/constants
    filepath = './input_file'
    times  = []
    distances = []
    wins = 0
    total_wins = 1

    ## Check if the input file exists
    if not os.path.isfile(filepath):
        print("File path {} does not exist. Exiting...".format(filepath))
        sys.exit()
    
    ## Iterate over the file, lne_by_line
    with open(filepath) as fp:
        for line in fp.readlines():
            line = line.strip()
            ## Parse the input
            header = line.split(':')
            ## Remove multiple spaces
            header[1] = re.split(r'\s{2,}', header[1].strip())
            ## Convert string values to int
            header[1] = list(map(int, header[1]))
            ## Assign values to appropriate array
            if header[0] == "Time":
                times = header[1]
            if header[0] == "Distance":
                distances = header[1]

    ## Iterate over the times array 
    for i in range(len(times)):
        total = times[i]
        ## For all the values, from 0 to value
        for t in range(total):
            ## Find the distance greater than the current one
            travelled_dist = calc_dist(t,total)
            if travelled_dist > distances[i]:
                ## Count each of these greater distances
                wins +=1
        ## Sum up all the wins
        total_wins *= wins
        wins = 0
    
    print(f"Number of ways you can beat the record: {total_wins}")

## Calculate the traveled distance,
### given the hold time and the max time
def calc_dist(time_hold, time_total):
    return (time_total - time_hold) * time_hold
    

if __name__ == '__main__':
    main()