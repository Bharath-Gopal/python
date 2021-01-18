#Tic Tac Toe
import random

board = {'1':' ','2':' ','3':' ',
         '4':' ','5':' ','6':' ',
         '7':' ','8':' ','9':' ',}

board_keys = []
for key in board:
    board_keys.append(key)

def print_board(tb):
    print(tb['1']+ '|' +tb['2']+ '|' +tb['3'])
    print('-+-+-')
    print(tb['4']+ '|' +tb['5']+ '|' +tb['6'])
    print('-+-+-')
    print(tb['7']+ '|' +tb['8']+ '|' +tb['9'])

def game():
    turn = 'X'
    count = 0

    for i in range(10):
        if turn == 'X':
            print_board(board)
            print("It is the User's turn. Enter position")
            move = input()
            if board[move] == ' ':
                board[move] = turn
                count += 1
            else :
                print("Position already filled. Please pick another position.")
                continue

        if turn == 'O':
            print_board(board)
            print("It is the Computer's turn.")
            move = str(random.randint(1,9))
            if board[move] == ' ':
                board[move] = turn
                count += 1
            else:
                while board[move] != ' ':
                    move = str(random.randint(1,9))
                if board[move] == ' ':
                    board[move] = turn
                    count += 1

            print(move)
        
        if count>= 5:
            if board['1'] == board['2'] == board['3'] != ' ':
                print_board(board)
                print("\nGAME OVER!\n")
                if board['1'] == 'X':
                    print("USER WON!")
                else :
                    print("COMPUTER WON!")
                break
            elif board['4'] == board['5'] == board['6'] != ' ':
                print_board(board)
                print("\nGAME OVER!\n")
                if board['4'] == 'X':
                    print("USER WON!")
                else :
                    print("COMPUTER WON!")
                break
            elif board['7'] == board['8'] == board['9'] != ' ':
                print_board(board)
                print("\nGAME OVER!\n")
                if board['7'] == 'X':
                    print("USER WON!")
                else :
                    print("COMPUTER WON!")
                break
            elif board['1'] == board['4'] == board['7'] != ' ':
                print_board(board)
                print("\nGAME OVER!\n")
                if board['1'] == 'X':
                    print("USER WON!")
                else :
                    print("COMPUTER WON!")
                break
            elif board['2'] == board['5'] == board['8'] != ' ':
                print_board(board)
                print("\nGAME OVER!\n")
                if board['2'] == 'X':
                    print("USER WON!")
                else :
                    print("COMPUTER WON!")
                break
            elif board['3'] == board['6'] == board['9'] != ' ':
                print_board(board)
                print("\nGAME OVER!\n")
                if board['3'] == 'X':
                    print("USER WON!")
                else :
                    print("COMPUTER WON!")
                break
            elif board['1'] == board['5'] == board['9'] != ' ':
                print_board(board)
                print("\nGAME OVER!\n")
                if board['1'] == 'X':
                    print("USER WON!")
                else :
                    print("COMPUTER WON!")
                break
            elif board['3'] == board['5'] == board['7'] != ' ':
                print_board(board)
                print("\nGAME OVER!\n")
                if board['3'] == 'X':
                    print("USER WON!")
                else :
                    print("COMPUTER WON!")
                break
        
        if count == 9:
            print("\nGAME OVER\n")
            print("IT IS A DRAW!")
        
        if turn == 'X':
            turn = 'O'
        else :
            turn = 'X'
    
    restart = input("Do want to play Again?(y/n)")
    if restart == "y" or restart == "Y":  
        for key in board_keys:
            board[key] = " "
        game()

if __name__ == "__main__":
    game() 
            