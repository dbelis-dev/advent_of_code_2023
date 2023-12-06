import sys
import os
import pprint

def main():
    ## Set the variables/constants
    filepath = './input_file'
    times  = 0
    distances = 0
    mid_time = 0
    total_wins = 0

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
            header[1] = header[1].replace(" ", "")
            ## Assign values to appropriate variable
            if header[0] == "Time":
                times = int(header[1])
            if header[0] == "Distance":
                distances = int(header[1])

    total = times
    mid_time = int(total / 2)
    ## For all the values, from mid to last
    for t in range(mid_time, total):
        ## Find the distance greater than the current one
        travelled_dist = calc_dist(t,total)
        if travelled_dist > distances:
            ## Count each of these greater disatnces
            total_wins +=1
        else:
            break

    ## For all the values, from 0 to mid
    for t in range(mid_time-1, 0, -1):
        ## Find the distance greater than the current one
        travelled_dist = calc_dist(t,total)
        if travelled_dist > distances:
            ## Count each of these greater distances
            total_wins +=1
        else:
            break
    
    print(f"Number of ways you can beat the record: {total_wins}")

## Calculate the travelled distance,
### given the hold time and the max time
def calc_dist(time_hold, time_total):
    return (time_total - time_hold) * time_hold
    

if __name__ == '__main__':
    main()