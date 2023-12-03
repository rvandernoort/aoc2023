result = 8

red = 12
green = 13
blue = 14

output = 0
games_done = []

with open('input.txt', 'r', encoding='utf-8') as f:
    content = f.read()
    
    for i, line in enumerate(content.strip().splitlines()):
        sets = line.strip().split(": ")
        games = sets[1].strip().split("; ")
        for game in games:
            # print(game) if i == 3 else None
            picks = game.strip().split(", ")
            print(picks) if i == 28 else None
            for pick in picks:
                pick = pick.strip().split(" ")
                print(pick) if i == 28 else None
                if (pick[1] == "red" and int(pick[0]) > red) or (pick[1] == "green" and int(pick[0]) > green) or (pick[1] == "blue" and int(pick[0]) > blue):
                    games_done.append(i)
        if i not in games_done:
            print(i + 1)
            games_done.append(i)
            output += i + 1
    print(output)
