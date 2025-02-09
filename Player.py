import pygame
from Common import game_state,run,screen, Px, Py, Pw, Ph, dir_x, dir_y, player_hit, hit_time, current_time, Player_alive, Screen_Width, Screen_Height, check_player_spirit_collision, check_player_sword_collision, Sword_picked_up, P_Health, Hw, damage_taken, idle_animation_timer, idle_animation_interval, idle_frame, walk_animation_timer, walk_animation_interval, walk_frame, RED, WHITE
from Images import player_image_idle_down1, player_image_idle_down2, player_image_idle_left1, player_image_idle_left2, player_image_idle_up1, player_image_idle_up2, player_image_idle_right1, player_image_idle_right2, player_image_walk_down1, player_image_walk_down2, player_image_walk_down3, player_image_walk_down4, player_image_walk_down5, player_image_walk_down6, player_image_walk_left1, player_image_walk_left2, player_image_walk_left3, player_image_walk_left4, player_image_walk_left5, player_image_walk_left6, player_image_walk_up1, player_image_walk_up2, player_image_walk_up3, player_image_walk_up4, player_image_walk_up5, player_image_walk_up6, player_image_walk_right1, player_image_walk_right2, player_image_walk_right3, player_image_walk_right4, player_image_walk_right5, player_image_walk_right6

pygame.init()

# Int
P_speed = float(1 / 4)
hit_duration = 200
Last_dir = 1
Hit_box = False
show_idle = True

# Run loop
while run:
    screen.fill(0)

    # Exit Screen
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        # Keys
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                Last_dir = 3
                show_idle = False
                dir_y = -1
                dir_x = 0

            if event.key == pygame.K_s:
                Last_dir = 1
                show_idle = False
                dir_y = 1
                dir_x = 0

            if event.key == pygame.K_d:
                Last_dir = 4
                show_idle = False
                dir_x = 1
                dir_y = 0

            if event.key == pygame.K_a:
                Last_dir = 2
                show_idle = False
                dir_x = -1
                dir_y = 0

            if event.key == pygame.K_ESCAPE and game_state == "game" and Player_alive:
                game_state = "pause"

            if event.key == pygame.K_h and not Hit_box and Player_alive:
                Hit_box = True

            if event.key == pygame.K_h and Hit_box and Player_alive:
                Hit_box = False

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                dir_y = 0
                show_idle = True

            if event.key == pygame.K_s:
                dir_y = 0
                show_idle = True

            if event.key == pygame.K_d:
                dir_x = 0
                show_idle = True

            if event.key == pygame.K_a:
                dir_x = 0
                show_idle = True

    # Player Movement
    if Player_alive:
        if dir_y != 0:
            Py += dir_y * P_speed

        if dir_x != 0:
            Px += dir_x * P_speed

        if Py < 0:
            Py = 0
        elif Py > Screen_Height - Ph:
            Py = Screen_Height - Ph

        if Px < 0:
            Px = 0
        elif Px > Screen_Width - Pw:
            Px = Screen_Width - Pw

    # Player Hit
    if player_hit and current_time - hit_time >= hit_duration:
        player_hit = False

    # Player
    if Player_alive:
        Pc = RED if player_hit else WHITE
        if Hit_box:
            pygame.draw.rect(screen, Pc, (Px, Py, Pw, Ph))

        # Idle animation
        if dir_x == 0 and dir_y == 0:
            if current_time - idle_animation_timer >= idle_animation_interval:
                idle_frame = 2 if idle_frame == 1 else 1
                idle_animation_timer = current_time

            if Last_dir == 1:
                screen.blit(player_image_idle_down1 if idle_frame == 1 else player_image_idle_down2, (Px - 32, Py - 8))
            if Last_dir == 2:
                screen.blit(player_image_idle_left1 if idle_frame == 1 else player_image_idle_left2, (Px - 32, Py - 8))
            if Last_dir == 3:
                screen.blit(player_image_idle_up1 if idle_frame == 1 else player_image_idle_up2, (Px - 32, Py - 8))
            if Last_dir == 4:
                screen.blit(player_image_idle_right1 if idle_frame == 1 else player_image_idle_right2, (Px - 32, Py - 8))

        # Walking animation
        if dir_x and dir_y in [1, -1]:
            if current_time - walk_animation_timer >= walk_animation_interval:
                walk_frame = (walk_frame + 1) % 6
                walk_animation_timer = current_time

            if dir_y == 1:
                screen.blit(player_image_walk_down1 if walk_frame == 0 else player_image_walk_down2 if walk_frame == 1 else player_image_walk_down3 if walk_frame == 2 else player_image_walk_down4 if walk_frame == 3 else player_image_walk_down5 if walk_frame == 4 else player_image_walk_down6, (Px - 32, Py - 8))
            if dir_x == -1:
                screen.blit(player_image_walk_left1 if walk_frame == 0 else player_image_walk_left2 if walk_frame == 1 else player_image_walk_left3 if walk_frame == 2 else player_image_walk_left4 if walk_frame == 3 else player_image_walk_left5 if walk_frame == 4 else player_image_walk_left6, (Px - 32, Py - 8))
            if dir_y == -1:
                screen.blit(player_image_walk_up1 if walk_frame == 0 else player_image_walk_up2 if walk_frame == 1 else player_image_walk_up3 if walk_frame == 2 else player_image_walk_up4 if walk_frame == 3 else player_image_walk_up5 if walk_frame == 4 else player_image_walk_up6, (Px - 32, Py - 8))
            if dir_x == 1:
                screen.blit(player_image_walk_right1 if walk_frame == 0 else player_image_walk_right2 if walk_frame == 1 else player_image_walk_right3 if walk_frame == 2 else player_image_walk_right4 if walk_frame == 3 else player_image_walk_right5 if walk_frame == 4 else player_image_walk_right6, (Px - 32, Py - 8))

    pygame.display.update()

pygame.quit()