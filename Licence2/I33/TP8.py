import random

def gentrianginf_inv(n, t):
    liste = [0]*n
    i = 0
    while i < n:
        liste[i] = [0]*n
        j = 0
        while j < i+1:
            nbre = random.randint(1, t-1)
            liste[i][j] = nbre
            j += 1
        i += 1
    return liste
#print(gentrianginf_inv(4, 7))

def transpose(M):
    liste = []
    for i in range(len(M[0])):
        liste = liste + [[0]*len(M)]
        for j in range(len(M)):
            liste[i][j] = M[j][i]
    return liste

def gentriangsup_inv(n, t):
    return transpose(gentrianginf_inv(n, t))
#print(gentrianginf_inv(4,7))

def genmatrix_inv(n):
    nbre = random.randint(10, 100)
    mat_inf = gentriangsup_inv(n, nbre)
    mat_sup = transpose(gentriangsup_inv(n, nbre))
    liste = [0] * len(mat_inf)
    el = 0
    while el < len(liste):
        liste[el] = [0] * len(mat_sup[0])
        j = 0
        while j < len(liste[0]):
            i = 0
            somme = 0
            while i < len(mat_inf[0]):
                somme += mat_inf[el][i]*mat_sup[i][j]
                i += 1
            liste[el][j] = somme
            j += 1
        el += 1
    return liste
#print(genmatrix_inv(4))

def gauss(a):
    i = 0
    while i < len(a) - 1:
        j = i + 1
        while j < len(a):
            for el in range(len(a[0])):
                a[j][el] = a[i][i]*a[j][el] - a[j][i]*a[i][el]
            j += 1
        i += 1
    for i in a:
        print(i)
mat = [[3,1,2],[1,2,0],[2,3,1]]
#print(gauss(mat))

def is_LU(A,L,U):
    i = 0
    flag = True
    while i < len(L) and flag:
        j = 0
        while j < i+1:
            if L[i][j] == 0:
                flag = False
            j += 1
        i += 1
    i = 0
    while i < len(U) and flag:
        j = i+1
        while j < len(U):
            if L[j][i] == 0:
                flag = False
            j += 1
        i += 1
    liste = [0] * len(L)
    el = 0
    while el < len(liste):
        liste[el] = [0] * len(U[0])
        j = 0
        while j < len(liste[0]):
            i = 0
            somme = 0
            while i < len(L[0]):
                somme += L[el][i]*U[i][j]
                i += 1
            liste[el][j] = somme
            j += 1
        el += 1
    for er in range(len(liste)):
        for et in range(len(liste)):
            if liste[er][et] != A[er][et]:
                flag = False
    return flag
a = [[1, 2, 3, 4], [1, 6, 9, 12], [1, 6, 18, 24], [1, 6, 18, 40]]
l = [[1,0,0,0],[1,2,0,0],[1,2,3,0],[1,2,3,4]] 
u = [[1,2,3,4],[0,2,3,4],[0,0,3,4],[0,0,0,4]]
#print(is_LU(a,l,u))

def est_inversible(L,U):
    pivot = 0
    while L[pivot][pivot] != 0 and U[pivot][pivot] != 0 and pivot < len(L):
        pivot += 1
        return True
    return False
