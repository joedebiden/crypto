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

def findCoprime(secret):
    while True:
        e = random.randint(2, secret - 1)
        if gcd(e, secret) == 1:
            return e

p = int(578686194785252290248347697089)
q = int(236369746748300413097241111169)
n = p*q
print(f"Vos chiffres top secrets : \np={p} \nq={q} \nn={n}")
secret = (p - 1) * (q - 1)
e = findCoprime(secret)

print(f"Valeur de e : {e}")
clef_publique = n, e
print(f"Votre clef publique : {clef_publique}")

# fonction cryptage
def cryptageRSA():
    message = input("Entrez votre message à chiffrer : ")
    message = wordToNumber(message)
    print(f"Votre message chiffré est : {message**e % n}")

cryptageRSA()







# bezout pour l'inverse modulaire
def bezoutRec(p, q) :
    if p%q == 0:
        return (0, 1)
    else:
        r, q = p%q, p//q
        u, v = bezoutRec(p, r)
        return(v,u - v*q)



