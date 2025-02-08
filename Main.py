import pygame
import math
import os

pygame.init()

#Int
Px=642
Py=350
Ph=96
Pw=60
Pih=64
Piw=64
Iconx=975
Icony=375
Hw=200
Hh=30
dir_y=0
dir_x=0
P_speed=float(1/4)
last_shot_time=pygame.time.get_ticks()
player_hit=False
Player_alive=True
hit_duration=200
hit_time=0
Last_dir=1
Hit_box=False
show_idle=True
death_run=False
pause_run=False

Spirit_x=321
Spirit_y=350
Spirit_w=15
Spirit_h=15
Spirit_d=5
SHw=50
SHh=10
Spirit_alive=True
Spirit_hit=False
Spirit_hit_duration=75
Spirit_hit_time=0
Spirit_Health=60
Spirit_damage=10
shot_interval=1500
S_speed=float(1/4)
orbs=[]
orb_speed=1

BLACK=(0,0,0)
WHITE=(255,255,255)
RED=(255,0,0)
GREEN=(0,128,0)
GREY=(128,128,128)
YELLOW=(255,255,0)
GOLD=(255,215,0)

#Health
P_Health=110

#Items
#Sword
Sword_x=500
Sword_y=500
Sword_w=96
Sword_h=96
Sword_picked_up=False

#Damage
#Player
Player_Fist_damage=5
Player_Sword_damage=10
Player_Axe_damage=15

#Screen
Screen_Width=1285
Screen_Height=700

screen=pygame.display.set_mode((Screen_Width,Screen_Height))
pygame.display.set_caption("Game")
pygame.display.toggle_fullscreen()

#Font Render
font=pygame.font.Font(None,296)
menu_font=pygame.font.Font(None, 75)
title_font=pygame.font.Font(None,150)
death_font=pygame.font.Font(None,100)

#Load Images
#Sword
sword_icon=pygame.image.load('Icons/Sprite Sheet/first-edged-weapon_icon.png')
sword_icon=pygame.transform.scale(sword_icon,(Sword_w+512,Sword_h+512))
sword_image=pygame.image.load('Weapons/sword.png')
sword_image=pygame.transform.scale(sword_image,(Sword_w+64,Sword_h+64))
#Player
#Idle
player_image_idle_down1=pygame.image.load('Main Character/Idle/Main Character Idle Down ITM-1.png')
player_image_idle_down1=pygame.transform.scale(player_image_idle_down1,(Piw+64,Pih+64))
player_image_idle_down2=pygame.image.load('Main Character/Idle/Main Character Idle Down ITM-2.png')
player_image_idle_down2=pygame.transform.scale(player_image_idle_down2,(Piw+64,Pih+64))

player_image_idle_left1=pygame.image.load('Main Character/Idle/Main Character Idle Left ITM-1.png')
player_image_idle_left1=pygame.transform.scale(player_image_idle_left1,(Piw+64,Pih+64))
player_image_idle_left2=pygame.image.load('Main Character/Idle/Main Character Idle Left ITM-2.png')
player_image_idle_left2=pygame.transform.scale(player_image_idle_left2,(Piw+64,Pih+64))

player_image_idle_up1=pygame.image.load('Main Character/Idle/Main Character Idle Up ITM-1.png')
player_image_idle_up1=pygame.transform.scale(player_image_idle_up1,(Piw+64,Pih+64))
player_image_idle_up2=pygame.image.load('Main Character/Idle/Main Character Idle Up ITM-2.png')
player_image_idle_up2=pygame.transform.scale(player_image_idle_up2,(Piw+64,Pih+64))

player_image_idle_right1=pygame.image.load('Main Character/Idle/Main Character Idle Right ITM-1.png')
player_image_idle_right1=pygame.transform.scale(player_image_idle_right1,(Piw+64,Pih+64))
player_image_idle_right2=pygame.image.load('Main Character/Idle/Main Character Idle Right ITM-2.png')
player_image_idle_right2=pygame.transform.scale(player_image_idle_right2,(Piw+64,Pih+64))

