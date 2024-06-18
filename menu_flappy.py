import sys
from sys import exit
import pygame
import pygame_gui
from pygame.locals import *




class Menu:

    def fonction_Menu(self):

        pygame.init()
        pygame.display.set_caption('Flappy Bird')
        window_surface = pygame.display.set_mode((880, 450))
        background = pygame.Surface((1900, 1080))
        background.fill(pygame.Color('Beige'))
        manager = pygame_gui.UIManager((1915, 1028))

        # creation des bouttons :

        Precision_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((150, 30), (250, 125)),
                                                      text='Precision over all',
                                                      manager=manager)

        Serre_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((500, 30), (250, 125)),
                                                   text='Tight as sardines',
                                                   manager=manager)


        Vitesse_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((150, 250), (250, 125)),
                                                    text='Faster than ever',
                                                    manager=manager)

        Train_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((500, 250), (250, 125)),
                                                    text='Improve yourself',
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
                    if event.ui_element == Precision_button:
                        from Flappy.Script.flappy1 import Window



                if event.type == pygame_gui.UI_BUTTON_PRESSED:
                    if event.ui_element == Serre_button:
                        from Flappy.Script.flappy2 import Window


                if event.type == pygame_gui.UI_BUTTON_PRESSED:
                    if event.ui_element == Vitesse_button:
                        from Flappy.Script.flappy3 import Window



                if event.type == pygame_gui.UI_BUTTON_PRESSED:
                    if event.ui_element == Train_button:
                        from Flappy.Script.flappy import Window






                manager.process_events(event)

            manager.update(time_delta)

            window_surface.blit(background, (0, 0))
            manager.draw_ui(window_surface)

            pygame.display.update()


if __name__ == '__main__':
    pygame.init()
    Menu().fonction_Menu()


