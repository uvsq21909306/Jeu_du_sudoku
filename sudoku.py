"""
Module: sudoku.py Un programme pour manipuler des grilles de sudoku.

Les variables grille_x peuvent vous servir à tester votre programme.
Elles représentent toutes des grilles de Sudoku valides à divers
stades d'avancement: grille_0 est vide, grille_1 semi-remplie et
grille_2 entièrement remplie.
"""



grille_0 = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
]

grille_1=[
    [0, 0, 0, 0, 0, 0, 0, 0, 8],
    [0, 2, 0, 0, 5, 0, 7, 6, 0],
    [0, 6, 0, 0, 0, 0, 0, 0, 3],
    [5, 0, 0, 0, 0, 0, 2, 0, 7],
    [0, 3, 0, 0, 1, 0, 0, 0, 0],
    [2, 0, 0, 4, 0, 0, 0, 3, 0],
    [0, 0, 0, 6, 0, 0, 0, 0, 0],
    [8, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 2, 7, 0, 0, 4, 0],
]

grille_2 = [
    [6, 2, 5, 8, 4, 3, 7, 9, 1],
    [7, 9, 1, 2, 6, 5, 4, 8, 3],
    [4, 8, 3, 9, 7, 1, 6, 2, 5],
    [8, 1, 4, 5, 9, 7, 2, 3, 6],
    [2, 3, 6, 1, 8, 4, 9, 5, 7],
    [9, 5, 7, 3, 2, 6, 8, 1, 4],
    [5, 6, 9, 4, 3, 2, 1, 7, 8],
    [3, 4, 2, 7, 1, 8, 5, 6, 9],
    [1, 7, 8, 6, 5, 9, 3, 4, 2],
]

"""
Les deux fonctions ci-dessous sont données à titre d'exemple.  Le
reste est à programmer à la suite de ces fonctions.
"""

def afficher(x):
    """
    Affiche une grille de sudoku g de taille 9x9 sur le terminal.
    """
    ligne0 = "╔═══╤═══╤═══╦═══╤═══╤═══╦═══╤═══╤═══╗"
    ligne1 = "║ . │ . │ . ║ . │ . │ . ║ . │ . │ . ║"
    ligne2 = "╟───┼───┼───╫───┼───┼───╫───┼───┼───╢"
    ligne3 = "╠═══╪═══╪═══╬═══╪═══╪═══╬═══╪═══╪═══╣"
    ligne4 = "╚═══╧═══╧═══╩═══╧═══╧═══╩═══╧═══╧═══╝"

    valeurs = [[""]+[" 1234567890"[case] for case in ligne] for ligne in x]

    print(ligne0)
    for ligne in range(1,9+1):
        print("".join(n+s for (n, s) in zip(valeurs[ligne-1], ligne1.split("."))))
        print([ligne2, ligne3, ligne4][(ligne % 9 == 0) + (ligne % 3 == 0)])


def unique(x) :
    """"
    Renvoie True si tous les éléments de x sont différents et False si au moins deux éléments de x sont identiques
    """
    #On parcourt la liste x
    for i in range(10) :
        #On compte le nombre d'occurence d'un élement dans la liste 
        #Si on trouve un nombre d'occurence d'un élément supérieur à 1 fois(c'est-à-dire que l'élément est retrouvé plus d'une fois dans la liste) alors on retourne false 
        if i > 0 and x.count(i) > 1 : # Décompte du nombre de l'élélent i dans la liste x en excluant le décompte des 0
            return False
        else : 
            pass
    return True     


def ligne(x, i) : 

    """
    Renvoie la ligne i de la grille de sudoku x
    """
    line = x[i-1]

    # print("Voici les chiffres de la ", i, "ème ligne : ", line)
    return line


def colonne(x, i) : 
    """
    Renvoie la colonne i de la grille de sudoku x
    """
    c =[] 

    for j in range(9) :
        c.append(x[j][i-1])
        
    # print("Voici les chiffres de la ", i, "ème colonne : ", c)
    return c  


