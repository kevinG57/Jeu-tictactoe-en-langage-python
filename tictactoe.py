from graphicalgrid import GraphicalGrid


# -------------------------------------------------------------------------- #
#         2. Représentation en mémoire de la grille de tictactoe             #
# -------------------------------------------------------------------------- #


# ------------ Generation de ma grille (Question 1) --------------------------

def cree_grille(taille):
    grille = []
    for i in range(taille):
        ligne = []
        for j in range(taille):
            ligne.append(" ")
        grille.append(ligne)
    return grille


# ------------ Longueur de la grille (Question 2) -----------------------------

def taille_grille(grille):
    n = len(grille)
    return n


# ------------- Vérifie que l'on soit dans la grille --------------------------

def est_dans_grille(grille, i, j):
    return 0 <= int(i) < taille_grille(grille) and 0 <= int(j) < taille_grille(grille)


# ------------- Vérifie si vide (Question 3) ----------------------------------

def est_vide(grille, i, j):
    i, j = int(i), int(j)
    return est_dans_grille(grille, i, j) and grille[i][j] == " "


# ------------- Ecrire un O ou un X (Question 4) -------------------------------

def ecrire(grille, i, j, symbole):
    if est_vide(grille, i, j):
        grille[i][j] = symbole


# ------------- Supprimer un X ou un O (Question 5) ----------------------------

def supprimer(grille, i, j):
    if est_dans_grille(grille, i, j) and not est_vide(grille, i, j):
        grille[i][j] = " "


# -------------- Vérifie si la case est X ou O (Question 6)---------------------

def est(grille, i, j, symbole):
    if est_dans_grille(grille, i, j):
        return symbole == grille[i][j]
    return False


# ------------- Affichage de la grille (Question 7) -----------------------------

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
            
            
# -------------------------------------------------------------------------- #
#                4. Mes fonctions pour jouer au tictactoe                    #
# -------------------------------------------------------------------------- #


# ------ Création de la grille de jeu-----------------------------------------------

def creation_de_grille():
    longueur_grille = test_taille_grille(input("Rentrez la taille de la grille :"))
    grille_graphique = GraphicalGrid(longueur_grille)
    tictac = cree_grille(longueur_grille)
    return tictac, grille_graphique


# ------ Test taille grille (doit etre supérieure à 2) ------------------------------

def test_taille_grille(chiffre):
    while not test_entier(chiffre) or chiffre == "" or chiffre < "3":
        if not test_entier(chiffre):
            print("Veuillez entrer un entier")
        elif chiffre == "":
            print("Veuillez rentrer un chiffre pour la taille de votre grille")
        elif int(chiffre) < 3:
            print("Veuillez renter un chiffre supérieur à 2")
        chiffre = input()
    return int(chiffre)


# ---------- Controle de grille pleine (égalité en cas de grille pleine) -----------

def grille_pleine(grille):
    for i in range(taille_grille(grille)):
        for j in range(taille_grille(grille)):
            if est_vide(grille, i, j):
                return False
    return True


# -------Controle si la partie est gagnee (lignes, colonnes et diagonales) ---------

def partie_gagnee_ligne(grille, li, tour):
    longueur = taille_grille(grille)
    for i in range(longueur):
        if not est(grille, int(li), i, joueur(tour-1)):
            return False
    return True


def partie_gagnee_col(grille, col, tour):
    longueur = taille_grille(grille)
    for i in range(longueur):
        if not est(grille, i, int(col), joueur(tour-1)):
            return False
    return True


def partie_gagnee_diagonale_1(grille, tour):
    longueur = taille_grille(grille)
    for i in range(longueur):
        if not est(grille, i, i, joueur(tour-1)):
            return False
    return True


def partie_gagnee_diagonale_2(grille, tour):
    longueur = taille_grille(grille)
    for i in range(longueur):
        if not est(grille, longueur-i-1, i, joueur(tour-1)):
            return False
    return True


# -------------------- Partie gagnée ----------------------------------------------------

def partie_gagnee(grille, i, j, tour):
    return partie_gagnee_ligne(grille, i, tour) or partie_gagnee_col(grille, j, tour) or partie_gagnee_diagonale_1(grille, tour) or partie_gagnee_diagonale_2(grille, tour)


