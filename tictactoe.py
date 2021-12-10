from graphicalgrid import GraphicalGrid

# NE PAS OUBLIER LE INPUT ligne 35

# A SUPPRIMER ligne 39 à 42

# Je dois reussir à creer une meme fonction pour coordonnee_col et coordonnee_li !!!!!!
##########################################################################################



# Generation de ma grille (question 1)

def cree_grille(taille):
    grille = []
    for i in range(taille):
        ligne = []
        for j in range(taille):
            ligne.append(" ")
        grille.append(ligne)

    return grille


# Longeur de la grille (question 2)

def taille_grille(grille):
    n = len(grille)

    return n

# Vérifie que l'on soit dans la grille

def est_dans_grille(grille, i, j):
    if 0 <= i < taille_grille(grille) and 0 <= j < taille_grille(grille):
        return True
    return False

#  Vérifie si vide (Question 3)

def est_vide(grille, i, j):
    if est_dans_grille(grille, i, j) and grille[i][j] == " ":
            return True
    return False
    

# Ecrire un O ou un X (Question 4)


def ecrire(grille, i, j, symbole):
    if est_vide(grille, i, j): #and (symbole == "X" or symbole == "O"): # A TESTER PUIS SUPPRIMER
        grille[i][j] = symbole


# Supprimer un X ou un O (Question 5)

def supprimer(grille, i, j):
    if est_dans_grille(grille, i, j) and not est_vide(grille, i, j):
        grille[i][j] = " "


# Vérifie si la case est X ou O (Question 6)

def est(grille, i, j, symbole):
    if est_dans_grille(grille, i, j):
        return symbole == grille[i][j]
    return False


# Affichage de la grille (Question 7)

def affiche(grille):
    taille = taille_grille(grille)
    for i in range(taille):
        if i == taille-1:
            for j in range(taille):
                if j == taille-1:
                    print("", grille[i][j], "", end="")
                else:
                    print("", grille[i][j], "|", end="")
            print()
        else:
            for j in range(taille):
                if j == taille-1:
                    print("", grille[i][j], "", end="")
                else:
                    print("", grille[i][j], "|", end="")
            print()
            print("----" * (taille-1) + "---")


############################################
# Essais de fonctionnements de mes fonctions
############################################

longeur_grille = 3 # int(input("Rentrez le nombre de lignes"))
tictac = cree_grille(longeur_grille)

# print(tictac)
# ecrire(tictac, 0, 0, "X")
# ecrire(tictac, 0, 1, "O")
# ecrire(tictac, 0, 2, "X")
# ecrire(tictac, 1, 0, "O")
# ecrire(tictac, 1, 1, "X")
# ecrire(tictac, 1, 2, "X")
# ecrire(tictac, 2, 0, "O")
# ecrire(tictac, 2, 1, "X")
# ecrire(tictac, 2, 2, "O")
# print(tictac)
# supprimer(tictac, 0, 0)
# print(tictac)
# print("est vide:", est_vide(tictac, 0, 1))
# print("est X", est(tictac, 0, 1, "X"))

affiche(tictac)

############################################
# Partie graphique
############################################

# grille_graphique = GraphicalGrid(10)

# grille_graphique.write(0, 1, "O")
# grille_graphique.write(3, 4, "X")
# grille_graphique.write(0, 0, "X")
# grille_graphique.erase(3, 4)

# grille_graphique.wait_quit()



#############################################
# Fonctions de fin de jeu (arret, gagné, nul)
#############################################

# Controle de grille pleine (pour arret de jeu)

def grille_pleine(grille):
    for i in range(taille_grille(grille)):
        for j in range(taille_grille(grille)):
            if est_vide(grille, i, j):
                return False
    return True

print(grille_pleine(tictac))


#############################
# Controle de partie gagnee (vraiment chaud...)
#############################


def partie_gagnee_ligne(grille, li):
    for i in range(taille_grille(grille)):
        if not est_vide(grille, li, i):   # AJOUT DE TEST SI VIDE AVANT DE TESTER EGALITE
            if grille[li][i] != grille[li][taille_grille(grille)-i]:
                return False
    return True


# def partie_gagnee_col(grille,col):
#     for i in taille_grille(grille):
#             if not est_vide(grille, i, col):
#                 if grille[i][col] != grille[col][taille_grille(grille)-i]:
#                     return False
#     return True


# def partie_gagnee_diagonale_1(grille):
#     for i in taille_grille(grille):
#         if not est_vide(grille, i, i):
#             if grille[i][i] != grille[taille_grille(grille)-i][taille_grille(grille)-i]:
#                 return False
#     return True

# def partie_gagnee_diagonale_2(grille):
#     for i in taille_grille(grille):
#             if not est_vide(grille, i, i-1):
#                 if grille[i][i-1] != grille[(taille_grille(grille)-i)-1][taille_grille(grille)-i]:
#                     return False
#     return True


# def partie_gagnee():
#     return partie_gagnee_col or partie_gagnee_ligne or partie_gagnee_diagonale_1 or partie_gagnee_diagonale_2

