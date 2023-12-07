from collections import defaultdict

with open('input.txt') as f:
    content = f.read()
    
    types = ['five_of_a_kind', 'four_of_a_kind', 'full_house', 'three_of_a_kind', 'two_pair', 'one_pair', 'high_card']
    order = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']
    
    hands = defaultdict(int)
    bids = defaultdict(int)
    for row in content.splitlines():
        [hand, bid] = row.split()
        bids[hand] = int(bid)
        
        cards = defaultdict(int)
        for char in hand:
            cards[char] += 1
        
        for card_count in cards.values():
            if hands[hand] == 0 and card_count == 5:
                hands[hand] = 6
            elif hands[hand] == 0 and card_count == 4:
                hands[hand] = 5
            elif hands[hand] == 1 and card_count == 3 or hands[hand] == 3 and card_count == 2:
                hands[hand] = 4
            elif hands[hand] == 0 and card_count == 3:
                hands[hand] = 3
            elif hands[hand] == 1 and card_count == 2:
                hands[hand] = 2
            elif hands[hand] == 0 and card_count == 2:
                hands[hand] = 1

    # Sort hands on biggest values first
    hands = dict(sorted(hands.items(), key=lambda x: x[1]))
    # print(hands)
    
    ranking = []
    for t in range(len(types)):
        duplicates = defaultdict(int)
        for hand, value in hands.items():
            if value == t:
                duplicates[hand] = value
        
        sorted_duplicates = dict(sorted(duplicates.items(), key=lambda x: [order.index(c) for c in x[0]], reverse=True))
        print(sorted_duplicates)
        
        for hand in sorted_duplicates.keys():
            ranking.append(hand)
            
    # print(ranking)
    
    winnings = 0
    for i, hand in enumerate(ranking):
        winnings += (i+1) * bids[hand]
    
    print(winnings)

    # wrong: 250693651