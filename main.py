try :
    import pygame
    import sys
    import random
    from pygame.locals import *
    from colors import *
except ImportError :
    print "Cannot import required module(s). Abort."

FPS = 15
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
CELL_SIZE = 20

assert WINDOW_WIDTH % CELL_SIZE == 0 , "WINDOW_WIDTH must be a multiple of CELL_SIZE"
assert WINDOW_HEIGHT % CELL_SIZE == 0 , "WINDOW_HEIGHT must be a multiple of CELL_SIZE"

HEAD = 0

# Draw Functions

def draw_grid():
    for x in range(0, WINDOW_WIDTH, CELL_SIZE):
        pygame.draw.line(DISPLAY, DARKGRAY, (x,0), (x,WINDOW_HEIGHT))
    for y in range(0, WINDOW_HEIGHT, CELL_SIZE):
        pygame.draw.line(DISPLAY, DARKGRAY, (0,y), (WINDOW_WIDTH,y))
        
def draw_cell(x,y, color):
    pygame.draw.rect(DISPLAY, color, (x, y, x+CELL_SIZE-1, y+CELL_SIZE-1))
    # -1 for one pixel that crosses grid markers

# main.py

def main():
    global FPS_CLOCK, DISPLAY, BASIC_FONT
    global snakeList
    
    pygame.init()
    FPS_CLOCK = pygame.time.Clock()
    DISPLAY = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Snake")
    
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        draw_grid()
        draw_cell(1,1,WHITE)
        pygame.display.update()
        

if __name__=='__main__':
    main()
