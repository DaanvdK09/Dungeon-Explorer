import pygame
import math
import os
import Common as Co
import Images as Im
import Menu as Me

pygame.init()

#Int
Last_dir=1
P_speed=float(1/4)
hit_duration=200
Hit_box=False
show_idle=True

#Idle Animation Timer
idle_animation_timer=pygame.time.get_ticks()
idle_animation_interval=500  # 0.5 seconds
idle_frame=1

# Walking Animation Timer
walk_animation_timer=pygame.time.get_ticks()
walk_animation_interval=100  # 0.1 seconds
walk_frame=0

#Run loop
while Co.run:

#Exit Screen
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            Co.run=False

        #Keys
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_w:
                Last_dir=3
                show_idle=False
                Co.dir_y=-1
                Co.dir_x=0

            if event.key==pygame.K_s:
                Last_dir=1
                show_idle=False
                Co.dir_y=1
                Co.dir_x=0

            if event.key==pygame.K_d:
                Last_dir=4
                show_idle=False
                Co.dir_x=1
                Co.dir_y=0

            if event.key==pygame.K_a:
                Last_dir=2
                show_idle=False
                Co.dir_x=-1
                Co.dir_y=0

            if event.key==pygame.K_ESCAPE and Me.game_state=="game" and Co.Player_alive==True:
                Me.game_state="pause"

            if event.key==pygame.K_h and Hit_box==False and Co.Player_alive==True:
                Hit_box==True

            if event.key==pygame.K_h and Hit_box==True and Co.Player_alive==True:
                Hit_box==False
                
        if event.type==pygame.KEYUP:
            if event.key==pygame.K_w:
                Co.dir_y=0
                show_idle=True

            if event.key==pygame.K_s:
                Co.dir_y=0
                show_idle=True

            if event.key==pygame.K_d:
                Co.dir_x=0
                show_idle=True

            if event.key==pygame.K_a:
                Co.dir_x=0
                show_idle=True

    #Player Movement
    if Co.Player_alive==True:
        if Co.dir_y!=0:
            Co.Py+=Co.dir_y*P_speed

        if Co.dir_x!=0:
            Co.Px+=Co.dir_x*P_speed

        if Co.dir_y!=0:
            Co.Py+=Co.dir_y*P_speed
        if Co.Py<0:
            Co.Py=0
        elif Co.Py>Co.Screen_Height-Co.Ph:
            Co.Py=Co.Screen_Height-Co.Ph

        if Co.dir_x!=0:
            Co.Px+=Co.dir_x*P_speed
        if Co.Px<0:
            Co.Px=0
        elif Co.Px>Co.Screen_Width-Co.Pw:
            Co.Px=Co.Screen_Width-Co.Pw

    #Player Hit
    if player_hit and current_time-Co.hit_time>=hit_duration:
        player_hit=False

    #Player
    if Co.Player_alive==True:
        Pc=Co.RED if player_hit else Co.WHITE
        if Hit_box==True:
            pygame.draw.rect(Co.screen,Pc,(Co.Px,Co.Py,Co.Pw,Co.Ph))
        
        # Idle animation
        current_time=pygame.time.get_ticks()
        if Co.dir_x==0 and Co.dir_y==0:
            if current_time-idle_animation_timer>=idle_animation_interval:
                idle_frame=2 if idle_frame==1 else 1
                idle_animation_timer=current_time
        
            if Last_dir==1:
                Co.screen.blit(Im.player_image_idle_down1 if idle_frame==1 else Im.player_image_idle_down2,(Co.Px-32,Co.Py-8))
            if Last_dir==2:
                Co.screen.blit(Im.player_image_idle_left1 if idle_frame==1 else Im.player_image_idle_left2,(Co.Px-32,Co.Py-8))
            if Last_dir==3:
                Co.screen.blit(Im.player_image_idle_up1 if idle_frame==1 else Im.player_image_idle_up2,(Co.Px-32,Co.Py-8))
            if Last_dir==4:
                Co.screen.blit(Im.player_image_idle_right1 if idle_frame==1 else Im.player_image_idle_right2,(Co.Px-32,Co.Py-8))

        #Walking animation
        current_time=pygame.time.get_ticks()
        if Co.dir_x and Co.dir_y==1 or -1:
            if current_time-walk_animation_timer>=walk_animation_interval:
                walk_frame=(walk_frame+1)%6
                walk_animation_timer=current_time
        
            if Co.dir_y==1:
                Co.screen.blit(Im.player_image_walk_down1 if walk_frame==0 else Im.player_image_walk_down2 if walk_frame==1 else Im.player_image_walk_down3 if walk_frame==2 else Im.player_image_walk_down4 if walk_frame==3 else Im.player_image_walk_down5 if walk_frame==4 else Im.player_image_walk_down6,(Co.Px-32,Co.Py-8))
            if Co.dir_x==-1:
                Co.screen.blit(Im.player_image_walk_left1 if walk_frame==0 else Im.player_image_walk_left2 if walk_frame==1 else Im.player_image_walk_left3 if walk_frame==2 else Im.player_image_walk_left4 if walk_frame==3 else Im.player_image_walk_left5 if walk_frame==4 else Im.player_image_walk_left6,(Co.Px-32,Co.Py-8))
            if Co.dir_y==-1:
                Co.screen.blit(Im.player_image_walk_up1 if walk_frame==0 else Im.player_image_walk_up2 if walk_frame==1 else Im.player_image_walk_up3 if walk_frame==2 else Im.player_image_walk_up4 if walk_frame==3 else Im.player_image_walk_up5 if walk_frame==4 else Im.player_image_walk_up6,(Co.Px-32,Co.Py-8))
            if Co.dir_x==1:
                Co.screen.blit(Im.player_image_walk_right1 if walk_frame==0 else Im.player_image_walk_right2 if walk_frame==1 else Im.player_image_walk_right3 if walk_frame==2 else Im.player_image_walk_right4 if walk_frame==3 else Im.player_image_walk_right5 if walk_frame==4 else Im.player_image_walk_right6,(Co.Px-32,Co.Py-8))

    pygame.display.update()

pygame.quit()