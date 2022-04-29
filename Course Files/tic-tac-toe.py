'''
 _____  _               _____                      _____              
|_   _|(_)  ___        |_   _|  __ _   ___        |_   _|  ___    ___ 
  | |  | | / __| _____   | |   / _` | / __| _____   | |   / _ \  / _ \
  | |  | || (__ |_____|  | |  | (_| || (__ |_____|  | |  | (_) ||  __/
  |_|  |_| \___|         |_|   \__,_| \___|         |_|   \___/  \___|

Two people play Tic Tac Toe with paper and pencil. One player is X and the other player is O. 
Players take turns placing their X or O. If a player gets three of their marks on the pos in a row, 
column or one of the two diagonals, they win. When the pos fills up with neither player winning, the game ends in a draw.

Requirements:

  a)  2 players should be able to play the game (both sitting at the same computer)
  b)  The pos should be printed out every time a player makes a move
  c)  You should be able to accept input of the player position and then place a symbol on the pos
  d)  Check if the game is won,tied, lost, or ongoing.

  *** Bonus : Enable Option to play against computer (Implementing Artificial Intelegence [AI] )

Designing the Game:

1) User Interaction
2) Processing
3) Display the pos
    |-----|-----|-----|
    |  7  |  8  |  9  |
    |-----|-----|-----|
    |  4  |  5  |  6  |
    |-----|-----|-----|
    |  1  |  2  |  3  |
    |-----|-----|-----|
'''

__version__ = "1.0.0"
__maintainer__ = "Shantanu Datta"
__status__ = "Development"

# Required Libraries
#from distutils.log import debug
from os import system
import random
from time import *
from art import * #Library to display decorative text

def banner():
    ## Function to display a game banner using art Library
    system('clear')
    banner_text = text2art("Welcome\n to \n Tic-Tac-Toe\n Game")
    print(banner_text)
    print('{ Version: ', __version__,'}')
    print(100*'_',end=3*'\n')


def new_game():
    #Function to initiate a new game by getting user input
    attempt=0
    while True:
        print("\nPlease choose one of the following options:\n\n 1. Play against computer\n 2. Play against a Friend\n")
        ch_type = input("Please enter 1 or 2: ")
        if ch_type.isdigit and ch_type in ['1','2']:
            players = get_player_name(ch_type)
            return players
        else:
            banner()
            print(50*'*')
            print('\nEh! Invalid Entry. Please try again!\n')
            print(50*'*')
            attempt += 1

            if attempt > 3:
                print('\n\n Seems you are sleeping.. Try Again Later.')
                input()
                break


def get_player_name(game_type):
    #Function to get Player's Name
    if game_type=='2':
            player1 = input("\nEnter Name of Player 1: ").upper()
            player2 = input("Enter Name of Player 1: ").upper()
    else:
        player1 = input("Enter Your Name: ").upper()
        player2 = 'Computer'
    
    return [game_type,player1,player2]


def player_character():
    #Randomly choose Character for Players by Index ([Player1, Player 2])
    if random.randint(0,1) == 0:
        return ['X','O']
    else:
        return ['O','X']


def who_will_begin():
    ## Decide who will start first
    return random.randint(1,2)


def display_board(pos,game, marker):
    #Display Dynamic Board
    system('clear')
    print(text2art('Tic-Tac-Toe'))
    print(100*'=',end='\n\n')
    print(f'\033[1m{game[1]}\033[0m, your character is \033[1m"{marker[0]}"\033[0m, while \033[1m{game[2]}\033[0m will use \033[1m"{marker[1]}"\033[0m.\n\n')

    print(6*'\t', '\033[4m Game Key Layout \033[0m')
    print('\n\n|-----|-----|-----|','|-----|-----|-----|', sep=4*'\t')
    print(f'|  {pos[7]}  |  {pos[8]}  |  {pos[9]}  |', '|  7  |  8  |  9  |', sep=4*'\t')
    print('|-----|-----|-----|','|-----|-----|-----|', sep=4*'\t')
    print(f'|  {pos[4]}  |  {pos[5]}  |  {pos[6]}  |', '|  4  |  5  |  6  |', sep=4*'\t')
    print('|-----|-----|-----|','|-----|-----|-----|', sep=4*'\t')
    print(f'|  {pos[1]}  |  {pos[2]}  |  {pos[3]}  |', '|  1  |  2  |  3  |', sep=4*'\t')
    print('|-----|-----|-----|','|-----|-----|-----|', sep=4*'\t', end='\n\n')


def pos_is_free(board_pos, position):
    #Validate if desired Position is available
    return board_pos[position] == ' '


def get_move(board_pos,name):
    #Get User move a validate if move available
    position = 0
    
    while position not in [1,2,3,4,5,6,7,8,9] or not pos_is_free(board_pos, position):
        try:
            position = int(input(f'\033[1m{name}\033[0m make your next move: (1-9) '))
        except ValueError:
            pass

    return position


def pos_is_free(board_pos, position):
    #Validate if desired Position is available
    return board_pos[position] == ' '


def is_board_full(board_pos):
    #Check if board has no position left
    for i in range(1,10):
        if pos_is_free(board_pos, i):
            return False
    return True


def update_board(board_pos, marker, position):
    #update board with Player selection
    board_pos[position] = marker