#Walking
player_image_walk_down1=pygame.image.load('Main Character/Walking/Main Character Walking Down ITM-1.png')
player_image_walk_down1=pygame.transform.scale(player_image_walk_down1,(Piw+64,Pih+64))
player_image_walk_down2=pygame.image.load('Main Character/Walking/Main Character Walking Down ITM-2.png')
player_image_walk_down2=pygame.transform.scale(player_image_walk_down2,(Piw+64,Pih+64))
player_image_walk_down3=pygame.image.load('Main Character/Walking/Main Character Walking Down ITM-3.png')
player_image_walk_down3=pygame.transform.scale(player_image_walk_down3,(Piw+64,Pih+64))
player_image_walk_down4=pygame.image.load('Main Character/Walking/Main Character Walking Down ITM-4.png')
player_image_walk_down4=pygame.transform.scale(player_image_walk_down4,(Piw+64,Pih+64))
player_image_walk_down5=pygame.image.load('Main Character/Walking/Main Character Walking Down ITM-5.png')
player_image_walk_down5=pygame.transform.scale(player_image_walk_down5,(Piw+64,Pih+64))
player_image_walk_down6=pygame.image.load('Main Character/Walking/Main Character Walking Down ITM-6.png')
player_image_walk_down6=pygame.transform.scale(player_image_walk_down6,(Piw+64,Pih+64))

player_image_walk_left1=pygame.image.load('Main Character/Walking/Main Character Walking Left ITM-1.png')
player_image_walk_left1=pygame.transform.scale(player_image_walk_left1,(Piw+64,Pih+64))
player_image_walk_left2=pygame.image.load('Main Character/Walking/Main Character Walking Left ITM-2.png')
player_image_walk_left2=pygame.transform.scale(player_image_walk_left2,(Piw+64,Pih+64))
player_image_walk_left3=pygame.image.load('Main Character/Walking/Main Character Walking Left ITM-3.png')
player_image_walk_left3=pygame.transform.scale(player_image_walk_left3,(Piw+64,Pih+64))
player_image_walk_left4=pygame.image.load('Main Character/Walking/Main Character Walking Left ITM-4.png')
player_image_walk_left4=pygame.transform.scale(player_image_walk_left4,(Piw+64,Pih+64))
player_image_walk_left5=pygame.image.load('Main Character/Walking/Main Character Walking Left ITM-5.png')
player_image_walk_left5=pygame.transform.scale(player_image_walk_left5,(Piw+64,Pih+64))
player_image_walk_left6=pygame.image.load('Main Character/Walking/Main Character Walking Left ITM-6.png')
player_image_walk_left6=pygame.transform.scale(player_image_walk_left6,(Piw+64,Pih+64))

player_image_walk_up1=pygame.image.load('Main Character/Walking/Main Character Walking Up ITM-1.png')
player_image_walk_up1=pygame.transform.scale(player_image_walk_up1,(Piw+64,Pih+64))
player_image_walk_up2=pygame.image.load('Main Character/Walking/Main Character Walking Up ITM-2.png')
player_image_walk_up2=pygame.transform.scale(player_image_walk_up2,(Piw+64,Pih+64))
player_image_walk_up3=pygame.image.load('Main Character/Walking/Main Character Walking Up ITM-3.png')
player_image_walk_up3=pygame.transform.scale(player_image_walk_up3,(Piw+64,Pih+64))
player_image_walk_up4=pygame.image.load('Main Character/Walking/Main Character Walking Up ITM-4.png')
player_image_walk_up4=pygame.transform.scale(player_image_walk_up4,(Piw+64,Pih+64))
player_image_walk_up5=pygame.image.load('Main Character/Walking/Main Character Walking Up ITM-5.png')
player_image_walk_up5=pygame.transform.scale(player_image_walk_up5,(Piw+64,Pih+64))
player_image_walk_up6=pygame.image.load('Main Character/Walking/Main Character Walking Up ITM-6.png')
player_image_walk_up6=pygame.transform.scale(player_image_walk_up6,(Piw+64,Pih+64))

