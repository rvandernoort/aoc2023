
result = 281

def is_number(char, index, line):
    numbers = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    if char.isnumeric():
        return True, char
    else:
        for i, number in enumerate(numbers):
            print(index)
            print(number in line[index:index+5] )
            print(line.find(number))
            if number in line[index:index+5] and line[index:index+5].find(number) == 0:
                return True, str(i+1)
    return False, None

with open('input.txt', 'r', encoding='utf-8') as f:
    content = f.read()
    calibration_values = []
    for line in content.strip().splitlines():
        first, last = None, None
        for i, char in enumerate(line.strip()):
            is_num, num = is_number(char, i, line)
            if first is None:
                if is_num:
                    first, last = num, num
                    print("First: " + first)
            else:
                if is_num:
                    last = num
                    print("Last: " + last)
        print("Adding: " + str(int(first + last)))
        calibration_values.append(int(first + last))
    print(sum(calibration_values))

