import math
import os
from random import randint


import pygame
from pygame.locals import *

red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)


FPS = 60
ANIMATION_SPEED = 0.18
WIN_WIDTH = 1024
WIN_HEIGHT = 600




class Bird(pygame.sprite.Sprite):
    """Représente l'oiseau contrôlé par le joueur.

Pepito est le "héros" de ce jeu.  Le joueur peut le faire grimper
    (monter rapidement), sinon il coule (descendre plus lentement).  Il doit
    passer dans l'espace entre les tuyaux (pour chaque tuyau passé, un point est marqué).
    point est marqué) ; s'il s'écrase sur un tuyau, le jeu se termine.

    Attributs :
    x : La coordonnée X de l'oiseau.
    y : Coordonnée Y de l'oiseau.
    msec_to_climb : Le nombre de millisecondes restant pour grimper, où une
        une ascension complète dure Bird.CLIMB_DURATION millisecondes.

    Constantes :
    WIDTH : La largeur, en pixels, de l'image de l'oiseau.
    HEIGHT : La hauteur, en pixels, de l'image de l'oiseau.
    SINK_SPEED : Vitesse, en pixels par milliseconde, à laquelle l'oiseau descend en une seconde sans monter.
        descend en une seconde sans monter.
    CLIMB_SPEED : vitesse, en pixels par milliseconde, à laquelle l'oiseau monte en une seconde tout en grimpant.
        l'oiseau monte en une seconde lorsqu'il grimpe, en moyenne.  Voir également la
        Bird.update docstring.
    CLIMB_DURATION : Le nombre de millisecondes nécessaires à l'oiseau pour
        pour effectuer une ascension complète.
    """

    class FlappyBird(object):
        def __init__(self, x, y, width, height):
            self.x = x
            self.y = y
            self.width = width
            self.height = height

        def draw(self):
            pygame.draw.rect(screen, red, (self.x, self.y, self.width, self.height))
    WIDTH = HEIGHT = 32
    SINK_SPEED = 0.18
    CLIMB_SPEED = 0.3
    CLIMB_DURATION = 333.3

    def __init__(self, x, y, msec_to_climb, images):
        """Initialise a new Bird instance.

        Arguments :
        x : La coordonnée X initiale de l'oiseau.
        y : La coordonnée Y initiale de l'oiseau.
        msec_to_climb : Le nombre de millisecondes restantes pour grimper, où une
            une ascension complète dure Bird.CLIMB_DURATION millisecondes.  Utilisez
            si vous voulez que l'oiseau fasse une (petite ?) ascension au tout début du jeu.
            au tout début du jeu.
        images : Un tuple contenant les images utilisées par cet oiseau.  Il
            doit contenir les images suivantes, dans l'ordre suivant :
                0. image de l'oiseau avec son aile pointant vers le haut
                1. image de l'oiseau avec l'aile pointant vers le bas

        """
        super(Bird, self).__init__()
        self.x, self.y = x, y
        self.msec_to_climb = msec_to_climb
        self._img_wingup, self._img_wingdown = images
        self._mask_wingup = pygame.mask.from_surface(self._img_wingup)
        self._mask_wingdown = pygame.mask.from_surface(self._img_wingdown)
        pipe_spacing = 350
        pipe_speed = 1
        space = 100
        p1_x = 300
        p1_y = 400
        p1_w = 50
        p1_h = HEIGHT

        p2_x = p1_x + pipe_spacing
        p2_y = 250
        p2_w = 50
        p2_h = HEIGHT

        p3_x = p2_x + pipe_spacing
        p3_y = 250
        p3_w = 50
        p3_h = HEIGHT

        pipe1 = Pipes(p1_x, p1_y, p1_w, p1_h, space, pipe_speed, red)
        pipe2 = Pipes(p2_x, p2_y, p2_w, p2_h, space, pipe_speed, green)
        pipe3 = Pipes(p3_x, p3_y, p3_w, p3_h, space, pipe_speed, blue)
        while loop:
            for event in pygame.event.get():
                # print(event)
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

        pipe1.draw_pipes()
        pipe2.draw_pipes()
        pipe3.draw_pipes()

        pipe1.check_if()
        pipe2.check_if()
        pipe3.check_if()

        p1_new_x = pipe1.pipe_move()
        p2_new_x = pipe2.pipe_move()
        p3_new_x = pipe3.pipe_move()



        pygame.display.update()
        clock.tick(FPS)

    class Pipes(object):
        def __init__(self, x, y, width, height, space, speed, color):
            self.x = x
            self.y = y
            self.width = width
            self.height = height
            self.space = space
            self.speed = speed
            self.color = color

        def draw_pipes(self):
            pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))
            pygame.draw.rect(screen, self.color, (self.x, self.y - self.space - self.height, self.width, self.height))

        def pipe_move(self):
            self.x -= self.speed
            return self.x


        def check_if(self):
            if self.x < 0:
                self.x = 1000
    def update(self, delta_frames=1):
        """Mettre à jour la position de l'oiseau.

        Cette fonction utilise la fonction cosinus pour obtenir une montée en douceur :
        Dans la première et la dernière image, l'oiseau grimpe très peu, au
        milieu de l'ascension, il grimpe beaucoup.
        Une montée complète dure CLIMB_DURATION millisecondes, pendant laquelle
        l'oiseau monte à une vitesse moyenne de CLIMB_SPEED px/ms.
        L'attribut msec_to_climb de cet oiseau sera automatiquement réduit en conséquence s'il était > 0 lors de la création de l'oiseau.
        automatiquement diminué en conséquence s'il était > 0 lorsque cette méthode a été appelée.

        Arguments :
        delta_frames : Nombre d'images écoulées depuis le dernier appel de cette méthode.
            dernière fois que cette méthode a été appelée.
        """
        if self.msec_to_climb > 0:
            frac_climb_done = 1 - self.msec_to_climb/Bird.CLIMB_DURATION
            self.y -= (Bird.CLIMB_SPEED * frames_to_msec(delta_frames) *
                       (1 - math.cos(frac_climb_done * math.pi)))
            self.msec_to_climb -= frames_to_msec(delta_frames)
        else:
            self.y += Bird.SINK_SPEED * frames_to_msec(delta_frames)

    @property
    def image(self):

        if pygame.time.get_ticks() % 500 >= 250:
            return self._img_wingup
        else:
            return self._img_wingdown

    @property
    def mask(self):

        if pygame.time.get_ticks() % 500 >= 250:
            return self._mask_wingup
        else:
            return self._mask_wingdown

    @property
    def rect(self):
        """Get the bird's position, width, and height, as a pygame.Rect."""
        return Rect(self.x, self.y, Bird.WIDTH, Bird.HEIGHT)


