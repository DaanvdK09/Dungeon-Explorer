import pygame
import math
import os
import Common as Co
import Menu as Me

pygame.init()

#Int
Spirit_d=5
SHh=10
Spirit_hit_duration=75
Spirit_damage=10
last_shot_time=pygame.time.get_ticks()
shot_interval=1500
S_speed=float(1/4)
orbs=[]
orb_speed=1

#Collision
def check_collision(player_rect,orb):
    orb_rect=pygame.Rect(orb[0]-5,orb[1]-5,10,10)
    return player_rect.colliderect(orb_rect)

#Run loop
while Co.run:

#Exit Screen
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            Co.run=False

    #Spirit Movement
    if Co.Spirit_alive==True:
        distance=math.sqrt((Co.Px-Co.Spirit_x)**2+(Co.Py-Co.Spirit_y)**2)
        if distance>100:
            if Co.Px+(Co.Pw/2)>Co.Spirit_x+(Co.Spirit_w/2):
                Co.Spirit_x+=S_speed
            elif Co.Px+(Co.Pw/2)<Co.Spirit_x+(Co.Spirit_w/2):
                Co.Spirit_x-=S_speed

        if distance<100:
            if Co.Py+(Co.Ph/2)>Co.Spirit_y+(Co.Spirit_h/2):
                Co.Spirit_y+=S_speed
            elif Co.Py+(Co.Ph/2)<Co.Spirit_y+(Co.Spirit_h/2):
               Co.Spirit_y-=S_speed

    #Spirit Attack
    if Co.Spirit_alive and Co.Player_alive==True:
        current_time=pygame.time.get_ticks()
        if distance<=500 and current_time-last_shot_time>=shot_interval:
            orbs.append([Co.Spirit_x+(Co.Spirit_w/2),Co.Spirit_y+(Co.Spirit_h/2),(Co.Px+(Co.Pw/2))-(Co.Spirit_x+(Co.Spirit_w/2)),(Co.Py+(Co.Ph / 2))-(Co.Spirit_y+(Co.Spirit_h/2))])
            last_shot_time=current_time

    #Ghost orb Movement
    orbs=[orb for orb in orbs if not check_collision(Co.player_rect,orb)]

    for orb in orbs:
        orb[0]+=orb[2]*orb_speed/150
        orb[1]+=orb[3]*orb_speed/150
        pygame.draw.circle(Co.screen,Co.GREY,(int(orb[0]),int(orb[1])),5)

        #Damage Player
        if Co.Player_alive==True:
            if check_collision(Co.player_rect,orb):
                Co.P_Health-=Spirit_damage
                Co.Hw-=(Spirit_damage/Co.P_Health)*Co.Hw
                damage_taken=Spirit_damage
                Co.player_hit=True
                hit_time=current_time
                orbs.remove(orb)
                if Co.P_Health<=10:
                    Co.Player_alive=False
                    Me.game_state="death"

    #Remove Ghost orbs that are off-screen
    orbs=[orb for orb in orbs if 0<=orb[0]<=Co.Screen_Width and 0<=orb[1]<=Co.Screen_Height]

    #Spirit Hit
    if Co.Spirit_hit and Co.Spirit_current_time-Co.Spirit_hit_time>=Spirit_hit_duration:
        Co.Spirit_hit=False

    #Spirit
    if Co.Spirit_alive==True:
        Sc=Co.RED if Co.Spirit_hit else Co.GREY
        pygame.draw.rect(Co.screen,Sc,(Co.Spirit_x,Co.Spirit_y,Co.Spirit_w,Co.Spirit_h))

    #Spirit Healthbar
    pygame.draw.rect(Co.screen,Co.GREEN,((Co.Spirit_x-(Co.SHw/2)+5),(Co.Spirit_y-25),Co.SHw,SHh))
    if Co.Spirit_hit:
        elapesed_time=Co.Spirit_current_time-Co.Spirit_hit_time
        SDw=(Co.Spirit_damage_taken/Co.Spirit_Health)*Co.SHw
        pygame.draw.rect(Co.screen,Co.RED,((Co.Spirit_x-((Co.SHw/2))+5)+Co.SHw,(Co.Spirit_y-25),SDw,SHh))

    pygame.display.update()

pygame.quit()