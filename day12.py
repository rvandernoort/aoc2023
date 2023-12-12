from tqdm import tqdm

def generate_combination(input):
    if "?" not in input:
        return [input]
    
    index = input.index("?")
    combinations = []
    
    for replacement in ["#", "."]:
        new_string = input[:index] + replacement + input[index+1:]
        combinations += generate_combination(new_string)
        
    return combinations

with open("input.txt") as f:
    data = f.read().splitlines()
    lengths = []
    
    for row in tqdm(data):
        [condition_records, contiguous_groups] = row.split()
        contiguous_groups = [int(x) for x in contiguous_groups.split(",")] 
        
        variations = generate_combination(condition_records)
        
        correct = []
        for variation in variations:
            start_index = 0
            skip = False
            for i, group in enumerate(contiguous_groups):
                if '#' not in variation[start_index:]:
                    skip = True
                    break
                index = variation.index("#", start_index)
                if index+group <= len(variation) and all(char == "#" for char in variation[index:index+group]) and (index+group >= len(variation) or variation[index+group] == "."):
                    start_index = index + group + 1
                    continue
                else:
                    skip = True
                    break
            if "#" in variation[start_index:]:
                skip = True
            if not skip:
                correct.append(variation)
        
        print(correct)
        lengths.append(len(correct))
    print(sum(lengths))
        
    # too high 10906
    # too low 4151
    #right 7032
                
            
