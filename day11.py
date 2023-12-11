import copy

input = """
...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#.....
"""

output = 374

with open("input.txt") as f:
    data = f.read().splitlines()
    expanded_data = []
    
    for row in data:
        expanded_data.append([*row])
        if "#" not in row:
            expanded_data.append([*row])
    
    expanded_data_2 = copy.deepcopy(expanded_data)
    
    count = 1
    for i in range(len(expanded_data[0])):
        amount = 0
        for j in range(len(expanded_data)):
            # print(f"POINT at {j}, {i}, is {expanded_data[j][i]}")
            if expanded_data[j][i] == "#":
                amount += 1
                break
        if amount == 0:
            for j in range(len(expanded_data)):
                expanded_data_2[j].insert(i+count, ".")
            count += 1

    print(expanded_data_2)
    
    galaxies = []
    for i in range(len(expanded_data_2)):
        for j in range(len(expanded_data_2[i])):
            if expanded_data_2[i][j] == "#":
                galaxies.append((i, j))
    
    distances = []
    for i, galaxy in enumerate(galaxies):
        other_galaxies = copy.deepcopy(galaxies)
        other_galaxies = other_galaxies[i+1:]
        for other in other_galaxies:
            print(f"Galaxy {galaxy} to {other} is {abs(galaxy[0]-other[0]) + abs(galaxy[1]-other[1])}")
            distances.append(abs(galaxy[0]-other[0]) + abs(galaxy[1]-other[1]))
    
    print(len(distances))
    print(sum(distances))