import array
import sys
import os
import pprint


def main():
    ## Set the variables/constants
    filepath = './input_file.txt'
    pp = pprint.PrettyPrinter(indent=4)
    ## Define the arrays
    global rocks_arr, plot_q
    rocks_arr = []
    plot_q = []

    ## Check if the input file exists
    if not os.path.isfile(filepath):
        print("File path {} does not exist. Exiting...".format(filepath))
        sys.exit()

    ## Iterate over the file, lne_by_line
    with open(filepath) as fp:
        i = 0
        for line in fp.readlines():
            line = line.strip()
            j = 0
            ## Parse the input
            for ch in line:
                ## Check for rocks
                ### keep their coords
                if ch == "#":
                    rocks_arr.append( (i,j) )
                ## Check for starting point
                ### keep its coords
                if ch == "S":
                    plot_q.append( (i,j) )
                j += 1
            i += 1
    ## Start the iterations from starting point
    pp.pprint(plot_q)
    max_iter = 64
    count = 0
    while count < max_iter:
        steps = len(plot_q)
        for step in range(steps):
            ## Pop first element in the queue
            current_plot = plot_q.pop(0)
            ## Identify all the possible plots around the current one
            find_possible_plot(current_plot)
        count += 1

    print(f"Number of garden plots the Elf reaches in exactly 64 steps: {len(plot_q)}")

## Identify all the possible plots on N,E,S,W
### Add the ones that are not rocks, but also not in the queue already
def find_possible_plot(current_plot):
    x,y = current_plot
    if ((x+1,y) not in rocks_arr) and ((x+1,y) not in plot_q):
        plot_q.append( (x+1,y) )
    if ((x,y+1) not in rocks_arr) and ((x,y+1) not in plot_q):
        plot_q.append( (x,y+1) )
    if ((x-1,y) not in rocks_arr) and ((x-1,y) not in plot_q):
        plot_q.append( (x-1,y) )
    if ((x,y-1) not in rocks_arr) and ((x,y-1) not in plot_q):
        plot_q.append( (x,y-1) )


if __name__ == '__main__':
    main()