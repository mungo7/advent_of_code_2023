import re

def read_input(input):
    processed_cards=[]
    with open(input) as f:
        for line in f:
            line = re.sub('Card\s+\d+:\s+', "", line)
            split_line = line.split('|')
            winning_numbers=[int(num) for num in re.split('\s+', split_line[0].strip())]
            given_numbers=[int(num) for num in re.split('\s+', split_line[1].strip())]
            print(winning_numbers, ' | ',  given_numbers)
            card={'winning_numbers' : winning_numbers, 'given_numbers' : given_numbers}
            processed_cards.append(card)
    return processed_cards

def count_points(processed_cards):
    total_points=0
    for card in processed_cards:
        points=0
        for number in card['given_numbers']:
            if number in card['winning_numbers']:
                if points == 0:
                    points+=1
                else:
                    points*=2
        total_points+=points
    print('Total points:', total_points)
    return total_points

def main():
    processed_cards = read_input('day4/day4_input.txt')
    count_points(processed_cards)
    return

if __name__=="__main__":
    main()