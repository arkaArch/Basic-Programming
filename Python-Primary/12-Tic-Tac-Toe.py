the_board = {'top_l': ' ', 'top_m': ' ', 'top_r': ' ',
             'mid_l': ' ', 'mid_m': ' ', 'mid_r': ' ',
             'low_l': ' ', 'low_m': ' ', 'low_r': ' '}

def print_board(board):
    print(' ' + board['top_l'] + ' | ' + board['top_m'] + ' | ' + board['top_r'] + ' ')
    print('---+---+---')
    print(' ' + board['mid_l'] + ' | ' + board['mid_m'] + ' | ' + board['mid_r'] + ' ')
    print('---+---+---')
    print(' ' + board['low_l'] + ' | ' + board['low_m'] + ' | ' + board['low_r'] + ' ')

turn = 'X'

for i in range(9):

    # Checks for right input
    while True:
        move = input('Turn for ' + turn + '. Move on which space? ')
        # Postion must be empty
        if(move in the_board.keys() and the_board[move] == ' '):
            the_board[move] = turn
            break
        else:
            print('Make a right move')
            continue
    
    # Check winning condition: 
    if(the_board['top_l'] == the_board['top_m'] == the_board['top_r'] != ' ' or
        the_board['mid_l'] == the_board['mid_m'] == the_board['mid_r'] != ' ' or
        the_board['low_l'] == the_board['low_m'] == the_board['low_r'] != ' ' or
        the_board['top_l'] == the_board['mid_l'] == the_board['low_l'] != ' ' or
        the_board['top_m'] == the_board['mid_m'] == the_board['low_m'] != ' ' or
        the_board['top_r'] == the_board['mid_r'] == the_board['low_r'] != ' ' or
        the_board['top_l'] == the_board['mid_m'] == the_board['low_r'] != ' ' or
        the_board['top_r'] == the_board['mid_m'] == the_board['low_l'] != ' '):
        print("GAME OVER.")
        print(turn + ' WON')
        break
    
    if turn == 'X': turn = 'O'
    else: turn = 'X'

    print_board(the_board)