def partie_gagnee(grille, i, j):
    return partie_gagnee_ligne(grille, i)


###################################
# Qui joue ? Joueur 1 ou joueur 2
###################################

def joueur(tour):
    if tour % 2:
        return "O" # a modifier en 1 et 2 si erreur
    return "X"

def coup(joueur):
    if joueur == "X":
        symbole = "X"
    if joueur == "O":
        symbole = "O"
    return symbole


# #####################
# # Partie finie
# #####################

def partie_continue(): 
    return not grille_pleine(tictac) and not partie_gagnee(tictac, coord_li, coord_col) and continuer_de_jouer(reponse)


##########
# ESSAI DE MISE EN FONCTION DE COL ET LI
###########

def def_col_li(coordonnee):
        coordonnee = input("Entrez un numéro de ligne")
        if coordonnee != "":
            while not test_entree_chiffre(coordonnee):
                print("Veuillez entrer un chiffre svp")
                coordonnee = input("Entrez un numéro de ligne")

            while not test_entree_coord(coordonnee):
                if int(coordonnee) < 0:                                                             # VOIR SI OK DE FAIRE DEUX FONCTIONS
                    print("Veuillez entrer un chiffre supperieur à 0")
                    coordonnee = input("Entrez un numéro de ligne")
                if int(coordonnee) > taille_grille(tictac):
                    print("Veuillez entrer un chiffre inferieur à la longeur")
                    coordonnee = input("Entrez un numéro de ligne")


            return int(coordonnee)


###############
# Controle de la bonne saisie d'un chiffre
###############

def test_entree_chiffre(saisie):
    chiffres = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "+", "-", " "]
    for i in str(saisie):
        drapeau = False
        for j in chiffres:
            if i == j:
                drapeau = True
        if drapeau == False:
            return False
    return True


################################
# Coordonnée est-elle correct ? NE PAS OUBLIER DE TRANSFORMER LE STR EN INT
################################

def test_entree_coord(saisie):
    if 0 <= int(saisie) < taille_grille(tictac):
        return True
    return False


#################
# Continuer de jouer ? O ou N ?
#################

def saisie_O_N(saisie):
    if saisie != "N" and saisie != "O":
        return False
    return True


def continuer_de_jouer(saisie):
    if saisie == "N":
        return False
    if saisie == "O":
        return True

#
# A FINIR POUR FAIRE UNE DEF DE O ET N
#

def test_O_N(reponse, question):
    while not saisie_O_N(reponse):
        print("""Veuillez entrer "O" ou "N" s'il vous plait""")
        if question == 1:
            reponse = input("Continuer ? [O]ui ou [N]on:")
        if question == 2:
            reponse == input("Annuler ? [O]ui ou [N]on")
    return reponse




##################################
# HISTORIQUE DES COUPS JOUE
##################################




##################################
# Déroulement du jeu
##################################

# Définition des variables avant de rentrer dans la boucle de jeu

tour = 1
coord_li = -1
coord_col = -1

reponse = "O"
annuler = ""

historique = []


while continuer_de_jouer(reponse):#partie_continue():                    # Boucle du jeu

    if historique != []:
        print("tour", tour)
        print("dernier coup joué", historique[tour-2]) # A FINIR DE FAIRE LES DEF POUR O ET N

        annuler = input("Annuler le coup ? [O]ui ou [N]on:")
        test_O_N(annuler, 2)
        if continuer_de_jouer(annuler):
            dernier_coup = historique.pop() 
    # A ANALYSER
            supprimer(tictac, dernier_coup[0], dernier_coup[1])
    print("C'est au tour du joueur", joueur(tour), "de jouer")

    coord_li = def_col_li(coord_li)
    coord_col = def_col_li(coord_col)


    if coord_li != "" and coord_col != "":                                              # ICI
        historique.append([coord_li, coord_col, joueur(tour)])
        ecrire(tictac, coord_li, coord_col, coup(joueur(tour)))

        affiche(tictac)
        print(historique)               # A SUPPRIMER SI TESTS OK
        tour += 1


    reponse = input("Continuer ? [O]ui ou [N]on:")                  # A FAIRE: IL MANQUE LE ANNULER LE COUP ET VOULEZ VOUS CONTINUER
    test_O_N(reponse, 1)

print("fin")


# while not partie_finie():

# if grille_pleine(tictac):
#     print("egalité !")
# elif partie_gagnee(tictac, coord_li, coord_col):
#     print("partie gagnée !")
# elif not continuer_de_jouer(reponse):
#     print("vous avez arreté de jouer")

# print("fin du programme")


# SI la grille n'est pas pleine ET que personne n'a gagné ET que personne n'a dit NON:
#  On joue ?
#    Si NON : 
#      StOP                                                  // OK
#        Si OUI :                                                  // EN COURS
#          Si l'entrée est un chiffre ET si l'entrée est entre 0 et len(n) et case est vide
#                     Alors on joue                                 //