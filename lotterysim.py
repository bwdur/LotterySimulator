import random

def num_matches():
    matches = set(my_numbers).intersection(winning_numbers)
    return len(matches)

def calc_win():
    matches = num_matches()
    powerball_win = (winning_powerball == my_powerball)
    winnings = 0

    if powerball_win:
        if matches == 2:
            winnings = 7
        elif matches == 3:
            winnings = 100
        elif matches == 4:
            winnings = 50000
        elif matches == 5:
            JACKPOT = True
            winnings = JACKPOT_AMOUNT
        else:
            winnings = 4
    else:
        if matches == 3:
            winnings = 7
        elif matches == 4:
            winnings = 100
        elif matches == 5:
            winnings = 1000000

    if PER_POWERPLAY == 1:
        powerplay = random.randint(1,NUM_POWERPLAY_BALLS)
        if powerplay <= 24:
            powerplay_multiplier = 2
        if powerplay > 24 and powerplay <= 37:
            powerplay_multiplier = 3
        if powerplay > 37 and powerplay <= 40:
            powerplay_multiplier = 4
        if powerplay > 40:
            powerplay_multiplier = 5

        if winnings < 1000000:
            winnings *= powerplay_multiplier
        elif winnings == 1000000:
            winnings *= 2
    return winnings

MAX_NUM = 69
MAX_POWERBALL = 26
NUM_POWERPLAY_BALLS = 42
PER_TICKET = 2
# set to 0 to turn off powerplay
PER_POWERPLAY = 1
JACKPOT = False
JACKPOT_AMOUNT = 650000000
dollars_won = 0
dollars_played = 0
count = 0
my_numbers = [8,9,14,38,44]
my_powerball = 11

while JACKPOT == False:
    balls = [x for x in range(1,MAX_NUM+1)]
    winning_powerball = random.randint(1,MAX_POWERBALL)
    winning_numbers = []

    for x in range(1,6):
        winning_index = random.randint(1,MAX_NUM-x)
        winning_numbers.append(balls[winning_index])
        balls.pop(winning_index)

    dollars_won += calc_win()
    dollars_played += 2 + PER_POWERPLAY
    count += 1
    if count % 10000000 == 0:
        print ("Net dollars: %s" % (dollars_won - dollars_played))
        print ("Num tickets: %s" % count)
print("It took this many times to win the Jackpot: %s" % count)
print("You won %s" % dollars_won)
print("But it cost you %s" % dollars_played)