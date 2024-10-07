'''
Choose 2 prime number (p and q) 
Compute n = pq (n is modulos and express the key lenght)
Carmichael function 
Choose integer 1 < e < lambda(n) and  pgcd(e, lambda(n)) = 1  now e and lamdba(n) are co-prime
determine d as d ≡ e^1 
'''


def wordToNumber(mot):
    num = 0
    i=0
    for lettre in mot[::-1]:
        num+=(ord(lettre)-65+1)*26**i
        i+=1
    return num - 1


print(wordToNumber("AA"))


