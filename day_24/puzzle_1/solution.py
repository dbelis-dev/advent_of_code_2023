import sys
import os
import pprint

def main():
    ## Set the variables/constants
    filepath = './input_file.txt'
    pp = pprint.PrettyPrinter(indent=4)
    ## Define the arrays
    global test_min, test_max
    hail_arr = []
    test_min = 200000000000000
    test_max = 400000000000000

    ## Check if the input file exists
    if not os.path.isfile(filepath):
        print("File path {} does not exist. Exiting...".format(filepath))
        sys.exit()

    ## Iterate over the file, lne_by_line
    with open(filepath) as fp:
        for line in fp.readlines():
            line = line.strip()
            points, vel = line.split(' @ ')
            x, y, z = [int(t) for t in points.split(', ')]
            vx, vy, vz = [int(t) for t in vel.split(', ')]
            hail_arr.append((x, y, z, x+vx, y+vy, z+vz))
    count = 0
    for i in range(len(hail_arr)):
        x, y, z, vx, vy, vz = hail_arr[i]
        for j in range(i+1, len(hail_arr)):
            xt, yt, zt, vxt, vyt, vzt = hail_arr[j]
            pt = line_intersect(x, y, vx, vy, xt, yt, vxt, vyt)
            if pt is not None:
                count += 1
                # pp.pprint(pt)
    
    print(f"Intersections occured within the test area: {count}")

## Returns a (x, y) tuple or None if there is no intersection
def line_intersect(Ax1, Ay1, Ax2, Ay2, Bx1, By1, Bx2, By2):
    d = (By2 - By1) * (Ax2 - Ax1) - (Bx2 - Bx1) * (Ay2 - Ay1)
    if d:
        uA = ((Bx2 - Bx1) * (Ay1 - By1) - (By2 - By1) * (Ax1 - Bx1)) / d
        uB = ((Ax2 - Ax1) * (Ay1 - By1) - (Ay2 - Ay1) * (Ax1 - Bx1)) / d
    else:
        return
    x = Ax1 + uA * (Ax2 - Ax1)
    y = Ay1 + uA * (Ay2 - Ay1)
    ## Check if the intersection lies within the test area
    ### or the intersection occurs in the past
    if Ax1 > Ax2 and x > Ax2:
        return
    if Ax1 < Ax2 and x < Ax2:
        return
    if Ay1 > Ay2 and y > Ay2:
        return
    if Ay1 < Ay2 and y < Ay2:
        return
    if Bx1 > Bx2 and x > Bx2:
        return
    if Bx1 < Bx2 and x < Bx2:
        return
    if By1 > By2 and y > By2:
        return
    if By1 < By2 and y < By2:
        return
    if not(test_min <= x <= test_max and test_min <= y <= test_max):
        return
    return x, y

if __name__ == '__main__':
    main()