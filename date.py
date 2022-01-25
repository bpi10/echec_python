# Implémentation des dates et calendriers
# Implémentation des tests (voir main en fin de fichier)

from typing import Dict, List, Tuple, NoReturn



# =============================================================================
def est_bissextile(annee: int) :
    """
    retourne vrai si l'année est bissextile
    une année est bissextile si :
        - elle est divisible par 4 et pas divisible par 100
        - ou elle est divisible par 100
        

    >>> est_bissextile(2020)
    True
    >>> est_bissextile(2021)
    False
    >>> est_bissextile(2022)
    False
    >>> est_bissextile(1900)
    False
    >>> est_bissextile(2000)
    True
    """
    # calcul d'une année, pour savoir si elle est bissextile ou non
    if (annee % 4 == 0 and annee % 100 != 0) or annee % 400 == 0 :
        return True
    else : 
        return False


    
# =============================================================================
def cree_date(j: int, m: int, a: int) :
    """
    Crée une date à partir des entiers la décrivant.
    Si l'un des paramètres n'est pas un entier, la fonction retournera None

    >>> cree_date(15,12,2020)
    {'jour': 15, 'mois': 12, 'annee': 2020}
    >>> cree_date(1.5,12,2020)

    """
    # création d'un dictionnaire vide
    dict = {}
    # vérification si les jours, mois et années sont des entiers
    if j%1 == 0 and m%1 == 0 and a%1 == 0 :
        # implémentation du dictionnaire
        dict = {"jour" : j, "mois" : m, "annee" : a}
        return dict


    
# =============================================================================
def copie_date(date: Dict):
    """
    copie la date passée en paramètre
    >>> copie_date({'jour': 15, 'mois': 12, 'annee': 2020})
    {'jour': 15, 'mois': 12, 'annee': 2020}
    """
    # copie une date sans que la valeur de cree_date soit effacé
    copie_date = cree_date(date["jour"], date["mois"] ,date["annee"])
    return copie_date


    
# =============================================================================
def compare(d1: Dict, d2: Dict) :
    """
    Permet de classer deux dates.
    Retourne
    -1 si la date d1 < d2
    +1 si la date d1 > d2
    0 si les dates sont identiques
    on considère que les dates sont croissantes 
    dans l'ordre chronologique

    >>> date1 = cree_date(25,12,2021)
    >>> date2 = cree_date(31,12,2021)
    >>> compare(date1,date2)
    -1
    >>> compare(date2,date1)
    1
    >>> compare(date1,date1)
    0
    >>> date1 = cree_date(15,11,2021)
    >>> date2 = cree_date(10,12,2021)
    >>> compare(date1,date2)
    -1
    >>> compare(date2,date1)
    1
    >>> compare(date1,date1)
    0
    """
    # on compare d'abord les années, ensuite les mois et pour
    # finir, les jours afin de pouvoir définir si les dates sont : 
    #  d1 < d2 -> -1
    #  d1 > d2 -> 1
    #  d1 = d2 -> 0
    
    
    if d1['annee'] < d2['annee']:
        return (-1)
    elif d1['annee'] > d2['annee']:
        return (1)
    else:
        if d1['mois'] < d2['mois']:
            return(-1)
        elif d1['mois'] > d2['mois']:
            return(1)
        else:
            if d1['jour'] < d2['jour']:
                return (-1)
            elif d1['jour'] > d2['jour']:
                return(1)
            else:
                return(0)
    
    

    


# =============================================================================
def valide_simple(d: Dict):
    """   
    retourne vrai si la date est valide.
    on supposera que la date est valide si :
    - si le premier (le jour) est un entier compris entre 1 et 31
    - si le second (le mois) est un entier compris entre 1 et 12

    >>> date = cree_date(1, 2, 0)
    >>> valide_simple(date)
    True
    >>> date = cree_date(1.5, 5, 6)
    >>> valide_simple(date)
    False
    >>> date = cree_date(0, 5, 6)
    >>> valide_simple(date)
    False
    >>> date = cree_date(20, 8, 2021)
    >>> valide_simple(date)
    True
    """
    if d == None:
        return False
    # vérification si les jours, mois ete années sont compris dans leur ensemble de définition
    elif  0 < d["jour"] < 32 and 0 < d["mois"] < 13 and type(d["jour"]) == int and type(d["mois"]) == int:
        return True
    else:
        return False
    
    
    

