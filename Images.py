import pygame
import Common as Co

#Int
Pih=64
Piw=64

#Load Images
#Sword
sword_icon=pygame.image.load('Icons/Sprite Sheet/first-edged-weapon_icon.png')
sword_icon=pygame.transform.scale(sword_icon,(Co.Sword_w+512,Co.Sword_h+512))
sword_image=pygame.image.load('Weapons/sword.png')
sword_image=pygame.transform.scale(sword_image,(Co.Sword_w+64,Co.Sword_h+64))
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
