import pygame
import random
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
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE =  ( 70,  70, 200)
GREEN = (  0, 255,   0)
RED =   (200,  30,  30)
position = (0, 0)
player_1 = ''
player_2 = ''


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
    pygame.draw.circle(screen, RED, [x , y], 85, 14)

def draw_board(screen):
    pygame.draw.line(screen, BLUE, [267, 0],[267, 600], 20)
    pygame.draw.line(screen, BLUE, [534, 0],[534, 600], 20)
    pygame.draw.line(screen, BLUE, [0, 200],[800, 200], 20)
    pygame.draw.line(screen, BLUE, [0, 400],[800, 400], 20)

def draw_cursor(screen, active, x, y):
    pygame.draw.circle(screen, WHITE, [x, y], 10)

def draw_markers(screen, position):
    global spots_taken
    x, y = position
    for i in range(len(spots_taken)):
        if spots_taken[i] == 'X':  
            draw_cross(screen, x, y)
        elif spots_taken[i] == 'O':
            draw_circle(screen, x, y)

def input_system(mouse_x, mouse_y, first_start, player, screen):
    global player_1, player_2, marker_spots, position
    if pygame.mouse.get_pressed()[0]:
        if first_start == True:
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
            # if mouse is within first box region
            if mouse_x >= 0 and mouse_x <= 267:
                if mouse_y <= 200:
                    spots_taken[0] = player
                    position = board_pos["pos_1"]
            # if mouse is within second box region
            if mouse_x >= 287 and mouse_x <= 534:
                if mouse_y <= 200:
                    spots_taken[1] = player
                    position = board_pos["pos_2"]
            # if mouse is within third box region
            if mouse_x >= 554:
                if mouse_y <= 200:
                    spots_taken[2] = player
                    position = board_pos["pos_3"]
# define a main function
def main():
     
    # initialize the pygame module
    pygame.init()
    # load and set the logo
    logo = pygame.image.load("logo32x32.png")
    pygame.display.set_icon(logo)
    pygame.display.set_caption("super awesome tic-tac-toe")
    myfont = pygame.font.SysFont("Times New Roman", 30, 1)
    
    screen_width = 800
    screen_height = 600
    
    xpos = 50
    ypos = 50
    step_x = 10
    step_y = 10
    FPS = 30

    screen = pygame.display.set_mode((screen_width,screen_height))
    background = pygame.Surface(screen.get_size())
    background.fill(BLACK) 
    background = background.convert()

    clock = pygame.time.Clock()
    pygame.mouse.set_visible(False)

    marker_text = myfont.render(f"CHOSE YOUR MARKER", False, (0, 255, 0))
    
    running = True
    first_start = True
    turn = 'X'
    while running:
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

        mouse_pos_x, mouse_pos_y = pygame.mouse.get_pos()

        screen.fill(BLACK)
        if first_start == True:
            screen.blit(marker_text, (220, 120))
            input_system(mouse_pos_x, mouse_pos_y, first_start, turn, screen)
            draw_cross(screen, 250, 250)
            draw_circle(screen, 550, 250)
            draw_cursor(screen, True, mouse_pos_x, mouse_pos_y)
            
            if player_1 != '' and player_2 != '':
                first_start = False
        else:
            draw_board(screen)
            draw_markers(screen, position)
            input_system(mouse_pos_x, mouse_pos_y, first_start, turn, screen)
            # player_x's turn
            if turn == 'X':
               draw_cross(screen, mouse_pos_x, mouse_pos_y)
            # player_o's turn
            elif turn == 'O':
                draw_circle(screen, mouse_pos_x, mouse_pos_y)
            #milliseconds = clock.tick(FPS)
            #print(milliseconds)
        pygame.display.flip()
    pygame.mouse.set_visible(True)
if __name__=="__main__":
    main()