from tqdm import tqdm

with open('input.txt') as f:
    content = f.read()
    lines = content.strip().splitlines()
    times = [ int(t) for t in [lines[0].split(": ")[1].replace(" ", '')] ]
    distances = [ int(d) for d in [lines[1].split(": ")[1].replace(" ", '')] ]
    
    print(f"Times: {times}, Distances: {distances}")
    
    count = 0
    for hold_time in tqdm(range(times[0])):
        move_time = times[0] - hold_time
        move_distance = hold_time * move_time
        if move_distance > distances[0]:
            count += 1

    print(count)
