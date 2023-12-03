symbols = ["*", "#", "+", "&", "$", "%", "@", "!", "?", "(", ")", "[", "]", "{", "}", "<", ">", ":", ";", ",", "-", "_", "=", "+", "|", "/", "\\"]

with open('input.txt', 'r', encoding='utf-8') as f:
    content = f.read()
    grid  = [['.' for _ in range(140 + 2)]]
    for line in content.strip().splitlines():
        grid.append(['.', *line, '.'])
    grid.append(['.' for _ in range(140 + 2)])
    
    print(grid)
    
    number_add = 0
    
    for i in range(len(grid)):
        going_number = ""
        connected = False
        for j in range(len(grid[i])):
            if grid[i][j].isnumeric() and grid[i][j+1].isnumeric():
                going_number += grid[i][j]
                if grid[i-1][j] in symbols or grid[i+1][j] in symbols or grid[i][j-1] in symbols or grid[i-1][j-1] in symbols or grid[i-1][j+1] in symbols or grid[i+1][j-1] in symbols or grid[i+1][j+1] in symbols:
                    connected = True
            elif grid[i][j].isnumeric():
                going_number += grid[i][j]
                if grid[i-1][j] in symbols or grid[i+1][j] in symbols or grid[i][j-1] in symbols or grid[i][j+1] in symbols or grid[i-1][j-1] in symbols or grid[i-1][j+1] in symbols or grid[i+1][j-1] in symbols or grid[i+1][j+1] in symbols:
                    connected = True
                if connected:
                    print(going_number)
                    number_add += int(going_number)
                    going_number = ""
                    connected = False
            else:
                going_number = ""
                
    print(number_add)
                