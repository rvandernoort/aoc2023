from collections import defaultdict

engine = "*"

with open('input.txt', 'r', encoding='utf-8') as f:
    content = f.read()
    grid  = [['.' for _ in range(140 + 2)]]
    for line in content.strip().splitlines():
        grid.append(['.', *line, '.'])
    grid.append(['.' for _ in range(140 + 2)])
    
    number_add = 0
    gears = defaultdict(list)
    gear_ratios = []
    
    for i in range(len(grid)):
        going_number = ""
        connected = (None, None)
        for j in range(len(grid[i])):
            if grid[i][j].isnumeric() and grid[i][j+1].isnumeric():
                going_number += grid[i][j]
                if grid[i-1][j] == engine:
                    connected = (i-1, j)
                elif grid[i+1][j] == engine:
                    connected = (i+1, j)
                elif grid[i][j-1] == engine:
                    connected = (i, j-1)
                elif grid[i-1][j-1] == engine:
                    connected = (i-1, j-1)
                elif grid[i-1][j+1] == engine:
                    connected = (i-1, j+1)
                elif grid[i+1][j-1] == engine:
                    connected = (i+1, j-1)
                elif grid[i+1][j+1] == engine:
                    connected = (i+1, j+1)
            elif grid[i][j].isnumeric():
                going_number += grid[i][j]
                if grid[i-1][j] == engine:
                    connected = (i-1, j)
                elif grid[i+1][j] == engine:
                    connected = (i+1, j)
                elif grid[i][j-1] == engine:
                    connected = (i, j-1)
                elif grid[i-1][j-1] == engine:
                    connected = (i-1, j-1)
                elif grid[i-1][j+1] == engine:
                    connected = (i-1, j+1)
                elif grid[i+1][j-1] == engine:
                    connected = (i+1, j-1)
                elif grid[i+1][j+1] == engine:
                    connected = (i+1, j+1)
                elif grid[i][j+1] == engine:
                    connected = (i, j+1)
                
                if all (connected):
                    # print(going_number)
                    # print(connected)
                    gears[connected].append(int(going_number))
                    going_number = ""
                    connected = (None, None)
            else:
                going_number = ""
                
    # print(gears.items())
     
    for gear in gears.items():
        if len(gear[1]) == 2:
            gear_ratios.append(gear[1][0] * gear[1][1])
            
    # print(gear_ratios)

    sum_gear_ratios = sum(gear_ratios)
    print(sum_gear_ratios)
                    
                    
                    