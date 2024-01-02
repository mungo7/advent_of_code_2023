def read_input(input):
    times, distances = open(input).read().split('\n')
    time = int(times.split(':')[1].replace(' ', ''))
    distance = int(distances.split(':')[1].replace(' ', ''))
    print(time, distance)
    race = (time, distance)
    print(race)
    return race

def run_race(race):
    time_ms, distance_mm = race
    wins = 0
    for button_hold_time_ms in range(0, time_ms):
        velocity_ms = button_hold_time_ms * 1 
        distance_travelled_mm = velocity_ms * (time_ms - button_hold_time_ms)
        if distance_travelled_mm > distance_mm:
            wins += 1
    return wins

def main():
    race = read_input('day6/day6_input.txt')
    race_wins = run_race(race)
    print(race_wins)
    return

if __name__=='__main__':
    main()