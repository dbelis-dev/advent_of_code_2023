import sys
import os
import re

def main():
    ## Set the variables/constants
    filepath = './input_file'
    max_red = 12
    max_green = 13
    max_blue = 14
    sum_of_ids = 0

    ## Check if the input file exists
    if not os.path.isfile(filepath):
        print("File path {} does not exist. Exiting...".format(filepath))
        sys.exit()

    ## Iterate over the file, lne-by-line
    with open(filepath) as fp:
        for line in fp.readlines():
            line = line.strip()
            fail = False
            ## Parse the input
            games = line.split(':')
            ## Remove the letters and convert to integer
            current_game = int(re.sub("[^0-9]", "", games[0]))
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
                        red_cubes += int(re.sub("[^0-9]", "", cubes))
                    if cubes.find('green') > -1:
                        green_cubes += int(re.sub("[^0-9]", "", cubes))
                    if cubes.find('blue') > -1:
                        blue_cubes += int(re.sub("[^0-9]", "", cubes))
                    ## If any value is above max, discard this draw
                    if (red_cubes > max_red) or (green_cubes > max_green) or (blue_cubes > max_blue):
                        fail = True
            ## Only count valid games
            if (not fail):
                sum_of_ids += current_game
    
    print(f"The sum of IDs is: {sum_of_ids}")

if __name__ == '__main__':
    main()