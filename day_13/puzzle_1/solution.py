import sys
import os
import pprint
import numpy as np

def main():
    ## Set the variables/constants
    filepath = './input_file.txt'
    pp = pprint.PrettyPrinter(indent=4)
    ## Set the size of the arrays
    mirror_arr = []
    sum_rows = 0
    sum_cols = 0

    ## Check if the input file exists
    if not os.path.isfile(filepath):
        print("File path {} does not exist. Exiting...".format(filepath))
        sys.exit()

    ## Iterate over the file, lne_by_line
    with open(filepath) as fp:
        for line in fp.readlines():
            line = line.strip()
            ## Parse the input
            if line != "":
                mirror_arr.append([c for c in line])
            else:
                mirror_arr = np.asarray(mirror_arr)
                # pp.pprint(mirror_arr)
                ## Iterate over the rows and identify the equal rows
                for i in range(len(mirror_arr)-1):
                    if np.all(mirror_arr[i, :] == mirror_arr[i+1, :]):
                        all_rows = True
                        # print(f"Checking row {i} == {i+1}")
                        p, n = (i-1, i+2)
                        while True:
                            # print(f"   Checking row {p} == {n}")
                            if (p < 0) or (n > len(mirror_arr) - 1):
                                break
                            if np.all(mirror_arr[p, :] == mirror_arr[n, :]):
                                # print(f"   Checking row {p} == {n}")
                                all_rows = True
                            else:
                                all_rows = False
                                break
                            p -= 1
                            n += 1
                        if all_rows:
                            # print(f"      Row: All True {i}")
                            sum_rows += (i+1) * 100
                ## Iterate over the columns and identify the equal columns
                for i in range(len(mirror_arr[0])-1):
                    if np.all(mirror_arr[:, i] == mirror_arr[:, i+1]):
                        # print(f"Checking col {i} == {i+1}")
                        all_cols = True
                        p, n = (i-1, i+2)
                        while True:
                            if (p < 0) or (n > len(mirror_arr[0]) - 1):
                                break
                            if np.all(mirror_arr[:, p] == mirror_arr[:, n]):
                                # print(f"   FOUND Checking col {p} == {n}")
                                all_cols = True
                            else:
                                # print(f"   NOT Checking col {p} == {n}")
                                all_cols = False
                                break
                            p -= 1
                            n += 1
                        if all_cols:
                            # print(f"      Col: All True {i}")
                            sum_cols += (i+1)
                mirror_arr = []
                continue
    
    print(f"Total of rows and cols: {sum_rows + sum_cols}")

if __name__ == '__main__':
    main()