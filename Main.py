import pygame
import math
from Common import dir_x,dir_y,screen, run, Spirit_alive, Player_alive, current_time, last_attack_time, attack_interval, Px, Py, Pw, Ph, Spirit_x, Spirit_y, Spirit_w, Spirit_h, Spirit_hit, Spirit_hit_time, Spirit_Health, SHw, Sword_picked_up, check_player_spirit_collision, check_player_sword_collision, player_rect, spirit_rect, sword_rect

pygame.init()

# Int
Player_Fist_damage = 5
Player_Sword_damage = 10
Player_Axe_damage = 15

# Run loop
run = True
while run:
    screen.fill(0)

    # Exit Screen
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        # Player Attack Spirit
        if Spirit_alive and Player_alive:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if current_time - last_attack_time >= attack_interval:
                        distance = math.sqrt((Px - Spirit_x) ** 2 + (Py - Spirit_y) ** 2)
                        if distance <= 75:
                            Spirit_current_time = pygame.time.get_ticks()
                            Spirit_hit = True
                            Spirit_hit_time = Spirit_current_time
                            damage = Player_Sword_damage if Sword_picked_up else Player_Fist_damage
                            Spirit_Health -= damage
                            SHw -= (damage / Spirit_Health) * SHw
                            if Spirit_Health <= 10:
                                Spirit_alive = False
                                last_attack_time = current_time

    # Collision Player-Spirit
    if Player_alive and Spirit_alive:
        if check_player_spirit_collision(player_rect, spirit_rect):
            if dir_x > 0:
                Px = Spirit_x - Pw
            elif dir_x < 0:
                Px = Spirit_x + Spirit_w
            if dir_y > 0:
                Py = Spirit_y - Ph
            elif dir_y < 0:
                Py = Spirit_y + Spirit_h

    # Player Pick Up Sword
    if Player_alive and not Sword_picked_up:
        if check_player_sword_collision(player_rect, sword_rect):
            Sword_picked_up = True

    pygame.display.update()

pygame.quit()