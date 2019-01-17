import pygame
from random import choice
from time import sleep

spots_taken = [1, 2, 3, 4, 5, 6, 7, 8, 9]
board_pos = {
		"pos_1": (130, 95),
		"pos_2": (400, 95),
		"pos_3": (670, 95),
		"pos_4": (130, 300),
		"pos_5": (400, 300),
		"pos_6": (670, 300),
		"pos_7": (130, 505),
		"pos_8": (400, 505),
		"pos_9": (670, 505)
		}

# this might seem strange, but let's pretend to dict was a bad idea
# and that I don't feel like making a case for deleting it yet.

positions = []
for _ in board_pos.values():
    positions.append(_)


BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE =  ( 70,  70, 200)
GREEN = (  0, 255,   0)
RED =   (200,  30,  30)
position = (0, 0)
player_1 = ''
player_2 = ''
localgame = False
multiplayer = False
player_turn = 'X'

# set screen size (x,y)
screen_width = 800
screen_height = 600

# draw main menu
def main_menu(screen):
	# localgame box
	pygame.draw.line(screen, BLUE, [300, 200],[500, 200], 10)
	pygame.draw.line(screen, BLUE, [300, 300],[500, 300], 10)
	pygame.draw.line(screen, BLUE, [300, 200],[300, 300], 10)
	pygame.draw.line(screen, BLUE, [500, 200],[500, 300], 10)
	# multiplayer box
	pygame.draw.line(screen, BLUE, [300, 330],[500, 330], 10)
	pygame.draw.line(screen, BLUE, [300, 430],[500, 430], 10)
	pygame.draw.line(screen, BLUE, [300, 330],[300, 430], 10)
	pygame.draw.line(screen, BLUE, [500, 330],[500, 430], 10)

# draw game components
def draw_cross(screen, x, y):
	#  a    b
	#    \/
	#    /\
	#  c   d
	offset = 65
	a = [x-offset,y-offset]
	b = [x+offset,y-offset]
	c = [x-offset,y+offset]
	d = [x+offset,y+offset]
	pygame.draw.line(screen, GREEN, a, d, 20)
	pygame.draw.line(screen, GREEN, b, c, 20)

def draw_circle(screen, x, y):
	pygame.draw.circle(screen, RED, [x , y], 75, 14)

def draw_board(screen):
	pygame.draw.line(screen, BLUE, [267, 0],[267, 600], 20)
	pygame.draw.line(screen, BLUE, [534, 0],[534, 600], 20)
	pygame.draw.line(screen, BLUE, [0, 200],[800, 200], 20)
	pygame.draw.line(screen, BLUE, [0, 400],[800, 400], 20)

def draw_cursor(screen, x, y):
	pygame.draw.circle(screen, WHITE, [x, y], 10)

def draw_markers(screen, position):
	global spots_taken
	x, y = position
	# loop the spots list and check if any of the spots are taken
	# this function goes hand in hand with input_system due to
	# spots_taken[board_position] = player (player being X or O) 
	for i in range(len(spots_taken)):
		if spots_taken[i] == 'X':  
			draw_cross(screen, x, y)
		elif spots_taken[i] == 'O':
			draw_circle(screen, x, y)

def switch_turn():
	global player_turn
	if player_turn == 'X':
		player_turn = 'O'
	elif player_turn == 'O':
		player_turn = 'X'

