try :
    import pygame
    import sys
    import random
    from pygame.locals import *
except ImportError :
    print "Cannot import required module(s). Abort."

FPS = 15
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480

def main():
    global FPS_CLOCK, DISPLAY, BASIC_FONT
    pygame.init()
    FPS_CLOCK = pygame.time.Clock()
    DISPLAY = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Snake")
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()

if __name__=='__main__':
    main()
