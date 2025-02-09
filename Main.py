import pygame
import math
import Common as Co

pygame.init()

#Int
Player_Fist_damage=5
Player_Sword_damage=10
Player_Axe_damage=15


#Run loop
Co.run=True
while Co.run:
    Co.screen.fill(0)

#Exit Screen
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            Co.run=False

        #Player Attack Spirit
        if Co.Spirit_alive and Co.Player_alive==True:
            if event.type==pygame.MOUSEBUTTONDOWN:
                if event.button==1:
                    if Co.current_time-Co.last_attack_time>=Co.attack_interval:
                        distance=math.sqrt((Co.Px-Co.Spirit_x)**2+(Co.Py-Co.Spirit_y)**2)
                        if distance<=75:
                            Spirit_current_time=pygame.time.get_ticks()#
                            Co.Spirit_hit=True
                            Co.Spirit_hit_time=Spirit_current_time
                            damage=Player_Sword_damage if Co.Sword_picked_up else Player_Fist_damage
                            Co.Spirit_Health-=damage
                            Co.SHw-=(damage/Co.Spirit_Health)*Co.SHw
                            if Co.Spirit_Health<=10:
                                Co.Spirit_alive=False
                                Co.last_attack_time=Co.current_time
                                
    #Collision Player-Spirit
    if Co.Player_alive and Co.Spirit_alive==True:
        if Co.check_player_spirit_collision(Co.player_rect,Co.spirit_rect):
            if Co.dir_x>0:
                Px=Co.Spirit_x-Co.Pw
            elif Co.dir_x<0:
                Px=Co.Spirit_x+Co.Spirit_w
            if Co.dir_y>0:
                Py=Co.Spirit_y-Co.Ph
            elif Co.dir_y<0:
                Py=Co.Spirit_y+Co.Spirit_h

    #Player Pick Up Sword
    if Co.Player_alive==True and Co.Sword_picked_up==False:
        if Co.check_player_sword_collision(Co.player_rect,Co.sword_rect):
            Co.Sword_picked_up=True

    pygame.display.update()

pygame.quit() 