# -- Partie finie (partie gagnée, grille pleine ou réponse [O] à "voulez-vous arreter ?"--

def partie_continue(grille, coord_li, coord_col, reponse, tour):
    if est_pas_entrer(coord_li) and est_pas_entrer(coord_col):
        return not grille_pleine(grille) and not partie_gagnee(grille, coord_li, coord_col, tour) and continuer_de_jouer(reponse)
    else:
        return True


# ------------- Qui joue ? -------------------------------------------------------------

def joueur(tour):
    if tour % 2:
        return "X"
    else:
        return "O"


# -------- Vérification des entrées de colonne et ligne --------------------------------

def definition_col_li(grille, coordonnee, txt_li_col):
    coordonnee = input("Entrez un numéro de " + txt_li_col)
    if est_pas_entrer(coordonnee):
        while est_pas_entrer(coordonnee) and not test_entree_coord(grille, coordonnee):
            if not test_entier(coordonnee):
                print("Veuillez entrer un chiffre svp")
                coordonnee = input("Entrez un numéro de " + txt_li_col)
            else:
                if not test_entree_coord(grille, coordonnee):
                    if int(coordonnee) < 0:
                        print("Veuillez entrer un chiffre supperieur à 0")
                    if int(coordonnee) >= taille_grille(grille):
                        print("Veuillez entrer un chiffre inferieur à la longueur")
                    coordonnee = input("Entrez un numéro de " + txt_li_col)
    return coordonnee


# -------- Vérification que la saisie est différente d'[ENTRER] -------------------------

def est_pas_entrer(saisie):
    return saisie != ""


# ----------Controle que la coordonnée rentrée est dans la grille -----------------------

def test_entree_coord(grille, saisie):
    return est_pas_entrer(saisie) and test_entier(saisie) and 0 <= int(saisie) < taille_grille(grille)


# ----------Continuer de jouer ? [O] ou [N] ?-----------------------------------------------

def saisie_O_N(saisie):
    if saisie != "N" and saisie != "O":
        return False
    return True


def continuer_de_jouer(saisie):
    if saisie == "N":
        return False
    elif saisie == "O":
        return True


# ---------- Boucle de test en attente de [O] ou de [N] ------------------------------------

def test_O_N(reponse, question):
    while not saisie_O_N(reponse):
        print("""Veuillez entrer "O" ou "N" s'il vous plait""")
        if question == 1:
            reponse = input("On continue ? [O]ui ou [N]on:")
        if question == 2:
            reponse = input("Voulez-vous annuler ce coup ? [O]ui ou [N]on")
    return reponse


# -------------- Ecriture d'un coup joué ---------------------------------------------------

def ecriture(grille, grille_graph, coord_li, coord_col, tour, historique):
    historique.append((coord_li, coord_col, joueur(tour)))
    ecrire(grille, coord_li, coord_col, joueur(tour))
    grille_graph.write(coord_li, coord_col, joueur(tour))


# ------- Suppression du coup précédent ----------------------------------------------------

def suppression(grille, grille_graph, historique):
    dernier_coup = historique.pop()
    supprimer(grille, dernier_coup[0], dernier_coup[1])
    grille_graph.erase(dernier_coup[0], dernier_coup[1])


# -------------- Resultat de la partie -----------------------------------------------------

def fin_de_jeu(grille, coord_li, coord_col, reponse, tour):
    if partie_gagnee(grille, coord_li, coord_col, tour):
        print("Le joueur", joueur(tour+1), "a gagné")
    elif grille_pleine(grille):
        print("egalité !")
    elif not continuer_de_jouer(reponse):
        print("vous avez arreté de jouer")


# ------------- Boucle de teste si case selectionnée est bien vide -------------------------

def test_case_vide(grille, coord_li, coord_col):
    while (est_pas_entrer(coord_li) and est_pas_entrer(coord_col)) and not est_vide(grille, coord_li, coord_col):
        print("La case n'est pas vide")
        coord_li = definition_col_li(grille, coord_li, "ligne (appuyez sur entrée pour annuler la saisie) :")
        coord_col = definition_col_li(grille, coord_col, "colonne (appuyez sur entrée pour annuler la saisie) :")

    return coord_li, coord_col


