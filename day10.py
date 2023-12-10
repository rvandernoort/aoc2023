

def get_start_position(data):
    for i, row in enumerate(data):
        for j, pos in enumerate(row):
            if pos == 'S':
                start = (i, j)
                return start

def get_all_connections(data, position, connections):
    connections = get_horizontal_connections(data, position, connections)
    connections = get_vertical_connections(data, position, connections)
    return connections

def get_vertical_connections(data, position, connections):
    if data[position[0]-1][position[1]] == "|" or data[position[0]-1][position[1]] == "7" or data[position[0]-1][position[1]] == "F":
            connections.append((position[0]-1, position[1]))
    if data[position[0]+1][position[1]] == "|" or data[position[0]+1][position[1]] == "J" or data[position[0]+1][position[1]] == "L":
        connections.append((position[0]+1, position[1]))
    return connections

def get_horizontal_connections(data, position, connections):
    if data[position[0]][position[1]-1] == "-" or data[position[0]][position[1]-1] == "L" or data[position[0]][position[1]-1] == "F":
            connections.append((position[0], position[1]-1))
    if data[position[0]][position[1]+1] == "-" or data[position[0]][position[1]+1] == "J" or data[position[0]][position[1]+1] == "7":
        connections.append((position[0], position[1]+1))
    return connections

def get_J_connections(data, position, connections):
    if data[position[0] - 1][position[1]] == "|" or data[position[0] - 1][position[1]] == "7" or data[position[0] - 1][position[1]] == "F":
            connections.append((position[0]-1, position[1]))
    if data[position[0]][position[1]-1] == "-" or data[position[0]][position[1]-1] == "F" or data[position[0]][position[1]-1] == "L":
        connections.append((position[0], position[1]-1))
    return connections

def get_L_connections(data, position, connections):
    if data[position[0] - 1][position[1]] == "|" or data[position[0] - 1][position[1]] == "7" or data[position[0] - 1][position[1]] == "F":
            connections.append((position[0]-1, position[1]))
    if data[position[0]][position[1]+1] == "-" or data[position[0]][position[1]+1] == "J" or data[position[0]][position[1]+1] == "7":
        connections.append((position[0], position[1]+1))
    return connections

def get_7_connections(data, position, connections):
    if data[position[0] + 1][position[1]] == "|" or data[position[0] + 1][position[1]] == "J" or data[position[0] + 1][position[1]] == "L":
            connections.append((position[0]+1, position[1]))
    if data[position[0]][position[1]-1] == "-" or data[position[0]][position[1]-1] == "F" or data[position[0]][position[1]-1] == "L":
        connections.append((position[0], position[1]-1))
    return connections

def get_F_connections(data, position, connections):
    if data[position[0] + 1][position[1]] == "|" or data[position[0] + 1][position[1]] == "J" or data[position[0] + 1][position[1]] == "L":
            connections.append((position[0] + 1, position[1]))
    if data[position[0]][position[1]+1] == "-" or data[position[0]][position[1]+1] == "J" or data[position[0]][position[1]+1] == "7":
        connections.append((position[0], position[1]+1))
    return connections

def get_connections(data, position):
    connections = []
    current = data[position[0]][position[1]]
    if current == "S":
        connections = get_all_connections(data, position, connections)
    elif current == "|":
        connections = get_vertical_connections(data, position, connections)
    elif current == "-":
        connections = get_horizontal_connections(data, position, connections)
    elif current == "J":
        connections = get_J_connections(data, position, connections)
    elif current == "L":
        connections = get_L_connections(data, position, connections)
    elif current == "7":
        connections = get_7_connections(data, position, connections)
    elif current == "F":
        connections = get_F_connections(data, position, connections)
    return connections

with open('input.txt') as f:
    data = f.read().splitlines()
    
    start = get_start_position(data)
    
    visiting = get_connections(data, start)
    previous = [start]
    steps = 0
    while len(visiting) > 0:
        print(visiting)
        steps += 1
        next_visiting = []
        for pos in visiting:
            next_visiting += get_connections(data, pos)
        next_visiting = [pos for pos in next_visiting if pos not in previous]
        previous += visiting
        visiting = next_visiting
        
        if len(visiting) != len(set(visiting)):
            print(visiting)
            print(f"Found a cycle at step {steps + 1}")
            break
    
