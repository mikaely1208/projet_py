import pygame #bibli à favoriser pour faire un jeu
import sys
import pygame_gui

class Grille:
    def __init__(self,ecran):
        self.ecran =ecran

        self.lignes = [( (200,0),(200,600)),
                       ((400,0),(400,600)),
                       ((0,200),(600,200)),
                       ((0,400),(600,400)),]#dimension du grillage
                #initier la grille
        self.grille =[[None for x in range(0,3)] for y in range (0,3)]
                # initier une variable pour voir on a le compteur qui est 'on'
        self.compteur_on = False
    def afficher(self):
        for ligne in self.lignes : #une ligne = d'une coordonnee a une autre

            pygame.draw.line(self.ecran,(0,0,0),ligne[0],ligne[1],2)  #(couleur des lignes, ici noires, des lignes 0, à la ligne 1, avec une epaisseur de 2:

        #affichage X et O
        for y in range(0,len(self.grille)): #loop a travers chaque ligne avec y = chaque ligne
            for x in range(0, len(self.grille)):#loop a travers chaque colonnes avec x = chaque colonne
                if self.grille[y][x] == 'X':
                    pygame.draw.line(self.ecran, (0,0,0), (x * 200, y * 200), (200 + (x * 200), 200+(y * 200)), 3) # dessin de lignes avec parametres line(surface, color, pos_depart, pos_fin)
                    pygame.draw.line(self.ecran, (0,0,0),((x * 200), 200 +(y * 200)), (200 + (x * 200),(y * 200)), 3)

                elif self.grille[y][x] == 'O':
                    pygame.draw.circle(self.ecran,(0,0,0), (100 + (x * 200), 100 + (y * 200)), 100, 3)

    def print_grille(self):
        #affiche la grille dans la console
        print(self.grille)


    def fixer_valeur(self,x,y,valeur):

        #condition si notre case possède la valeur 'none'
        if self.grille[y][x] == None :
            self.grille[y][x] = valeur  #dans la grille x et y sont égaux à la valeur
            #qd le compteur est 'on'
            self.compteur_on = True

        #fonction qui fixe valurs des cases a 'none'
    def fixer_None(self,ligne,colonne,valeur):

            self.grille[ligne][colonne] = valeur

