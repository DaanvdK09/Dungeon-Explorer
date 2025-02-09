import pygame
from Common import game_state,run,screen, title_font, menu_font, death_font, Screen_Width, Screen_Height, WHITE

pygame.init()

# Int
death_run = False
pause_run = False

# Main Menu
def main_menu():
    menu_run = True
    while menu_run:
        screen.fill(0)
        title_text = title_font.render("ITM", True, WHITE)
        start_text = menu_font.render("Start Game", True, WHITE)
        options_text = menu_font.render("Options", True, WHITE)
        quit_text = menu_font.render("Quit", True, WHITE)

        screen.blit(title_text, (Screen_Width / 2 - title_text.get_width() / 2, 50))
        screen.blit(start_text, (Screen_Width / 2 - start_text.get_width() / 2, 350))
        screen.blit(options_text, (Screen_Width / 2 - options_text.get_width() / 2, 500))
        screen.blit(quit_text, (Screen_Width / 2 - quit_text.get_width() / 2, 700))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                menu_run = False
                pygame.quit()
                return "quit"
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.display.toggle_fullscreen()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button
                    mouse_x, mouse_y = event.pos
                    if start_text.get_rect(center=(Screen_Width / 2, 350 + start_text.get_height() / 2)).collidepoint(mouse_x, mouse_y):
                        return "game"  # Transition to game state
                    elif options_text.get_rect(center=(Screen_Width / 2, 500 + options_text.get_height() / 2)).collidepoint(mouse_x, mouse_y):
                        return "options"
                    elif quit_text.get_rect(center=(Screen_Width / 2, 650 + quit_text.get_height() / 2)).collidepoint(mouse_x, mouse_y):
                        pygame.quit()
                        return "quit"

        pygame.display.update()

# Pause Menu
def pause_menu():
    pause_run = True
    while pause_run:
        screen.fill(0)
        resume_text = menu_font.render("Resume Game", True, WHITE)
        pause_options_text = menu_font.render("Options", True, WHITE)
        main_menu_text = menu_font.render("Main Menu", True, WHITE)

        screen.blit(resume_text, (Screen_Width / 2 - resume_text.get_width() / 2, 250))
        screen.blit(pause_options_text, (Screen_Width / 2 - pause_options_text.get_width() / 2, 350))
        screen.blit(main_menu_text, (Screen_Width / 2 - main_menu_text.get_width() / 2, 450))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pause_run = False
                pygame.quit()
                return "quit"
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button
                    mouse_x, mouse_y = event.pos
                    if resume_text.get_rect(center=(Screen_Width / 2, 250 + resume_text.get_height() / 2)).collidepoint(mouse_x, mouse_y):
                        return "game"
                    elif pause_options_text.get_rect(center=(Screen_Width / 2, 350 + pause_options_text.get_height() / 2)).collidepoint(mouse_x, mouse_y):
                        return "pause options"
                    elif main_menu_text.get_rect(center=(Screen_Width / 2, 450 + main_menu_text.get_height() / 2)).collidepoint(mouse_x, mouse_y):
                        return "menu"

        pygame.display.update()

# Death Screen
def death_screen():
    death_run = True
    while death_run:
        screen.fill(0)
        retry_text = death_font.render("Main Menu", True, WHITE)
        game_over_text = title_font.render("Game Over", True, WHITE)

        screen.blit(game_over_text, (Screen_Width / 2 - game_over_text.get_width() / 2, Screen_Height / 2 - game_over_text.get_height() / 2))
        screen.blit(retry_text, (Screen_Width / 2 + 25 - retry_text.get_width() / 2, 600))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                death_run = False
                pygame.quit()
                return "quit"
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button
                    mouse_x, mouse_y = event.pos
                    if retry_text.get_rect(center=(Screen_Width / 2 + 25, 600 + retry_text.get_height() / 2)).collidepoint(mouse_x, mouse_y):
                        return "menu"

        pygame.display.update()

# Run loop
while run:
    screen.fill(0)
    if game_state == "menu":
        game_state = main_menu()
    elif game_state == "pause":
        game_state = pause_menu()
    elif game_state == "death":
        game_state = death_screen()
    elif game_state == "game":
        run=True

    # Exit Screen
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False

    pygame.display.update()

pygame.quit()