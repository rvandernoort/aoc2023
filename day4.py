
with open('input.txt', 'r') as f:
    content = f.read()
    scores = []
    for row in content.strip().splitlines():
        card = row.split(": ")[1:]
        numbers = row.split("| ")
        winning, own = [], None
        for n in numbers[0].split():
            winning.append(n)
        for n in numbers[1].split():
            print(n)
            print(own)
            if n in winning and own is None:
                own = 1
            elif n in winning and own is not None:
                own *= 2
        if own is not None:
            print(f"Add score: {own}")
            scores.append(own)
            own = None
            
    print(sum(scores))
