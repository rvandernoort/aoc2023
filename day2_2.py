result = 8



with open('input.txt', 'r', encoding='utf-8') as f:
    content = f.read()
    powers = []
    for i, line in enumerate(content.strip().splitlines()):
        sets = line.strip().split(": ")
        games = sets[1].strip().split("; ")
        minimum = [0, 0, 0]
        for game in games:
            picks = game.strip().split(", ")
            for pick in picks:
                pick = pick.strip().split(" ")
                if pick[1] == "red":
                    minimum[0] = max(minimum[0], int(pick[0]))
                if pick[1] == "green":
                    minimum[1] = max(minimum[1], int(pick[0]))
                if pick[1] == "blue":
                    minimum[2] = max(minimum[2], int(pick[0]))
        power = minimum[0] * minimum[1] * minimum[2]
        print(power)
        powers.append(power)
        print(powers)
    print(sum(powers))