class PipePair(pygame.sprite.Sprite):


    WIDTH = 100
    PIECE_HEIGHT = 50
    ADD_INTERVAL = 3000


def load_images():


    def load_image(img_file_name):

    #chercher les images correspondantes et les mettre au bon endroits bon dossier tt ca
        file_name = os.path.join(os.path.dirname(__file__),
                                 'images', img_file_name)
        img = pygame.image.load(file_name)
        img.convert()
        return img

            'bird-wingup': load_image('ironTOP.png'),
            'bird-wingdown': load_image('ironBottom.png')}


def frames_to_msec(frames, fps=FPS):

    return 1000.0 * frames / fps


def msec_to_frames(milliseconds, fps=FPS):

    return fps * milliseconds / 1000.0


if (self.bird_y <= (p1_y - space)) and (self.bird_y <= p1_y) and ((self.bird_x + bird_width) >= p1_new_x) and (
        self.bird_x <= (p1_new_x + p1_w)):
    print("collision")
    break
    exit(0)  # Just in case.
def main():

    pygame.init()

    display_surface = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
    pygame.display.set_caption('Pygame Flappy Bird')

    clock = pygame.time.Clock()
    score_font = pygame.font.SysFont(None, 32, bold=True)  # default font
    images = load_images()


    bird = Bird(50, int(WIN_HEIGHT/2 - Bird.HEIGHT/2), 2,
                (images['bird-wingup'], images['bird-wingdown']))





    pygame.quit()


if __name__ == '__main__':
    main()
