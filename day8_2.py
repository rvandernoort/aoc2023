from collections import defaultdict
import copy
from math import lcm


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

    current_nodes = copy.copy(starting_nodes)
    paths = defaultdict(int)
    while not set(starting_nodes).issubset(paths.keys()):
        for instruction in instructions:
            for i, current in enumerate(current_nodes):
                if instruction == "L":
                    current = nodes[current][0]
                elif instruction == "R":
                    current = nodes[current][1]
                if current in ending_nodes and starting_nodes[i] not in paths.keys():
                    print(current)
                    paths[starting_nodes[i]] = steps + 1
                current_nodes[i] = current
            steps += 1
    print(*paths.values())
    print(lcm(*paths.values()))

    # too high: 2388568148733210885000
    # off by one error: add one to reduce by a lot haha
