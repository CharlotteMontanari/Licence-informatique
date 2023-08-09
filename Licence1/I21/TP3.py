from math import *

def bit(n,i):
    if n & (1<<i):
        return 1
    else:
        return 0
# print(bit(10,4))

def set_bit(x,i,val):
    if val == 1:
        return (x | val<<1)
    else:
        return (x & (~(val<<i)))
# print(set_bit(19,3,1))

def pop_count(x):
    somme = 0
    l = bin(x)
    for chiffre in str(l):
        if chiffre == '1':
            somme += 1
    return somme
# print(pop_count(19))

def expo_gd(x,k):
    liste = []
    if k == 0:
        return 1
    p = 1
    l = floor((log(k))/log(2)) + 1
    for i in range(l-1, -1, -1):
        p = p * p
        liste += [p]
        if bit(k,i):
            p = p * x
            liste += [p]
    return liste
# print(expo_gd(2,6))

def expo_dg(x,k):
    if k == 0:
        return 1
    l = [1]
    p = 1
    ll = floor((log(k))/log(2)) + 1
    for i in range(ll):
        l += [x]
        if bit(k,i):
            p = p * x
            l += [p]
        x = x * x
    return l
# print(expo_dg(3,5))

def fibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        liste = [0,1]
        for i in range(n):
            liste += [liste[-1] + liste[-2]]
    return liste[n]
# print(fibo(10))

def matmult(m1, m2):
    return [[m1[0][0] * m2[0][0] + m1[0][1] * m2[1][0],
             m1[0][0] * m2[0][1] + m1[0][1] * m2[1][1]],
            [m1[1][0] * m2[0][0] + m1[1][1] * m2[1][0],
             m1[1][0] * m2[0][1] + m1[1][1] * m2[1][1]]]
# print(matmult([[1,2], [1,2]], [[1,2], [1,2]]))

def matcarre(m):
    return [[m[0][0] * m[0][0] + m[0][1] * m[1][0],
             m[0][0] * m[0][1] + m[0][1] * m[1][1]],
            [m[1][0] * m[0][0] + m[1][1] * m[1][0],
             m[1][0] * m[0][1] + m[1][1] * m[1][1]]]
# print(matcarre([[1,2], [1,2], [1,2], [1,2]]))

def fibo2(n):
    p = [[1,0],[0,1]]
    x = [[1,1],[1,0]]
    for i in range(floor(log(n)/log(2)), -1, -1):
        p = matcarre(p)
        if bit(n,i):
            p = matmult(p,x)
    return p[0][1]
# print(fibo2(10))