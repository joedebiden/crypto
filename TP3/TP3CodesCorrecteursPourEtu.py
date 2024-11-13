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
fleur=imread('floral.tif')
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
    vectSortie = np.zeros(len(vectBool), dtype=np.uint8)
    
    for i in range(len(vectBool)):
        if np.random.rand() < p:
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
    nouvelleMatrice = np.zeros(matriceBool.shape, dtype=np.uint8)
    for i in range(matriceBool.shape[0]):
        nouvelleMatrice[i] = transmettreVectBool(matriceBool[i], p)
    return nouvelleMatrice

## Question I.3                        
p=0.01
fleur=imread('floral.tif')
imshow(fleur)
show()
fleurB=transmettreMatrice(fleur,p)
imsave("fleurB.tif",fleurB*255)
imshow(fleurB)
show()
##afficher ensuite la fleur bruitée                      
##show(imshow(fleurBruite))
## vous afficherez l'image bruitee
##créez une fonction calculant le taux d'erreur 
##print ("taux erreurs" ,tauxErreurs(fleur,fleurBruite))    

## Question I.4            
def tauxErreurs(fleur, fleurB):
    if fleur.shape != fleurB.shape:
        raise ValueError("not the same size!")
    differences = np.sum(fleur != fleurB)
    total_pixels = fleur.size
    taux_erreur = differences / total_pixels
    return taux_erreur

print(tauxErreurs(fleur, fleurB))   





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
  # à compléter

    return 
## Question II.2
#***************************************************************************************************************************

#******************************************************************************************************************************
def transBlocParite(mb):
   # à compléter
    return 

## Question II.3
#*********************************************************************************************************************************
#  Fonction restituant, à partir d'une matrice de booleens dont chaque groupe de 4 éléments est complété par un bit de parité paire,
#   la matrice d'origine sans bit de parité
#  entree  mb : une matrice de booléens avce bits de parité paire
#  valeur retournée : la matrice de booléens en entrée mais sans les bits de parité
#******************************************************************************************************************************
def transMatriceParite(mb):
   # à compléter
    return 


## Question II.5
#********************************************************************************************************
#  Fonction calulant le taux des differences (dues aux erreurs de transmission)?Ce sera un nombre entre 0 et 1
#  entre deux matrices booléennes
#  entree mb1  : une matrice de booleens 
#  entree mb2  : une matrice de booleens
#  valeur retournee : pourcentage de differences entre les  2 matrices
#  precondition : les 2 matrices seront de même taille (même nombre de lignes, même nombre de colonnes)
#*********************************************************************************************************
def tauxErreurs(mb1,mb2):
   #à compléter



    return 



#

