def convert_number(source_number, map):
    #print('source number', source_number)
    converted_number=source_number
    #print(map)
    for subset in map:
        print(subset)
        source_range_start=subset['source_range_start']
        dest_range_start=subset['dest_range_start']
        range_length=subset['range_length']
        if source_number in range(source_range_start, source_range_start+range_length):
            distance_from_source_start=source_number-source_range_start
            converted_number=dest_range_start+distance_from_source_start
    #print('converted number', converted_number)
    return converted_number

def get_lowest_number(seeds, maps):
    converted_numbers=[]
    for seed in seeds:
        source_number = seed
        for map in maps:
            print('seed number', source_number)
            source_number = convert_number(source_number, maps[map])
            print('location number', source_number)
        converted_numbers.append(source_number)
    return min(converted_numbers)

def read_input(input):
    with open(input) as f:
        almanac = f.readlines()
        seeds = list(map(int, almanac[0].strip().split(' ')[1:]))
        print(seeds)
        maps={}
        current_map=None
        for line in almanac[2:]:           
            #print(line, end='')
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
        print(maps)
        return seeds, maps

def main():
    seeds, maps = read_input('day5/day5_input.txt')
    lowest_number = get_lowest_number(seeds,maps)
    print('lowest number is', lowest_number)
    return

if __name__=="__main__":
    main()