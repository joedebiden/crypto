#************************************************************************************
#  TP1 : chiffrement par fonction affine et force brute
#  Noms : 
#  Groupe : 
#  Date :
#  Bilan  d'avancement :
#************************************************************************************
import time 
from time import perf_counter
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
    b = 1 
    while (a*b) %n != 1 :
        b = b+1
        #print(b)
    return b

#************************************************************************************
#  l'inverse modulaire et le x qu'on recherche pour que quand on divise notre a*x par n pour obtenir 1 ce qui confirme qu'ils sont bien premiers entre eux
# a*x≡1 (mod n)
# 3*x≡1 (mod 7) /// 3*x≡15 (mod 7) /// 15%7=1 donc x=5
# pour absolument avoir l'inverse modulaire il faut PGCD(a,n)=1
# utiliser les coef de bezout pour touver le x et y dans : a*x+n*y=PGCD(a,n)
#************************************************************************************
a = 5
b = 221
def inverseModulaire(a, n) :
    def bezout(a, b):
        if b == 0:
            return a, 1, 0
        else: 
            d, x1, y1 = bezout(b, a % b)
            x = y1
            y = x1 - (a // b) * y1
            #print(d, x, y)
            return d, x, y
    d, x, y = bezout(a, n)
    if d != 1:
        raise ValueError("Pas d'inverse modulaire")
    return x % n
print(inverseModulaire(a,b))
c = (33**77) % 221
print(c)

#************************************************************************************
# TEST de la fonction inverseModulaire NAIF vs RECURSIVE
'''
a = 5452322311
n = 21435323131231

t2_start = perf_counter()
inverseModulaire(a, n)
t2_stop = perf_counter()

t1_start = perf_counter()
inverseModulaireNaif(a, n)
t1_stop = perf_counter()

print("inverseModulaireNaif : ", t1_stop-t1_start, "\ninverseModulaire :", t2_stop-t2_start)
print("inverseModulaire avec la recursivité est trop fast")
'''

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
    def fonctAffine(car):
        if 'A' <= car <= 'Z':
            return chr((a * (ord(car) - ord('A')) + b) % n + ord('A'))
        else:
            return car  # Ne pas chiffrer les caractères non alphabétiques
    return fonctAffine

# ============= test de la fonctChiffreCarAffine =============
#f = fonctChiffreCarAffine(8, 15, 26)
#print("A B C D E F G H I J K L M N O P Q R S T U V W X Y Z")
#print(f('A'), f('B'), f('C'), f('D'), f('E'), f('F'), f('G'), f('H'), f('I'), f('J'), f('K'), f('L'), f('M'), f('N'), f('O'), f('P'), f('Q'), f('R'), f('S'), f('T'), f('U'), f('V'), f('W'), f('X'), f('Y'), f('Z'))


#************************************************************************************
#  charge le dictionnaire francais sous forme d'une liste de chaines de caractères
#  dans la variable globale gl_dicoFrancais
#************************************************************************************
def chargeDicoFrancais ():
    global gl_dicoFrancais
    with open('dictionnaire.txt', 'r') as f:
        gl_dicoFrancais = f.read().splitlines()

#chargeDicoFrancais()  #// je le charge déjà dans la derniere fonction 
#print(gl_dicoFrancais[100:200])

#********************************************************************************************
# recherche si un mot est dans le dictionnaire supposé être dans la variable
# globale gl_dicoFrancais et  renvoie True si c'est le cas et False dans le cas contraire
#*********************************************************************************************
def estMotFrancais (mot):
    mot = mot.upper()
    if mot in gl_dicoFrancais:
        return True
    else: 
        return False

#choix = input("Entrez un mot : ")
#print(estMotFrancais(choix))

#********************************************************************************************
# à compléter
#*********************************************************************************************
def pourcentageMotsFrancaisReconnus(chain) :
    mots = chain.split()
    if len(mots) == 0:
        return 0
    pourcMot = sum(1 for mot in mots if estMotFrancais(mot))
    return (pourcMot/len(mots))*100


#********************************************************************************************
# programme  principal qui essaie sur un message chiffré tous les codes affines possibles
# qui détermine le meilleur et affiche pour ce code le message déchiffré , la fonction
# utilisée pour le déchiffrer ainsi que la fonction ayant permis le chiffrement. On affichera
# aussi le temps qui a été nécessaire au déchiffrement
#*********************************************************************************************
def forceBruteChiffrementAffine (messageChiffre, n=26):
    meilleurPourcentage = 0
    meilleurMessage = ""
    meilleurFonction = None
    meilleurTemps = 0
    chargeDicoFrancais()
    
    for a in range(1, n):
        if pgcd(a, n) == 1:
            for b in range(n):
                try:
                    a_inv = inverseModulaire(a, n)
                except ValueError:
                    continue

                dechiffreCarAffine = fonctChiffreCarAffine(a_inv, -a_inv*b, n)
                start_time = time.perf_counter()
                messageDechiffre = "".join(dechiffreCarAffine(car) for car in messageChiffre)
                end_time = time.perf_counter()
                pourc = pourcentageMotsFrancaisReconnus(messageDechiffre)

                if pourc > meilleurPourcentage:
                    meilleurPourcentage = pourc
                    meilleurMessage = messageDechiffre
                    meilleurFonction = dechiffreCarAffine
                    meilleurTemps = end_time - start_time
    
    print(f"Meilleur message : {meilleurMessage}")
    print(f"Meilleur pourcentage : {meilleurPourcentage}")
    print(f"Meilleur temps : {meilleurTemps}")
    print(f"Meilleur fonction : {meilleurFonction}")

#************************************************************************************
#  TEST de la fonction forceBruteChiffrementAffine

#messageChiffre = litFichier("messageChiffreAffine1.txt")
#forceBruteChiffrementAffine(messageChiffre)

#************************************************************************************
# messageChiffreAffine2.txt
chaine = litFichier("messageChiffreAffine2.txt")
def nbMotsFrancaisReconnusSansSepar(chaine):
    chargeDicoFrancais()
    
    Mot = chaine[0:10]
    CheckMot = fonctChiffreCarAffine(Mot)
    CompareDico = estMotFrancais(Mot) 
    
    X = 10
    while Mot != CompareDico is True:
        CheckMot(Mot)
        X = 10 - 1

    
        

nbMotsFrancaisReconnusSansSepar(chaine)