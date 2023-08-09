def norme(M):
    maxi = 0
    i = 0
    while i < len(M[0]):
        j = 0
        somme = 0
        while j < len(M):
            somme += abs(M[j][i])
            j += 1
        if maxi < somme:
            maxi = somme
        i += 1
    return maxi
#print(norme([[1,2,3], [4,5,6], [7,8,9], [10,11,12]]))

def poids(entier):
    somme = 0
    while entier != 0:
        if entier % 2 == 1:
            somme += 1
        entier = entier // 2
    return somme
#print(poids(17))

def prod_mat_vec_F2(M, V):
    chiffre = 0
    for el in range(len(M)):
        nbre = M[el] & V
        chiffre = chiffre | (poids(nbre) & 1)
        chiffre = chiffre << 1
    return chiffre >> 1
#print(prod_mat_vec_F2([9, 15, 5], 7))

import copy
def gencirculante(L):
    new_l = L.copy()
    liste = [new_l] + [0]*(len(L)-1)
    for el in range(1, len(L)):
        liste[el] = [new_l[-1]] + new_l[:-1]
        new_l = liste[el].copy()
    return liste
#print(gencirculante([1, 2, 3, 4]))

def circmultvec(V, Y):
    W = [0] * len(V)
    modulo = len(V)
    i = 0
    while i < len(V):
        somme = 0
        j = 0
        nbre = (modulo-i) % modulo
        while j < len(Y):
            somme += V[nbre] * Y[j]
            j += 1
            nbre = (nbre + 1) % modulo
        W[i] = somme
        i += 1
    return W
#print(circmultvec([1,2,3], [4,5,6]))

def gen_circulante2(k, t):
    liste = [9]
    i = t
    while i > 0:
        nbre = k & 1
        k = k >> 1
        k = k | (nbre << 1)
        liste += [k]
        i -= 1
    return liste
#print(gen_circulante2(9, 4))