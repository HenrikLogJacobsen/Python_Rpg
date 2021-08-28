
import pygame 
import sys
from buttons import Button
import entity
from pygame.constants import QUIT
from map import Map


pygame.init()
screen_pos = [0, 0]
white = 255, 255, 255
vel = 2


SCREEN_HEIGHT = 500
SCREEN_WIDHT = 800
screen = pygame.display.set_mode((SCREEN_HEIGHT, SCREEN_WIDHT))
screen.fill((202, 228, 241))
start_img = pygame.image.load('main/game/media/start.png').convert_alpha()
settings_img = pygame.image.load('main/game/media/settings.png').convert_alpha()
back_img = pygame.image.load('main/game/media/back.png').convert_alpha()

tree_pos = [[-200, 200], [300, 200], [-100, -100], [200, -100]]
map1 = Map("tree.jpg", tree_pos, screen)

start_button = Button(50, 200, start_img, 0.6)
settings_button = Button(250, 200, settings_img, 0.6)
back_button = Button(250, 400, back_img, 0.5)


player = entity.Entity([0, 0], "intro_ball.gif")
player.center_coord(SCREEN_WIDHT / 2, SCREEN_HEIGHT / 2)

clock = pygame.time.Clock()
fps = 60

run_menu = True
settings_menu = False

LAUNCH_GAME = False


while run_menu:

    
    screen.fill((202, 228, 241))

    for event in pygame.event.get():
        if event.type == QUIT:
            run_menu = False
            pygame.quit

    #draw_button = buttons.Button.draw(screen)
    if start_button.draw(screen) == True:
        LAUNCH_GAME = True
        run_menu = False
    
        
    pygame.display.update()



while LAUNCH_GAME: 

    screen.fill((202, 228, 241))


    for event in pygame.event.get():

        if event.type == QUIT:
            LAUNCH_GAME = False
            pygame.quit
            

    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT]:
        screen_pos[0] += vel
    if keys[pygame.K_RIGHT]:
        screen_pos[0] -= vel
    if keys[pygame.K_UP]:
        screen_pos[1] += vel
    if keys[pygame.K_DOWN]:
        screen_pos[1] -= vel

    # DRAW
    screen.blit(player.img, player.pos)
    map1.draw(screen_pos)
    pygame.display.update()
    clock.tick(60)



        
    
    





       




        
