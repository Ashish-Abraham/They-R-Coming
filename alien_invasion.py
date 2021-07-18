import sys
import pygame
import game_funcs as gf
from settings import Settings
from ship import Ship
from pygame.sprite import Group


def run_game():
    #initialize game and create a game object
    pygame.init()
    ai_settings=Settings()
    screen=pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("ALIEN INVASION")

    #make ship 
    ship=Ship(ai_settings,screen)

    #make a group to store bullets
    bullets=Group()

    #main loop for game
    while True:
        #Check for input from hardware and update position of ship accordingly
        gf.check_events(ai_settings,screen,ship,bullets)
        ship.update()
        gf.update_bullets(bullets)

        #redraw screen during each pass with the loop and update images
        gf.update_screen(ai_settings,screen,ship,bullets)
run_game()                

