import copy
from tqdm import tqdm

def generate_combination(input):
    combinations = [input]
    lengths = []
    
    while len(combinations) > 0 and '?' in combinations[-1]:
        current_string = combinations.pop()
        index = current_string.index('?')

        for replacement in ['#', '.']:
            new_string = current_string[:index] + replacement + current_string[index + 1:]
            if "?" in new_string:
                combinations.append(new_string)
            else: 
                correct = []
                variation = new_string
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
                
                # print(correct)
                lengths.append(len(correct))
    print(sum(lengths))

with open("input.txt") as f:
    data = f.read().splitlines()
    lengths = []
    
    for row in tqdm(data):
        [condition_records, contiguous_groups] = row.split()
        contiguous_groups = [int(x) for x in contiguous_groups.split(",")] 
        
        original_records = condition_records
        original_groups = copy.deepcopy(contiguous_groups)
        for i in range(5):
            condition_records += original_records + "?"
            contiguous_groups += original_groups
            
        # print(condition_records)
        # print(contiguous_groups)
        
        variations = generate_combination(condition_records)
        print("GENERATED VARIATIONS")
        

    
    # 52120 too low
    # 11016 too low
    # 195387500744 too low
    
        

                
            
