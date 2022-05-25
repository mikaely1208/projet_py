import pygame
import sys
import pygame as pg
from pygame.locals import *
pygame.init()

#Taille ecran,time etc
larg = 700
haut = 500
FPS = 60
screen = pygame.display.set_mode((larg, haut))
clock = pygame.time.Clock()



# Def des différentes couleurs des tubes + heros, fond etc ...
#fond = pygame.image.load("images/background.jpg")
white = (255, 255, 255)
red = (248, 51, 60)
yellow = (252, 171, 16)
purple = (151,40, 199)
FPS = 60

class Flappy(object):
    def __init__(self, x, y, larg, haut):
        self.x = x
        self.y = y
        self.larg = larg
        self.haut = haut

    def draw(self):
                pygame.draw.rect(screen, red, (self.x, self.y, self.larg, self.haut))

class Tubes(object):
    def __init__(self, x, y, larg, haut, esp, vit, couleur):
        self.x = x
        self.y = y
        self.larg = larg
        self.haut = haut
        self.esp = esp
        self.vit = vit
        self.couleur = couleur

    def draw_tubes(self):
        pygame.draw.rect(screen, self.couleur, (self.x, self.y, self.larg, self.haut))
        pygame.draw.rect(screen, self.couleur, (self.x, self.y - self.esp - self.haut, self.larg, self.haut))

    def moov_tubes(self):
        self.x -= self.vit
        return self.x

    def verif(self):
        if self.x < 0:
            self.x = 1000


# Coder le main

class Window(object):
    def __init__(self, larg, haut):
        self.larg = larg
        self.haut = haut
        self.main()

    def main(self):
        loop = True
        # def oiseau localisation, taille, déplacement
        larg_heros = 30
        haut_heros = 20
        self.X_heros = 100
        self.Y_heros = ((haut / 2) - int(haut_heros / 2.0))
        moov_X_heros = 0
        moov_Y_heros = 0
        esp_tube = 250
        vit_tube = 4
        pg.init()
        font = pg.font.Font(None, 40)
        gray = pg.Color('blue')
        blue = pg.Color('blue')
        timer = 0
        dt = 0  # time dernier tick

        #code premier pipe
        esp = 100
        Tub_1x = 400
        Tub_1y = 350
        Tub_1_larg = 50
        Tub_1_haut = haut
        # code second pipe
        Tub_2x = Tub_1x + esp_tube
        Tub_2y = 150
        Tub_2_larg = 50
        Tub_2_haut = haut
        # code troisième pipe
        Tub_3x = Tub_2x + esp_tube
        Tub_3y = 450
        Tub_3_larg = 50
        Tub_3_haut = haut

        #on ajoute les coordonnés + L'espace entre eux + Rapidité + couleurs
        Tube1 = Tubes(Tub_1x, Tub_1y, Tub_1_larg, Tub_1_haut, esp, vit_tube, red)
        Tube2 = Tubes(Tub_2x, Tub_2y, Tub_2_larg, Tub_2_haut, esp, vit_tube, yellow)
        Tube3 = Tubes(Tub_3x, Tub_3y, Tub_3_larg, Tub_3_haut, esp, vit_tube, purple)


       #definir les touches quitter jeux et monter
        while loop:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        moov_Y_heros = -6

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_SPACE:
                        moov_Y_heros = 4

                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            timer += dt
            if timer >= 100000000000000000000000:
                timer = 0  # Reset it to 10 or do something else.
            self.X_heros += moov_X_heros
            self.Y_heros += moov_Y_heros
            heros = Flappy(self.X_heros, self.Y_heros, larg_heros, haut_heros)
            heros.draw()

            Tube1.draw_tubes()
            Tube2.draw_tubes()
            Tube3.draw_tubes()

            Tube1.verif()
            Tube2.verif()
            Tube3.verif()

            txt = font.render(str(round(timer, 2)), True, blue)
            screen.blit(txt, (70, 70))
            pg.display.flip()
            dt = clock.tick(0)  # /1000 to convert to seconds.

            new_Tub_1x = Tube1.moov_tubes()
            new_Tub_2x = Tube2.moov_tubes()
            new_Tub_3x = Tube3.moov_tubes()

            if (self.Y_heros >= (Tub_1y - esp)) and (self.Y_heros >= Tub_1y) and ((self.X_heros + larg_heros) >= new_Tub_1x) and (self.X_heros <= (new_Tub_1x + Tub_1_larg)):
                    print("perdu")
                    print(timer)
                    break  # on break la loop pour collision signe de fin du jeu
                    exit(0)
            if (self.Y_heros <= (Tub_1y - esp)) and (self.Y_heros <= Tub_1y) and ((self.X_heros + larg_heros) >= new_Tub_1x) and (self.X_heros <= (new_Tub_1x + Tub_1_larg)):
                    print("perdu")
                    print(timer)
                    break  # on break la loop pour collision signe de fin du jeu
                    exit(0)
            if (self.Y_heros <= (Tub_2y - esp)) and (self.Y_heros <= Tub_2y) and ((self.X_heros + larg_heros) >= new_Tub_2x) and (self.X_heros <= (new_Tub_2x + Tub_2_larg)):
                    print("perdu")
                    print(timer)
                    break  # on break la loop pour collision signe de fin du jeu
                    exit(0)
            if (self.Y_heros >= (Tub_2y - esp)) and (self.Y_heros >= Tub_2y) and ((self.X_heros + larg_heros) >= new_Tub_2x) and (self.X_heros <= (new_Tub_2x + Tub_2_larg)):
                    print("perdu")
                    print(timer)
                    break  # on break la loop pour collision signe de fin du jeu
                    exit(0)
            if (self.Y_heros >= (Tub_3y - esp)) and (self.Y_heros >= Tub_3y) and ((self.X_heros + larg_heros) >= new_Tub_3x) and (self.X_heros <= (new_Tub_3x + Tub_3_larg)):
                    print("perdu")
                    print(timer)
                    break  # on break la loop pour collision signe de fin du jeu
                    exit(0)
            if (self.Y_heros <= (Tub_3y - esp)) and (self.Y_heros <= Tub_3y) and ((self.X_heros + larg_heros) >= new_Tub_3x) and (self.X_heros <= (new_Tub_3x + Tub_3_larg)):
                    print("perdu")
                    print(timer)
                    break  # on break la loop pour collision signe de fin du jeu
                    exit(0)
            pygame.display.update()
            clock.tick(FPS)
            screen.fill(white)


Window(larg, haut)