def input_system(mouse_x, mouse_y, first_start, player, choose_marker, screen):
	global player_1, player_2, marker_spots, position, localgame, multiplayer, cur_round, last_round
	# check if mouse1 is pressed
	if pygame.mouse.get_pressed()[0] == True:
		print("Mouse is clicked")
		if first_start == True:
			# if mouse is within local game region
			if mouse_x >= 300 and mouse_x <= 500:
				if mouse_y >= 200 and mouse_y <= 300:
					localgame = True
			# if mouse is within multiplayer region
			if mouse_x >= 300 and mouse_x <= 500:
				if mouse_y >= 330 and mouse_y <= 430:
					multiplayer = True
		else:
			if choose_marker == True:
				# if mouse is within x region
				if mouse_x >= 170 and mouse_x <= 330:
					if mouse_y >= 170 and mouse_y <= 330:
						player_1 = 'X'
						player_2 = 'O'
				# if mouse is within o region
				if mouse_x >= 470 and mouse_x <= 630:
					if mouse_y >= 170 and mouse_y <= 330:
						player_1 = 'O'
						player_2 = 'X'
			else:
				# check if mouse is within any box region
				if mouse_x <= 267:
					if mouse_y <= 200:
						if spots_taken[0] != 1:
							return False
						else:
							spots_taken[0] = player
							position = board_pos["pos_1"]
				if mouse_x >= 287 and mouse_x <= 534:
					if mouse_y <= 200:
						if spots_taken[1] != 2:
							return False
						else:
							spots_taken[1] = player
							position = board_pos["pos_2"]
				if mouse_x >= 554:
					if mouse_y <= 200:
						if spots_taken[2] != 3:
							return False
						else:
							spots_taken[2] = player
							position = board_pos["pos_3"]
				if mouse_x <= 267:
					if mouse_y >= 220 and mouse_y <= 400:
						if spots_taken[3] != 4:
							return False
						else:
							spots_taken[3] = player
							position = board_pos["pos_4"]
				if mouse_x >= 287 and mouse_x <= 534:
					if mouse_y >= 220 and mouse_y <= 400:
						if spots_taken[4] != 5:
							return False
						else:
							spots_taken[4] = player
							position = board_pos["pos_5"]
				if mouse_x >= 554:
					if mouse_y >= 220 and mouse_y <= 400:
						if spots_taken[5] != 6:
							return False
						else:
							spots_taken[5] = player
							position = board_pos["pos_6"]
				if mouse_x <= 267:
					if mouse_y >= 420:
						if spots_taken[6] != 7:
							return False
						else:
							spots_taken[6] = player
							position = board_pos["pos_7"]
				if mouse_x >= 287 and mouse_x <= 534:
					if mouse_y >= 420:
						if spots_taken[7] != 8:
							return False
						else:
							spots_taken[7] = player
							position = board_pos["pos_8"]
				if mouse_x >= 554:
					if mouse_y >= 420:
						if spots_taken[8] != 9:
							return False
						else:
							spots_taken[8] = player
							position = board_pos["pos_9"]
				
				if winner_check(spots_taken) == False:
					switch_turn()

# toggle fullscreen (ON/OFF)
def toggle_fullscreen(fullscreen):
	if fullscreen:
		screen = pygame.display.set_mode((screen_width,screen_height), pygame.RESIZABLE)
	else:
		screen = pygame.display.set_mode((screen_width,screen_height), pygame.FULLSCREEN)
	return not fullscreen


def alike(a, b, c):
	return a == b and b == c


# check if there's a winning play on the board
def winner_check(spots_taken):
	win_cases = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
	for item in win_cases:
		if alike(spots_taken[item[0]], spots_taken[item[1]], spots_taken[item[2]]):
			return True
	return False




