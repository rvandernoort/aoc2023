import numpy as np
from tqdm import tqdm

with open('input.txt') as f:
    content = f.read()
    lines = content.strip().splitlines()
    times = [ int(t) for t in lines[0].split(": ")[1].split() ]
    distances = [ int(d) for d in lines[1].split(": ")[1].split() ]
    
    print(f"Times: {times}, Distances: {distances}")
    
    
    counts = []
    for race in tqdm(range(len(times))):
        count = 0
        for hold_time in tqdm(range(times[race])):
            move_time = times[race] - hold_time
            move_distance = hold_time * move_time
            if move_distance > distances[race]:
                count += 1
        counts.append(count)
        
print(np.prod(counts))
        