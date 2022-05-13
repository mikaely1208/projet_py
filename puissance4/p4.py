import pygame
import sys
pygame.init()

# def de la grille
Gr = [[0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0]]

NbrJetons = 0
Puissance4 = False
joueur = 1


def Order():
    # Cette fonction retourne le numero du joueur qui doit jouer
    if (NbrJetons % 2 == 0):
        joueur = 1
    else:
        joueur = 2
    return joueur


def choix_col(x, y):
    # Cette fonction retourne la colonne demandee au joueur1
    # Tant que la valeur n'est pas acceptable, on demande la colonne a jouer
    col = x - 16
    col = col / 97
    if col in range(0, 7):
        for lig in range(8):
            if Gr[lig][col] == 0: return col
    return col



def verification_Puissance4():
    test2 = False

    # test d'un P4 horizontal
    i = j = 0
    while (not (i == 5 and j == 3)):
        if (Gr[i][j] == Gr[i][j + 1] and Gr[i][j] == Gr[i][j + 2] \
                and Gr[i][j] == Gr[i][j + 3] and Gr[i][j] == joueur):
            test2 = True
        if (j == 3):
            i = i + 1
            j = 0
        else:
            j = j + 1

    # test d'un P4 vertical
    i = j = 0
    while (not (i == 2 and j == 6)):
        if (Gr[i][j] == Gr[i + 1][j] and Gr[i][j] == Gr[i + 2][j] \
                and Gr[i][j] == Gr[i + 3][j] and Gr[i][j] == joueur):
            test2 = True
        if (j == 6):
            i = i + 1
            j = 0
        else:
            j = j + 1

    # test d'un P4 diagonal vers la droite
    i = j = 0
    while (not (i == 2 and j == 3)):
        if (Gr[i][j] == Gr[i + 1][j + 1] and Gr[i][j] == Gr[i + 2][j + 2] \
                and Gr[i][j] == Gr[i + 3][j + 3] and Gr[i][j] == joueur):
            test2 = True
        if (j == 3):
            i = i + 1
            j = 0
        else:
            j = j + 1

    # test d'un P4 diagonal vers la gauche
    i = 0
    j = 3
    while (not (i == 2 and j == 6)):
        if (Gr[i][j] == Gr[i + 1][j - 1] and Gr[i][j] ==GrM[i + 2][j - 2] \
                and Gr[i][j] == Gr[i + 3][j - 3] and Gr[i][j] == joueur):
            test2 = True
        if (j == 6):
            i = i + 1
            j = 3
        else:
            j = j + 1

    return test2




def choix_lig():
    # Cette fonction retourne la ligne vide correspondant a la colonne demandee
    lig = 0
    for i in range(1, 6):
        if (Gr[i][col] == 0 and Gr[i - 1][col] != 0):
            lig = i
    return lig



image = pygame.image.load("Grille2.png")
sizeim = image.get_size()
size = (sizeim[0] * 1, sizeim[1])
screen = pygame.display.set_mode(size)
screen.blit(image, (0, 0))
pygame.display.flip()


def affichage(matrice):
    screen.fill((0, 0, 0))
    screen.blit(image, (0, 0))
    for i in range(len(matrice)):
        for j in range(len(matrice[i])):
            if matrice[i][j] == 1:
                screen.blit(pionrouge, (16 + 97 * j, 13 - 97.5 * i + 486))
            pygame.display.flip()
            if matrice[i][j] == 2:
                screen.blit(pionjaune, (16 + 97 * j, 13 - 97.5 * i + 486))
            pygame.display.flip()


pionjaune = pygame.image.load("PionJaune.png")
pionrouge = pygame.image.load("PionRouge.png")
font = pygame.font.Font("freesansbold.ttf", 15)

import time

while (not Puissance4 and NbrJetons < 42):
    time.sleep(0.1)
    # Le joueur joue
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONUP:
            x, y = pygame.mouse.get_pos()
            joueur = Order()
            colonne = choix_col(x, y)
            # On modifie les variables pour tenir compte du jeton depose.
            Gr[choix_lig()][col] = joueur
            NbrJetons = NbrJetons + 1
            Puissance4 = verification_Puissance4()
            affichage(Gr)
            pygame.display.flip()

        if event.type == pygame.QUIT:
            sys.exit()