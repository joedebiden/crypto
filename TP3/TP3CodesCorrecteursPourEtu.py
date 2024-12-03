#************************************************************************************
#  Maths Info 2 TP3 :
#  Detection et correction d'erreurs par bit de parité 
#  Noms : PERISSET HUGUES
#  Groupe : TP1 H
#  Date : 8/11/24
#  Bilan  d'avancement : 
#************************************************************************************

from numpy import *
from matplotlib.pylab import *
from imread import *
from random import *
from numpy import *
from imread import *
from random import *
#************************************************************************************
# Pour prendre en main les tableaux (array) 
#************************************************************************************
# lit le fichier image (noir et blanc) et le renvoie sous forme d'une matrice de booleens.
fleur=imread('floral.TIF')
# Directement à la  console faites afficher fleur, fleur[0], len (fleur) et len (fleur[0]) et donnez leur
# signification en regardant la taille de l'image dans le gestionnaire de fichier windows

# pour créer une matrice de 4 lignes et 3 colonnes remplie de "False".
x=zeros ((4,3),dtype=bool)
print(x)
   
# affichez directement x à la console
#puis faire   x[1,2]=2   
# et afficher x de nouveau
#on peut aussi écrire  x[1][2]  à la place de x[1,2] 
# faites x[1]=[1,1,1] puis affichez x. Que constatez vous ?
#  que va afficher  x[1:3]  et  x[1][0:2] ?
#  que fait x[1:3]=[[0,0,1],[1,0,0]] ?
#Question I.1
#************************************************************************************
#  Fonction simulant par  bruitage la transmission d'une liste de booléens
#  entree listebool  : une liste de booleens 
#  entree p : probabilité d'erreur
#  valeur reournee : la liste de booleens bruitée

# Cette fonction permet transformer une ligne avec en parametre vectBool les pixels et p la proba de corruption
def transmettreVectBool(vectBool, p):
    vectSortie = zeros(len(vectBool), dtype=np.uint8)
    
    for i in range(len(vectBool)):
        if random() < p: 
            vectSortie[i] = not vectBool[i]
        else:
            vectSortie[i] = vectBool[i]
    
    return vectSortie

#************************************************************************************

## Question I.2
#************************************************************************************
#  Fonction simulant par  bruitage la transmission  d'une matrice (array) de booéens
#  entree mb  : une matrice de booleens 
#  entree p : probabilité d'erreur
#  valeur reournee : la matrice de booleens bruitée
#************************************************************************************
def transmettreMatrice(matriceBool, p):
    nouvelleMatrice = zeros(matriceBool.shape, dtype=np.uint8)
    for i in range(matriceBool.shape[0]):
        nouvelleMatrice[i] = transmettreVectBool(matriceBool[i], p)
    return nouvelleMatrice

## Question I.3                        
p=0.01
fleur=imread('floral.TIF')
imshow(fleur)
show()
fleurB=transmettreMatrice(fleur,p)
imsave("fleurB.tif",fleurB*255)
imshow(fleurB)
# show()
##afficher ensuite la fleur bruitée                      
##show(imshow(fleurBruite))
## vous afficherez l'image bruitee
##créez une fonction calculant le taux d'erreur 
##print ("taux erreurs" ,tauxErreurs(fleur,fleurBruite))    

## Question I.4            
def tauxErreurs(fleur, fleurB):
    differences = sum(fleur != fleurB)
    total_pixels = fleur.size
    taux_erreur = differences / total_pixels
    return taux_erreur

# print(tauxErreurs(fleur, fleurB))   


## II. Contrôle de parité simple
## Question II.1
#******************************************************************************************************************
#  Fonction calculant un bit de parite paire sur une liste de booleen et le rajoutant à la fin de la liste
#  entree  listebool : une liste de booléens
#  valeur retournée :d la liste entrée plus le bit de parité paire placé à la fin e la liste
#  tenez compte du fait que pour l'addition True vaut 1 et False 0  True+True=2  True+False=1  True+True+True =3 etc ..
#  utilisez la fonction sum (liste)  qui fait la somme des termes d'une liste
#  valider avec  x=array ([[0,1,0,1,0]],dtype=bool)
#************************************************************************************************************************
def controlPar(listebool):
        
    somme = sum(listebool)
    listebool.append(somme %2)
    return listebool


# print(controlPar([1,1,1,0]))





## Question II.2
#***************************************************************************************************************************
# ajout du bit de parité 
# simuler transmission erreur 
# check erreur de parité
# récupérer résultat corompu (avec erreur sur le bit de parité)
# re simuler pour renvoyer le vecteur 
#******************************************************************************************************************************
def transBlocParite(vectbool, p):
    ajout_bit = controlPar(list(vectbool)) #ajout bit paritématriceBool
    gen_erreur = transmettreVectBool(ajout_bit, p) #transmittion avec % erreurs
    
    # check l'erreur, si le total des bits et impair alors refaire la transmition 
    while sum(gen_erreur)%2==1:
        print(f"L'erreur: {gen_erreur}")
        gen_erreur = transmettreVectBool(ajout_bit, p)
        
    print(f"Bonne transmission: {gen_erreur}")
    return gen_erreur[0:-1]
 

# print(transBlocParite([0,1,1,1], 0.5))



## Question II.3
#*********************************************************************************************************************************
#  Fonction restituant, à partir d'une matrice de booleens dont chaque groupe de 4 éléments est complété par un bit de parité paire,
#   la matrice d'origine sans bit de parité
#  entree  mb : une matrice de booléens avce bits de parité paire
#  valeur retournée : la matrice de booléens en entrée mais sans les bits de parité
#******************************************************************************************************************************

def transMatriceParite(mb,p):
    nouvelleMatrice = zeros(shape(mb), dtype=np.uint8)
    for i in range(len(mb)):
        for j in range(0, len(mb[i]), 4):
            nouvelleMatrice[i, j:j+4] = transBlocParite(mb[i, j:j+4], p)
    return nouvelleMatrice

test = transMatriceParite(fleur, 0.3)
imshow(test)
show()
imsave("floral_corriged.tif", test*255)

