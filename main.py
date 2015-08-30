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

def draw_score(score):
    scoreDisp = SCORE_FONT.render("Score : %s" %(score), True, WHITE)
    scoreRect = scoreDisp.get_rect()
    scoreRect.topleft = (480, 20)
    DISPLAY.blit(scoreDisp, scoreRect)

def draw_title():
    titleDisp = TITLE_FONT.render("Snake", True, WHITE)
    titleRect = titleDisp.get_rect()
    titleRect.topleft = (60, 15)
    DISPLAY.blit(titleDisp, titleRect)

def draw_press_key_message():
    titleDisp = TITLE_FONT.render("Press any key to Play", True, WHITE)
    titleRect = titleDisp.get_rect()
    titleRect.center = (WINDOW_WIDTH/2, 15)
    DISPLAY.blit(titleDisp, titleRect)

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

def if_snake_bitten_itself():
    head = SNAKE_LIST[HEAD]
    for i in range(1,len(SNAKE_LIST)):
        if SNAKE_LIST[i]==head:
            print 'DEAD'

def getRandomAppleLocation():
    return {'x':random.randint(0,H_CELLS-1), 'y':random.randint(0,V_CELLS-1)}

def check_key_press_event():
    if len(pygame.event.get(QUIT)) > 0:
        pygame.quit()
        sys.exit()
    
    keyUpEvents = pygame.event.get(KEYUP)
    if len(keyUpEvents) == 0:
        return None
    if keyUpEvents[0].key == K_ESCAPE:
        pygame.quit()
        sys.exit()
    return keyUpEvents[0].key

# main.py

def main():
    global FPS_CLOCK, DISPLAY, SCORE_FONT, TITLE_FONT, HEADER_FONT
    
    pygame.init()
    FPS_CLOCK = pygame.time.Clock()
    DISPLAY = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    SCORE_FONT = pygame.font.Font('freesansbold.ttf', 20)
    TITLE_FONT = pygame.font.Font('freesansbold.ttf', 30)
    HEADER_FONT = pygame.font.Font('freesansbold.ttf', 100)
    pygame.display.set_caption("Snake")

    while True:
        run_start_screen()
        run_game()

def run_start_screen():
    header_green = HEADER_FONT.render("Snake", True, GREEN)
    header_white = HEADER_FONT.render("Snake", True, WHITE)

    angle_green = 0
    angle_white = 0
    
    while True:
        DISPLAY.fill(BGCOLOR)
        
        rotated_green = pygame.transform.rotate(header_green, angle_green)
        rotated_green_rect = rotated_green.get_rect()
        rotated_green_rect.center = (WINDOW_WIDTH/2, WINDOW_HEIGHT/2)
        DISPLAY.blit(rotated_green, rotated_green_rect)

        rotated_white = pygame.transform.rotate(header_white, angle_white)
        rotated_white_rect = rotated_white.get_rect()
        rotated_white_rect.center = (WINDOW_WIDTH/2, WINDOW_HEIGHT/2)
        DISPLAY.blit(rotated_white, rotated_white_rect)

        angle_green = (angle_green+1)%360
        angle_white = (angle_white-1)%360

        draw_press_key_message()

        if check_key_press_event():
            pygame.event.get()
            return

        pygame.display.update()
        FPS_CLOCK.tick(FPS)

def run_game():
    global SNAKE_LIST
    
    SNAKE_LIST = [{'x':2,'y':2},
                 {'x':3,'y':2},
                 {'x':4,'y':2}]

    direction = RIGHT

    apple = getRandomAppleLocation()

    score = 0
    
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
            # And increment score
            score+=1
        else:
            SNAKE_LIST.pop()
        # check if snake has bitten itself
        if_snake_bitten_itself()
        # Update Display
        draw_grid()
        draw_snake()
        draw_apple(apple['x'],apple['y'])
        draw_score(score)
        draw_title()
        pygame.display.update()
        move_snake(direction)
        
        FPS_CLOCK.tick(FPS) # Add delay beween move of Snake    
        

if __name__=='__main__':
    main()
