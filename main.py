try :
    import pygame
    import sys
    import random
    from pygame.locals import *
    from colors import *
except ImportError :
    print "Cannot import required module(s). Abort."

FPS = 5
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
GRID_WIDTH = 560
GRID_HEIGHT = 380
GRID_ORIGIN = {'x' : (WINDOW_WIDTH-GRID_WIDTH)/2,
                'y' : 60}#(WINDOW_HEIGHT-GRID_HEIGHT)/2}
CELL_SIZE = 20
H_CELLS = GRID_WIDTH/CELL_SIZE
V_CELLS = GRID_HEIGHT/CELL_SIZE

assert GRID_WIDTH % CELL_SIZE == 0 , "WINDOW_WIDTH must be a multiple of CELL_SIZE"
assert GRID_HEIGHT % CELL_SIZE == 0 , "WINDOW_HEIGHT must be a multiple of CELL_SIZE"

HEAD = 0

# Directions
UP = 'up'
DOWN = 'down'
LEFT = 'left'
RIGHT = 'right'

# Draw Functions

def draw_grid():
    DISPLAY.fill(BGCOLOR)
    for x in range(GRID_ORIGIN['x'], GRID_WIDTH+GRID_ORIGIN['x']+1, CELL_SIZE):
        pygame.draw.line(DISPLAY, DARKGRAY, (x, GRID_ORIGIN['y']), (x,GRID_HEIGHT+GRID_ORIGIN['y']))
    for y in range(GRID_ORIGIN['y'], GRID_HEIGHT+GRID_ORIGIN['y']+1, CELL_SIZE):
        pygame.draw.line(DISPLAY, DARKGRAY, (GRID_ORIGIN['x'], y), (GRID_WIDTH+GRID_ORIGIN['x'], y))
        
def draw_cell(x,y, color):
    pygame.draw.rect(DISPLAY, color, (x*CELL_SIZE+GRID_ORIGIN['x'], y*CELL_SIZE +GRID_ORIGIN['y'],
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
    return {'x':random.randint(0,H_CELLS-1), 'y':random.randint(0,V_CELLS-1)}
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
        # Event handling
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
        # Check if Snake has eaten Apple
        if SNAKE_LIST[HEAD]==apple:
            # Our gorgeous snake has eaten the apple
            # So generate new one
            apple = getRandomAppleLocation()
            # And don't remove tail
        else:
            SNAKE_LIST.pop()
        # Update Display
        draw_grid()
        draw_snake()
        draw_apple(apple['x'],apple['y'])
        pygame.display.update()
        move_snake(direction)
        
        FPS_CLOCK.tick(FPS) # Add delay beween move of Snake
        
        

if __name__=='__main__':
    main()
