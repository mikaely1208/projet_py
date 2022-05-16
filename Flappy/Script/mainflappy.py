import math
import os
from random import randint
from collections import deque

import pygame
from pygame.locals import *


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

    def __init__(self, pipe_end_img, pipe_body_img):

        self.x = float(WIN_WIDTH - 1)
        self.score_counted = False

        self.image = pygame.Surface((PipePair.WIDTH, WIN_HEIGHT), SRCALPHA)
        self.image.convert()
        self.image.fill((0, 0, 0, 0))
        total_pipe_body_pieces = int(
            (WIN_HEIGHT -
             3 * Bird.HEIGHT -
             3 * PipePair.PIECE_HEIGHT) /
            PipePair.PIECE_HEIGHT
        )
        self.bottom_pieces = randint(1, total_pipe_body_pieces)
        self.top_pieces = total_pipe_body_pieces - self.bottom_pieces

        # bottom pipe
        for i in range(1, self.bottom_pieces + 1):
            piece_pos = (0, WIN_HEIGHT - i*PipePair.PIECE_HEIGHT)
            self.image.blit(pipe_body_img, piece_pos)
        bottom_pipe_end_y = WIN_HEIGHT - self.bottom_height_px
        bottom_end_piece_pos = (0, bottom_pipe_end_y - PipePair.PIECE_HEIGHT)
        self.image.blit(pipe_end_img, bottom_end_piece_pos)

        # top pipe
        for i in range(self.top_pieces):
            self.image.blit(pipe_body_img, (0, i * PipePair.PIECE_HEIGHT))
        top_pipe_end_y = self.top_height_px
        self.image.blit(pipe_end_img, (0, top_pipe_end_y))

        # compensate for added end pieces
        self.top_pieces += 1
        self.bottom_pieces += 1

        # for collision detection
        self.mask = pygame.mask.from_surface(self.image)

    @property
    def top_height_px(self):

        return self.top_pieces * PipePair.PIECE_HEIGHT

    @property
    def bottom_height_px(self):

        return self.bottom_pieces * PipePair.PIECE_HEIGHT

    @property
    def visible(self):

        return -PipePair.WIDTH < self.x < WIN_WIDTH

    @property
    def rect(self):
        return Rect(self.x, 0, PipePair.WIDTH, PipePair.PIECE_HEIGHT)

    def update(self, delta_frames=1):

        self.x -= ANIMATION_SPEED * frames_to_msec(delta_frames)

    def collides_with(self, bird):

        ''' Arguments:
                bird: The Bird which should be tested for collision with this
                    PipePair.
                '''

def load_images():


    def load_image(img_file_name):

    #chercher les images correspondantes et les mettre au bon endroits bon dossier tt ca
        file_name = os.path.join(os.path.dirname(__file__),
                                 'images', img_file_name)
        img = pygame.image.load(file_name)
        img.convert()
        return img

    return {'background': load_image('background.jpg'),
            'pipe-end': load_image('tuyauba.png'),
            'pipe-body': load_image('tuyauo.png'),
            'bird-wingup': load_image('ironTOP.png'),
            'bird-wingdown': load_image('ironBottom.png')}


def frames_to_msec(frames, fps=FPS):

    return 1000.0 * frames / fps


def msec_to_frames(milliseconds, fps=FPS):

    return fps * milliseconds / 1000.0


def main():

    pygame.init()

    display_surface = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
    pygame.display.set_caption('Pygame Flappy Bird')

    clock = pygame.time.Clock()
    score_font = pygame.font.SysFont(None, 32, bold=True)  # default font
    images = load_images()


    bird = Bird(50, int(WIN_HEIGHT/2 - Bird.HEIGHT/2), 2,
                (images['bird-wingup'], images['bird-wingdown']))

    pipes = deque()

    frame_clock = 0
    score = 0
    done = paused = False
    while not done:
        clock.tick(FPS)

        if not (paused or frame_clock % msec_to_frames(PipePair.ADD_INTERVAL)):
            pp = PipePair(images['pipe-end'], images['pipe-body'])
            pipes.append(pp)

        for e in pygame.event.get():
            if e.type == QUIT or (e.type == KEYUP and e.key == K_ESCAPE):
                done = True
                break
            elif e.type == KEYUP and e.key in (K_PAUSE, K_p):
                paused = not paused
            elif e.type == MOUSEBUTTONUP or (e.type == KEYUP and
                    e.key in (K_UP, K_RETURN, K_SPACE)):
                bird.msec_to_climb = Bird.CLIMB_DURATION

        if paused:
            continue

        pipe_collision = any(p.collides_with(bird) for p in pipes)
        if pipe_collision or 0 >= bird.y or bird.y >= WIN_HEIGHT - Bird.HEIGHT:
            done = True

        for x in (0, WIN_WIDTH ):
            display_surface.blit(images['background'], (x, 0))

        while pipes and not pipes[0].visible:
            pipes.popleft()

        for p in pipes:
            p.update()
            display_surface.blit(p.image, p.rect)

        bird.update()
        display_surface.blit(bird.image, bird.rect)

        for p in pipes:
            if p.x + PipePair.WIDTH < bird.x and not p.score_counted:
                score += 1
                p.score_counted = True

        score_surface = score_font.render(str(score), True, (255, 255, 255))
        score_x = WIN_WIDTH/2 - score_surface.get_width()/2
        display_surface.blit(score_surface, (score_x, PipePair.PIECE_HEIGHT))

        pygame.display.flip()
        frame_clock += 1
    print('Game over! Score: %i' % score)
    pygame.quit()


if __name__ == '__main__':
    main()
