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
            # print(card_sets)
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
    
    cards_array = [1] * len(win_array)
    i = 0
    while i < len(own_array):
        ## Find the intersection of the 2 sets
        common_elements = set(win_array[i]) - (set(win_array[i]) - set(own_array[i]))
        card_wins = len(common_elements)
        if card_wins == 0:
            i += 1
            continue
        ## Iterate over the winning cards
        for k in range(i+1, i+1+card_wins):
            ## Increase the count for each win
            cards_array[k] += cards_array[i]
        i += 1
    ## Calculate the total
    for i in cards_array:
        total += i
    print(f"Total: {total}")


if __name__ == '__main__':
    main()