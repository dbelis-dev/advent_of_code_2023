import sys
import os

def main():
    ## Set the variables/constants
    filepath = './input_file'
    win_array = []
    own_array = []
    total = 0

    ## Check if the input file exists
    if not os.path.isfile(filepath):
        print("File path {} does not exist. Exiting...".format(filepath))
        sys.exit()
    
    ## Iterate over the file, lne-by-line
    with open(filepath) as fp:
        for line in fp.readlines():
            common_elements = []
            line = line.strip()
            ## Parse the input
            cards = line.split(':')
            ## Split string into winning and own cards
            card_sets = cards[1].strip().split(' | ')
            win_set = card_sets[0]
            own_set = card_sets[1]
            ## Split further into individual cards
            win_cards = win_set.split(' ')
            own_cards = own_set.split(' ')
            ## Remove double-spaces
            win_cards = list(filter(None, win_cards))
            own_cards = list(filter(None, own_cards))
            ## Add the cards into an array
            win_array.append(win_cards)
            own_array.append(own_cards)
            ## Find the intersection of the 2 sets ()
            common_elements = set(win_cards) - (set(win_cards) - set(own_cards))
            total += calculate_score( len(common_elements) )
    print(f"Total: {total}")

def calculate_score(num):
    sum = 0
    for i in range(num):
        if i == 0:
            sum = 1
            continue
        sum = sum * 2
    return sum

if __name__ == '__main__':
    main()