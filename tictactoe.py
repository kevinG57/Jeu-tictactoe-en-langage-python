from graphicalgrid import GraphicalGrid


#------------ Generation de ma grille (question 1) -------------------

def cree_grille(taille):
    grille = []
    for i in range(taille):
        ligne = []
        for j in range(taille):
            ligne.append(" ")
        grille.append(ligne)

    return grille


#------------ Longeur de la grille (question 2) ----------------------

def taille_grille(grille):
    n = len(grille)

    return n


#------------- Vérifie que l'on soit dans la grille ------------------

def est_dans_grille(grille, i, j):
    if 0 <= i < taille_grille(grille) and 0 <= j < taille_grille(grille):
        return True
    return False


#------------- Vérifie si vide (Question 3) --------------------------

def est_vide(grille, i, j):
    i, j = int(i), int(j)
    if est_dans_grille(grille, i, j) and grille[i][j] == " ":
            return True
    return False
    

#------------- Ecrire un O ou un X (Question 4) ----------------------


def ecrire(grille, i, j, symbole):
    if est_vide(grille, i, j):
        grille[i][j] = symbole


#------------- Supprimer un X ou un O (Question 5) --------------------

def supprimer(grille, i, j):
    if est_dans_grille(grille, i, j) and not est_vide(grille, i, j):
        grille[i][j] = " "


#-------------- Vérifie si la case est X ou O (Question 6)-------------

def est(grille, i, j, symbole):
    if est_dans_grille(grille, i, j):
        return symbole == grille[i][j]
    return False


#------------- Affichage de la grille (Question 7) -------------------

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


# ------ Creation grille ----------------------------------------------------------

def creation_de_grille():    
    longeur_grille = test_taille_grille(input("Rentrez la taille de la grille :"))
    grille_graphique = GraphicalGrid(longeur_grille)
    tictac = cree_grille(longeur_grille)
    return tictac, grille_graphique


# ------ Test taille grille -------------------------------------------------------

def test_taille_grille(chiffre):

    while not test_entree_chiffre(chiffre) or chiffre == "" or int(chiffre) < 3:
        if not test_entree_chiffre(chiffre):
            print("Veuillez entrer un entier")
        elif chiffre == "":
            print("Veuillez rentrer un chiffre pour la taille de votre grille")
        elif int(chiffre) < 3:
            print("Veuillez renter un chiffre supérieur à 2")
        chiffre = input()
    return int(chiffre)


# ---------- Controle de grille pleine (pour arret de jeu) ------------------------

def grille_pleine(grille):
    for i in range(taille_grille(grille)):
        for j in range(taille_grille(grille)):
            if est_vide(grille, i, j):
                return False
    return True


# -------Controle si la partie est gagnee (lignes, colonnes et diagonales) ------------------------------------

def partie_gagnee_ligne(grille, li, tour): 
    longueur = taille_grille(grille)
    for i in range(longueur):
        if not est(grille, li, longueur-i-1, joueur(tour-1)) or est_vide(grille, li, 0):
            return False
    return True


def partie_gagnee_col(grille,col, tour):
    longueur = taille_grille(grille)
    for i in range(longueur):
        if not est(grille, longueur-i-1, col, joueur(tour-1)) or est_vide(grille, 0, col):
            return False
    return True


def partie_gagnee_diagonale_1(grille, tour):
    longueur = taille_grille(grille)
    for i in range(longueur):
        if not est(grille, i, i, joueur(tour-1)) or est_vide(grille, 0, 0):
            return False
    return True 


def partie_gagnee_diagonale_2(grille, tour):
    longueur = taille_grille(grille)
    for i in range(longueur):
        if not est(grille, longueur-i-1, i, joueur(tour-1)) or est_vide(grille, longueur-1, 0):
            return False
    return True


def partie_gagnee(grille, i, j, tour):
    return partie_gagnee_ligne(grille, i, tour) or partie_gagnee_col(grille, j, tour) or partie_gagnee_diagonale_1(grille, tour) or partie_gagnee_diagonale_2(grille, tour)


#-------------------- Partie finie ----------------------------------------------------

def partie_continue(grille, coord_li, coord_col, reponse, tour): 
    return not grille_pleine(grille) and not partie_gagnee(grille, coord_li, coord_col, tour) and continuer_de_jouer(reponse)


# ------------- Qui joue ? -------------------------------------------------------------

def joueur(tour):
    if tour % 2:
        return "X"
    else:
        return "O"


# -------- Vérification des entrées de col et li -----------------------------------------


def definition_col_li(grille, coordonnee, txt_li_col):                                 # Fonction un peu compliquée...
    coordonnee = input("Entrez un numéro de " + txt_li_col)
    if pas_entrer(coordonnee):
        while pas_entrer(coordonnee) and not test_entree_chiffre(coordonnee) or not test_entree_coord(grille, coordonnee):

            if not test_entree_chiffre(coordonnee):
                print("Veuillez entrer un chiffre svp")
                coordonnee = input("Entrez un numéro de " + txt_li_col)
            else:
                if not test_entree_coord(grille, coordonnee):                       
                    if int(coordonnee) < 0:
                        print("Veuillez entrer un chiffre supperieur à 0")
                    if int(coordonnee) >= taille_grille(grille):
                        print("Veuillez entrer un chiffre inferieur à la longeur")
                    coordonnee = input("Entrez un numéro de " + txt_li_col)
    return coordonnee


# --------- Controle de la bonne saisie d'un chiffre -------------------------------------      # ICI en cours