player_image_walk_right1=pygame.image.load('Main Character/Walking/Main Character Walking Right ITM-1.png')
player_image_walk_right1=pygame.transform.scale(player_image_walk_right1,(Piw+64,Pih+64))
player_image_walk_right2=pygame.image.load('Main Character/Walking/Main Character Walking Right ITM-2.png')
player_image_walk_right2=pygame.transform.scale(player_image_walk_right2,(Piw+64,Pih+64))
player_image_walk_right3=pygame.image.load('Main Character/Walking/Main Character Walking Right ITM-3.png')
player_image_walk_right3=pygame.transform.scale(player_image_walk_right3,(Piw+64,Pih+64))
player_image_walk_right4=pygame.image.load('Main Character/Walking/Main Character Walking Right ITM-4.png')
player_image_walk_right4=pygame.transform.scale(player_image_walk_right4,(Piw+64,Pih+64))
player_image_walk_right5=pygame.image.load('Main Character/Walking/Main Character Walking Right ITM-5.png')
player_image_walk_right5=pygame.transform.scale(player_image_walk_right5,(Piw+64,Pih+64))
player_image_walk_right6=pygame.image.load('Main Character/Walking/Main Character Walking Right ITM-6.png')
player_image_walk_right6=pygame.transform.scale(player_image_walk_right6,(Piw+64,Pih+64))

#Idle Animation Timer
idle_animation_timer=pygame.time.get_ticks()
idle_animation_interval=500  # 0.5 seconds
idle_frame=1

# Walking Animation Timer
walk_animation_timer=pygame.time.get_ticks()
walk_animation_interval=100  # 0.1 seconds
walk_frame=0

#collision
def check_player_spirit_collision(player_rect,spirit_rect):
    return player_rect.colliderect(spirit_rect)

def check_player_sword_collision(player_rect,sword_rect):
    return player_rect.colliderect(sword_rect)

def check_collision(player_rect,orb):
    orb_rect=pygame.Rect(orb[0]-5,orb[1]-5,10,10)
    return player_rect.colliderect(orb_rect)

#Attack Interval
last_attack_time=pygame.time.get_ticks()
attack_interval=5000 #5 sec

#Main Menu
def main_menu():
    menu_run=True
    while menu_run:
        screen.fill(0)
        title_text=title_font.render("ITM",True,WHITE)
        start_text=menu_font.render("Start Game",True,WHITE)
        options_text=menu_font.render("Options",True,WHITE)
        quit_text=menu_font.render("Quit",True,WHITE)

        screen.blit(title_text,(Screen_Width/2-title_text.get_width()/2,50))
        screen.blit(start_text,(Screen_Width/2-start_text.get_width()/2,350))
        screen.blit(options_text,(Screen_Width/2-options_text.get_width()/2,500))
        screen.blit(quit_text,(Screen_Width-quit_text.get_width()/2,700))

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                menu_run=False
                pygame.quit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_ESCAPE:
                    pygame.display.toggle_fullscreen()
            if event.type==pygame.MOUSEBUTTONDOWN:
                if event.button==1:  # Left mouse button
                    mouse_x,mouse_y=event.pos
                    if start_text.get_rect(center=(Screen_Width/2,350+start_text.get_height()/2)).collidepoint(mouse_x,mouse_y):
                        return "game"
                    elif options_text.get_rect(center=(Screen_Width/2,500+options_text.get_height()/2)).collidepoint(mouse_x,mouse_y):
                        return "options"
                    elif quit_text.get_rect(center=(Screen_Width,700+quit_text.get_height()/2)).collidepoint(mouse_x,mouse_y):
                        pygame.quit()

        pygame.display.update()

