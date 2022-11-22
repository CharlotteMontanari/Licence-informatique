from math import sin, cos
from time import time
from random import randrange
import random

def intervalle(a, b, inc):
    inter = []
    while a <= b:
        inter += [a]
        a += 0.2
    return inter
# print(intervalle(0, 1, 0.2))

def valeur_sin(t):
    sinus = []
    for el in t:
        sinus += [sin(el)]
    return sinus
# print(valeur_sin(intervalle(0, 1, 0.2)))

def valeur_cos(t):
    cosinus = []
    for el in t:
        cosinus += [cos(el)]
    return cosinus
# print(valeur_cos(intervalle(0, 1, 0.2)))

def multiplication_cha(n1, n2):
    liste = []
    nbre = n1 * n2
    while nbre != 0:
        nbre1 = nbre % 10
        liste += [nbre1]
        nbre = nbre // 10
    return liste
# print(multiplication_cha(1676, 4))

def multiplication(n1, n2):
    n3 = [0] * len(n1) * 2
    j = 0
    while j < len(n1):
        i = 0
        r = 0
        while i < len(n1):
            p = n3[i + j] + n1[i] * n2[j] + r
            n3[i + j] = p % 10
            r = p // 10
            i += 1
        n3[i + j] = r
        j += 1
    return n3
# print(multiplication([6], [4]))

def time_mult_py(n, k):
    lim = 10**n
    test = []
    for i in range(k):
        n1 = randrange(lim)
        n2 = randrange(lim)
        test += [(n1, n2)]
    start = time()
    for n1, n2 in test:
        n3 = n1 * n2
    end = time()
    print(end - start)
# print(time_mult_py(20, 1000))

def nombre_alea(n):
    alea = []
    for i in range(0, n):
        alea += [random.randint(0, 9)]
    return alea
# print(nombre_alea(5))

def time_my_mult_py(n, k):
    i = 0
    start = time()
    while i < k:
        a = multiplication(nombre_alea(n), nombre_alea(n))
        i += 1
    end = time()
    return (end-start)
# print(time_my_mult_py(20, 1000))

def time_plus(n, k):
    liste = []
    start = time()
    for i in range(n, k, 2):
        liste = liste + [i]
    end = time()
    return (end-start)
# print(time_plus(1, 10))

def time_inc(n, k):
    liste = []
    start = time()
    for i in range(n, k, 2):
        liste += [i]
    end = time()
    return (end-start)
# print(time_inc(1, 10))

def time_append(n, k):
    liste = []
    start = time()
    for i in range(n, k, 2):
        liste.append(i)
    end = time()
    return (end-start)
# print(time_append(1, 10))

def list_alea(n, k):
    liste = []
    for i in range(0, n):
        liste += [random.randint(0, k-1)]
    return liste
# print(list_alea(5, 6))

def time_min(n, k):
    i = 0
    start = time()
    while i < k:
        a = list_alea(n, k)
        b = min(a)
        i += 1
    end = time()
    return (end-start)
# print(time_min(1, 10))

def time_max(n, k):
    i = 0
    start = time()
    while i < k:
        a = list_alea(n, k)
        b = max(a)
        i += 1
    end = time()
    return (end-start)
# print(time_max(1, 10))

def liste_alea(n):
    liste = []
    for i in range(0, n):
        liste += [random.randint(0, n-1)]
    return liste
# print(liste_alea(6))

def dict_alea(n):
    dico = {}
    for i in range(0, n):
        dico[random.randint(0, n)] = {random.randint(0, n)}
    return dico
# print(dict_alea(6))