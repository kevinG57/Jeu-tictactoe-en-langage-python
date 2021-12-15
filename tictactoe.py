from graphicalgrid import GraphicalGrid

# BOUCLE A ETUDIER:
# A FAIRE IMPORTANT : probleme d'entrée de coordonnée (str)
# test_entree_chiffre à etudier pour decouper en "est-ce que je ne peux pas decouper en espace, +/- et chiffre"

# Les trois test O et N sont TRES BIZARRES: à etudier
 
# N à la question "voulez vous continuer" ne sort pas de la boucle 

# Problème de boucle quand on demande d'annuler ce coup


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
    if est_vide(grille, i, j):
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


#---------Fonctions de fin de jeu (arret, gagné, nul)----------------


# Controle de grille pleine (pour arret de jeu)

def grille_pleine(grille):
    for i in range(taille_grille(grille)):
        for j in range(taille_grille(grille)):
            if est_vide(grille, i, j):
                return False
    return True


# -------Controle si la partie est gagnee ou non-----------------------------------

def partie_gagnee_ligne(grille, li):  
    for i in range(taille_grille(grille)):
        if grille[li][0] != grille[li][taille_grille(grille)-i-1] or est_vide(grille, li, 0):
            return False
    return True


def partie_gagnee_col(grille,col):
    for i in range(taille_grille(grille)):
            if grille[0][col] != grille[taille_grille(grille)-i-1][col] or est_vide(grille, 0, col):
                return False
    return True


def partie_gagnee_diagonale_1(grille):
    for i in range(taille_grille(grille)):
            if grille[0][0] != grille[i][i] or est_vide(grille, 0, 0):
                return False
    return True


def partie_gagnee_diagonale_2(grille):
        longeur = taille_grille(grille)
        for i in range(longeur):
            if grille[longeur-1][0] != grille[longeur-1-i][i] or est_vide(grille, longeur-1, 0):
                return False
        return True


def partie_gagnee(grille, i, j):
    return partie_gagnee_ligne(grille, i) or partie_gagnee_col(grille, j) or partie_gagnee_diagonale_1(grille) or partie_gagnee_diagonale_2(grille)


#--------------------Partie finie------------------------

def partie_continue(grille, coord_li, coord_col, reponse): 
    return not grille_pleine(grille) and not partie_gagnee(grille, coord_li, coord_col) and continuer_de_jouer(reponse)


# -------------Qui joue ?---------------------------------

def joueur(tour):
    if tour % 2:
        return "O"
    else:
        return "X"

def coup(joueur):
    if joueur == "X":
        symbole = "X"
    if joueur == "O":
        symbole = "O"
    return symbole



# --------Vérification des entrées de col et li---------------------------


def def_col_li(coordonnee, li_col):
    coordonnee = input("Entrez un numéro de " + li_col)                     # DEMANDER AU PROF SI OK VARIABLE
    if coordonnee != "":
        while not test_entree_chiffre(coordonnee):
            print("Veuillez entrer un chiffre svp")
            coordonnee = input("Entrez un numéro de " + li_col)

        while not test_entree_coord(coordonnee):
            if int(coordonnee) < 0:                                          # VOIR SI OK DE FAIRE DEUX FONCTIONS
                print("Veuillez entrer un chiffre supperieur à 0")
                coordonnee = input("Entrez un numéro de " + li_col)
            if int(coordonnee) > taille_grille(tictac):
                print("Veuillez entrer un chiffre inferieur à la longeur")
                coordonnee = input("Entrez un numéro de " + li_col)

        return int(coordonnee)

    return coordonnee


# ---------Controle de la bonne saisie d'un chiffre-------------------------

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


# ----------Coordonnée est-elle correct ? ------------------------------------

def test_entree_coord(saisie):
    if 0 <= int(saisie) < taille_grille(tictac):
        return True
    return False


# ----------Continuer de jouer ? O ou N ?------------------------------------

def saisie_O_N(saisie):
    if saisie != "N" and saisie != "O":
        return False
    return True


def continuer_de_jouer(saisie):
    if saisie == "N":
        return False
    if saisie == "O":
        return True


