# def controle_saisie(saisie):
#     while type(saisie) != int:
#         print("Il faut saisir un entier")
#         saisie = input("Saisir un chiffre")
#         print("type", type(saisie))

# controle_saisie(input("essai"))


# saisie = "  -42      "
# print(saisie, type(saisie))
# saisie = int(saisie)
# print(saisie, type(saisie))

essai = input("ecrire")
if essai == " ":
    print("entrer")


def def_col_li(coordonnee, li_col):
    coordonnee = input("Entrez un numéro de " + li_col)                     # DEMANDER AU PROF SI OK VARIABLE
    if coordonnee != "":
        while not test_entree_chiffre(coordonnee) or not test_entree_coord(coordonnee):
            while not test_entree_chiffre(coordonnee):
                print("Veuillez entrer un chiffre svp")
                coordonnee = input("Entrez un numéro de " + li_col)

            while not test_entree_coord(coordonnee):
                if test_entree_chiffre(coordonnee):
                    if int(coordonnee) < 0:                                          # VOIR SI OK DE FAIRE DEUX FONCTIONS
                        print("Veuillez entrer un chiffre supperieur à 0")
                        coordonnee = input("Entrez un numéro de " + li_col)
                    if int(coordonnee) > taille_grille(tictac):
                        print("Veuillez entrer un chiffre inferieur à la longeur")
                        coordonnee = input("Entrez un numéro de " + li_col)


        return int(coordonnee)
    return coordonnee        drapeau = True


    longeur_grille = int(input("Rentrez la taille de la grille :"))
taille_grille(longeur_grille)
grille_graphique = GraphicalGrid(longeur_grille)
tictac = cree_grille(longeur_grille)