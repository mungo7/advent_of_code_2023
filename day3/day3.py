import re

def read_input(file):
    '''
    Read the input file and return symbol and part lists
    '''
    symbol_list= []
    part_list = []
    gear_list = []
    with open(file) as f:
        for line_index, line in enumerate(f):
            line = line.strip()
            enumerated_line = enumerate(line)
            symbols_indexes = [index for index, char in enumerated_line if not char.isalnum() and char != '.']
            line_symbols={'line_number': line_index, 'symbol_indexes': symbols_indexes}
            symbol_list.append(line_symbols) 
            enumerated_line = enumerate(line)
            matches = re.finditer('\d+', line)
            for match in matches:
                new_part = {'line_number': line_index, 'part_number': int(match.group()), 'start_index': int(match.start()), 'end_index': int(match.end())}
                part_list.append(new_part)
            enumerated_line = enumerate(line)
            gear_indexes = [index for index, char in enumerated_line if char == '*']
            line_gears={'line_number': line_index, 'gear_indexes': gear_indexes}
            gear_list.append(line_gears)
    return symbol_list, part_list, gear_list

def check_adjacency(part, symbol_list):
    '''
    Check if a part has a symbol placed adjacently in the line before, the current line, or the next line.
    '''
    line_number = part['line_number']
    lines_to_check=[]
    if line_number == 0:
        lines_to_check = [symbol_list[line_number], symbol_list[line_number+1] ]
    if line_number >= 1 and line_number < len(symbol_list)-1:
        lines_to_check = [symbol_list[line_number-1], symbol_list[line_number], symbol_list[line_number+1]]
    if line_number == len(symbol_list)-1:
        lines_to_check = [symbol_list[line_number-1], symbol_list[line_number]]
    
    part_required=False
    for line in lines_to_check:
        for number in range(part['start_index']-1, part['end_index']+1):
            if number in line['symbol_indexes']:
                part_required=True
    return part_required

def get_gear_ratio(gear_list, part_list):
    gear_ratio=0
    for gear in gear_list:
        line_number = gear['line_number']
        parts_to_check=[]
        for part in part_list:
            if line_number == 0:
                if part.get('line_number') == line_number or part.get('line_number') == line_number+1:
                    parts_to_check.append(part)
            if line_number >= 1 and line_number < len(gear_list)-1:
                if part.get('line_number') == line_number-1 or part.get('line_number') == line_number or part.get('line_number') == line_number+1:
                    parts_to_check.append(part)
            if line_number == len(gear_list)-1:
                if part.get('line_number') == line_number-1 or part.get('line_number') == line_number:
                    parts_to_check.append(part)
        for number in gear.get('gear_indexes'):
            adjacent_parts=[]
            for part in parts_to_check:
                if number in range(part.get('start_index')-1, part.get('end_index')+1):
                    adjacent_parts.append(part)
            if len(adjacent_parts) == 2:
                gear_ratio+=(adjacent_parts[0].get('part_number')*adjacent_parts[1].get('part_number'))
    print(gear_ratio)


def process_parts(symbol_list, part_list):
    '''
    Take part and symbol lists and return the sum of all parts, determined by which are adjacent to special symbols.
    '''
    required_parts = []
    for part in part_list:
        part_required = check_adjacency(part, symbol_list)
        if part_required == True:
            required_parts.append(part['part_number'])
    print(sum(required_parts))

def main():
    symbol_list, part_list, gear_list = read_input('day3_input.txt')
    process_parts(symbol_list, part_list)   
    get_gear_ratio(gear_list, part_list)

if __name__=="__main__":
    main()