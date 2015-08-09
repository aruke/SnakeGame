try :
    import pygame
    import sys
    import random
    from pygame.locals import *
    from colors import *
except ImportError :
    print "Cannot import required module(s). Abort."

FPS = 2
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
CELL_SIZE = 20
H_CELLS = WINDOW_WIDTH/CELL_SIZE
V_CELLS = WINDOW_HEIGHT/CELL_SIZE

assert WINDOW_WIDTH % CELL_SIZE == 0 , "WINDOW_WIDTH must be a multiple of CELL_SIZE"
assert WINDOW_HEIGHT % CELL_SIZE == 0 , "WINDOW_HEIGHT must be a multiple of CELL_SIZE"

HEAD = 0

# Directions
UP = 'up'
DOWN = 'down'
LEFT = 'left'
RIGHT = 'right'

# Draw Functions

def draw_grid():
    DISPLAY.fill(BGCOLOR)
    for x in range(0, WINDOW_WIDTH, CELL_SIZE):
        pygame.draw.line(DISPLAY, DARKGRAY, (x,0), (x,WINDOW_HEIGHT))
    for y in range(0, WINDOW_HEIGHT, CELL_SIZE):
        pygame.draw.line(DISPLAY, DARKGRAY, (0,y), (WINDOW_WIDTH,y))
        
def draw_cell(x,y, color):
    pygame.draw.rect(DISPLAY, color, (x*CELL_SIZE, y*CELL_SIZE,
                                      CELL_SIZE+1, CELL_SIZE+1))
    # +1 for one pixel that crosses grid markers

def draw_snake():
    for cell in SNAKE_LIST:
        draw_cell(cell['x'], cell['y'], GREEN)

def draw_apple(x,y):
    draw_cell(x, y, RED)

# Logic functions
def move_snake(direction):
    if direction==UP:
        new_head = { 'x' : SNAKE_LIST[HEAD]['x'], 'y' : SNAKE_LIST[HEAD]['y']-1 }
    elif direction==DOWN:
        new_head = { 'x' : SNAKE_LIST[HEAD]['x'], 'y' : SNAKE_LIST[HEAD]['y']+1 }
    elif direction==LEFT:
        new_head = { 'x' : SNAKE_LIST[HEAD]['x']-1, 'y' : SNAKE_LIST[HEAD]['y'] }
    elif direction==RIGHT:
        new_head = { 'x' : SNAKE_LIST[HEAD]['x']+1, 'y' : SNAKE_LIST[HEAD]['y'] }
    SNAKE_LIST.insert(0, new_head)

def getRandomAppleLocation():
    return {'x':random.randint(0,H_CELLS), 'y':random.randint(0,V_CELLS)}
# main.py

def main():
    global FPS_CLOCK, DISPLAY, BASIC_FONT
    global SNAKE_LIST
    
    pygame.init()
    FPS_CLOCK = pygame.time.Clock()
    DISPLAY = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Snake")

    SNAKE_LIST = [{'x':2,'y':2},
                 {'x':3,'y':2},
                 {'x':4,'y':2}]

    direction = RIGHT

    apple = getRandomAppleLocation()
    
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                key = event.key
                if (key==K_UP or key==K_a) and direction!=DOWN:
                    direction = UP
                elif (key==K_DOWN or key==K_s) and direction!=UP:
                    direction = DOWN
                elif (key==K_LEFT or key==K_a) and direction!=RIGHT:
                    direction = LEFT
                elif (key==K_RIGHT or key==K_d) and direction!=LEFT:
                    direction = RIGHT
        draw_grid()
        draw_snake()
        draw_apple(apple['x'],apple['y'])
        pygame.display.update()
        move_snake(direction)
        SNAKE_LIST.pop()
        FPS_CLOCK.tick(FPS) # Add delay beween move of Snake
        
        

if __name__=='__main__':
    main()
