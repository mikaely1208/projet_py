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




#fonctiiion pour dessiner
def draw(x,y,Obj):
    global score
    global PlatformCount
    global CurColor
    global NumClr

    if Obj == "Overlay":
        pygame.draw.rect(gameDisplay,(100,100,100),(0,0,150,800),0)
        pygame.draw.rect(gameDisplay,(100,100,100),(650,0,150,800),0)
        pygame.draw.rect(gameDisplay,(0,0,0),(0,0,150,800),10)
        pygame.draw.rect(gameDisplay,(0,0,0),(650,0,150,800),10)
    if Obj == "Score":
        game_font = pygame.freetype.Font("Font.ttf", 24)
        text_surface, rect = game_font.render(("Score: " + str(int(score))), (0, 0, 0))
        gameDisplay.blit(text_surface, (20, 50))
        text_surface, rect = game_font.render(("Platforms: " + str(int(PlatformCount))), (0, 0, 0))
        gameDisplay.blit(text_surface, (20, 80))
    if Obj == "platform":
        pygame.draw.rect(gameDisplay,(100,100,100),(x,y,200,20),0)
        pygame.draw.rect(gameDisplay,(0,0,0),(x,y,200,20),5)
    if Obj == "player":
        if CurColor != "rainbow":
            pygame.draw.rect(gameDisplay,CurColor,(x,y,50,50),0)
        else:
            if NumClr >= 0 and NumClr <= 37:
                pygame.draw.rect(gameDisplay,(NumClr * 4,0 ,0 ),(x,y,50,50),0)
            elif NumClr >= 38 and NumClr <= 75:
                pygame.draw.rect(gameDisplay,(255,NumClr * 2,0 ),(x,y,50,50),0)
            elif NumClr >= 76 and NumClr <= 150:
                pygame.draw.rect(gameDisplay,(255,255,NumClr),(x,y,50,50),0)
            elif NumClr >= 151 and NumClr <= 200:
                pygame.draw.rect(gameDisplay,(255 - (200-NumClr) * 5,255,255),(x,y,50,50),0)
            elif NumClr >= 201 and NumClr <= 225:
                pygame.draw.rect(gameDisplay,(0,255 - (225-NumClr) * 5,255),(x,y,50,50),0)
            elif NumClr >= 226 and NumClr <= 255:
                pygame.draw.rect(gameDisplay,(0,0,255 - (255-NumClr) * 5),(x,y,50,50),0)
            else:
                NumClr = 0
            NumClr += 2



#update tt le contenu dla page
pygame.display.flip()

#temps def a tick 60s = 1mn
clock.tick(60)