# define a main function
def main():
	global player_turn
	# initialize the pygame module
	pygame.init()
	# load and set the logo
	logo = pygame.image.load("logo32x32.png")
	pygame.display.set_icon(logo)
	# set window title
	pygame.display.set_caption("Tic-Tac-Toe by Frosty and Patience")
	# create a font for text stuff in the program
	myfont = pygame.font.SysFont("Comic Sans MS", 30, 1)
		
	# create a main surface we can render stuff on
	screen = pygame.display.set_mode((screen_width,screen_height)) #, pygame.FULLSCREEN)
	# get the size of our main surface and create a sub surface
	background = pygame.Surface(screen.get_size())
	# set previous sub surface to color black and fill the whole surface
	background.fill(BLACK) 
	background = background.convert()
	fullscreen = False

	pygame.mouse.set_visible(False)

	marker_text = myfont.render(f"PLAYER 1, CHOSE YOUR MARKER", False, (0, 255, 0))

	# main menu texts
	main_menu_title = myfont.render("MAIN MENU", False, (255, 255, 255))
	localgame_text = myfont.render("Local Game", False, (255, 255, 255))
	multiplayer_text = myfont.render("Multiplayer", False, (255, 255 ,255))
	# cool variable we all love    
	running = True
	choose_marker = False
	first_start = True
	# our game loop
	while running:
		# check if any events are happening and if
		# they are related to pressing the exit button
		# in the top right or pressing the ESC key on your keyboard
		for event in pygame.event.get():
			if event.type == pygame.QUIT or pygame.key.get_pressed()[pygame.K_ESCAPE]:
				running = False
			if pygame.key.get_pressed()[pygame.K_F12]:
				fullscreen = toggle_fullscreen(fullscreen)

		# get mouse position (tuple unpacking)
		mouse_pos_x, mouse_pos_y = pygame.mouse.get_pos()
		# fill the screen with black
		screen.fill(BLACK)
		if first_start == True:
			main_menu(screen)
			screen.blit(main_menu_title, (305, 125))
			screen.blit(localgame_text, (320, 225))
			screen.blit(multiplayer_text, (320, 355))
			draw_cursor(screen, mouse_pos_x, mouse_pos_y)
			input_system(mouse_pos_x, mouse_pos_y, first_start, player_turn, choose_marker, screen)

			if localgame == True or multiplayer == True:
				first_start = False
				choose_marker = True
		else:
			if localgame == True:
				if choose_marker == True:
					# render our starting screen text
					screen.blit(marker_text, (150, 120))
					# call the input system to know what we chose
					input_system(mouse_pos_x, mouse_pos_y, first_start, player_turn, choose_marker, screen)
					# draw the cross option
					draw_cross(screen, 250, 250)
					# draw the circle option
					draw_circle(screen, 550, 250)
					# draw the beautiful white ball cursor
					draw_cursor(screen, mouse_pos_x, mouse_pos_y)
					# chose a starting player at random
					player_turn = choice(['X','O'])

					# make sure everything was assigned correctly until we proceed to the actual game
					if player_1 != '' and player_2 != '':
						first_start = False
						choose_marker = False
						sleep(0.5)
				else:
					# draw our beautiful board
					draw_board(screen)
					# draw the markers we set on screen
					# draw_markers(screen, position)
					# call the input system to know what the do
					input_system(mouse_pos_x, mouse_pos_y, first_start, player_turn, choose_marker, screen)
					
					for i, _ in enumerate(spots_taken):
						if _ == 'X':
							x, y = positions[i]
							draw_cross(screen, x, y)
						elif _ == 'O':
							# draw an... yeah O
							x, y = positions[i]
							draw_circle(screen, x, y)
						 
					# player_x's turn
					if player_turn == 'X':
						draw_cross(screen, mouse_pos_x, mouse_pos_y)
						#print(spots_taken)
						if winner_check(spots_taken) == True:
							winner_text = myfont.render(f"{player_turn} IS THE WINNER", True, (0, 255, 0))
							screen.blit(winner_text, (screen_width / 2 - 140, screen_height / 2))
					# player_o's turn
					elif player_turn == 'O':
						draw_circle(screen, mouse_pos_x, mouse_pos_y)
						#print(spots_taken)
						if winner_check(spots_taken) == True:
							winner_text = myfont.render(f"{player_turn} IS THE WINNER", True, (255, 0, 0))
							screen.blit(winner_text, (screen_width / 2 - 140, screen_height / 2))
			# else if multiplayer we do somme magic stuff
			# with packets and stuff. Omagawd
		pygame.display.flip()
	pygame.mouse.set_visible(True)

if __name__=="__main__":
	main()