def test_O_N(reponse, question):
    while not saisie_O_N(reponse):
        print("""Veuillez entrer "O" ou "N" s'il vous plait""")
        if question == 1:
            reponse = input("On continue ? [O]ui ou [N]on:")
        if question == 2:
            reponse == input("Voulez-vous annuler ce coup ? [O]ui ou [N]on")
    return reponse

# ------- Suppression ----------------------------------------------------------

def suppression(grille, histo):
    dernier_coup = histo.pop() 
    supprimer(grille, dernier_coup[0], dernier_coup[1])
    grille_graphique.erase(dernier_coup[0], dernier_coup[1])  


# -------------- Ecriture ---------------------------------------------------

def ecriture(grille, coord_li, coord_col, tour, histo):
    histo.append((coord_li, coord_col, joueur(tour)))
    ecrire(grille, coord_li, coord_col, coup(joueur(tour)))
    grille_graphique.write(coord_li, coord_col, joueur(tour))


# -------Déroulement du jeu-----------------------------------------


# ecrire(tictac, 0, 0, "X")
# ecrire(tictac, 0, 1, "X")
# ecrire(tictac, 0, 2, "X")
# ecrire(tictac, 1, 0, " ")
# ecrire(tictac, 1, 1, " ")
# ecrire(tictac, 1, 2, "O")
# ecrire(tictac, 2, 0, "O")
# ecrire(tictac, 2, 1, " ")
# ecrire(tictac, 2, 2, " ")
# affiche(tictac)



# Définition des variables avant de rentrer dans la boucle de jeu

tour = 1
coord_li = 0
coord_col = 0
reponse = "O"
annuler = ""
historique = []
coord_vide = False

longeur_grille = int(input("Rentrez la taille de la grille :"))
grille_graphique = GraphicalGrid(longeur_grille)
tictac = cree_grille(longeur_grille)


while partie_continue(tictac, coord_li, coord_col, reponse):                          # Boucle du jeu

    reponse = input("On continue ? [O]ui ou [N]on :")
    test_O_N(reponse, 1)

    if reponse == "O":
        print("tour", tour)

        if len(historique) > 0: # historique != []                                        # Affiche l'historique si il existe
            print("dernier coup joué =", historique[tour-2])                              # Out of range à régler
            annuler = test_O_N(input("Voulez-vous annuler ce coup ? [O]ui ou [N]on :"), 2) 
            if annuler == "O":                                                            # Annule ou non le coup précedent
                tour -= 1
                suppression(tictac, historique)             # ESSAI

        if annuler != "O":
            print("C'est au tour du joueur", joueur(tour))  #
            coord_li = def_col_li(coord_li, "ligne (appuyez sur entrée pour annuler la saisie) :")
            if coord_li != "":              # FAIRE NE PLUS PROPRE
                coord_col = def_col_li(coord_col, "colonne (appuyez sur entrée pour annuler la saisie) :")      

        if coord_li != "" and coord_col != "" and annuler != "O":
            while not est_vide(tictac, coord_li, coord_col):
                print("La case n'est pas vide")
                coord_li = def_col_li(coord_li, "ligne (appuyez sur entrée pour annuler la saisie) :")
                coord_col = def_col_li(coord_col, "colonne (appuyez sur entrée pour annuler la saisie) :")
                
            ecriture(tictac, coord_li, coord_col, tour, historique)

            print("tour ajouté")            # TEST
            affiche(tictac)                 # TEST
            print(historique)               # TEST
            tour += 1
            
        annuler = "N"
        coord_li = 0                            # A etudier pour faire plus propre
        coord_col = 0


if grille_pleine(tictac):
    print("egalité !")
elif partie_gagnee(tictac, coord_li, coord_col):
    print("Le joueur", joueur(tour+1), "a gagné")
elif not continuer_de_jouer(reponse):
    print("vous avez arreté de jouer")

grille_graphique.wait_quit()                                                        # Partie graphique

# print("ligne", partie_gagnee_ligne(tictac, 2))
# print("colonne", partie_gagnee_col(tictac, 2))
# print("diag 1", partie_gagnee_diagonale_1(tictac))
# print("diag 2", partie_gagnee_diagonale_2(tictac))                # TEST A SUPPRIMER
# print("grille pleine", grille_pleine(tictac))
# print("gagné", partie_gagnee(tictac, coord_li, coord_col))