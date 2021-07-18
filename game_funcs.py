import sys
import pygame
from bullet import Bullet

#respond and check for input from hardware
def check_keydown_events(event,ai_settings,screen,ship,bullets):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True 
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)    

def check_keyup_events(event,ship):    
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False    

def check_events(ai_settings,screen,ship,bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:   #if user quits
            sys.exit()
        elif event.type == pygame.KEYDOWN:   #if a keypress is detected
            check_keydown_events(event,ai_settings,screen,ship,bullets)
        elif event.type == pygame.KEYUP:   #if a key release is detected
            check_keyup_events(event,ship) 
                        

#update screen images and flip to new screen
def update_screen(ai_settings,screen,ship,bullets):
    screen.fill(ai_settings.bg_color)
    ship.blitme()
        
    # Redraw all bullets behind ship and aliens.
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    #update screen
    pygame.display.flip()    

#create a new bullet and add it to the group when space is pressed
def fire_bullet(ai_settings, screen, ship, bullets):
    if len(bullets)<ai_settings.bullets_allowed:
        new_bullet=Bullet(ai_settings,screen,ship)
        bullets.add(new_bullet)

#delete bullets which go out of screen so that memory is freed
def update_bullets(bullets):
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom<=0:
            bullets.remove(bullet)

