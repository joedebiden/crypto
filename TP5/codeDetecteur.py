import random

def transmettreListe(liste, p):
    """
    Simule la transmission d'une liste de bits avec un taux d'erreur p.
    """
    return [bit ^ (random.random() < p) for bit in liste]

def codeDouble(liste, p):
    """
    Duplique une séquence de 4 bits et simule sa transmission jusqu'à ce que
    les 4 premiers bits correspondent exactement aux 4 derniers.
    
    Parameters:
    - liste (list): Liste de 4 bits à transmettre.
    - p (float): Taux d'erreur de transmission.
    
    Returns:
    - list: Les 4 bits transmis correctement.
    """
    if len(liste) != 4:
        raise ValueError("La liste doit contenir exactement 4 bits.")
    
    # Dupliquer la liste
    bloc_transmis = liste * 2
    
    while True:
        # Simuler la transmission
        bloc_recu = transmettreListe(bloc_transmis, p)
        
        # Vérifier si les 4 premiers bits correspondent aux 4 derniers
        if bloc_recu[:4] == bloc_recu[4:]:
            return bloc_recu[:4]

# Exemple d'utilisation
if __name__ == "__main__":
    # Liste initiale de 4 bits
    liste_bits = [0, 1, 0, 1]
    
    # Taux d'erreur
    p = 0.1  # 10% d'erreur
    
    # Transmission avec détection d'erreur
    resultat = codeDouble(liste_bits, p)
    print("Bits transmis correctement :", resultat)



import numpy as np

def transMatriceDouble(matrice, p):
    """
    Applique la fonction codeDouble à chaque bloc de 4 bits de chaque ligne
    d'une matrice.
    
    Parameters:
    - matrice (list of list of int): Matrice de bits (booléens) où le nombre de colonnes est un multiple de 4.
    - p (float): Taux d'erreur de transmission.
    
    Returns:
    - list of list of int: Matrice avec les blocs de 4 bits corrigés.
    """
    if len(matrice[0]) % 4 != 0:
        raise ValueError("Le nombre de colonnes doit être un multiple de 4.")
    
    # Matrice résultante
    matrice_corrigee = []
    
    for ligne in matrice:
        ligne_corrigee = []
        # Diviser la ligne en blocs de 4 bits
        for i in range(0, len(ligne), 4):
            bloc = ligne[i:i+4]
            # Appliquer codeDouble à chaque bloc
            bloc_corrige = codeDouble(bloc, p)
            ligne_corrigee.extend(bloc_corrige)
        matrice_corrigee.append(ligne_corrigee)
    
    return matrice_corrigee

# Exemple d'utilisation
if __name__ == "__main__":
    # Exemple de matrice (chaque ligne contient un multiple de 4 bits)
    matrice_exemple = [
        [0, 1, 0, 1, 1, 0, 1, 0],
        [1, 0, 1, 1, 0, 0, 1, 1]
    ]
    
    # Taux d'erreur
    p = 0.1  # 10% d'erreur
    
    # Transmission et correction
    matrice_corrigee = transMatriceDouble(matrice_exemple, p)
    print("Matrice corrigée :", matrice_corrigee)




import numpy as np
from PIL import Image
import random

def simulerErreur(liste, p):
    """
    Simule une erreur de transmission sur une liste de bits.
    Chaque bit a une probabilité p d'être inversé.
    """
    return [(bit if random.random() > p else 1 - bit) for bit in liste]

def tauxErreur(matrice1, matrice2):
    """
    Calcule le pourcentage d'erreurs entre deux matrices de même taille.
    """
    differences = np.sum(np.array(matrice1) != np.array(matrice2))
    total = np.prod(np.array(matrice1).shape)
    return (differences / total) * 100

def transMatriceDouble(matrice, p):
    """
    Applique la méthode de transmission par duplication avec correction.
    """
    matrice_corrigee = []
    for ligne in matrice:
        ligne_corrigee = []
        for i in range(0, len(ligne), 4):
            bloc = ligne[i:i+4]
            bloc_corrige = codeDouble(bloc, p)
            ligne_corrigee.extend(bloc_corrige)
        matrice_corrigee.append(ligne_corrigee)
    return matrice_corrigee

# Charger l'image floral.tif
def charger_image(filepath):
    """
    Charge une image en niveaux de gris et la convertit en matrice binaire.
    """
    image = Image.open(filepath).convert("L")  # Conversion en niveaux de gris
    image_array = np.array(image)
    matrice_binaire = (image_array > 127).astype(int)  # Conversion en binaire
    return matrice_binaire, image.size

def sauvegarder_image(matrice, size, output_path):
    """
    Sauvegarde une matrice binaire sous forme d'image TIFF.
    """
    matrice_image = (np.array(matrice) * 255).astype(np.uint8)
    image = Image.fromarray(matrice_image, mode="L")
    image.save(output_path)

# Simulation et test
filepath = "floral.tif"  # Chemin de l'image originale
output_path = "floral_corrige.tif"  # Chemin pour l'image corrigée
p = 0.01  # Taux d'erreur
essais = 10  # Nombre de répétitions

# Charger l'image
matrice_originale, size = charger_image(filepath)

erreurs_residuelles = []
for _ in range(essais):
    # Appliquer la transmission avec correction
    matrice_corrigee = transMatriceDouble(matrice_originale, p)
    
    # Calculer le taux d'erreurs résiduelles
    erreur_residuelle = tauxErreur(matrice_originale, matrice_corrigee)
    erreurs_residuelles.append(erreur_residuelle)

# Sauvegarder l'image corrigée
sauvegarder_image(matrice_corrigee, size, output_path)

# Calculer le taux moyen d'erreurs résiduelles
taux_moyen_erreurs = np.mean(erreurs_residuelles)
print(f"Taux moyen d'erreurs résiduelles : {taux_moyen_erreurs:.2f}%")


