import pygame
from Common import run,screen,damage_taken,Sword_picked_up, Sword_w, Sword_h, P_Health, Hw, player_hit, hit_time, current_time, Spirit_x, Spirit_y, Spirit_w, Spirit_h, Spirit_hit, Spirit_hit_time, Spirit_damage_taken, Spirit_Health, Screen_Width, Screen_Height, GOLD, BLACK, GREEN, RED
from Images import sword_icon

pygame.init()

# Int
Iconx = 975
Icony = 375
Hh = 30
SHh = 10

# Run loop
while run:
    screen.fill(0)

    # Exit Screen
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # Inventory
    pygame.draw.circle(screen, GOLD, (1350, 750), 200)
    pygame.draw.circle(screen, BLACK, (1345, 745), 185)

    # Inventory Icon
    if Sword_picked_up:
        screen.blit(sword_icon, (Iconx, Icony))

    # Healthbar
    pygame.draw.rect(screen, GOLD, (float(22 + (1 / 2)), float(36 + (1 / 2)), 205, 38))
    pygame.draw.rect(screen, BLACK, (25, 40, 200, 30))
    pygame.draw.rect(screen, GREEN, (25, 40, Hw, Hh))
    if player_hit:
        elapsed_time = current_time - hit_time
        Dw = (damage_taken / P_Health) * Hw
        pygame.draw.rect(screen, RED, (25 + Hw, 40, Dw, Hh))

    # Spirit Healthbar
    pygame.draw.rect(screen, GREEN, ((Spirit_x - (Spirit_w / 2) + 5), (Spirit_y - 25), Spirit_w, SHh))
    if Spirit_hit:
        elapsed_time = current_time - Spirit_hit_time
        SDw = (Spirit_damage_taken / Spirit_Health) * Spirit_w
        pygame.draw.rect(screen, RED, ((Spirit_x - ((Spirit_w / 2)) + 5) + Spirit_w, (Spirit_y - 25), SDw, SHh))

    pygame.display.update()

pygame.quit()