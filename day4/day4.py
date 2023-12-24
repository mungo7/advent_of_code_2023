import re

def read_input(input):
    processed_cards=[]
    with open(input) as f:
        for line in f:
            card_number = re.search('\d+', line).group(0)
            line = re.sub('Card\s+\d+:\s+', "", line)
            split_line = line.split('|')
            winning_numbers=[int(num) for num in re.split('\s+', split_line[0].strip())]
            given_numbers=[int(num) for num in re.split('\s+', split_line[1].strip())]
            card={'card_number' : card_number, 'winning_numbers' : winning_numbers, 'given_numbers' : given_numbers, 'instances' : 1}
            processed_cards.append(card)
    return processed_cards

def count_points(card):
    points=0
    for number in card['given_numbers']:
        if number in card['winning_numbers']:
            if points == 0:
                points+=1
            else:
                points*=2
    return points

def count_cards(card):
    points=0
    for number in card['given_numbers']:
        if number in card['winning_numbers']:
            points+=1
    return points

def add_won_cards(processed_cards):
    for card in processed_cards:
        card_number = int(card['card_number'])
        new_cards_num = count_cards(card)
        for num in range(1, new_cards_num+1):
            if card_number+num < len(processed_cards)+1:
                processed_cards[card_number+num-1]['instances']+=(1*card['instances'])

    return processed_cards

def sum_cards(processed_cards):
    sum=0
    for card in processed_cards:
        sum+=card['instances']
    return sum

def main():
    processed_cards = read_input('day4/day4_input.txt')
    total_points=0
    for card in processed_cards:
        points = count_points(card)
        total_points += points
    print('Total points:', total_points)
    processed_cards = add_won_cards(processed_cards)
    sum = sum_cards(processed_cards)
    print('Sum of all cards:', sum)

if __name__=="__main__":
    main()