def find_winner(board_pos,mark):
    #Find if Current player has won the game
    return ((board_pos[7] == mark and board_pos[8] == mark and board_pos[9] == mark) or # across the top
    (board_pos[4] == mark and board_pos[5] == mark and board_pos[6] == mark) or # across the middle
    (board_pos[1] == mark and board_pos[2] == mark and board_pos[3] == mark) or # across the bottom
    (board_pos[7] == mark and board_pos[4] == mark and board_pos[1] == mark) or # down the middle
    (board_pos[8] == mark and board_pos[5] == mark and board_pos[2] == mark) or # down the middle
    (board_pos[9] == mark and board_pos[6] == mark and board_pos[3] == mark) or # down the right side
    (board_pos[7] == mark and board_pos[5] == mark and board_pos[3] == mark) or # diagonal
    (board_pos[9] == mark and board_pos[5] == mark and board_pos[1] == mark)) # diagonal


''' Let's make the computer play the game with you '''
#region Code for AI

def duplicate_board(board_pos):
    #Create a duplicate Board 
    dup_board=[]

    for i in board_pos:
        dup_board.append(i)
    
    return dup_board


def get_random_move(board_pos, move_list):
    #Return a Valid move from given list
    valid_move =[]

    for i in move_list:
        if pos_is_free(board_pos,i):
            valid_move.append(i)

    if len(valid_move)!=0:
        return random.choice(valid_move)
    else:
        return None


def ai_player_move(board_pos, c_mark):
    lm = lambda com: 'O' if com == 'X' else 'X'
    u_mark = lm(c_mark)

    #Define the AI Parameters to determine the next move

    #Validate if Computer can win in next move
    for i in range(1,10):
        copy_board = duplicate_board(board_pos)
        if pos_is_free(copy_board,i):
            update_board(copy_board,c_mark,i)
            if find_winner(copy_board,c_mark):
                return i
    

    #Can the Player win on the next move? If yes, block the move
    for i in range(1,10):
        copy_board = duplicate_board(board_pos)
        if pos_is_free(copy_board,i):
            update_board(copy_board,u_mark,i)
            if find_winner(copy_board,u_mark):
                return i
    
    #Get Any Corner
    ai_move = get_random_move(board_pos, [1,3,7,9])
    if ai_move != None:
        return ai_move
    
    #capture the Centre
    if pos_is_free(board_pos,5):
        return 5
    
    #or else make side moves
    return get_random_move(board_pos,[2,4,6,8])

#endregion


def start_game(game):
    #Game controller
    while True:
        system('clear')
        in_game = True
        marker = player_character() # Return X or O

        board_pos = [' '] * 10 #Setting initial Board Structure
        current_player = game[who_will_begin()]
        print(f'{current_player} - You go first\n')        
        display_board(board_pos, game, marker)


        while in_game:

            #Check Game Mode
            if game[0] == '2': #play 1 on 1

                if current_player == game[1]:
                    display_board(board_pos, game, marker)

                    position = get_move(board_pos, game[1])
                    update_board(board_pos,marker[0], position)

                    if find_winner(board_pos,marker[0]):
                        display_board(board_pos, game, marker)
                        print(f'\n \033[1mCongratulation! {game[1]} has own the game!\033[0m')
                        in_game = False
                    else:
                        if is_board_full(board_pos):
                            display_board(board_pos, game, marker)
                            print(f'It\'s a draw!\n\n')
                            break
                        else:
                            current_player = game[2]
                
                else:
                    display_board(board_pos, game, marker)

                    position = get_move(board_pos,game[2])
                    update_board(board_pos,marker[1], position)

                    if find_winner(board_pos,marker[1]):
                        display_board(board_pos, game, marker)
                        print(f'\n \033[1mCongratulation! {game[2]} has own the game!\033[0m')
                        in_game = False
                    else:
                        if is_board_full(board_pos):
                            display_board(board_pos, game, marker)
                            print(f'It\'s a draw!\n\n')
                            break
                        else:
                            current_player = game[1]

            else: #play against Computer
                if current_player == game[1]:
                    display_board(board_pos, game, marker)

                    position = get_move(board_pos, game[1])
                    update_board(board_pos,marker[0], position)

                    if find_winner(board_pos,marker[0]):
                        display_board(board_pos, game, marker)
                        print(f'\n \033[1mCongratulation! {game[1]} has own the game!\033[0m')
                        in_game = False
                    else:
                        if is_board_full(board_pos):
                            display_board(board_pos, game, marker)
                            print(f'\n \033[1mIt\'s a draw!\033[0m\n\n')
                            break
                        else:
                            current_player = game[2]

                else:
                    display_board(board_pos, game, marker)

                    position = ai_player_move(board_pos,marker[1])
                    update_board(board_pos,marker[1], position)

                    if find_winner(board_pos,marker[1]):
                        display_board(board_pos, game, marker)
                        print(f'\n \033[1mOuch! {game[2]} has own the game! \033[0m')
                        in_game = False
                    else:
                        if is_board_full(board_pos):
                            display_board(board_pos, game, marker)
                            print(f'\n \033[1mIt\'s a draw!\033[0m\n\n')
                            break
                        else:
                            current_player = game[1]

        if input('\n\nDo you want to Play Again? (y/n): ').lower() != 'y':
            print('\n\nThank you for playing Tic-Tac-Toe!!!')
            input()
            system('clear')
            break



if __name__ == '__main__':
    
    banner()
    game = new_game()
    start_game(game)