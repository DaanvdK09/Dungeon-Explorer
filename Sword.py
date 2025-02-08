import pygame
import Common as Co
import Images as Im

pygame.init()

#Run loop
while Co.run:

#Exit Screen
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            Co.run=False

    #Sword
    if Co.Sword_picked_up==False:
        Co.screen.blit(Im.sword_image,(Co.Sword_x,Co.Sword_y))
        
    pygame.display.update()

pygame.quit()