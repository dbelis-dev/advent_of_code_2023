import sys
import os
import re

def main():
    ## Set the variables/constants
    filepath = './input_file'
    total = 0

    ## Check if the input file exists
    if not os.path.isfile(filepath):
        print("File path {} does not exist. Exiting...".format(filepath))
        sys.exit()

    ## Iterate over the file, lne-by-line
    with open(filepath) as fp:
        for line in fp.readlines():
            line = line.strip()
            max_red = 0
            max_green = 0
            max_blue = 0
            ## Parse the input
            games = line.split(':')
            game_sets = games[1].split(';')
            ## Iterate over the sets
            for cube_draw in game_sets:
                red_cubes = 0
                green_cubes = 0
                blue_cubes = 0
                cubes_per_set = cube_draw.split(',')
                ## Parse colors
                for cubes in cubes_per_set:
                    ## For the particular color, remove the letters and convert to integer
                    if cubes.find('red') > -1:
                        red_cubes = int(re.sub("[^0-9]", "", cubes))
                    if cubes.find('green') > -1:
                        green_cubes = int(re.sub("[^0-9]", "", cubes))
                    if cubes.find('blue') > -1:
                        blue_cubes = int(re.sub("[^0-9]", "", cubes))
                ## Find the maximum per color
                if (red_cubes > max_red):
                    max_red = red_cubes
                if (green_cubes > max_green):
                    max_green = green_cubes
                if (blue_cubes > max_blue):
                    max_blue = blue_cubes
            ## Calculate the power and add to total
            total += max_red * max_green * max_blue
    
    print(f"The total is: {total}")

if __name__ == '__main__':
    main()