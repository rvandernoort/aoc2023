import copy
from collections import defaultdict

saved_scores = defaultdict(list)

def lookup(scores):
    for score in reversed(scores.items()):
        print(score)
        print([ saved_scores[other] for other in score[1] if other is not None])
        saved_scores[score[0]] = sum([ saved_scores[other] for other in score[1] if other is not None]) + 1
        print(saved_scores)
    return sum(saved_scores.values())

with open('input.txt', 'r') as f:
    content = f.read()
    scores = defaultdict(list)
    for i, row in enumerate(content.strip().splitlines()):
        card = row.split(": ")[1:]
        numbers = row.split("| ")
        winning, j = [], 1
        for n in numbers[0].split():
            winning.append(n)
        for n in numbers[1].split():
            if n in winning:
                scores[i].append(i + j)
                j += 1
        if i not in scores:
            scores[i].append(None)
    
    print(scores)
    total_cards = lookup(scores)
    # multiplier = defaultdict(lambda: 1)
    # print(scores.items())
    # for score in scores.items():
    #     for other in score[1]:
    #         multiplier[other] += 1 * multiplier[score[0]]
    # for score in scores.items():
    #     print(score)
    #     print((len(score[1]) + 1) * multiplier[score[0]])
    #     total_cards += (len(score[1]) + 1) * multiplier[score[0]]
            
    print(total_cards)
