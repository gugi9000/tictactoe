import pygame
from time import sleep

BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE =  ( 70,  70, 200)
GREEN = (  0, 255,   0)
RED =   (200,  30,  30)
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

def select_marker(mouse_x, mouse_y, first_start, font, screen):
    if pygame.mouse.get_pressed()[0]:
        if first_start == True:
            # if mouse is within x region
            if mouse_x >= 170 and mouse_x <= 330:
                if mouse_y >= 170 and mouse_y <= 330:
                    player_1 = 'X'
                    player_2 = 'O'
                    marker_text = font.render(f"Player_1 is {player_1}, Player_2 is {player_2}", False, (0, 255, 0))
                    screen.blit(marker_text, (220, 40))
            # if mouse is within o region
            if mouse_x >= 470 and mouse_x <= 630:
                if mouse_y >= 170 and mouse_y <= 330:
                    player_1 = 'O'
                    player_2 = 'X'
                    marker_text = font.render(f"Player_1 is {player_1}, Player_2 is {player_2}", False, (0, 255, 0))
                    screen.blit(marker_text, (220, 40))
 
        # else game_board regions
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
    pygame.mouse.set_visible(True)

    marker_text = myfont.render(f"CHOSE YOUR MARKER", False, (0, 255, 0))
    
    running = True
    first_start = True
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
            select_marker(mouse_pos_x, mouse_pos_y, first_start, myfont, screen)
            draw_cross(screen, 250, 250)
            draw_circle(screen, 550, 250)
            draw_cursor(screen, True, mouse_pos_x, mouse_pos_y)
            
            if player_1 != '' and player_2 != '':
                first_start = False
        #draw_board(screen)
        mouse_pos_x, mouse_pos_y = pygame.mouse.get_pos()
        #draw_cross(screen, mouse_pos_x, mouse_pos_y)
        #draw_circle(screen, mouse_pos_x, mouse_pos_y)
        pygame.display.flip()
        #milliseconds = clock.tick(FPS)
        #print(milliseconds)

    pygame.mouse.set_visible(True)
if __name__=="__main__":
    main()