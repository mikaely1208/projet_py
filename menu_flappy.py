import sys

import pygame
import pygame_gui



class Menu:

    def fonction_Menu(self):

        pygame.init()
        pygame.display.set_caption('Flappy Bird')
        window_surface = pygame.display.set_mode((880, 450))
        background = pygame.Surface((1900, 1080))
        background.fill(pygame.Color('Blue'))
        manager = pygame_gui.UIManager((1915, 1028))

        # creation des bouttons :

        Debutant_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((150, 30), (250, 125)),
                                                      text='Debutant',
                                                      manager=manager)

        Amateur_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((500, 30), (250, 125)),
                                                   text='Amateur',
                                                   manager=manager)

        Pro_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((500, 250), (250, 125)),
                                                   text='Pro',
                                                   manager=manager)

        free_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((150, 250), (250, 125)),
                                                    text='Free level',
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
                    if event.ui_element == Debutant_button:


                if event.type == pygame_gui.UI_BUTTON_PRESSED:
                    if event.ui_element == Amateur_button:


                if event.type == pygame_gui.UI_BUTTON_PRESSED:
                    if event.ui_element == free_button:


                if event.type == pygame_gui.UI_BUTTON_PRESSED:
                    if event.ui_element == Pro_button:


                manager.process_events(event)

            manager.update(time_delta)

            window_surface.blit(background, (0, 0))
            manager.draw_ui(window_surface)

            pygame.display.update()


if __name__ == '__main__':
    Menu().fonction_Menu()


