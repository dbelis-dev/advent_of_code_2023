import sys
import os
import pprint
from collections import Counter

def main():
    ## Set the variables/constants
    filepath = './input_file'
    global pp,five_kind_arr, four_kind_arr, full_house_arr, three_kind_arr, one_pair_arr, two_pair_arr, high_card_arr, strengths
    pp = pprint.PrettyPrinter(indent=4)
    strengths = "J23456789TQKA"
    five_kind_arr = []
    four_kind_arr = []
    full_house_arr = []
    three_kind_arr = []
    one_pair_arr = []
    two_pair_arr = []
    high_card_arr = []
    
    ## Check if the input file exists
    if not os.path.isfile(filepath):
        print("File path {} does not exist. Exiting...".format(filepath))
        sys.exit()
    
    ## Iterate over the file, lne_by_line
    with open(filepath) as fp:
        for line in fp.readlines():
            line = line.strip()
            ## Parse the input
            hand, bid = line.split(' ')
            evaluate_hand(hand, bid)
    ## Calculate the bids
    count_bid = 1
    sum = 0
    for hand in high_card_arr:
        sum += int(hand[1]) * count_bid
        count_bid += 1
    for hand in one_pair_arr:
        sum += int(hand[1]) * count_bid
        count_bid += 1
    for hand in two_pair_arr:
        sum += int(hand[1]) * count_bid
        count_bid += 1
    for hand in three_kind_arr:
        sum += int(hand[1]) * count_bid
        count_bid += 1
    for hand in full_house_arr:
        sum += int(hand[1]) * count_bid
        count_bid += 1
    for hand in four_kind_arr:
        sum += int(hand[1]) * count_bid
        count_bid += 1
    for hand in five_kind_arr:
        # print(f"Adding {int(hand[1])} * {count_bid} = {int(hand[1]) * count_bid}")
        sum += int(hand[1]) * count_bid
        count_bid += 1
    print(f"Total winnings: {sum}")

    # pp.pprint(f"High Card: {high_card_arr}")
    # pp.pprint(f"One Pair: {one_pair_arr}")
    # pp.pprint(f"Two Pair: {two_pair_arr}")
    # pp.pprint(f"Three Kind: {three_kind_arr}")
    # pp.pprint(f"Full House: {full_house_arr}")
    # pp.pprint(f"Four Kind: {four_kind_arr}")
    # pp.pprint(f"Five Kind: {five_kind_arr}")


def evaluate_hand(hand, bid):
    counters = Counter(hand)
    upd_hand = hand
    if 'J' in counters.keys():
        if 5 in counters.values():
            upd_hand = "AAAAA"
        else:
            counters.pop('J', None)
            max_key = max(counters, key=counters.get)
            upd_hand = hand.replace('J', max_key)
    counters = Counter(upd_hand)
    ## Check if Five-of-a-Kind
    if len(counters) == 1:
        arr = five_kind_arr
    ## Check if High-card
    elif len(counters) == 5:
        arr = high_card_arr
    ## Check if One-Pair
    elif len(counters) == 4:
        arr = one_pair_arr
    ## Check if Two-Pair or Three-of-a-Kind
    elif len(counters) == 3:
        if 3 in counters.values():
            arr = three_kind_arr
        else:
            arr = two_pair_arr
    ## Check if Full-House or Four-of-a-Kind
    elif len(counters) == 2:
        if 4 in counters.values():
            arr = four_kind_arr
        else:
            arr = full_house_arr
    
    ## Add the new hand to the respective array
    arr.append([hand, bid])
    ## Add to array and process this 
    if len(arr) > 0:
        ## process
        for i in range(len(arr)-1):
            rec = arr[i]
            ## Check each character in the hand, either swap
            for idx in range(len(hand)):
                if strengths.find(hand[idx]) == strengths.find(rec[0][idx]):
                    continue
                if strengths.find(hand[idx]) > strengths.find(rec[0][idx]):
                    break
                else:
                    arr[i], arr[len(arr)-1] = arr[len(arr)-1], arr[i]
                    break


if __name__ == '__main__':
    main()