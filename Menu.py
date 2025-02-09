import pygame
import Common as Co

pygame.init()

#Int
death_run=False
pause_run=False

#Main Menu
def main_menu():
    menu_run=True
    while menu_run:
        Co.screen.fill(0)
        title_text=Co.title_font.render("ITM",True,Co.WHITE)
        start_text=Co.menu_font.render("Start Game",True,Co.WHITE)
        options_text=Co.menu_font.render("Options",True,Co.WHITE)
        quit_text=Co.menu_font.render("Quit",True,Co.WHITE)

        Co.screen.blit(title_text,(Co.Screen_Width/2-title_text.get_width()/2,50))
        Co.screen.blit(start_text,(Co.Screen_Width/2-start_text.get_width()/2,350))
        Co.screen.blit(options_text,(Co.Screen_Width/2-options_text.get_width()/2,500))
        Co.screen.blit(quit_text,(Co.Screen_Width/2-quit_text.get_width()/2,700))

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                menu_run=False
                pygame.quit()
                return "quit"
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_ESCAPE:
                    pygame.display.toggle_fullscreen()
            if event.type==pygame.MOUSEBUTTONDOWN:
                if event.button==1:  # Left mouse button
                    mouse_x,mouse_y=event.pos
                    if start_text.get_rect(center=(Co.Screen_Width/2,350+start_text.get_height()/2)).collidepoint(mouse_x,mouse_y):
                        return "game"
                    elif options_text.get_rect(center=(Co.Screen_Width/2,500+options_text.get_height()/2)).collidepoint(mouse_x,mouse_y):
                        return "options"
                    elif quit_text.get_rect(center=(Co.Screen_Width/2,650+quit_text.get_height()/2)).collidepoint(mouse_x,mouse_y):
                        pygame.quit()
                        return "quit"

        pygame.display.update()

#Pause Menu
def pause_menu():
    pause_run=True
    while pause_run:
        Co.screen.fill(0)
        resume_text=Co.menu_font.render("Resume Game",True,Co.WHITE)
        pause_options_text=Co.menu_font.render("Options",True,Co.WHITE)
        main_menu_text=Co.menu_font.render("Main Menu",True,Co.WHITE)

        Co.screen.blit(resume_text,(Co.Screen_Width/2-resume_text.get_width()/2,250))
        Co.screen.blit(pause_options_text,(Co.Screen_Width/2-pause_options_text.get_width()/2,350))
        Co.screen.blit(main_menu_text,(Co.Screen_Width/2-main_menu_text.get_width()/2,450))

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pause_run=False
                pygame.quit()
                return "quit"
            if event.type==pygame.MOUSEBUTTONDOWN:
                if event.button==1:  # Left mouse button
                    mouse_x,mouse_y=event.pos
                    if resume_text.get_rect(center=(Co.Screen_Width/2,250+resume_text.get_height()/2)).collidepoint(mouse_x,mouse_y):
                        return "game"
                    elif pause_options_text.get_rect(center=(Co.Screen_Width/2,350+pause_options_text.get_height()/2)).collidepoint(mouse_x,mouse_y):
                        return "pause options"
                    elif main_menu_text.get_rect(center=(Co.Screen_Width/2,450+main_menu_text.get_height()/2)).collidepoint(mouse_x,mouse_y):
                        return "menu"

        pygame.display.update()

#Death Screen
def death_screen():
    death_run=True
    while death_run:
        Co.screen.fill(0)
        retry_text=Co.death_font.render("Main Menu",True,Co.WHITE)
        game_over_text=Co.font.render("Game Over",True,Co.RED)

        Co.screen.blit(game_over_text,(Co.Screen_Width/2-game_over_text.get_width()/2,Co.Screen_Height/2-game_over_text.get_height()/2))
        Co.screen.blit(retry_text,(Co.Screen_Width/2+25-retry_text.get_width()/2,600))

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                death_run=False
                pygame.quit()
                return "quit"
            if event.type==pygame.MOUSEBUTTONDOWN:
                if event.button==1:  # Left mouse button
                    mouse_x,mouse_y=event.pos
                    if retry_text.get_rect(center=(Co.Screen_Width/2+25,600+retry_text.get_height()/2)).collidepoint(mouse_x,mouse_y):
                        return "menu"

        pygame.display.update()

#Run loop
Co.run=True
game_state="menu"
while Co.run:
    Co.screen.fill(0)
    if game_state=="menu":
        game_state=main_menu()
    elif game_state=="pause":
        game_state=pause_menu()
    elif game_state=="death":
        game_state=death_screen()

    #Exit Screen
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            Co.run=False

    pygame.display.update()

pygame.quit()