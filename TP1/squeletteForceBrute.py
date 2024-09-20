#************************************************************************************
#  TP1 : chiffrement par fonction affine et force brute
#  Noms : 
#  Groupe : 
#  Date :
#  Bilan  d'avancement :
#************************************************************************************
import time
import operator

#*******************************************************************************************
# fonction qui lit un fichier texte et qui renvoie
# son contenu sous forme d'une chaine de caractères. Le nom du fichier est passé en paramètre
# sous forme d'une chaîne de caractères
#*******************************************************************************************
def litFichier(nomFich):
    try:
        f=open(nomFich,"r")
        ch=f.read()
        f.close()
        return ch
    except IOError:
        print ("impossible d'ouvrir  " ,nomFich)


############### variables globales """"""""""""""""""""""""
gl_dicoFrancais=[]  # liste de chaines qui contiendra les mots français 
#************************************************************************************
#  calcul du pgcd de deux nombres  version itérative
#  2 paramètres :les deux nombres entiers 
#  valeur retournee : le pgcd des deux nombres
#************************************************************************************
def pgcd(a,b) :
    while a%b!=0:
        a,b=b, a%b
    return b 

a=12 
b=18
print(pgcd(a,b))


#************************************************************************************
#  calcul du pgcd de deux nombres  version recursive
#  2 paramètres :les deux nombres
#  valeur retournee : le pgcd des deux nombres
#************************************************************************************
def pgcdRec(a,b) :
    if a%b == 0:
        return b
    else:
        return pgcdRec(b, a%b)

#************************************************************************************
#  def bezoutIt(a, b) :
    r, R, u, U, v, V = a, b, 1, 0, 0, 1
    while r > 0:
        q = r//R
        r, R, u, U, v, V = R, r%R, U, u - q*U, V, v - q*V
    return (u, v)
#************************************************************************************
def bezoutIt(a, b):
    r, R, u, U, v, V = a, b, 1, 0, 0, 1
    while R > 0:
        q = r // R
        r, R = R, r % R
        u, U = U, u - q * U
        v, V = V, v - q * V
    return (u, v)

    
#************************************************************************************
#  commentaire à compléter
#************************************************************************************
def bezoutRec(a, b) :
    if a%b == 0:
        return (0, 1)
    else: 
        r, q = a%b, a//b
        u, v = bezoutRec(b, r)
        return(v,u - v*q)

#************************************************************************************
#  commentaire à compléter
#************************************************************************************
def inverseModulaireNaif(a, n) :
    while a*b == 1%n:
        b = b+1
    return b

#************************************************************************************
#  l'inverse modulaire et le x qu'on recherche pour que quand on divise notre a*x par n pour obtenir 1 ce qui confirme qu'ils sont bien premiers entre eux
# a*x≡1 (mod n)
# 3*x≡1 (mod 7) /// 3*x≡15 (mod 7) /// 15%7=1 donc x=5
# pour absolument avoir l'inverse modulaire il faut PGCD(a,n)=1
# utiliser les coef de bezout pour touver le x et y dans : a*x+n*y=PGCD(a,n)
#************************************************************************************
def inverseModulaire(a, n) :
    def bezout(a, b):
        if b == 0:
            return a, 1, 0
        else: 
            d, x1, y1 = bezout(b, a % b)
            x = y1
            y = x1 - (a // b) * y1
            return d, x, y
    d, x, y = bezout(a, n)
    if d != 1:
        raise ValueError("Pas d'inverse modulaire")
    return x % n

#************************************************************************************


# TEST INVERSE MODULAIRE
am, nm = 3, 29
im = inverseModulaire(am, nm)
print(am, nm,  im)

# TEST INVERSE MODULAIRE NAIF
a, n  = 3, 29
i = inverseModulaireNaif(a, n)
print(a, n,  i)


#************************************************************************************************************************************
# contruction fonction de chiffrage (ou de déchiffrage) monoalphabétique affine   
# 3 parametres :    3 éléments a,b,n déterminant la fonction de chiffrage f(x)=(a*x+b)%n
#                   où x est le rang dans l'alphabet. Seuls sont chiffrés les caractères alphanumériques qui seront transformés en
#                   majuscule avant chiffrage. Les caractères non alphabétiques sont chiffrés par un espace.
# valeur retournée: la fonction de chiffrage qui prendra le caractère à chiffrer comme paramètre
#
# exemple : fonctChiffreCarAffine(8,15,26)('A') doit retourner le chiffrage de la lettre 'A' par la clef de chiffrage affine f(x) = 8x + 15 (modulo 26)
#
#***********************************************************************************************************************************
def fonctChiffreCarAffine(a,b,n):
    def fonctAffine (car):
        #.............................
        # à completer par vos soins
        #.............................
        return
    return fonctAffine

#************************************************************************************
#  charge le dictionnaire francais sous forme d'une liste de chaines de caractères
#  dans la variable globale gl_dicoFrancais
#************************************************************************************
def chargeDicoFrancais ():
    global gl_dicoFrancais
       # a completer
#********************************************************************************************
# recherche si un mot est dans le dictionnaire supposé être dans la variable
# globale gl_dicoFrancais et  renvoie True si c'est le cas et False dans le cas contraire
#*********************************************************************************************
def estMotFrancais (mot):
      # a completer
      return

#********************************************************************************************
# à compléter
#*********************************************************************************************
def pourcentageMotsFrancaisReconnus(chain) :
    return


#********************************************************************************************
# programme  principal qui essaie sur un message chiffré tous les codes affines possibles
# qui détermine le meilleur et affiche pour ce code le message déchiffré , la fonction
# utilisée pour le déchiffrer ainsi que la fonction ayant permis le chiffrement. On affichera
# aussi le temps qui a été nécessaire au déchiffrement
#*********************************************************************************************
   # à compléter