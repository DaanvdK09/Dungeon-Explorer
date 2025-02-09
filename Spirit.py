import pygame
import math
from Common import game_state,Spirit_hit_time,Hw,P_Health,run,screen, Px, Py, Pw, Ph, Spirit_x, Spirit_y, Spirit_w, Spirit_h, Spirit_alive, Player_alive, current_time, check_collision, Screen_Width, Screen_Height, GREY, RED

pygame.init()

# Int
last_shot_time = pygame.time.get_ticks()
Spirit_hit_duration = 75
Spirit_damage = 10
shot_interval = 1500
S_speed = float(1 / 4)
orbs = []
orb_speed = 1

# Run loop
while run:

    # Exit Screen
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # Spirit Movement
    if Spirit_alive:
        distance = math.sqrt((Px - Spirit_x) ** 2 + (Py - Spirit_y) ** 2)
        if distance > 100:
            if Px + (Pw / 2) > Spirit_x + (Spirit_w / 2):
                Spirit_x += S_speed
            elif Px + (Pw / 2) < Spirit_x + (Spirit_w / 2):
                Spirit_x -= S_speed

        if distance < 100:
            if Py + (Ph / 2) > Spirit_y + (Spirit_h / 2):
                Spirit_y += S_speed
            elif Py + (Ph / 2) < Spirit_y + (Spirit_h / 2):
                Spirit_y -= S_speed

    # Spirit Attack
    if Spirit_alive and Player_alive:
        if distance <= 500 and current_time - last_shot_time >= shot_interval:
            orbs.append([Spirit_x + (Spirit_w / 2), Spirit_y + (Spirit_h / 2), (Px + (Pw / 2)) - (Spirit_x + (Spirit_w / 2)), (Py + (Ph / 2)) - (Spirit_y + (Spirit_h / 2))])
            last_shot_time = current_time

    # Ghost orb Movement
    orbs = [orb for orb in orbs if not check_collision(pygame.Rect(Px, Py, Pw, Ph), orb)]

    for orb in orbs:
        orb[0] += orb[2] * orb_speed / 150
        orb[1] += orb[3] * orb_speed / 150
        pygame.draw.circle(screen, GREY, (int(orb[0]), int(orb[1])), 5)

        # Damage Player
        if Player_alive:
            if check_collision(pygame.Rect(Px, Py, Pw, Ph), orb):
                P_Health -= Spirit_damage
                Hw -= (Spirit_damage / P_Health) * Hw
                damage_taken = Spirit_damage
                player_hit = True
                hit_time = current_time
                orbs.remove(orb)
                if P_Health <= 10:
                    Player_alive = False
                    game_state = "death"

    # Remove Ghost orbs that are off-screen
    orbs = [orb for orb in orbs if 0 <= orb[0] <= Screen_Width and 0 <= orb[1] <= Screen_Height]

    # Spirit Hit
    if Spirit_hit and current_time - Spirit_hit_time >= Spirit_hit_duration:
        Spirit_hit = False

    # Spirit
    if Spirit_alive:
        Sc = RED if Spirit_hit else GREY
        pygame.draw.rect(screen, Sc, (Spirit_x, Spirit_y, Spirit_w, Spirit_h))

    pygame.display.update()

pygame.quit()