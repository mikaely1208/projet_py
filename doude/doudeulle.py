import pygame, sys, time, random
from pygame import freetype

pygame.init()

#taille screen optimale pr jeu ?
DisplayWidth,DisplayHeight = 800, 800

#nom de fenetre
pygame.display.set_caption('Doodle')

#def temps pr compteur score
clock = pygame.time.Clock()

#init fenetre
gameDisplay = pygame.display.set_mode((DisplayWidth,DisplayHeight))

#créa nvl instance de police depuis fichier de police (font.ttf à dl)
game_font = pygame.freetype.Font("Font.ttf", 24)






pygame.display.flip()
clock.tick(60)




