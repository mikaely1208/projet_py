import pygame, sys, time, random
from pygame import freetype
from pygame.locals import *

#init tt les import et import from
pygame.init()

#taille screen optimale pr jeu ??
DisplayWidth,DisplayHeight = 800, 800

#nom de fenetre
pygame.display.set_caption('Doodle')

#def temps pr compteur score
clock = pygame.time.Clock()

#init fenetre
gameDisplay = pygame.display.set_mode((DisplayWidth,DisplayHeight))

#créa nvl instance de police depuis fichier de police (font.ttf à dl)
game_font = pygame.freetype.Font("Font.ttf", 24)





#update tt le contenu dla page
pygame.display.flip()

#temps def a tick 60s = 1mn
clock.tick(60)




