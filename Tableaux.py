###
# Pierre Brenel
# TP1 TPA
# tp1 python
###
import numpy as np
import random as rd

# exercice 1

def menu():
    print("1 = remplir aléatoirement un tableau")
    print("2 = afficher un tableau")
    print("3 = rechercher la valeur minimum d’un tableau")
    print("4 = compter le nombre d’occurrences d’une valeur demandée à l’utilisateur dans un tableau")
    print("5 = rechercher une valeur dans un tableau")
    print("6 = calculer la moyenne des valeurs d’un tableau")
    print("7 = quitter")

def remplir_tableau():
    """
    rempli le tableau de valeurs random
    """
    tableau = np.random.randint(11,size = 10)
    return tableau

def affiche_tableau(tableau):
    """
    affiche le tableau
    """
    print (tableau)

def valeur_minimum_tableau(tableau, valeur_min : int):
    """
    recherche la valeur minimum du tableau
    """
    valeur_min = valeur_min[0]
    for i in  valeur_min:
        if i < valeur_min :
            valeur_min  = i
    return valeur_min



def occurence(cpt : int, valeur : str, tableau):
    """
    recherche le nombre de fois où la valeur est dans le tableau
    """
    cpt = 0
    valeur = print(input('Quel caractère voulez vous compter ? : '))
    if valeur is not str:
        print('Relancer et taper une valeur entière.')
        for i in range (tableau):
            if valeur == tableau[i]:
                cpt = cpt + 1
    return cpt

def recherche_valeur_tableau(tableau, valeur):
    """
    recherche une valeur dans le tableau
    """
    valeur  = input("Quelle valeur voulez vous chercher ? : ")
    for i in range (tableau):
        if valeur == tableau[i]:
            return ("La valeur a été trouvé dans le tableau à l'emplacement :", tableau[i])
        else:
            return ("La valeur n'a pas été trouvé dans le tableau; désolé...")
    return
    
def calcul_moy_tab(tableau, moyenne : float):
    """
    Calcul la moyenne de toutes les valeurs rentrées dans le tableau
    """
    nbr_valeurs = 10
    moyenne = 0
    for i in range (tableau):
        moyenne = moyenne + tableau[i]
    return moyenne / nbr_valeurs

def quitter():
    """
    quitte le programme
    """
    print("Vous quitter le programme")
    


if __name__ == "__main__" :
    valeur : int; demand : int; valeur_min : int; cpt : int
    moyenne : float
    demand = 0
    
    while demand != 7:
        menu()
        demand = int(input("Que voulez vous faire ? Rentrer un chiffre de 1 à 7 : "))
        if demand == 1:
            tableau=remplir_tableau()
        elif demand == 2:
            affiche_tableau(tableau)
        elif demand == 3:
            print(valeur_minimum_tableau(tableau, valeur_min))
        elif demand == 4:
            print(occurence(cpt, valeur, tableau))
        elif demand == 5:
            print(recherche_valeur_tableau(tableau, moyenne))
        elif demand == 6:
            print(calcul_moy_tab(tableau, moyenne))
        elif demand == 7:
            quitter()
    