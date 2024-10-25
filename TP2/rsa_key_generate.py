'''
Choose 2 prime number (p and q) 
Compute n = pq (n is modulos and express the key lenght)
create e [est un entier en premier avec (p-1)x(q-1) donc le pgcd (e, (p-1)x(q-1)) = 1 ]
clé publique : (n,e)
partie chiffrage :       chiffrage
    nombre x non chiffré ==========> x^e (mod n)

partie dechiffrage :
    clé secrete : (n,d) ou d est l'inverse modulaire de e modulo (p-1)x(q-1)
     déchiffrage
    y =======> (y^d) (mod n)
'''
import random
from math import gcd

def wordToNumber(mot):
    num = 0
    i=0
    for lettre in mot[::-1]:
        num+=(ord(lettre)-65+1)*26**i
        i+=1
    return num - 1

def numberToWord(n):
    mot = ""
    while n>=0:
        mot = chr(n%26+65)+mot
        n = n//26-1
    return mot


''' === test convertion ===
mot = "CHARENSOL"
encrypted = wordToNumber(mot)
deencrypted = numberToWord(encrypted)
print(mot)
print(encrypted)
print(deencrypted)
'''

# to do
p = int(578686194785252290248347697089)
q = int(236369746748300413097241111169)
n=p*q
def testCoprime(n):
    e = (p-1)*(q-1)
    e = random.randint(2, n - 1)
    if gcd(e, n) == 1:
        return True
    else :
        return False

print(testCoprime(n))

def puiMod(x,e,n):
    if e==0:
        return 1
    if e==1:
        return x
    else:
        if e % n ==0:
            b = x^(e/2)%n
            return b*b%n 
        else:
            b = x^((e-1)/2)%n
            return b*b*x%n
        
def chiffreRSA(n,e,liste):
    return null
    


'''

secret = (p - 1) * (q - 1)
e = findCoprime(secret)
clef_publique = n, e

print(f"Vos chiffres top secrets : \np={p} \nq={q} \nn={n}")
print(f"Valeur de e : {e}")
print(f"Votre clef publique : {clef_publique}")

liste = input("Entrez votre message à chiffrer : ")
liste = wordToNumber(liste)
print(f"Votre message chiffré est : {message**e % n}")
# fonction cryptage
def cryptageRSA(n, e, liste):

cryptageRSA(e, n)
'''


# bezout pour l'inverse modulaire
def bezoutRec(p, q) :
    if p%q == 0:
        return (0, 1)
    else:
        r, q = p%q, p//q
        u, v = bezoutRec(p, r)
        return(v,u - v*q)



