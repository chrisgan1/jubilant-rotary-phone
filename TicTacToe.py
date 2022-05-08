from curses import nocbreak
import os
import random

board = [' '] * 10

def clear():
    os.system('cls')

def display_board(board):
    clear()

    print(board[0]+'|'+board[1]+'|'+board[2])
    print('-|-|-')
    print(board[3]+'|'+board[4]+'|'+board[5])
    print('-|-|-')
    print(board[6]+'|'+board[7]+'|'+board[8])

def player_input():
    marker = ''

    while marker != 'X' and marker != 'O':
        marker = input("Player 1, choose X or O: ").upper()

    if marker == 'X':
        return('X', 'O')
    else:
        return('O', 'X')

def place_marker(board, marker, position):

    position = 'WRONG'

    while position not in [0,1,2,3,4,5,6,7,8]:
        position = int(input("Enter the position you would like to place a marker at: "))

        if position not in [0,1,2,3,4,5,6,7,8]:
            print("Must be between 0 and 9! ")

    board[position] = marker

def win_check(board, mark):

    return ((board[7] == mark and board[8] == mark and board[9] == mark) or # across the top
    (board[4] == mark and board[5] == mark and board[6] == mark) or # across the middle
    (board[1] == mark and board[2] == mark and board[3] == mark) or # across the bottom
    (board[7] == mark and board[4] == mark and board[1] == mark) or # down the middle
    (board[8] == mark and board[5] == mark and board[2] == mark) or # down the middle
    (board[9] == mark and board[6] == mark and board[3] == mark) or # down the right side
    (board[7] == mark and board[5] == mark and board[3] == mark) or # diagonal
    (board[9] == mark and board[5] == mark and board[1] == mark))

def choose_first():
    player_first = random.randint(0,1)

    if player_first == 0:
        return 'Player 1'
    else:
        return 'Player 2'


def space_check(board, position):

    if board[position] == ' ':
        print("Position is free! ")
        return True
    else:
        print("Position taken! ")
        return False

def full_board_check(board):

    if ' ' not in board:
        print("Board is full! ")
        return True
    else:
        return False

def player_check(board):

    player_check = 'WRONG'
    
    while player_check not in [0,1,2,3,4,5,6,7,8]:
        player_check = int(input("Please choose a number between 0 and 8 to check: "))

        if player_check not in [0,1,2,3,4,5,6,7,8]:
            print("Choose again! ")

    if board[int(player_check)] == ' ':
        print("Free!")
        return player_check
    else:
        return False

def play_again():

    replay = 'WRONG'

    while replay not in ['Y', 'N']:

        replay = input("Would you like to play again? Y or N: ")

        if replay not in ['Y', 'N']:
            print("Sorry, I don't understand! ")

    if replay == 'Y':
        return True
    else:
        return False

print("Welcome to Tic Tac Toe! ")

while True:

    board = [' '] * 10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn + ' will go first.')

    start_game = input('Are you ready to play? Enter Y or N: ')

    if start_game.lower() == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == 'Player 1':
            display_board(board)
            position = player_check(board)
            place_marker(board, player1_marker, position)

            if win_check(board, player1_marker):
                display_board(board)
                print('Congratulations! You have won the game!')
                game_on = False
            else:
                if full_board_check(board):
                    display_board(board)
                    print('Game is a draw!')
                    break
                else:
                    turn = 'Player 2'
        
        else:
            display_board(board)
            position = player_check(board)
            place_marker(board, player2_marker, position)

            if win_check(board, player2_marker):
                display_board(board)
                print('Congratulations! You have won the game!')
                game_on = False
            else:
                if full_board_check(board):
                    display_board(board)
                    print('Game is a draw!')
                    break
                else:
                    turn = 'Player 1'

    if not play_again():
        break






