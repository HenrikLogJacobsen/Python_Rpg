
import pygame 
import sys
from buttons import Button
import entity
from pygame.constants import QUIT

pygame.init()
speed = [0,0]
vel = 2


SCREEN_HEIGHT = 500
SCREEN_WIDHT = 800
screen = pygame.display.set_mode((SCREEN_HEIGHT, SCREEN_WIDHT))
screen.fill((202, 228, 241))
start_img = pygame.image.load('main/start.png').convert_alpha()

start_button = Button(100, 200, start_img, 0.6)
player = entity.Entity([0, 0], "intro_ball.gif")
player.center_coord(SCREEN_WIDHT / 2, SCREEN_HEIGHT / 2)


run_start = True

LAUNCH_GAME = False

while run_start:

    
    screen.fill((202, 228, 241))

    #draw_button = buttons.Button.draw(screen)
    if start_button.draw(screen) == True:
        LAUNCH_GAME = True
        run_start = False


    for event in pygame.event.get():
        if event.type == QUIT:
            run_start = False
            pygame.quit
        
    pygame.display.update()

while LAUNCH_GAME: 

    screen.fill((202, 228, 241))

    for event in pygame.event.get():
        if event.type == QUIT:
            run_start = False
            pygame.quit
        
    pygame.display.update()

        
    
    





       




        
