###
# Pierre Brenel
# TP1 TPA
# tp2 python echiquier
###

from tkinter import *
import numpy as np
import random as rd

coord_dam=[
    'a8','b8','c8','d8','e8','f8','g8','h8',
    'a7','b7','c7','d7','e7','f7','g7','h7',
    'a6','b6','c6','d6','e6','f6','g6','h6',
    'a5','b5','c5','d5','e5','f5','g5','h5',
    'a4','b4','c4','d4','e4','f4','g4','h4',
    'a3','b3','c3','d3','e3','f3','g3','h3',
    'a2','b2','c2','d2','e2','f2','g2','h2',
    'a1','b1','c1','d1','e1','f1','g1','h1']

#damier = [[0,0,0,0,0,0,0,0],
#           [0,0,0,0,0,0,0,0],
#           [0,0,0,0,0,0,0,0],
#           [0,0,0,0,0,0,0,0],
#           [0,0,0,0,0,0,0,0],
#           [0,0,0,0,0,0,0,0],
#           [0,0,0,0,0,0,0,0],
#           [0,0,0,0,0,0,0,0]]


# création de fonctions 
def menu():
    print("---------------------------------------")
    print("------------ Jeu d'échecs -------------")
    print("---------------------------------------")


#def creation_damier():
#   damier = np.zeros((8, 8),dtype=np.string_)
#    return damier

def crea_damier():
   liste = [[0 for i in range(8)] for j in range(8)]
   return liste
#def crea_damier():
#    tableau  = np.chaarray((8,8), itemsize = 2)
#    tableau[:] = " "
#    return tableau

def creation_pions():
    pions_blanc = 'PB'
    pions_noirs = 'PN'
    cavalier_blanc = 'CB'
    cavalier_noir = 'CN'
    fou_blanc = 'FB'
    fou_noir = 'FN'
    tour_blanche = 'TB'
    tour_noire = 'TN'
    dame_blanche = 'DB'
    dame_noire = 'DN'
    roi_blanc = 'RB'
    roi_noir = 'RN'

def placement():
    damier[0][0] = '♜'
    damier[0][1] = '♞'
    damier[0][2] = '♝'
    damier[0][3] = '♚'
    damier[0][4] = '♛'
    damier[0][5] = '♝'
    damier[0][6] = '♞'
    damier[0][7] = '♜'
    damier[1][0] = '♟'
    damier[1][1] = '♟'
    damier[1][2] = '♟'
    damier[1][3] = '♟'
    damier[1][4] = '♟'
    damier[1][5] = '♟'
    damier[1][6] = '♟'
    damier[1][7] = '♟'

    damier[7][0] = '♖'
    damier[7][1] = '♘'
    damier[7][2] = '♗'
    damier[7][3] = '♔'
    damier[7][4] = '♕'
    damier[7][5] = '♗'
    damier[7][6] = '♘'
    damier[7][7] = '♖'
    damier[6][0] = '♙'
    damier[6][1] = '♙'
    damier[6][2] = '♙'
    damier[6][3] = '♙'
    damier[6][4] = '♙'
    damier[6][5] = '♙'
    damier[6][6] = '♙'
    damier[6][7] = '♙'

#def affichage_damier_v2(liste):
#    for i in range (8):
#        for j in range (8):
#            print(liste[i][j],end = ' ')
#        print()

def affichage_damier(liste):
    for i in range(8):
        for _ in range (20):
            print('-', end = ' ')
        print()

        print ("|", end = ' ')
        for j in range (8):
            print(liste[i][j], end = ' |  ')
        print()

    for _ in range (20):
        print('-', end = ' ')
    print()
 
def demand(column, ligne):
    column, ligne = int(input("Rentrer le nom de la colonne et la ligne que vous voulez :"))
    while column <= 'A' and column >= 'G'and ligne <= 0 and ligne >= 8:
        print (int(input("Rentrer le nom de la colonne et la ligne que vous voulez :")))
    else:
        return column, ligne




def placement_pieces():
    reponse = 1
    while reponse != 0:
        coord = print(int(input('Rentrer les coordonnées d une case dans le damier : ')))
        if coord in range(0 and 7) :
            return(coord)
        else:
            return()
    return


        


# programme principale 
if __name__ == "__main__":
    damier : list

    menu()
    damier = crea_damier()
    placement()
    affichage_damier(damier)



