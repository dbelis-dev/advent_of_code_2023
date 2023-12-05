import sys
import os
import pprint

def main():
    ## Set the variables/constants
    filepath = './input_file-example'
    pp = pprint.PrettyPrinter(indent=4)
    seeds = []
    seeds_range = {}
    seed_to_soil = {}
    soil_to_fertilizer = {}
    fertilizer_to_water = {}
    water_to_light = {}
    light_to_temperature = {}
    temperature_to_humidity = {}
    humidity_to_location = {}
    lowest_loc = 0
    first_min = True

    ## Check if the input file exists
    if not os.path.isfile(filepath):
        print("File path {} does not exist. Exiting...".format(filepath))
        sys.exit()
    
    ## Iterate over the file, lne_by_line
    with open(filepath) as fp:
        for line in fp.readlines():
            line = line.strip()
            ## Parse the input
            section = line.split(':')
            if section[0] == "":
                continue
            if section[0] == "seeds":
                seeds = [int(x) for x in section[1].strip().split(' ')]
                continue
            if line == "":
                continue
            ## Switch to the appropriate dictionary
            match line:
                case "seed-to-soil map:":
                    curr_dict = seed_to_soil
                    continue
                case "soil-to-fertilizer map:":
                    curr_dict = soil_to_fertilizer
                    continue
                case "fertilizer-to-water map:":
                    curr_dict = fertilizer_to_water
                    continue
                case "water-to-light map:":
                    curr_dict = water_to_light
                    continue
                case "light-to-temperature map:":
                    curr_dict = light_to_temperature
                    continue
                case "temperature-to-humidity map:":
                    curr_dict = temperature_to_humidity
                    continue
                case "humidity-to-location map:":
                    curr_dict = humidity_to_location
                    continue
                # If an exact match is not confirmed, this last case will be used
                case _:
                    ## Get the destination, source and range
                    dst, src, rng = [int(x) for x in line.strip().split(' ')]
                    ## Fill_in the source and destination columns
                    curr_dict[src] = [dst, rng]
                    continue
    ## Create a dict of the starting seed and its range
    for s in range(0, len(seeds), 2):
        seeds_range[ seeds[s] ] = seeds[s+1]

    # pp.pprint(seeds_range)
    ## Iterate over the seed ranges
    for sd, rng in seeds_range.items():
        print(f"Range {'{:,}'.format(rng)}")
        for seed in range(sd, sd+rng):
            curr = seed
            next = 0
            # print(f"Looking for seed: {curr}")
            for key, values in seed_to_soil.items():
                if curr in range(key, key + values[1]):
                    next = values[0] + (curr - key)
                    break
                else:
                    next = curr
            curr = next
            for key, values in soil_to_fertilizer.items():
                if curr in range(key, key + values[1]):
                    # print(f"found soil: {curr}")
                    next = values[0] + (curr - key)
                    break
                else:
                    next = curr
            curr = next
            for key, values in fertilizer_to_water.items():
                if curr in range(key, key + values[1]):
                    next = values[0] + (curr - key)
                    break
                else:
                    next = curr
            curr = next
            for key, values in water_to_light.items():
                if curr in range(key, key + values[1]):
                    next = values[0] + (curr - key)
                    break
                else:
                    next = curr
            curr = next
            for key, values in light_to_temperature.items():
                if curr in range(key, key + values[1]):
                    next = values[0] + (curr - key)
                    break
                else:
                    next = curr
            curr = next
            for key, values in temperature_to_humidity.items():
                if curr in range(key, key + values[1]):
                    next = values[0] + (curr - key)
                    break
                else:
                    next = curr
            curr = next
            for key, values in humidity_to_location.items():
                if curr in range(key, key + values[1]):
                    next = values[0] + (curr - key)
                    break
                else:
                    next = curr
            if first_min:
                lowest_loc = next
                first_min = False
            ## Keep the location for each seed
            # locations.append(next)
            if (lowest_loc > next):
                lowest_loc = next

    ## Print the minimum number in the list
    print(f"The lowest location no is: {lowest_loc}")


if __name__ == '__main__':
    main()