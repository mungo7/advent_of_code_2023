import re
file = open('day2_input.txt')

limit_red=12
limit_green=13
limit_blue=14
successful_games=[]

for line in file:
    game_number=int(re.search('\d+', line).group(0))
    line = re.sub('Game \d+:\s', "", line)
    games = line.split(';')
    fail_flag=False
    for game in games:
        game = game.strip()
        draws = game.split(',')
        for draw in draws:
            draw=draw.strip()
            number = int(re.search('\d+', draw).group(0))
            colour = re.search('[a-zA-Z]+', draw).group(0)
            print(number)
            print(colour)
            if colour == 'red' and int(number) > limit_red:
                fail_flag=True
            if colour == 'green' and int(number) > limit_green:
                fail_flag=True
            if colour == 'blue' and int(number) > limit_blue:
                fail_flag=True
    if fail_flag == False:
        successful_games.append(game_number)
print(sum(successful_games))

file.close()


## Make sure to close the file if just using open. Otherwise use 'with open(file) as f'
## Learned some regex here.
## 