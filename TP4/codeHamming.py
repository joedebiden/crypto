from numpy import *
from matplotlib.pylab import *
from imread import *
from random import *


def codeHamming(listebool):
    """
    Fonction pour encoder un message avec le code Hamming (7,4).
    
    :param listebool: Liste de 4 booléens (message à coder).
    :return: Liste de 7 booléens (message codé avec les bits de contrôle).
    """
    
    # check taille liste 
    if len(listebool) != 4:
        raise ValueError("La liste doit contenir exactement 4 booléens.")
    
    # Matrice génératrice 
    G = np.array([
        [1, 1, 1, 0],
        [1, 0, 1, 1],
        [1, 0, 0, 0],
        [0, 1, 1, 1],
        [0, 1, 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1]
    ], dtype=bool)
    
    # Convertit la liste en un vecteur colonne
    D = np.array(listebool, dtype=bool)
    
    # Produit matriciel dans Z2 (mod 2)
    C = np.dot(G, D) % 2  # Produit matriciel et opération mod 2
    
    
    return C.astype(bool).tolist()


message = [1, 0, 1, 1]  
message_code = codeHamming(message)
print("Message codé avec Hamming (7,4) :", message_code)





def syndromeHamming(listebool):
    """
    Fonction pour détecter la position de l'erreur dans un message encodé avec Hamming (7,4).
    
    :param listebool: Liste de 7 booléens (message reçu avec ou sans erreur).
    :return: Un entier entre 0 et 7 correspondant à la position de l'erreur (0 = pas d'erreur).
    """
    if len(listebool) != 7:
        raise ValueError("La liste doit contenir exactement 7 booléens.")
    
    # Matrice de vérification (parité) pour Hamming (7,4)
    H = np.array([
        [1, 0, 1, 0, 1, 0, 1],  # Vérifie p1 (positions binaires avec bit de poids faible 1)
        [0, 1, 1, 0, 0, 1, 1],  # Vérifie p2 (positions binaires avec bit du milieu 1)
        [0, 0, 0, 1, 1, 1, 1]   # Vérifie p3 (positions binaires avec bit de poids fort 1)
    ], dtype=bool)
    
    # Convertit la liste en un vecteur colonne
    C = np.array(listebool, dtype=bool)
    
    # Calcule le syndrome (produit matriciel dans Z2)
    S = np.dot(H, C) % 2  # Produit matriciel mod 2
    
    # Convertit le syndrome en entier (position de l'erreur)
    syndrome_value = int("".join(str(int(b)) for b in S[::-1]), 2)  # Inverse l'ordre pour binaire -> décimal
    
    # Retourne la position de l'erreur (0 si pas d'erreur)
    return syndrome_value


message_recu = [0, 1, 1, 0, 1, 1, 1]  # Message reçu avec une erreur
position_erreur = syndromeHamming(message_recu)
print("Position de l'erreur :", position_erreur)




def decodeHamming(listebool):
    """
    Fonction pour décoder un message encodé avec Hamming (7,4).
    Corrige une éventuelle erreur et renvoie les 4 bits originaux.
    
    :param listebool: Liste de 7 booléens (message reçu avec ou sans erreur).
    :return: Liste de 4 booléens correspondant au message original corrigé.
    """
    # Vérifie que la liste contient exactement 7 bits
    if len(listebool) != 7:
        raise ValueError("La liste doit contenir exactement 7 booléens.")
    
    # Matrice de vérification (parité) pour Hamming (7,4)
    H = np.array([
        [1, 0, 1, 0, 1, 0, 1],  # Vérifie p1 (positions binaires avec bit de poids faible 1)
        [0, 1, 1, 0, 0, 1, 1],  # Vérifie p2 (positions binaires avec bit du milieu 1)
        [0, 0, 0, 1, 1, 1, 1]   # Vérifie p3 (positions binaires avec bit de poids fort 1)
    ], dtype=bool)
    
    # Convertit la liste en un vecteur colonne
    C = np.array(listebool, dtype=bool)
    
    # Calcule le syndrome (produit matriciel dans Z2)
    S = np.dot(H, C) % 2  # Produit matriciel mod 2
    
    # Convertit le syndrome en entier (position de l'erreur)
    syndrome_value = int("".join(str(int(b)) for b in S[::-1]), 2)  # Inverse l'ordre pour binaire -> décimal
    
    # Si le syndrome est non nul, corrige l'erreur
    if syndrome_value != 0:
        # Corrige l'erreur en inversant le bit fautif
        C[syndrome_value - 1] = not C[syndrome_value - 1]
    
    # Les bits de données sont en positions 3, 5, 6 et 7
    data_bits = [C[2], C[4], C[5], C[6]]
    
    return data_bits


message_recu = [0, 1, 1, 0, 1, 1, 1]  # Message reçu avec une erreur
message_decode = decodeHamming(message_recu)
print("Message original corrigé :", message_decode)





def codeHamMat(matricebool):
    """
    Fonction qui code une matrice de blocs de 4 bits en blocs de 7 bits 
    en utilisant le code Hamming (7,4).
    
    :param matricebool: Matrice (liste de listes) de 4 booléens par ligne.
    :return: Matrice (liste de listes) de 7 booléens par ligne.
    """
    # Matrice génératrice pour Hamming (7,4)
    G = np.array([
        [1, 1, 1, 0],  # p1
        [1, 1, 0, 1],  # p2
        [1, 0, 1, 1],  # d1
        [0, 1, 1, 1],  # p3
        [1, 0, 0, 0],  # d2
        [0, 1, 0, 0],  # d3
        [0, 0, 1, 0]   # d4
    ], dtype=bool)
    
    # Initialiser la matrice codée
    matrice_codee = []
    
    # Parcourir chaque ligne de la matrice d'entrée
    for bloc in matricebool:
        if len(bloc) != 4:
            raise ValueError("Chaque bloc de la matrice doit contenir exactement 4 booléens.")
        
        # Convertir le bloc en un vecteur colonne
        D = np.array(bloc, dtype=bool)
        
        # Calculer le bloc codé (produit matriciel dans Z2)
        C = np.dot(G, D) % 2  # Produit matriciel mod 2
        
        # Ajouter le bloc codé à la matrice
        matrice_codee.append(C.astype(int).tolist())
    
    return matrice_codee

matrice_entree = [
    [1, 0, 1, 1],
    [0, 1, 1, 0],
    [1, 1, 0, 0]
]
matrice_codee = codeHamMat(matrice_entree)
print("Matrice codée :")
for ligne in matrice_codee:
    print(ligne)




