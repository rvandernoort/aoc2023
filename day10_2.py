import numpy as np


def get_start_position(data):
    for i, row in enumerate(data):
        for j, pos in enumerate(row):
            if pos == 'S':
                start = (i, j)
                return start
            
def determine_start_type(data, start):
    if data[start[0]][start[1] + 1] in  ["-", "J", "7"] and data[start[0] + 1][start[1]] in ["|", "J", "L"]:
        return "F"
    elif data[start[0]][start[1] + 1] in ["-", "J", "7"] and data[start[0] - 1][start[1]] in ["|", "7", "F"]:
        return "L"
    elif data[start[0]][start[1] - 1] in ["-", "L", "F"] and data[start[0] + 1][start[1]] in ["|", "J", "L"]:
        return "7"
    elif data[start[0]][start[1] - 1] in ["-", "L", "F"] and data[start[0] - 1][start[1]] in ["|", "7", "F"]:
        return "J"
    elif data[start[0]][start[1] + 1] in ["-", "J", "7"] and data[start[0]][start[1] - 1] in ["-", "L", "F"]:
        return "-"
    elif data[start[0] + 1][start[1]] in ["|", "J", "L"] and data[start[0] - 1][start[1]] in ["|", "7", "F"]:
        return "|"
    
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
            
def find_loop(data, start):
    visiting = get_connections(data, start)
    previous = [start]
    loop = [start]
    while len(visiting) > 0:
        loop += visiting
        next_visiting = []
        for pos in visiting:
            next_visiting += get_connections(data, pos)
        next_visiting = [pos for pos in next_visiting if pos not in previous]
        previous += visiting
        visiting = next_visiting
        if len(visiting) != len(set(visiting)):
            loop += visiting
            return loop
        
def map_to_only_loop(data, loop):
    for i in range(len(data)):
        for j in range(len(data[i])):
            if (i, j) not in loop:
                data[i][j] = "."
    return data
            
with open('input.txt') as f:
    data = f.read().splitlines()
    
    for i, row in enumerate(data):
        data[i] = [*row]
    
    start = get_start_position(data)
    data[start[0]][start[1]] = determine_start_type(data, start)
    
    loop = find_loop(data, start)
    print(loop)
    data = map_to_only_loop(data, loop)
    
    for i in data:
        print('\t'.join(map(str, i)))
    
    inside = 0
    
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] == ".":
                before, after = 0, 0
                left, right = 0, 0
                next_to = ""
                for k in range(i):
                    if data[k][j] == "J" and next_to == "F":
                        before += 1
                    elif data[k][j] == "L" and next_to == "7":
                        before += 1
                    elif data[k][j] == "-":
                        before += 1
                    if data[k][j] != "|":
                        next_to = data[k][j]
                for k in range(i + 1, len(data)):
                    if data[k][j] == "J" and next_to == "F":
                        after += 1
                    elif data[k][j] == "L" and next_to == "7":
                        after += 1
                    elif data[k][j] == "-":
                        after += 1
                    if data[k][j] != "|":
                        next_to = data[k][j]
                next_to = ""
                for k in range(j):
                    if data[i][k] == "7" and next_to == "L":
                        left += 1
                    elif data[i][k] == "J" and next_to == "F":
                        left += 1
                    elif data[i][k] == "|":
                        left += 1
                    if data[i][k] != "-":
                        next_to = data[i][k]
                for k in range(j + 1, len(data[i])):
                    if data[i][k] == "7" and next_to == "L":
                        right += 1
                    elif data[i][k] == "J" and next_to == "F":
                        right += 1
                    elif data[i][k] == "|":
                        right += 1
                    if data[i][k] != "-":
                        next_to = data[i][k]
                if (before % 2 != 0 or after % 2 != 0) and (left % 2 != 0 or right % 2 != 0):
                    print(i, j)
                    inside += 1

    print(inside)
    # low 156
    # 493