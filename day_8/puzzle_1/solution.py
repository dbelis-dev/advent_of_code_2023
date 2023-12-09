import sys
import os
import pprint

def main():
    ## Set the variables/constants
    filepath = './input_file'
    pp = pprint.PrettyPrinter(indent=4)
    global directions, nodes
    directions = []
    nodes = {}

    ## Check if the input file exists
    if not os.path.isfile(filepath):
        print("File path {} does not exist. Exiting...".format(filepath))
        sys.exit()
    
    cnt = 0
    ## Iterate over the file, lne_by_line
    with open(filepath) as fp:
        for line in fp.readlines():
            line = line.strip()
            ## Parse the input
            if line == '':
                continue
            if cnt == 0:
                directions = line
                cnt = 1 
            else:
                node, l_r_node = line.split(' = ')
                l_r_node = l_r_node.replace('(','').replace(')','')
                left, right = l_r_node.split(', ')
                nodes[node] = [left, right]
    # pp.pprint(directions)
    # pp.pprint(nodes)
    steps = 0
    found = False
    ## Get first node
    # next_node = list(nodes.keys())[0]
    next_node = 'AAA'
    print(f"Starting from node: {next_node}")
    ## Set last node
    end_node = 'ZZZ'
    while not found:
        ## Iterate over all the direction instructions
        for dir in directions:
            steps += 1
            ## Get the next node, based on current and the direction
            next_node = get_next(next_node, dir)
            ## If reached the last node, finish
            if next_node == end_node:
                found = True
                break
    
    print(f"Steps required to reach node {end_node}: {steps}")


def get_next(node, dir):
    ## Split the directions in left and right
    lf, rg = nodes[node]
    ## Keep the appropriate direction
    if dir == 'R':
        next_node = rg
    else:
        next_node = lf
    # print(f"Next node: {next_node}")
    return next_node


if __name__ == '__main__':
    main()