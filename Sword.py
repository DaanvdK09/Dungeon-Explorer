import pygame
import Common as Co
import Images as Im

#Run loop
Co.run=True
game_state="menu"
while Co.run:
    Co.screen.fill(0)

#Exit Screen
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            Co.run=False

    #Sword
    if Co.Sword_picked_up==False:
        Co.screen.blit(Im.sword_image,(Co.Sword_x,Co.Sword_y))

    pygame.display.update()

pygame.quit() 