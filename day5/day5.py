# Was able to complete part 1 with this code, but wasn't able to complete part 2. See day5_2 for part 2 code.

import sys
def convert_number(source_number, maps):
    #print('source number', source_number)
    converted_number=source_number
    #print(map)
    for subset in maps:
        #print(subset)
        source_range_start=subset['source_range_start']
        dest_range_start=subset['dest_range_start']
        range_length=subset['range_length']
        if source_number in range(source_range_start, source_range_start+range_length):
            distance_from_source_start=source_number-source_range_start
            converted_number=dest_range_start+distance_from_source_start
    #print('converted number', converted_number)
    return converted_number

def get_lowest_number(seed_range, maps):
    lowest_converted_number=int(sys.maxsize)
    for set in seed_range:
        print(set)
        start=set[0]
        length=set[1]
        for seed in range(start,start+length):
            source_number = seed
            for map in maps:
                #print('source number', source_number)
                source_number = convert_number(source_number, maps[map])
            if source_number<lowest_converted_number:
                #print(source_number, lowest_converted_number)
                lowest_converted_number=source_number
                #print('location number', source_number)
    return lowest_converted_number

def read_input(input):
    with open(input) as f:
        almanac = f.readlines()
        first_line = list(map(int, almanac[0].strip().split(' ')[1:]))
        seed_ranges = []
        for start, length in zip(first_line[0::2], first_line[1::2]):
            print(start, length)
            start, length = int(start), int(length)
            seed_ranges.append([start, length])
        print(seed_ranges)
        maps={}
        current_map=None
        for line in almanac[2:]:           
            if not line.strip():
                continue
            if line.endswith('map:\n'):
                current_map=line.split()[0]
                maps[current_map] = []
                print(current_map)
            else:
                dest_range_start, source_range_start, range_length = map(int, line.split())
                maps[current_map].append({'dest_range_start': dest_range_start, 'source_range_start': source_range_start, 'range_length': range_length})
        for x, y in enumerate(maps):
            print(x, y)
        return seed_ranges, maps

def main():
    seed_ranges, maps = read_input('day5/day5_input.txt')
    lowest_number = get_lowest_number(seed_ranges,maps)
    print('lowest number is', lowest_number)
    return

if __name__=="__main__":
    main()