#Pause Menu
def pause_menu():
    pause_run=True
    while pause_run:
        screen.fill(0)
        resume_text=menu_font.render("Resume Game",True,WHITE)
        pause_options_text=menu_font.render("Options",True,WHITE)
        main_menu_text=menu_font.render("Main Menu",True,WHITE)

        screen.blit(resume_text,(Screen_Width/2-resume_text.get_width()/2,250))
        screen.blit(pause_options_text,(Screen_Width/2-pause_options_text.get_width()/2,350))
        screen.blit(main_menu_text,(Screen_Width/2-main_menu_text.get_width()/2,450))

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pause_run=False
                pygame.quit
            if event.type==pygame.MOUSEBUTTONDOWN:
                if event.button==1:  # Left mouse button
                    mouse_x,mouse_y=event.pos
                    if resume_text.get_rect(center=(Screen_Width/2,250+resume_text.get_height()/2)).collidepoint(mouse_x,mouse_y):
                        return "game"
                    elif pause_options_text.get_rect(center=(Screen_Width/2,350+pause_options_text.get_height()/2)).collidepoint(mouse_x,mouse_y):
                        return "pause options"
                    elif main_menu_text.get_rect(center=(Screen_Width/2,450+main_menu_text.get_height()/2)).collidepoint(mouse_x,mouse_y):
                        return "menu"

        pygame.display.update()

#Death Screen
def death_screen():
    death_run=True
    while death_run:
        screen.fill(0)
        retry_text=death_font.render("Main Menu",True,WHITE)
        game_over_text=font.render("Game Over",True,RED)

        screen.blit(game_over_text,(Screen_Width/2-game_over_text.get_width()/2,Screen_Height/2-game_over_text.get_height()/2))
        screen.blit(retry_text,(Screen_Width/2+25-retry_text.get_width()/2,600))

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                death_run=False
                pygame.quit()
            if event.type==pygame.MOUSEBUTTONDOWN:
                if event.button==1:  # Left mouse button
                    mouse_x,mouse_y=event.pos
                    if retry_text.get_rect(center=(Screen_Width/2+25,600+retry_text.get_height()/2)).collidepoint(mouse_x,mouse_y):
                        return "menu"

        pygame.display.update()

#Run loop
run=True
game_state="menu"
while run:
    screen.fill(0)
    if game_state=="menu":
        game_state=main_menu()
    elif game_state=="pause":
        game_state=pause_menu()
    elif game_state=="death":
        game_state=death_screen()

#Exit Screen
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False

