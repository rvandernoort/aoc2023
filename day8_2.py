from collections import defaultdict


with open("input.txt", "r") as f:
    data = f.read().splitlines()

    instructions = [char for char in data[0]]
    nodes = defaultdict(str)
    steps = 0

    for row in data[2:]:
        [start, end] = row.split(" = ")
        [left, right] = end.replace("(", "").replace(")", "").split(", ")
        nodes[start] = (left, right)

    starting_nodes, ending_nodes = [], []
    for key in nodes.keys():
        if key[2] == "A":
            starting_nodes.append(key)
        elif key[2] == "Z":
            ending_nodes.append(key)

    current_nodes = starting_nodes
    while not all(node in ending_nodes for node in current_nodes):
        print(current_nodes)
        for instruction in instructions:
            for i, current in enumerate(current_nodes):
                if instruction == "L":
                    current = nodes[current][0]
                elif instruction == "R":
                    current = nodes[current][1]
                current_nodes[i] = current
            steps += 1
            if all(node in ending_nodes for node in current_nodes):
                break
    print(steps)
