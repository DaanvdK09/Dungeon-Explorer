import pygame

pygame.init()

#Int
Px = 642
Py = 350
Ph = 96
Pw = 60
Hw = 200
dir_y = 0
dir_x = 0
player_hit = False
Player_alive = True
hit_time = 0
P_Health = 110

Spirit_x = 321
Spirit_y = 350
Spirit_w = 15
Spirit_h = 15
Spirit_d = 5
SHw = 50
Spirit_hit = False
Spirit_alive = True
Spirit_hit_time = 0
Spirit_Health = 60

Sword_x = 500
Sword_y = 500
Sword_w = 96
Sword_h = 96
Sword_picked_up = False

damage_taken = 0
Spirit_damage_taken = 5
current_time = pygame.time.get_ticks()

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 128, 0)
GREY = (128, 128, 128)
YELLOW = (255, 255, 0)
GOLD = (255, 215, 0)

# Screen
Screen_Width = 1285
Screen_Height = 700
screen = pygame.display.set_mode((Screen_Width, Screen_Height))
pygame.display.set_caption("Game")
pygame.display.toggle_fullscreen()

# Font
font = pygame.font.Font(None, 296)
menu_font = pygame.font.Font(None, 75)
title_font = pygame.font.Font(None, 150)
death_font = pygame.font.Font(None, 100)

# Idle Animation Timer
idle_animation_timer = pygame.time.get_ticks()
idle_animation_interval = 500  # 0.5 seconds
idle_frame = 1

# Walking Animation Timer
walk_animation_timer = pygame.time.get_ticks()
walk_animation_interval = 100  # 0.1 seconds
walk_frame = 0

# Collision
def check_player_spirit_collision(player_rect, spirit_rect):
    return player_rect.colliderect(spirit_rect)

def check_player_sword_collision(player_rect, sword_rect):
    return player_rect.colliderect(sword_rect)

def check_collision(player_rect, orb):
    orb_rect = pygame.Rect(orb[0] - 5, orb[1] - 5, 10, 10)
    return player_rect.colliderect(orb_rect)

# Attack Interval
last_attack_time = pygame.time.get_ticks()
attack_interval = 5000  # 5 sec

# Run loop
run = True
while run:
    screen.fill(0)

    # Exit Screen
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    player_rect = pygame.Rect(Px, Py, Pw, Ph)
    spirit_rect = pygame.Rect(Spirit_x, Spirit_y, Spirit_w, Spirit_h)
    sword_rect = pygame.Rect(Sword_x, Sword_y, Sword_w, Sword_h)

    pygame.display.update()

pygame.quit()