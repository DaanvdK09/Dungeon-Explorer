import pygame
import math
import os

pygame.init()

#Int
Px=642
Py=350
Ph=96
Pw=60
dir_y=0
dir_x=0
hit_time=0
player_hit=False
Player_alive=True
P_Health=110

Spirit_x=321
Spirit_y=350
Spirit_w=15
Spirit_h=15
SHw=50
Spirit_alive=True
Spirit_hit=False
Spirit_hit_time=0
Spirit_Health=60

Sword_x=500
Sword_y=500
Sword_w=96
Sword_h=96
Sword_picked_up=False

#Attack Interval
last_attack_time=pygame.time.get_ticks()
attack_interval=5000 #5 sec

#Damage
Player_Fist_damage=5
Player_Sword_damage=10
Player_Axe_damage=15

#Screen
Screen_Width=1285
Screen_Height=700
screen=pygame.display.set_mode((Screen_Width,Screen_Height))
pygame.display.set_caption("Game")
pygame.display.toggle_fullscreen()

#Colors
BLACK=(0,0,0)
WHITE=(255,255,255)
RED=(255,0,0)
GREEN=(0,128,0)
GREY=(128,128,128)
YELLOW=(255,255,0)
GOLD=(255,215,0)

#Fonts
font=pygame.font.Font(None,296)
menu_font=pygame.font.Font(None, 75)
title_font=pygame.font.Font(None,150)
death_font=pygame.font.Font(None,100)

#collision
def check_player_spirit_collision(player_rect,spirit_rect):
    return player_rect.colliderect(spirit_rect)

def check_player_sword_collision(player_rect,sword_rect):
    return player_rect.colliderect(sword_rect)

#Run loop
run=True
while run:

#Exit Screen
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False

        #Player attack Spirit
        if Spirit_alive and Player_alive==True:
            Spirit_current_time=pygame.time.get_ticks()
            if event.type==pygame.MOUSEBUTTONDOWN:
                if event.button==1:
                    current_time=pygame.time.get_ticks()
                    if current_time-last_attack_time>=attack_interval:
                        distance=math.sqrt((Px-Spirit_x)**2+(Py-Spirit_y)**2)
                        if distance<=75:
                            damage=Player_Sword_damage if Sword_picked_up else Player_Fist_damage
                            Spirit_Health-=damage
                            SHw-=(damage/Spirit_Health)*SHw
                            Spirit_hit=True
                            Spirit_hit_time=Spirit_current_time
                            Spirit_damage_taken=Player_Fist_damage
                            if Spirit_Health<=10:
                                Spirit_alive=False
                                last_attack_time=current_time
    
    #Rect  
    player_rect=pygame.Rect(Px,Py,Pw,Ph)
    spirit_rect=pygame.Rect(Spirit_x,Spirit_y,Spirit_w,Spirit_h)
    sword_rect=pygame.Rect(Sword_x,Sword_y,Sword_w,Sword_h)

    #Collision Player-Spirit
    if Player_alive and Spirit_alive==True:
        if check_player_spirit_collision(player_rect,spirit_rect):
            if dir_x>0:
                Px=Spirit_x-Pw
            elif dir_x<0:
                Px=Spirit_x+Spirit_w
            if dir_y>0:
                Py=Spirit_y-Ph
            elif dir_y<0:
                Py=Spirit_y+Spirit_h
        
    #Player Pick Up Sword
    if Player_alive==True and Sword_picked_up==False:
        if check_player_sword_collision(player_rect,sword_rect):
            Sword_picked_up=True

    pygame.display.update()

pygame.quit()