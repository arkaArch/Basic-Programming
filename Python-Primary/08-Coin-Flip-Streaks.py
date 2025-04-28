import random
six_in_a_row = 0

for experiment_number in range(10000):
    # Creates a list of 100 'heads' or 'tails' values
    coin_flip_result = []
    for flip in range(100):
        if random.randint(0, 1) == 1:
            coin_flip_result.append('H')
        else:
            coin_flip_result.append('T')

    streak_a_row = 1;   # For first 'H' or 'T'
    for i in range(len(coin_flip_result) - 1):
        if(coin_flip_result[i] == coin_flip_result[i+1]):
            streak_a_row += 1;
        else:
            streak_a_row = 0;
    
        # Check if streak of six heads or six tails in a row
        if(streak_a_row == 6):
            six_in_a_row += 1
            # Count again from zero
            streak_a_row = 0

print('Chance of streak: %s%%' % (six_in_a_row / 100))



