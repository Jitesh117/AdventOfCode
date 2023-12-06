with open('day4/input.txt', 'r') as file:
    input_text = file.read()
lines = input_text.split('\n')

def parse_games(lines):
    cards = [1] * len(lines)
    games = []
    for line in lines:
        game = line.split(': ')[1]
        games.append(game) 
    winning_nums = []
    # for game in games:
        # print(game)
    player_nums = []
    for game in games:
        winning_nums.append(game.split('|')[0])
        player_nums.append(game.split('|')[1])
    wins = []
    plays = []
    for win in winning_nums:
        wins.append(win.split())
    for play in player_nums:
        plays.append(play.split())
    
    result = 0
    for i in range(len(lines)):
        count = 0 
        for win in wins[i]:
            if win in plays[i]: 
                count = count + 1
        result += count 
        for j in range(count):
            cards[i + j + 1] += cards[i]
    result_a = result
    result_b = sum(cards)  
    print(result_a)
    print(result_b)

parse_games(lines)
    


