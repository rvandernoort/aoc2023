
from collections import defaultdict


with open('input.txt') as f:
    data = f.read().splitlines()
    histories = []
    
    for row in data:
        seq = [int(num) for num in row.split()]
        difference = defaultdict(list)
        depth = 0
        difference[depth] = seq
        while not all(item == 0 for item in difference[depth]):
            depth += 1
            for s in range(len(difference[depth - 1]) - 1):
                difference[depth].append(difference[depth - 1][s+1] - difference[depth - 1][s])
        
        for i in range(len(difference.items()) - 1, 0, -1):
                difference[i-1] = [difference[i-1][0] - difference[i][0]] + difference[i-1]
        histories.append(difference[0][0])
    
    print(sum(histories))
                
            
            