# ------------------------------------------------------------------------------------- #
#                                 5. Saisie d'un entier                                 #
# ------------------------------------------------------------------------------------- #


def est_chiffre(saisie):
    return "0" <= saisie <= "9"


def est_signe(saisie):
    return saisie == "+" or saisie == "-"


def est_espace(saisie):
    return saisie == " "


def un_chiffre_min(saisie):
    for i in range(len(saisie)):
        if est_chiffre(saisie[i]):
            return True
    return False


def est_pas_lettre(saisie):
    for i in range(len(saisie)):
        if not est_chiffre(saisie[i]) and not est_signe(saisie[i]) and not est_espace(saisie[i]):
            return False
    return True


def pas_signe_multiple(saisie):
    signe_flag = 0
    for i in saisie:
        if est_signe(i):
            signe_flag += 1
    if signe_flag > 1:
        return False
    else:
        return True


def est_pas_signe_espace(saisie):
    for i in range(len(saisie)-1):
        if est_signe(saisie[i]) and est_espace(saisie[i+1]):
            return False
    return True


def est_pas_chiffre_signe(saisie):
    for i in range(len(saisie)-1):
        if est_chiffre(saisie[i]) and est_signe(saisie[i+1]):
            return False
    return True


def est_pas_chiffre_espace_chiffre(saisie):
    chiffre_espace = 0
    if len(saisie) > 2:
        for i in range(len(saisie)):
            if est_chiffre(saisie[i]) and chiffre_espace == 1:
                return False
            if i < (len(saisie)-1):
                if est_chiffre(saisie[i]) and est_espace(saisie[i+1]):
                    chiffre_espace = 1
    return True


def test_entier(saisie):
    return un_chiffre_min(saisie) and pas_signe_multiple(saisie) and est_pas_signe_espace(saisie) and est_pas_chiffre_signe(saisie) and est_pas_chiffre_espace_chiffre(saisie) and est_pas_lettre(saisie)


# ----------------------------------------------------------------------------- #
#                          Déroulement d'une partie                             #
# ----------------------------------------------------------------------------- #


def jeu():

    # Définition des variables (en dehors de la boucle de jeu)

    tour = 1
    coord_li = "0"
    coord_col = "0"
    reponse = "O"
    annuler = ""
    historique = []

    # Création de la grille

    tictac, grille_graphique = creation_de_grille()

    # Boucle de jeu

    while partie_continue(tictac, coord_li, coord_col, reponse, tour):

        reponse = test_O_N(input("On continue ? [O]ui ou [N]on :"), 1)

        # Gestion de l'historique (et annulation du coup précédent)

        if reponse == "O":
            if len(historique) > 0:
                print("dernier coup joué =", historique[tour-2])
                annuler = test_O_N(input("Voulez-vous annuler ce coup ? [O]ui ou [N]on :"), 2)
                if annuler == "O":
                    tour -= 1
                    suppression(tictac, grille_graphique, historique)

            # Entrée des coordonnées de lignes et de colonnes

            if annuler != "O":
                print("C'est au tour du joueur", joueur(tour))
                coord_li = definition_col_li(tictac, coord_li, "ligne (appuyez sur entrée pour annuler la saisie) :")
                if est_pas_entrer(coord_li):
                    coord_col = definition_col_li(tictac, coord_col, "colonne (appuyez sur entrée pour annuler la saisie) :")

                coord_li, coord_col = test_case_vide(tictac, coord_li, coord_col)

                if est_pas_entrer(coord_li) and est_pas_entrer(coord_col):
                    ecriture(tictac, grille_graphique, int(coord_li), int(coord_col), tour, historique)
                    tour += 1
                    

    # Fin du jeu (partie gagnée, grille pleine ou arret de la partie d'un des deux joueurs)
    fin_de_jeu(tictac, coord_li, coord_col, reponse, tour)

    grille_graphique.wait_quit()


jeu()
