def tobase2(n):
    liste = []
    while n != 0:
        liste = [n%2] + liste
        n = n // 2
    return liste
#print(tobase2(25))

def tobase2(n):
    liste = []
    while n != 0:
        liste = [n&1] + liste
        n = n >> 1
    return liste
#print(tobase2(25))

def tobase(n, b):
    liste = []
    while n != 0:
        liste = [n%b] + liste
        n = n // b
    return liste
#print(tobase(25, 3))

def hammingweight(n):
    poids = 0
    while n != 0:
        if n&1 == 1:
            poids += 1
        n = n >> 1
    return poids
#print(hammingweight(25))

def hammingweight2(n):
    poids = 0
    while n != 0:
        n = n&(n-1)
        poids += 1
    return poids
#print(hammingweight2(25))

def base2int(L, b):
    nbre = 0
    i = 0
    p = len(L) - 1
    while i < len(L):
        nbre = nbre + L[i] * pow(b, p)
        p -= 1
        i += 1
    return nbre
#print(base2int([3,2,1], 5))

def multbyalpha(b, f):
    new_f = len(bin(f)) - 3
    y = b << 1
    if (y & (1 << new_f)) != 0:
        y = y ^ f
    return y
#print(mulbyalpha(8,19))