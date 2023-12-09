import sys
import os
import pprint

def main():
    ## Set the variables/constants
    filepath = './input_file'
    pp = pprint.PrettyPrinter(indent=4)
    global directions, nodes, a_nodes
    directions = []
    nodes = {}
    a_nodes = []
    found = ""

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
                if node[-1:] == 'A':
                    a_nodes.append(node)

    # pp.pprint(a_nodes)
    # pp.pprint(directions)
    # pp.pprint(nodes)
    steps = 0
    found_all_z = False

    while not found_all_z:
        ## Iterate over all the direction instructions
        for dir in directions:
            steps += 1
            found = ""
            ## Iterate over all the nodes ending in A
            for i  in range(len(a_nodes)):
                next_node = a_nodes[i]
                # print(f"Starting from node: {next_node}")
                ## Get the next node, based on current and the direction
                next_node = get_next(next_node, dir)
                a_nodes[i] = next_node
                ## If found a node ending in Z, set 'true' flag
                if next_node[-1:] == 'Z':
                    found += "T"
                else:
                    found += "F"
        ## If all flags are 'true', finish
        if 'F' not in found:
            found_all_z = True
    
    print(f"Steps required to reach: {steps} with {found}")


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