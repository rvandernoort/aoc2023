
result = 142

with open('input.txt', 'r', encoding='utf-8') as f:
    content = f.read()
    calibration_values = []
    for line in content.strip().splitlines():
        first, last = None, None
        for char in line.strip():
            if first is None:
                if char.isnumeric():
                    first, last = char, char
            else:
                if char.isnumeric():
                    last = char
        calibration_values.append(int(first + last))
    print(sum(calibration_values))
