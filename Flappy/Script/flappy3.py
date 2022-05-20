import pygame
import sys
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
blanc = (255, 255, 255)
rouge = (248, 51, 60)
jaune = (252, 171, 16)
violet = (151, 40, 199)
vert = (130, 255, 158)
rose = (229, 99, 153)
taupe = (122, 101, 99)
bleu = (0, 53, 84)
argent = (117, 119, 128)
bleu_foncer = (27, 40, 69)
orange = (237, 155, 64)
FPS = 60

class Flappy(object):
    def __init__(self, x, y, larg, haut):
        self.x = x
        self.y = y
        self.larg = larg
        self.haut = haut

    def draw(self):
            pygame.draw.rect(screen, rouge, (self.x, self.y, self.larg, self.haut))

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
        larg_heros = 20
        haut_heros = 20
        self.X_heros = 100
        self.Y_heros = ((haut / 2) - int(haut_heros / 2.0))
        moov_X_heros = 0
        moov_Y_heros = 0
        esp_tube = 300
        vit_tube = 1.5

        #code premier pipe
        esp = 200
        Tub_1x = 500
        Tub_1y = 350
        Tub_1_larg = 50
        Tub_1_haut = haut
        # code second pipe
        Tub_2x = Tub_1x + esp_tube
        Tub_2y = 390
        Tub_2_larg = 50
        Tub_2_haut = haut
        # code troisième pipe
        Tub_3x = Tub_2x + esp_tube
        Tub_3y = 380
        Tub_3_larg = 50
        Tub_3_haut = haut
        # code quatrièmes pipe
        Tub_4x = Tub_3x + esp_tube
        Tub_4y = 380
        Tub_4_larg = 50
        Tub_4_haut = haut
        # code cinquièmes pipe
        Tub_5x = Tub_4x + esp_tube
        Tub_5y = 380
        Tub_5_larg = 50
        Tub_5_haut = haut
        # code sixième pipe
        Tub_6x = Tub_5x + esp_tube
        Tub_6y = 380
        Tub_6_larg = 50
        Tub_6_haut = haut
        # code septièmes pipe
        Tub_7x = Tub_6x + esp_tube
        Tub_7y = 380
        Tub_7_larg = 50
        Tub_7_haut = haut
        # code cinquièmes pipe
        Tub_8x = Tub_7x + esp_tube
        Tub_8y = 380
        Tub_8_larg = 50
        Tub_8_haut = haut
        # code sixième pipe
        Tub_9x = Tub_8x + esp_tube
        Tub_9y = 380
        Tub_9_larg = 50
        Tub_9_haut = haut
        # code septièmes pipe
        Tub_10x = Tub_9x + esp_tube
        Tub_10y = 380
        Tub_10_larg = 50
        Tub_10_haut = haut

        #on ajoute les coordonnés + L'espace entre eux + Rapidité + couleurs
        Tube1 = Tubes(Tub_1x, Tub_1y, Tub_1_larg, Tub_1_haut, esp, vit_tube, rouge)
        Tube2 = Tubes(Tub_2x, Tub_2y, Tub_2_larg, Tub_2_haut, esp, vit_tube, jaune)
        Tube3 = Tubes(Tub_3x, Tub_3y, Tub_3_larg, Tub_3_haut, esp, vit_tube, violet)
        Tube4 = Tubes(Tub_4x, Tub_4y, Tub_4_larg, Tub_4_haut, esp, vit_tube, vert)
        Tube5 = Tubes(Tub_5x, Tub_5y, Tub_5_larg, Tub_5_haut, esp, vit_tube, rose)
        Tube6 = Tubes(Tub_6x, Tub_6y, Tub_6_larg, Tub_6_haut, esp, vit_tube, taupe)
        Tube7 = Tubes(Tub_7x, Tub_7y, Tub_7_larg, Tub_7_haut, esp, vit_tube, bleu)
        Tube8 = Tubes(Tub_8x, Tub_8y, Tub_8_larg, Tub_8_haut, esp, vit_tube, rose)
        Tube9 = Tubes(Tub_9x, Tub_9y, Tub_9_larg, Tub_9_haut, esp, vit_tube, taupe)
        Tube10 = Tubes(Tub_10x, Tub_10y, Tub_10_larg, Tub_10_haut, esp, vit_tube, bleu)

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

            self.X_heros += moov_X_heros
            self.Y_heros += moov_Y_heros
            heros = Flappy(self.X_heros, self.Y_heros, larg_heros, haut_heros)
            heros.draw()

            Tube1.draw_tubes()
            Tube2.draw_tubes()
            Tube3.draw_tubes()
            Tube4.draw_tubes()
            Tube5.draw_tubes()
            Tube6.draw_tubes()
            Tube7.draw_tubes()
            Tube8.draw_tubes()
            Tube9.draw_tubes()
            Tube10.draw_tubes()

            Tube1.verif()
            Tube2.verif()
            Tube3.verif()
            Tube4.verif()
            Tube5.verif()
            Tube6.verif()
            Tube7.verif()
            Tube8.verif()
            Tube9.verif()
            Tube10.verif()


            new_Tub_1x = Tube1.moov_tubes()
            new_Tub_2x = Tube2.moov_tubes()
            new_Tub_3x = Tube3.moov_tubes()
            new_Tub_4x = Tube4.moov_tubes()
            new_Tub_5x = Tube5.moov_tubes()
            new_Tub_6x = Tube6.moov_tubes()
            new_Tub_7x = Tube7.moov_tubes()
            new_Tub_8x = Tube8.moov_tubes()
            new_Tub_9x = Tube9.moov_tubes()
            new_Tub_10x = Tube10.moov_tubes()


            if (self.Y_heros >= (Tub_1y - esp)) and (self.Y_heros >= Tub_1y) and ((self.X_heros + larg_heros) >= new_Tub_1x) and (self.X_heros <= (new_Tub_1x + Tub_1_larg)):
                    print("perdu")
                    break  # on break la loop pour collision signe de fin du jeu
                    exit(0)
            if (self.Y_heros <= (Tub_1y - esp)) and (self.Y_heros <= Tub_1y) and ((self.X_heros + larg_heros) >= new_Tub_1x) and (self.X_heros <= (new_Tub_1x + Tub_1_larg)):
                    print("perdu")
                    break  # on break la loop pour collision signe de fin du jeu
                    exit(0)
            if (self.Y_heros <= (Tub_2y - esp)) and (self.Y_heros <= Tub_2y) and ((self.X_heros + larg_heros) >= new_Tub_2x) and (self.X_heros <= (new_Tub_2x + Tub_2_larg)):
                    print("perdu")
                    break  # on break la loop pour collision signe de fin du jeu
                    exit(0)
            if (self.Y_heros >= (Tub_2y - esp)) and (self.Y_heros >= Tub_2y) and ((self.X_heros + larg_heros) >= new_Tub_2x) and (self.X_heros <= (new_Tub_2x + Tub_2_larg)):
                    print("perdu")
                    break  # on break la loop pour collision signe de fin du jeu
                    exit(0)
            if (self.Y_heros >= (Tub_3y - esp)) and (self.Y_heros >= Tub_3y) and ((self.X_heros + larg_heros) >= new_Tub_3x) and (self.X_heros <= (new_Tub_3x + Tub_3_larg)):
                    print("perdu")
                    break  # on break la loop pour collision signe de fin du jeu
                    exit(0)
            if (self.Y_heros <= (Tub_3y - esp)) and (self.Y_heros <= Tub_3y) and ((self.X_heros + larg_heros) >= new_Tub_3x) and (self.X_heros <= (new_Tub_3x + Tub_3_larg)):
                    print("perdu")
                    break  # on break la loop pour collision signe de fin du jeu
                    exit(0)
            if (self.Y_heros >= (Tub_4y - esp)) and (self.Y_heros >= Tub_4y) and ((self.X_heros + larg_heros) >= new_Tub_4x) and (self.X_heros <= (new_Tub_4x + Tub_4_larg)):
                    print("perdu")
                    break  # on break la loop pour collision signe de fin du jeu
                    exit(0)
            if (self.Y_heros <= (Tub_4y - esp)) and (self.Y_heros <= Tub_4y) and ((self.X_heros + larg_heros) >= new_Tub_4x) and (self.X_heros <= (new_Tub_4x + Tub_4_larg)):
                    print("perdu")
                    break  # on break la loop pour collision signe de fin du jeu
                    exit(0)
            if (self.Y_heros >= (Tub_5y - esp)) and (self.Y_heros >= Tub_5y) and ((self.X_heros + larg_heros) >= new_Tub_5x) and (self.X_heros <= (new_Tub_5x + Tub_5_larg)):
                    print("perdu")
                    break  # on break la loop pour collision signe de fin du jeu
                    exit(0)
            if (self.Y_heros <= (Tub_5y - esp)) and (self.Y_heros <= Tub_5y) and ((self.X_heros + larg_heros) >= new_Tub_5x) and (self.X_heros <= (new_Tub_5x + Tub_5_larg)):
                    print("perdu")
                    break  # on break la loop pour collision signe de fin du jeu
                    exit(0)
            if (self.Y_heros >= (Tub_6y - esp)) and (self.Y_heros >= Tub_6y) and ((self.X_heros + larg_heros) >= new_Tub_6x) and (self.X_heros <= (new_Tub_6x + Tub_6_larg)):
                    print("perdu")
                    break  # on break la loop pour collision signe de fin du jeu
                    exit(0)
            if (self.Y_heros <= (Tub_6y - esp)) and (self.Y_heros <= Tub_6y) and ((self.X_heros + larg_heros) >= new_Tub_6x) and (self.X_heros <= (new_Tub_6x + Tub_6_larg)):
                    print("perdu")
                    break  # on break la loop pour collision signe de fin du jeu
                    exit(0)
            if (self.Y_heros >= (Tub_7y - esp)) and (self.Y_heros >= Tub_7y) and ((self.X_heros + larg_heros) >= new_Tub_7x) and (self.X_heros <= (new_Tub_7x + Tub_7_larg)):
                    print("perdu")
                    break  # on break la loop pour collision signe de fin du jeu
                    exit(0)
            if (self.Y_heros <= (Tub_7y - esp)) and (self.Y_heros <= Tub_7y) and ((self.X_heros + larg_heros) >= new_Tub_7x) and (self.X_heros <= (new_Tub_7x + Tub_7_larg)):
                    print("perdu")
                    break  # on break la loop pour collision signe de fin du jeu
                    exit(0)
            if (self.Y_heros >= (Tub_8y - esp)) and (self.Y_heros >= Tub_8y) and ((self.X_heros + larg_heros) >= new_Tub_8x) and (self.X_heros <= (new_Tub_8x + Tub_8_larg)):
                    print("perdu")
                    break  # on break la loop pour collision signe de fin du jeu
                    exit(0)
            if (self.Y_heros <= (Tub_8y - esp)) and (self.Y_heros <= Tub_8y) and ((self.X_heros + larg_heros) >= new_Tub_8x) and (self.X_heros <= (new_Tub_8x + Tub_8_larg)):
                    print("perdu")
                    break  # on break la loop pour collision signe de fin du jeu
                    exit(0)
            if (self.Y_heros >= (Tub_9y - esp)) and (self.Y_heros >= Tub_9y) and ((self.X_heros + larg_heros) >= new_Tub_9x) and (self.X_heros <= (new_Tub_9x + Tub_9_larg)):
                    print("perdu")
                    break  # on break la loop pour collision signe de fin du jeu
                    exit(0)
            if (self.Y_heros <= (Tub_9y - esp)) and (self.Y_heros <= Tub_9y) and ((self.X_heros + larg_heros) >= new_Tub_9x) and (self.X_heros <= (new_Tub_9x + Tub_9_larg)):
                    print("perdu")
                    break  # on break la loop pour collision signe de fin du jeu
                    exit(0)
            if (self.Y_heros >= (Tub_10y - esp)) and (self.Y_heros >= Tub_10y) and ((self.X_heros + larg_heros) >= new_Tub_10x) and (self.X_heros <= (new_Tub_10x + Tub_10_larg)):
                    print("perdu")
                    break  # on break la loop pour collision signe de fin du jeu
                    exit(0)
            if (self.Y_heros <= (Tub_10y - esp)) and (self.Y_heros <= Tub_10y) and ((self.X_heros + larg_heros) >= new_Tub_10x) and (self.X_heros <= (new_Tub_10x + Tub_10_larg)):
                    print("perdu")
                    break  # on break la loop pour collision signe de fin du jeu
                    exit(0)


            pygame.display.update()
            clock.tick(FPS)
            screen.fill(blanc)


Window(larg, haut)