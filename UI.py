import pygame
import Common as Co
import Images as Im

#Int
Iconx=975
Icony=375
Hh=30
SHh=10

#Run loop
Co.run=True
while Co.run:
    Co.screen.fill(0)

#Exit Screen
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            Co.run=False

    #Inventory
    pygame.draw.circle(Co.screen,Co.GOLD,(1350,750),200)
    pygame.draw.circle(Co.screen,Co.BLACK,(1345,745),185)

    #Inventory Icon
    if Co.Sword_picked_up==True:
        Co.screen.blit(Im.sword_icon,(Iconx,Icony))

    #Healthbar
    pygame.draw.rect(Co.screen,Co.GOLD,(float(22+(1/2)),float(36+(1/2)),205,38))
    pygame.draw.rect(Co.screen,Co.BLACK,(25,40,200,30))
    pygame.draw.rect(Co.screen,Co.GREEN,(25,40,Co.Hw,Hh))
    if Co.player_hit:
        elapsed_time=Co.current_time-Co.hit_time
        Dw=(Co.damage_taken/Co.P_Health)*Co.Hw
        pygame.draw.rect(Co.screen,Co.RED,(25+Co.Hw,40,Dw,Hh))

    #Spirit Healthbar
    pygame.draw.rect(Co.screen,Co.GREEN,((Co.Spirit_x-(Co.SHw/2)+5),(Co.Spirit_y-25),Co.SHw,SHh))
    if Co.Spirit_hit:
        elapesed_time=Co.Spirit_current_time-Co.Spirit_hit_time
        SDw=(Co.Spirit_damage_taken/Co.Spirit_Health)*Co.SHw
        pygame.draw.rect(Co.screen,Co.RED,((Co.Spirit_x-((Co.SHw/2))+5)+Co.SHw,(Co.Spirit_y-25),SDw,SHh))

    pygame.display.update()

pygame.quit()