def test_entree_chiffre(saisie):
    chiffres = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "+", "-", " "]
    signe_flag = 0
    chiffre_flag = 0
    if saisie == "+" or saisie == "-":
        return False
    else:
        for i in saisie:
            drapeau = False
            for j in chiffres:
                if i == j:
                    drapeau = True
                    if i == "+" or i == "-":
                        signe_flag += 1
                    elif i != "+" or i != "-" or i != " ":
                        chiffre_flag += 1
                    if chiffre_flag > 0 and (i == "+" or i == "-"):
                        return False
            if drapeau == False or signe_flag > 1 :
                return False
        return True

# Test: 
# -------- Vérification que la saisie est différent d'ENTRER -------------------------------------------------

def pas_entrer(saisie):
    return saisie != ""


def est_chiffre(saisie):
    return "0" < saisie < "9"

def est_signe(saisie):
    return saisie == "+" or saisie == "-"

def est_espace(saisie):
    return saisie == " "

def est_signe_seul(saisie):
    for i in range(len(saisie)):
        if not est_chiffre(saisie[i]):
            return False
    return True

def est_lettre(saisie):
    for i in range(len(saisie)):
        if not est_chiffre(saisie[i]) and not est_signe(saisie[i]) and not est_espace(saisie[i]):
            return False
    return True

def est_signe_multiple(saisie):
    signe_flag = 0
    for i in saisie:
        if est_signe(i):
            signe_flag += 1
    if signe_flag > 1:
        return False
    else:
        return True

def est_signe_espace(saisie):
    for i in range(len(saisie)-1):
        if est_signe(saisie[i]) and est_espace(saisie[i+1]):
            return False
    return True

def est_chiffre_signe(saisie):
    for i in range(len(saisie)-1):
        if est_chiffre(saisie[i]) and est_signe(saisie[i+1]):
            return False
    return True

def test_entree_chiffre2(saisie):
    return est_chiffre(saisie) and est_signe_seul(saisie) and est_lettre(saisie) and est_signe_multiple(saisie) and est_signe_espace(saisie) and est_chiffre_signe(saisie)

saisie_essai = "+3"
print("signe seul", est_signe_seul(saisie_essai))
print(est_lettre(saisie_essai))
print(est_signe_multiple(saisie_essai))
print(est_signe_espace(saisie_essai))
print(est_chiffre_signe(saisie_essai))
print(test_entree_chiffre2(saisie_essai))


# ----------Coordonnée est-elle correct ? -------------------------------------------------

def test_entree_coord(grille, saisie):
    if 0 <= int(saisie) < taille_grille(grille):
        return True
    return False


# ----------Continuer de jouer ? O ou N ?--------------------------------------------------

def saisie_O_N(saisie):
    if saisie != "N" and saisie != "O":
        return False
    return True


def continuer_de_jouer(saisie):
    if saisie == "N":
        return False
    elif saisie == "O":
        return True


# ---------- Boucle de test en attente de "O" ou de "N" ------------------------------------

def test_O_N(reponse, question):
    while not saisie_O_N(reponse):
        print("""Veuillez entrer "O" ou "N" s'il vous plait""")
        if question == 1:
            reponse = input("On continue ? [O]ui ou [N]on:")
            print("essai", reponse)
        if question == 2:
            reponse = input("Voulez-vous annuler ce coup ? [O]ui ou [N]on")
    print(reponse)
    return reponse


# -------------- Ecriture d'un coup joué ---------------------------------------------------

def ecriture(grille, grille_graph, coord_li, coord_col, tour, histo):
    histo.append((coord_li, coord_col, joueur(tour)))
    ecrire(grille, coord_li, coord_col, joueur(tour))
    grille_graph.write(coord_li, coord_col, joueur(tour))


# ------- Suppression du coup précédent ----------------------------------------------------

def suppression(grille, grille_graph, histo):
    dernier_coup = histo.pop() 
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


# -------Déroulement du jeu------------------------------------------------------------------


def jeu():

    tour = 1
    coord_li = 0
    coord_col = 0
    reponse = "O"
    annuler = ""
    historique = []                                                                            # Définition des différentes variables

    tictac, grille_graphique = creation_de_grille()

    while partie_continue(tictac, coord_li, coord_col, reponse, tour):                         # Boucle du jeu

        reponse = test_O_N(input("On continue ? [O]ui ou [N]on :"), 1)
        
        if reponse == "O":
            if len(historique) > 0:
                print("dernier coup joué =", historique[tour-2])                               
                annuler = test_O_N(input("Voulez-vous annuler ce coup ? [O]ui ou [N]on :"), 2) 
                if annuler == "O":
                    tour -= 1
                    suppression(tictac, grille_graphique, historique) 

            if annuler != "O":                                                                 # Si on n'a pas répondu O à annuler, on demande la ligne et colonne à jouer
                print("C'est au tour du joueur", joueur(tour))
                coord_li = definition_col_li(tictac, coord_li, "ligne (appuyez sur entrée pour annuler la saisie) :")
                if pas_entrer(coord_li):
                    coord_col = definition_col_li(tictac, coord_col, "colonne (appuyez sur entrée pour annuler la saisie) :")

                while (pas_entrer(coord_li) and pas_entrer(coord_col)) and not est_vide(tictac, coord_li, coord_col) :
                    print("La case n'est pas vide")
                    coord_li = definition_col_li(tictac, coord_li, "ligne (appuyez sur entrée pour annuler la saisie) :")
                    coord_col = definition_col_li(tictac, coord_col, "colonne (appuyez sur entrée pour annuler la saisie) :")
                if pas_entrer(coord_li) and pas_entrer(coord_col):
                    ecriture(tictac, grille_graphique, int(coord_li), int(coord_col), tour, historique)
                    tour += 1

            annuler, coord_li, coord_col = "N", 0, 0                                        # Réinitialisation des variables en fin de boucle

    fin_de_jeu(tictac, coord_li, coord_col, reponse, tour)
    grille_graphique.wait_quit()


jeu()