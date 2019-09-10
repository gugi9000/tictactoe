from os import system, name


def draw_board(board):
    for line in board:  # FIXME: This should print pretty with
        for piece in line:  # FIXME: varied length numbers
            print(piece, end=" ")
        print()


def winner(board, dim=3):
    for line in board:
        if len(set(line)) == 1:
            return True
    for x in range(dim):
        if len(set(([board[y][x] for y in range(dim)]))) == 1:
            return True
    if len(set([board[i][j] for i, j in enumerate(range(dim - 1, -1, -1))])) == 1:
        return True
    if len(set([board[i][i] for i in range(dim)])) == 1:
        return True
    return False


def pos_from_move(move, dim=3):
    if move < dim:
        return (0, move)
    return (move // dim, move % dim)


def play(board, placement, turns):
    if placement < 0 or placement > 9:  # FIXME: This doesn't care about dimensions
        return turns
    else:
        x, y = pos_from_move(placement)
        if board[x][y] == "X" or board[x][y] == "O":
            return turns
        else:
            board[x][y] = player  # FIXME: How is the global board affected?
            return turns + 1


player = "X"
board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]  # FIXME: This should care about dimensions
turns = 0
while True:
    if turns == len(board) * len(board):
        print(f"Turns out there are no available spots left.")
        print(f"Game has tied.")
        break
    system("cls" if name == "nt" else "clear")
    draw_board(board)
    move = input(f"Where do you want to place {player}? ")
    if move.isdigit():
        move = int(move) - 1
        turns = play(board, move, turns)
        if winner(board):
            print(f"Player {player} is the winner")
            break
        player = "O" if player == "X" else "X"
draw_board(board)
print("Bye..")
