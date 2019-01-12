import pygame
from time import sleep

BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE =  ( 70,  70, 200)
GREEN = (  0, 255,   0)
RED =   (200,  30,  30)


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
    pygame.draw.circle(screen, RED, [x , y], 90, 20)

def draw_board(screen):
    pygame.draw.line(screen, BLUE, [267, 0],[267, 600], 20)
    pygame.draw.line(screen, BLUE, [534, 0],[534, 600], 20)
    pygame.draw.line(screen, BLUE, [0, 200],[800, 200], 20)
    pygame.draw.line(screen, BLUE, [0, 400],[800, 400], 20)

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

    #pygame.draw.circle(screen, RED, [130 , 90], 90, 20)

    #draw_cross(screen, 660, 90)
    # image = pygame.image.load("logo32x32.png")

    clock = pygame.time.Clock()
    pygame.mouse.set_visible(False)
    # screen.blit(image, (50,50)) 

    marker_text = myfont.render(f"CHOSE YOUR MARKER", False, (0, 255, 0))
    
    running = True
    first_start = True
    while running:
        # if xpos>screen_width-64 or xpos<0:
        #     step_x = -step_x
        # if ypos>screen_height-64 or ypos<0:
        #     step_y = -step_y
        # xpos += step_x
        # ypos += step_y
        
        # screen.blit(image, (xpos, ypos))
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

        screen.fill(BLACK)
        if first_start == True:
            screen.blit(marker_text, (200, 20))
            draw_cross(screen, 250, 150)
            draw_circle(screen, 550, 150)
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