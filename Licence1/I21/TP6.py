from random import randint
import random
from math import sin

def gen_tableau(n):
    tableau = []
    i = 0
    while i < n:
        alea = random.randint(1, 2*n)
        tableau += [alea]
        i += 1
    tableau.sort()
    return tableau
# print(gen_tableau(10))

def recherche_binaire(t, x):
    gauche = 0
    droite = len(t)
    comparaison = 0
    while gauche <= droite:
        milieu = (gauche + droite) // 2
        if t[milieu] == x:
            comparaison += 1
            return comparaison
        elif t[milieu] > x:
            droite = milieu - 1
            comparaison += 2
        elif t[milieu] < x:
            gauche = milieu + 1
            comparaison += 3
    return -1
# print(recherche_binaire([4, 5, 6, 7, 8, 22, 23, 24, 25, 30, 40, 90], 8))

def recherche_ternaire(t, x):
    gauche = 0
    droite = len(t)
    comparaison = 0
    while gauche <= droite:
        gauche1 = (2 * gauche + droite) // 3
        droite1 = (2 * droite + gauche) // 3
        if t[gauche1] == x:
            comparaison += 1
            return comparaison
        if t[droite1] == x:
            comparaison += 1
            return comparaison
        elif t[gauche1] > x:
            droite = gauche1 - 1
            comparaison += 2
        elif t[droite1] < x:
            gauche = droite1 + 1
            comparaison += 3
        else:
            droite = droite1 - 1
            gauche = gauche1 + 1
            comparaison += 4
    return -1
# print(recherche_ternaire([4, 5, 6, 7, 8, 22, 23, 24, 25, 30, 40, 90], 23))

def complexite_binaire(t):
    comparaison = 0
    for el in t:
        comparaison += recherche_binaire(t, el)
    return comparaison // len(t)
# print(complexite_binaire([4, 5, 6, 7, 8, 22, 23, 24, 25, 30, 40, 90]))

def complexite_ternaire(t):
    comparaison = 0
    for el in t:
        comparaison += recherche_ternaire(t, el)
    return comparaison // len(t)
# print(complexite_ternaire([4, 5, 6, 7, 8, 22, 23, 24, 25, 30, 40, 90]))

def recherche_zero(a, b, prec):
    g, d = min(a,b), max(a,b)
    zero = []
    while d-g > prec:
        m = (g+d)//2
        if (b-a) < prec:
            zero += [m]
        if m == 0:
            return 0
        elif (a*b) < 0:
            d = m
            zero += [d]
        else:
            g = m
            zero += [g]
    return (g+d)/2
# print(recherche_zero(-2.3, 1.5, 0.01))

def zero_dic(a, b, prec):
    zero = []
    while b - a > prec:
        zero += [[a,b]]
        m = (a + b) / 2
        if sin(m) == 0:
            return m
        elif sin(m) > 0:
            b = m
        else:
            a = m
    return zero + [[a,b]]  
# print(recherche_zero(-2.3, 1.5, 0.01))