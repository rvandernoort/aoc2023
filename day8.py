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

    start = "AAA"
    end = "ZZZ"
    current = "AAA"
    while current != end:
        for instruction in instructions:
            if instruction == "L":
                current = nodes[current][0]
            elif instruction == "R":
                current = nodes[current][1]
            steps += 1
            if current == end:
                break
    print(steps)
