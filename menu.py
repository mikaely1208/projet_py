import sys
import pygame
import pygame_gui
from pygame.locals import *



class Menu:

    def fonction_Menu(self):

        pygame.init()
        pygame.display.set_caption('Jeux')
        window_surface = pygame.display.set_mode((880, 450))
        background = pygame.Surface((1900, 1080))
        background.fill(pygame.Color('Black'))
        manager = pygame_gui.UIManager((1915, 1028))

        # creation des bouttons :

        morpion_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((150, 30), (250, 125)),
                                                      text='Morpion',
                                                      manager=manager)

        demineur_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((500, 30), (250, 125)),
                                                   text='Demineur',
                                                   manager=manager)

        P4_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((500, 250), (250, 125)),
                                                   text='Puissance 4',
                                                   manager=manager)

        flappy_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((150, 250), (250, 125)),
                                                    text='Flappy Bird',
                                                    manager=manager)


        clock = pygame.time.Clock()
        is_running = True

        while is_running:
            time_delta = clock.tick(60) / 1000.0
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    is_running = False
                    pygame.quit()

                if event.type == pygame_gui.UI_BUTTON_PRESSED:
                    if event.ui_element == morpion_button:
                        from jeu_morpion.main_morpion import Jeu
                        pygame.init()
                        Jeu().fonction_principale()
                        pygame.quit()

                if event.type == pygame_gui.UI_BUTTON_PRESSED:
                    if event.ui_element == demineur_button:
                        from démineur.main_demineur import Grid
                        #gameLoop()
                        pygame.quit()
                        quit()

                if event.type == pygame_gui.UI_BUTTON_PRESSED:
                    if event.ui_element == flappy_button:
                        from menu_flappy import Menu
                        Menu().fonction_Menu()

                if event.type == pygame_gui.UI_BUTTON_PRESSED:
                    if event.ui_element == P4_button:
                        from puissance4 import p4


                manager.process_events(event)

            manager.update(time_delta)

            window_surface.blit(background, (0, 0))
            manager.draw_ui(window_surface)

            pygame.display.update()


if __name__ == '__main__':
    pygame.init()
    Menu().fonction_Menu()
sys.exit()

