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
            
with open('input.txt') as f:
    data = f.read().splitlines()
    
    for i, row in enumerate(data):
        data[i] = [*row]
    
    start = get_start_position(data)
    data[start[0]][start[1]] = determine_start_type(data, start)
    
    print(data)
    
    inside = 0
    
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] == ".":
                before, after = 0, 0
                left, right = 0, 0
                next_to = ""
                for k in range(i):
                    if data[k][j] == ".":
                        break
                    if data[k][j] in ["F", "7"]:
                        next_to = "vertical"
                    elif data[k][j] in ["J", "L"]:
                        next_to = "horizontal"
                    if data[k][j] in ["-", "F", "7", "L", "J"] and next_to != "vertical":
                        before += 1
                for k in range(i + 1, len(data)):
                    if data[k][j] == ".":
                        break
                    if data[k][j] in ["F", "7"]:
                        next_to = "vertical"
                    elif data[k][j] in ["J", "L"]:
                        next_to = "horizontal"
                    if data[k][j] in ["-", "F", "7", "L", "J"] and next_to != "vertical":
                        after += 1
                next_to = ""
                for k in range(j):
                    if data[i][k] == ".":
                        break
                    if data[i][k] in ["F", "L"]:
                        next_to = "left"
                    elif data[i][k] in ["7", "J"]:
                            next_to = "right"
                    if data[i][k] in ["|", "F", "7", "L", "J"] and next_to != "left":
                        left += 1
                for k in range(j + 1, len(data[i])):
                    if data[i][k] == ".":
                        break
                    if data[i][k] in ["F", "L"]:
                        next_to = "left"
                    elif data[i][k] in ["7", "J"]:
                            next_to = "right"
                            left -= 1
                    if data[i][k] in ["|", "F", "7", "L", "J"] and next_to != "left":
                        right += 1
                        
                if before > 0 and after > 0 and left > 0 and right > 0 and (before % 2 != 0 or after % 2 != 0) and (left % 2 != 0 or right % 2 != 0):
                    print(i, j)
                    inside += 1

    print(inside)