#Keys
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_w:
                Last_dir=3
                show_idle=False
                dir_y=-1
                dir_x=0

            if event.key==pygame.K_s:
                Last_dir=1
                show_idle=False
                dir_y=1
                dir_x=0

            if event.key==pygame.K_d:
                Last_dir=4
                show_idle=False
                dir_x=1
                dir_y=0

            if event.key==pygame.K_a:
                Last_dir=2
                show_idle=False
                dir_x=-1
                dir_y=0

            if event.key==pygame.K_ESCAPE and game_state=="game" and Player_alive==True:
                game_state="pause"

            if event.key==pygame.K_h and Hit_box==False and Player_alive==True:
                Hit_box==True

            if event.key==pygame.K_h and Hit_box==True and Player_alive==True:
                Hit_box==False
                
        if event.type==pygame.KEYUP:
            if event.key==pygame.K_w:
                dir_y=0
                show_idle=True

            if event.key==pygame.K_s:
                dir_y=0
                show_idle=True

            if event.key==pygame.K_d:
                dir_x=0
                show_idle=True

            if event.key==pygame.K_a:
                dir_x=0
                show_idle=True

        #Player Attack Spirit
        if Spirit_alive and Player_alive==True:
            Spirit_current_time=pygame.time.get_ticks()
            if event.type==pygame.MOUSEBUTTONDOWN:
                if event.button==1:
                    current_time=pygame.time.get_ticks()
                    if current_time-last_attack_time>=attack_interval:
                        distance=math.sqrt((Px-Spirit_x)**2+(Py-Spirit_y)**2)
                        if distance<=75:
                            Spirit_hit=True
                            Spirit_hit_time=Spirit_current_time
                            damage=Player_Sword_damage if Sword_picked_up else Player_Fist_damage
                            Spirit_Health-=damage
                            SHw-=(damage/Spirit_Health)*SHw
                            Spirit_damage_taken=Player_Fist_damage
                            if Spirit_Health<=10:
                                Spirit_alive=False
                                last_attack_time=current_time
    #Player Movement
    player_rect=pygame.Rect(Px,Py,Pw,Ph)
    spirit_rect=pygame.Rect(Spirit_x, Spirit_y, Spirit_w, Spirit_h)
    sword_rect=pygame.Rect(Sword_x,Sword_y,Sword_w,Sword_h)

    if Player_alive==True:
        if dir_y!=0:
            Py+=dir_y*P_speed

        if dir_x!=0:
            Px+=dir_x*P_speed

        if dir_y!=0:
            Py+=dir_y*P_speed
        if Py<0:
            Py=0
        elif Py>Screen_Height-Ph:
            Py=Screen_Height-Ph

        if dir_x!=0:
            Px+=dir_x*P_speed
        if Px<0:
            Px=0
        elif Px>Screen_Width-Pw:
            Px=Screen_Width-Pw


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

    #Spirit Movement
    if Spirit_alive==True:
        distance=math.sqrt((Px-Spirit_x)**2+(Py-Spirit_y)**2)
        if distance>100:
            if Px+(Pw/2)>Spirit_x+(Spirit_w/2):
                Spirit_x+=S_speed
            elif Px+(Pw/2)<Spirit_x+(Spirit_w/2):
                Spirit_x-=S_speed

        if distance<100:
            if Py+(Ph/2)>Spirit_y+(Spirit_h/2):
                Spirit_y+=S_speed
            elif Py+(Ph/2)<Spirit_y+(Spirit_h/2):
               Spirit_y-=S_speed

    #Player Hit
    if player_hit and current_time-hit_time>=hit_duration:
        player_hit=False

    #Player
    if Player_alive==True:
        Pc=RED if player_hit else WHITE
        if Hit_box==True:
            pygame.draw.rect(screen,Pc,(Px,Py,Pw,Ph))
        
        # Idle animation
        current_time=pygame.time.get_ticks()
        if dir_x==0 and dir_y==0:
            if current_time-idle_animation_timer>=idle_animation_interval:
                idle_frame=2 if idle_frame==1 else 1
                idle_animation_timer=current_time
        
            if Last_dir==1:
                screen.blit(player_image_idle_down1 if idle_frame==1 else player_image_idle_down2,(Px-32,Py-8))
            if Last_dir==2:
                screen.blit(player_image_idle_left1 if idle_frame==1 else player_image_idle_left2,(Px-32,Py-8))
            if Last_dir==3:
                screen.blit(player_image_idle_up1 if idle_frame==1 else player_image_idle_up2,(Px-32,Py-8))
            if Last_dir==4:
                screen.blit(player_image_idle_right1 if idle_frame==1 else player_image_idle_right2,(Px-32,Py-8))

        #Walking animation
        current_time=pygame.time.get_ticks()
        if dir_x and dir_y==1 or -1:
            if current_time-walk_animation_timer>=walk_animation_interval:
                walk_frame=(walk_frame+1)%6
                walk_animation_timer=current_time
        
            if dir_y==1:
                screen.blit(player_image_walk_down1 if walk_frame==0 else player_image_walk_down2 if walk_frame==1 else player_image_walk_down3 if walk_frame==2 else player_image_walk_down4 if walk_frame==3 else player_image_walk_down5 if walk_frame==4 else player_image_walk_down6,(Px-32,Py-8))
            if dir_x==-1:
                screen.blit(player_image_walk_left1 if walk_frame==0 else player_image_walk_left2 if walk_frame==1 else player_image_walk_left3 if walk_frame==2 else player_image_walk_left4 if walk_frame==3 else player_image_walk_left5 if walk_frame==4 else player_image_walk_left6,(Px-32,Py-8))
            if dir_y==-1:
                screen.blit(player_image_walk_up1 if walk_frame==0 else player_image_walk_up2 if walk_frame==1 else player_image_walk_up3 if walk_frame==2 else player_image_walk_up4 if walk_frame==3 else player_image_walk_up5 if walk_frame==4 else player_image_walk_up6,(Px-32,Py-8))
            if dir_x==1:
                screen.blit(player_image_walk_right1 if walk_frame==0 else player_image_walk_right2 if walk_frame==1 else player_image_walk_right3 if walk_frame==2 else player_image_walk_right4 if walk_frame==3 else player_image_walk_right5 if walk_frame==4 else player_image_walk_right6,(Px-32,Py-8))

    #Spirit Attack
    if Spirit_alive and Player_alive==True:
        current_time=pygame.time.get_ticks()
        if distance<=500 and current_time-last_shot_time>=shot_interval:
            orbs.append([Spirit_x+(Spirit_w/2),Spirit_y+(Spirit_h/2),(Px+(Pw/2))-(Spirit_x+(Spirit_w/2)),(Py+(Ph / 2))-(Spirit_y+(Spirit_h/2))])
            last_shot_time=current_time

    #Ghost orb Movement
    orbs=[orb for orb in orbs if not check_collision(player_rect,orb)]

    for orb in orbs:
        orb[0]+=orb[2]*orb_speed/150
        orb[1]+=orb[3]*orb_speed/150
        pygame.draw.circle(screen,GREY,(int(orb[0]),int(orb[1])),5)

        #Damage Player
        if Player_alive==True:
            if check_collision(player_rect,orb):
                P_Health-=Spirit_damage
                Hw-=(Spirit_damage/P_Health)*Hw
                damage_taken=Spirit_damage
                player_hit=True
                hit_time=current_time
                orbs.remove(orb)
                if P_Health<=10:
                    Player_alive=False
                    game_state="death"

    #Remove Ghost orbs that are off-screen
    orbs=[orb for orb in orbs if 0<=orb[0]<=Screen_Width and 0<=orb[1]<=Screen_Height]

    #Spirit Hit
    if Spirit_hit and Spirit_current_time-Spirit_hit_time>=Spirit_hit_duration:
        Spirit_hit=False

    #Spirit
    if Spirit_alive==True:
        Sc=RED if Spirit_hit else GREY
        pygame.draw.rect(screen,Sc,(Spirit_x,Spirit_y,Spirit_w,Spirit_h))

    #Sword
    if Sword_picked_up==False:
        screen.blit(sword_image,(Sword_x,Sword_y))

    #Inventory
    pygame.draw.circle(screen,GOLD,(1350,750),200)
    pygame.draw.circle(screen,BLACK,(1345,745),185)

    #Inventory Icon
    if Sword_picked_up==True:
        screen.blit(sword_icon,(Iconx,Icony))

    #Healthbar
    pygame.draw.rect(screen,GOLD,(float(22+(1/2)),float(36+(1/2)),205,38))
    pygame.draw.rect(screen,BLACK,(25,40,200,30))
    pygame.draw.rect(screen,GREEN,(25,40,Hw,Hh))
    if player_hit:
        elapsed_time=current_time-hit_time
        Dw=(damage_taken/P_Health)*Hw
        pygame.draw.rect(screen,RED,(25+Hw,40,Dw,Hh))

    #Spirit Healthbar
    pygame.draw.rect(screen,GREEN,((Spirit_x-(SHw/2)+5),(Spirit_y-25),SHw,SHh))
    if Spirit_hit:
        elapesed_time=Spirit_current_time-Spirit_hit_time
        SDw=(Spirit_damage_taken/Spirit_Health)*SHw
        pygame.draw.rect(screen,RED,((Spirit_x-((SHw/2))+5)+SHw,(Spirit_y-25),SDw,SHh)) 
    pygame.display.update()

pygame.quit() 