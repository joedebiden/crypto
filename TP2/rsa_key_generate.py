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
p = int(5786878)
q = int(234830)
n=p*q
def testPrime(n):
    miaouw = (p - 1) * (q - 1)
    e = random.randint(2, miaouw - 1)
    if gcd(e, miaouw) == 1:
        return True
    else:
        return False

def aleaE(p, q):
    e = random.randint(2, (p-1)*(q-1))
    while gcd(e, (p-1)*(q-1)) != 1:
        e = random.randint(2, (p-1)*(q-1))
    return e

    

def puiMod(x, e, n):
    if e == 0:
        return 1
    if e == 1:
        return x % n
    if e % 2 == 0:
        b = puiMod(x, e // 2, n)
        return (b * b) % n
    else:
        b = puiMod(x, (e - 1) // 2, n)
        return (b * b * x) % n
        

def chiffreRSA(n,e,liste):
    list_num = []
    list_crypt = []
    list_result = []

    for mot in liste:
        list_num.append(wordToNumber(mot))


    for num in list_num:
        list_crypt.append(puiMod(num, e, n))


    for num in list_crypt:
        list_result.append((numberToWord(num)))
    return list_result

        
    

liste = ["ACHETEZ", "MES", "KINDER", "ILS", "SONT", "A", "UN", "EURO"]
e=aleaE(p,q)
print(chiffreRSA(n, e, liste))




# bezout pour l'inverse modulaire
def bezoutRec(p, q) :
    if p%q == 0:
        return (0, 1)
    else:
        r, q = p%q, p//q
        u, v = bezoutRec(p, r)
        return(v,u - v*q)



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

d=inverseModulaire(e, (p-1)*(q-1))
print(chiffreRSA(n, d, chiffreRSA(n, e, liste)))