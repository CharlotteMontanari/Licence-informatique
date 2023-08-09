import random
from TP4 import *

def genmatrix(n, p, t):
    liste = [0] * n
    for i in range(0, n):
        liste[i] = [0] * p
    return liste
#print(genmatrix(2, 3, 7))

def gendiag(n, t):
    alea = random.randint(0, t)
    liste = [0] * n
    for i in range(0, n):
        liste[i] = [0] * n
        liste[i][i] = alea
    return liste
#print(gendiag(4, 10))

def gentrianginf(n, t):
    liste = [0] * n
    for i in range(n):
        liste[i] = [0] * n
        for el in range(i):
            liste[i][el] = random.randrange(0, t)
    return liste
#print(gentrianginf(4, 7))

def gensym(n, t):
    prog = gentrianginf(n, t)
    for i in range(n):
        for j in range(i):
            prog[i][j] = prog[j][i]
    return prog
#print(gensym(4, 10))

def transpose(M):
    liste = []
    for i in range(len(M[0])):
        liste = liste + [[0]*len(M)]
        for j in range(len(M)):
            liste[i][j] = M[j][i]
    return liste
#print(transpose([[1, 2, 3], [4, 5, 6]]))

def gentriangsup(n, t):
    g = gentrianginf(n, t)
    return transpose(g)
#print(gentriangsup(4, 7))

def matmat(A, B):
    liste = [0] * len(A)
    el = 0
    while el < len(liste):
        liste[el] = [0] * len(B[0])
        j = 0
        while j < len(liste[0]):
            i = 0
            somme = 0
            while i < len(A[0]):
                somme += A[el][i]*B[i][j]
                i += 1
            liste[el][j] = somme
            j += 1
        el += 1
    return liste
l = [[2,3,1,4],[0,1,2,3],[4,1,5,1],[1,2,5,1]] 
u = [[1,2,3,4],[0,2,3,4],[0,0,3,4],[0,0,0,4]]
print(matmat(l, u))

def matvec(M, V):
    el = 0
    liste = [0] * len(M)
    while el < len(liste):
        i = 0
        somme = 0
        while i < len(V):
            somme += M[el][i] * V[i]
            i += 1
        liste[el] = somme
        el += 1
    return liste
#print(matvec([[2, 1, 2], [2, 1, 2], [2, 1, 0]], [1, 0, 2]))

def matmat(A, B, P):
    liste = [0] * len(A)
    el = 0
    while el < len(liste):
        liste[el] = [0] * len(B[0])
        j = 0
        while j < len(liste[0]):
            i = 0
            somme = 0
            while i < len(A[0]):
                somme = somme ^ multiplie(A[el][i], B[i][j], P)
                i += 1
            liste[el][j] = somme
            j += 1
        el += 1
    return liste
#print(matmat([[14, 8, 9], [0, 4, 12], [12, 10, 12]], [[11, 12, 8], [7, 8, 15], [4, 9, 5]], 19))