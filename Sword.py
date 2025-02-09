import pygame
from Common import run,screen,Sword_picked_up, Sword_x, Sword_y, Screen_Width, Screen_Height
from Images import sword_image

pygame.init()

# Run loop
while run:
    screen.fill(0)

    # Exit Screen
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # Sword
    if not Sword_picked_up:
        screen.blit(sword_image,(Sword_x, Sword_y))

    pygame.display.update()

pygame.quit()