def region(x, i) :  
    """
    renvoie la region i de la grille de sudoku 
    """    
    # Région 1 = haut gauche 
    # Région 2 = milieu centre
    # Région 3 = haut droite
    # Région 4 = milieu droite
    # Région 5 = milieu centre
    # Région 6 = milieu gauche
    # Région 7 = bas gauche 
    # Région 8 = bas centre
    # Région 9 = Bas droite 
       
    if i >= 10 or i <1 : # Vérification de l'existence de la région 
        return False

    c = []
    for line in range(9):
        for colu in range(9):
            k = 3*(line//3) + (colu//3) + 1
            if not k != i:
                c.append(x[line][colu])
    # print("Voici les chiffres de la ", i, "ème région : ", c)
    return c    
    

def ajouter(x, i, j, v ) :

    if i < 1 or j < 1 or i > 9 or j > 9 : # Vérification de l'existence des coordonnées
        return False  

    """ 
    La partie de la ligne 144 à la ligne 147 part du principe qu'il s'agit d'un nouvelle partie et que les cases pré-remplies ne doivent pas être modifiées.
    Seules les cases contenat des zéros peuvent être modifiées.
     """
    v = x[i - 1][j - 1] # Une fois les coordonnées obtenuees, on vérifie qu'il s'agit d'une case vide (c'est à dire 0)
    # print(v)
    if v != 0 :
        return False  

    
# On cherche à savoir s'il s'agit d'une case vide. on vérifie donc si la valeur présente 
    '''ajoute la valeur v au coordonnées (i,j) de la grille x'''
    k = 3 * ((i - 1) // 3) + ((j - 1)//3) + 1
    sauvegarde = x[i - 1][j - 1]
    x[i - 1][j - 1] = v
    if (not unique(ligne(x, i)) or not unique(colonne(x, j)) or not unique(region(x, k))):
        x[i - 1][j - 1] = sauvegarde

    return x
    """
    on vérifie que la valeur n'est pas disponible sur ligne, sur la colonne et sur la région (appel de la fonction unique) 
    Si la valeur est déjà dans la colonne, région ou ligne avec restaurer la valeur 0
    
    """
    

def verifier(x) :
    """
    Vérifie que la grille de sudoku a été correctement remplie et renvoie True si oui
    """
    # Verification du remplissage de la grille 
    for i in range(len(x)) :
        for j in range(len(x)) :
            if x[i][j]==0 :
                return False

    # Verification des lignes
    for i in range(1,10) : 
        line = ligne(x, i)
        #print('line: ', ligne(x, i))
        if unique(line)  == False :
            return False

    # Verification des colonnes
    for i in range(1, 10) : 
        colu = colonne(x, i)
        # print('colonne :', colu)
        if unique(colu) == False : 
            return False 

    # Verification des régions
    for i in range(1, 10) : 
        reg = region(x, i)
        # print('region :', reg)
        if unique(reg) == False :
            return False 
    
    return True


def jouer(x) :
    #On affiche la grille une première fois
    afficher(x)
    remplie = verifier(x)

    while remplie==False :
        #Je demande à l'utlisateur de saisir une ligne, colonne et valeur
        ligne = input("Entrez le numéro de la ligne")
        colonne = input("Entrez le numéro de la colonne")
        valeur = input("Entrez la valeur")

        #J'ajoute cette valeur à l'emplacement choisi par l'utlisateur (à la case d'indice x[i][j])
        ajouter(x, ligne, colonne, valeur)
        remplie = verifier(x)

        #J'affiche la nouvelle grille
        afficher(x)

    print("La grille et remplie")

def resoudre(x) : 

    pass 

def nouvelle() : 

    pass


# L'argument d'une fonction c'est ce qu'on lui donne pour quelle puisse nous renvoyeer qqch

# Fonction len() : Pour nous donner le nombre d'éléments dans la liste ou chaîne de charactère

# Pour récuperer l'élément d'une liste : 
# liste = [1, 2, 5, 7] 
# print(liste[2]) // Et cela renvoie 5

# Pour rajouter un élément à la liste on utilise .append()
# liste = liste.append(5)
# print(liste) // Cela renvoie [1, 2, 5, 7, 5]

# le mot return explique à la fonction ce qu'elle doit nous renvoyer 

# Pour la région 1 exemple :  On cherche a ce que ça nous renvoie les trois premiers des trois premières lignes 
# 3 × ((i − 1)//3) + ((j − 1)//3) + 1

x = grille_1

jouer(x)