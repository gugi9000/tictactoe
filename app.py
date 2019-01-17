from os import system, name


def clear():
    if name == "nt":
        _ = system("cls")
    else:
        _ = system("clear")


def draw_board(board):
    for x in range(0, len(board)):
        if ((x + 1) % 3) != 0:
            print(board[x], end=" ")
        else:
            print(board[x])


def is_int(input):
    try:
        _ = int(input)
    except ValueError:
        return False
    return True


def winner(board):
    win_cases = [ (1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7), (2, 5, 8), (3, 6, 9), (1, 5, 9), (3, 5, 7), ]
    for item in win_cases:
        if board[item[0] - 1] == board[item[1] - 1] and board[item[1] - 1] == board[item[2] - 1]:
            return True
    return False


def available(board, piece, placement):
    if placement < 0 or placement > 9:
        return False
    else:
        if board[placement] == "X" or board[placement] == "O":
            return False
        else:
            return True


player = "X"
board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
turns = 0
while True:
    if turns == 9:
        print(f"Turns out there are no available spots left.")
        print(f"Game has tied.")
        break
    clear()
    draw_board(board)
    move = input(f"Where do you want to place {player}? ")
    if is_int(move):
        move = int(move) - 1 
        if available(board, player, move):
            board[int(move)] = player
            turns = turns + 1
        if winner(board):
            print(f"Player {player} is the winner")
            draw_board(board)
            break
        if player == "X":
            player = "O"
        else:
            player = "X"
print("Bye..")