class Jeu :
    def __init__(self):
        self.ecran = pygame.display.set_mode((600,600)) #dimension de l'ig (longueur, largeur)
        pygame.display.set_caption('Le morpion') #set le nom du jeu
        self.jeu_encours = True #définie si le jeu est en cours, ici vrai
        self.grille = Grille(self.ecran)
        #fixation de "X" et "O"
        self.player_X = 'X'
        self.player_O = 'O'

        #fixation compteur
        self.compteur = 0

        self.ecran_debut = True

    def fonction_principale(self): #fonction principale
        while self.jeu_encours:

            while self.ecran_debut:
                for event in pygame.event.get():  # permet de recevoir tt les evenements et de les gerer
                    if event.type == pygame.QUIT:
                        sys.exit()  # quitter le jeu à l'appuie de la croix rouge

                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            self.ecran_debut = False


                self.ecran.fill((205, 145, 158, 255))

                self.creer_message('grande', 'Morpion X/O', (0, 0, 0),[200,30,2000,50])

                self.creer_message('petite', 'Ce jeu se joue à deux et chacun aura son symbole', (0, 0, 0), [150, 130, 400, 50])
                self.creer_message('petite', 'X ou O', (0, 0, 0), [280, 150, 100, 100])
                self.creer_message('petite', 'Le premier joueur qui aligne trois de ses symboles gagne', (0, 0, 0), [130, 170, 200, 50])
                self.creer_message('moyenne', 'Pour restart le jeu, appuyer sur Entrée', (0, 0, 0,), [70, 350, 200, 50])
                self.creer_message('moyenne', 'Pour commencer le jeu, appuyer sur Espace', (0, 0, 0,), [70, 400, 200, 50])
                self.creer_message('moyenne', 'Pour revenir à cette page, appuyer sur Echap', (0, 0, 0,), [70, 450, 200, 50])


                pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                #ajout de l'event du clique gauche
                if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0]:
                #obtenir position souris
                    position = pygame.mouse.get_pos()
                    print(position)
                    position_x, position_y = position[0]//200, position[1]//200 #division avec partie entiere assignée à x et y ce qui crée des zones : [0/0],[1/0], etc...
                    print(position_x,position_y)

                    #condition avec le compteur
                    if self.compteur %2 == 0: #defini si compteur est pair ou impair soit le reste de la division = 0
                        self.grille.fixer_valeur(position_x,position_y,self.player_X)
                    else:
                        self.grille.fixer_valeur(position_x, position_y,self.player_O)
                    #condition compteur 'on' vrai
                    if self.grille.compteur_on:
                        self.compteur += 1
                    #condition compteur 'on' faux
                        self.grille.compteur_on = False

                if event.type == pygame.KEYDOWN: #si l'venement une touche du clavier est pressé
                    if event.key == pygame.K_RETURN: #la touche entrée
                        self.recommencer()
                    if event.key == pygame.K_ESCAPE:
                        self.ecran_debut = True


            liste_X = [] #prend les cases où on a x
            liste_O = [] #prend les cases où on a o
            liste_lignes_X = []
            liste_colonnes_X = []
            liste_lignes_O = []
            liste_colonnes_O = []

            for ligne in range(0,len(self.grille.grille)):
                for colonne in range(0,len(self.grille.grille)):

                    if self.grille.grille[ligne][colonne] == 'X':

                        X_position = (ligne,colonne)
                        liste_X.append(X_position)

                    elif self.grille.grille[ligne][colonne] == 'O':

                        O_position = (ligne, colonne)
                        liste_O.append(O_position)

            if len(liste_X) >=3 :
                for (ligne,colonne) in liste_X :
                    liste_lignes_X.append(ligne)
                    liste_colonnes_X.append(colonne)

                if liste_lignes_X.count(0) == 3 or liste_lignes_X.count(1) == 3 or liste_lignes_X.count(2) == 3 :
                    print('X a win')
                    #break
                if liste_colonnes_X.count(0) == 3 or liste_colonnes_X.count(1) == 3 or liste_colonnes_X.count(2) == 3 :
                    print('X a win')
                    #break
                if liste_lignes_X == liste_colonnes_X or liste_lignes_X == liste_colonnes_X[::-1]: #[::-1] signifie à l'envers
                    print('X a win')
                    #break

            if len(liste_O) >=3 :
                for (ligne,colonne) in liste_O :
                    liste_lignes_O.append(ligne)
                    liste_colonnes_O.append(colonne)

                if liste_lignes_O.count(0) == 3 or liste_lignes_O.count(1) == 3 or liste_lignes_O.count(2) == 3 :
                    print('O a win')
                    #break
                if liste_colonnes_O.count(0) == 3 or liste_colonnes_O.count(1) == 3 or liste_colonnes_O.count(2) == 3 :
                    print('O a win')
                    #break
                if liste_lignes_O == liste_colonnes_O or liste_lignes_O == liste_colonnes_O[::-1]: #[::-1] signifie à l'envers
                    print('O a win')
                    #break

            #print(self.compteur)
            #self.grille.print_grille()
            self.ecran.fill((240,240,240)) #couleur blanche attribuée à l'écran
            self.grille.afficher()
            pygame.display.flip() #met l'écran à jour

    #fonction 'none' a chaque case
    def recommencer(self):
        for ligne in range(0,len(self.grille.grille)):
            for colonne in range(0,len(self.grille.grille)):
                self.grille.fixer_None(ligne,colonne,None)

    def creer_message(self,font,message,couleur,messsage_rectangle):
        if font == 'petite':
            font = pygame.font.SysFont('Lato',20,False)

        elif font == 'moyenne':
            font = pygame.font.SysFont('Lato',30,False)

        elif font == 'grande':
            font = pygame.font.SysFont('Lato',40,True)

        message = font.render(message,False,couleur)
        self.ecran.blit(message,messsage_rectangle)

if __name__ == '__main__':
    pygame.init()
    Jeu().fonction_principale()
    pygame.quit()
