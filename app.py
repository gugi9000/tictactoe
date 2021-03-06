from os import system, name


def draw_board(board, dim):
    prefix = len(str(dim * dim))
    for line in board:
        for piece in line:
            print(f"{piece:{prefix}}", end=" ")
        print()


def winner(board, dim):
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


def pos_from_move(move, dim):
    if move < dim:
        return (0, move)
    return (move // dim, move % dim)


def play(board, placement, turns):
    if placement < 0 or placement > dim * dim:
        return turns
    else:
        x, y = pos_from_move(placement, dim)
        if board[x][y] == "X" or board[x][y] == "O":
            return turns
        else:
            board[x][y] = player
            return turns + 1


player = "X"
dim = 12
board = list(map(list, zip(*[iter([x for x in range(1, dim * dim + 1)])] * dim)))
turns = 0
while True:
    if turns == dim * dim:
        print(f"Turns out there are no available spots left.")
        print(f"Game has tied.")
        break
    system("cls" if name == "nt" else "clear")
    draw_board(board, dim)
    move = input(f"Where do you want to place {player}? ")
    if move.isdigit():
        turns = play(board, int(move) - 1, turns)
        if winner(board, dim):
            print(f"Player {player} is the winner")
            break
        player = "O" if player == "X" else "X"
draw_board(board, dim)
print("Bye..")