# =============================================================================
def valide_complet(d: Dict)  :
    """ 
    retourne vrai si la date est valide.
    on supposera que la date est valide si :
    - la validation simple est vraie
    - si la date représente une date réelle 

    >>> date = cree_date(15, 1, 2022)
    >>> valide_complet(date)
    True
    >>> date = cree_date(32, 1, 2022)
    >>> valide_complet(date)
    False
    >>> date = cree_date(-1, 1, 2022)
    >>> valide_complet(date)
    False
    >>> date = cree_date(31, 6, 2022)
    >>> valide_complet(date)
    False
    >>> date = cree_date(29, 2, 2020)
    >>> valide_complet(date)
    True
    >>> date = cree_date(29, 2, 2022)
    >>> valide_complet(date)
    False
    """
    # vérification des jours dans un mois selon si l'année est bissextile ou non
    # année classique [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    # année bissextile [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if valide_simple(d) == True and (1000 <= d["annee"] <= 9999) :
        if (d["mois"] == 1):
            if 1 <= d["jour"] <= 31:
                return True
            else : 
                return False
        elif est_bissextile(d["annee"]) == True and d["mois"] == 2:
            if 1 <= d["jour"] <= 29:
                return True
            else : 
                return False
        elif est_bissextile(d["annee"]) == False and d["mois"] == 2:
            if 1 <= d["jour"] <= 28:
                return True
            else : 
                return False
        elif (d["mois"] == 3):
            if 1 <= d["jour"] <= 31 :
                return True
            else : 
                return False
        elif (d["mois"] == 4):
            if 1 <= d["jour"] <= 30:
                return True
            else : 
                return False
        elif (d["mois"] == 5):
            if 1 <= d["jour"] <= 31:
                return True
            else : 
                return False
        elif (d["mois"] == 6):
            if 1 <= d["jour"] <= 30:
                return True
            else : 
                return False
        elif (d["mois"] == 7):
            if 1 <= d["jour"] <= 31:
                return True
            else : 
                return False
        elif (d["mois"] == 8):
            if 1 <= d["jour"] <= 31:
                return True
            else : 
                return False
        elif (d["mois"] == 9):
            if 1 <= d["jour"] <= 30:
                return True
            else : 
                return False
        elif (d["mois"] == 10):
            if 1 <= d["jour"] <= 31:
                return True
            else : 
                return False
        elif (d["mois"] == 11):
            if 1 <= d["jour"] <= 30:
                return True
            else : 
                return False
        elif (d["mois"] == 12):
            if 1 <= d["jour"] <= 31:
                return True
            else : 
                return False
    else:
        return False


# =============================================================================
def ajoute_calendrier(calendrier: List, date: Dict, description: str ):
    """
    ajoute un élément à la liste du calendrier.
    >>> calendrier = []
    >>> ajoute_calendrier(calendrier, cree_date(25, 12, 2021), Noel)
    Le 25/12/2022 : Noel
    >>> ajoute_calendrier(calendrier, cree_date(1 ,1 ,2022 ),  Jour de l’an )
    Le 1/1/2022 : Jour de l’an
    """
    # création de descri qui est un dictionnaire comprenant la description
    descri = {"description": description}
    # si la date est vérifiée par la fonction valide_complet alors on peut ajouter au dictionnaire "calendrier" les valeurs
    if valide_complet(date) ==  True:
        calendrier = calendrier.append(date) and calendrier.append(descri)
        return('Le', date, ':', description)
        

    
# =============================================================================
def affiche_calendrier(calendrier: List) :
    """
    affiche le calendrier sous forme de liste.
    >>> ajoute_calendrier(calendrier, cree_date(25, 12, 2021), Noel)
    Le 25/12/2022 : Noel
    """
    # si la date est vérifiée, alors on affiche la fonction ajoute_date le nombre de fois qu'il y a de dates et description
    for i in range (len(calendrier)):
        if valide_complet() == True:
            print(ajoute_calendrier)
        else:
            print (input('Veuillez rentrer une bonne date'))
        


def trouve_evenement ( calendrier : List , date : Dict ): 
    """
    recherche le nom d’un évenement dont on connait la date, 
    elle permet permet d’avoir le choix dans la date et de retourner
    l’évenement qui correspond. Si aucun événement n’est trouvé alors
    la fonctione retournera None
    
    """
    # pour i de 1 jusque la longueur du calendrier
    for i in range (len(calendrier)):
        # on compare si la date rentrée est la même que celle du calendrier
        if compare(calendrier,date ) == 0:
            return ('La date :', date,'est dans le calendrier')
        else:
            return (('La date :', date,'n est pas dans le calendrier'))


            
def calcule_jour (date: Dict ):
    """
    Ajoutez une fonction qui calcule le jour de la semaine d’une date (lundi, mardi ...).
    >>> calcule_jour({'jour': 9, 'mois': 12, 'annee': 2021})
    c'est un Jeudi
    >>> calcule_jour({'jour': 9, 'mois': 12, 'annee': 2020})
    c'est un Mercredi
    """
    coef = round((14 - date["mois"]) / 12)

    a = date["annee"] - coef

    m = round((date["mois"] + 12 * coef)- 2)

    if date["mois"] == 1 or date["mois"] == 2:
        coef = 1
    
    # calcul du jour de la date  
    j = round((date["jour"] + a + (a / 4) - (a / 400) + (31 * m) / 12) % 7)

    if valide_complet(date):
        # si j = 1 alors c'est un Lundi
        if j == 1:
            print("c'est un Lundi")
        # si j = 2 alors c'est un Mardi
        elif j == 2:
            print("c'est un Mardi")
        # si j = 3 alors c'est un Mercredi
        elif j == 3:
            print("c'est un Mercredi")
        # si j = 4 alors c'est un Jeudi
        elif j == 4:
            print("c'est un Jeudi")
        # si j = 5 alors c'est un Vendredi
        elif j == 5:
            print("c'est un Vendredi")
        # si j = 6 alors c'est un Samedi
        elif j == 6:
            print("c'est un Samedi")
        # si j = 0 alors c'est un Dimanche
        elif j == 0:
            print("c'est un Dimanche")
    # sinon si j != au tests précédents, alors cela n'affiche rien
    else:
        return None 
    



# =============================================================================    
if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
    


