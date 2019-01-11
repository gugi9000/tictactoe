from os import system, name 

def clear():
	if name == 'nt':
		_ = system('cls')

	# for mac and linux(here, os.name is 'posix')
	else:
		_ = system('clear')
	
board = [1,2,3,4,5,6,7,8,9]
turns = 0

print(board)

def draw_board(board):
	for x in range(0,len(board)):
		if ((x+1) % 3) != 0:
			print (board[x], end=' ')
		else:
			print (board[x]) 
			
def is_int(input):
	try:
		num = int(input)
	except ValueError:
		return False
	return True
	
def alike(a, b, c):
	return a == b and b == c

def winner(board):
	if alike(board[0], board[1], board[2]):
		return (board[0])
	elif alike(board[3], board[4], board[5]):
		return (board[3])
	elif alike(board[6], board[7], board[8]):
		return (board[6])
	elif alike(board[0], board[4], board[8]):
		return (board[0])
	elif alike(board[0], board[3], board[6]):
		return (board[0])
	elif alike(board[1], board[4], board[7]):
		return (board[1])
	elif alike(board[2], board[5], board[8]):
		return (board[8])
	elif alike(board[0], board[3], board[6]):
		return (board[0])
	elif alike(board[6], board[4], board[2]):
		return (board[2])
	else:
		return False

				
def available(board, piece, placement):
	if placement < 0 or placement > 9:
		return False
	else:
		if board[placement] == 'X' or board[placement] == 'O':
				return False
		else:
			return True


move = ''
player = 'X'
		
while move != 'q':
	clear()
	draw_board(board)
	print(f'Next player is {player}')
	move = input(f'Where do you want to place {player}? ')
	if is_int(move):
		move = int(move)
		move = move - 1
		if available(board, player, int(move)):
			board[int(move)] = player
			turns = turns + 1
		else:
			print('False move, turn passes.')
		if winner(board):
				print(f'Player {player} is the winner')
				draw_board(board)
				break
		if turns == 9:
			print(f'Turns out there are no available spots left.')		
			print(f'Game has tied.')
			break	
		if player == 'X':
			player = 'O'
		else:
			player = 'X'

print('Bye..')