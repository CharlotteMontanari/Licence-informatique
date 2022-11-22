from random import randrange

def rand_table(n,a,b):
    liste = []
    for i in range(n):
        c = randrange(a,b)
        liste += [c]
    return liste
# print(rand_table(9,0,5))

def echanger(t,i,j):
    aux = t[i]
    t[i] = t[j]
    t[j] = aux
    return t
tf = [4,6,8,1,7,5,2,3]
# print(echanger(tf,0,1))

def tri_selection(t):
    i = 0
    somme = 0
    while i <= len(t) - 1:
        imin = i
        j = i + 1
        while j < len(t):
            if t[j] < t[imin]:
                imin = j
            j += 1
        echanger(t,i,imin)
        i += 1
        somme += 1
    return somme
# print(tri_selection([4,6,8,1,7,5,2,3]))

def tri_bulle(t):
    d = len(t) - 1
    echange = True
    somme = 0
    while echange:
        i = 0
        echange = False
        while i < d:
            if t[i] > t[i + 1]:
                echanger(t, i, i+1)
                somme += 1
                echange = True
            i += 1
        d -= 1
    return somme
# print(tri_bulle([4,6,8,1,7,5,2,3]))

def tri_insertion(t):
    somme = 0
    for i in range(1, len(t)):
        j = i
        while j > 0 and t[j - 1] > t[j]:
            echanger(t,j,j-1)
            j -= 1
            somme += 1
    return somme
# print(tri_insertion([4,6,8,1,7,5,2,3]))

def compare_tri(t):
    liste = ()
    s = tri_selection([4,6,8,1,7,5,2,3])
    b = tri_bulle([4,6,8,1,7,5,2,3])
    i = tri_insertion([4,6,8,1,7,5,2,3])
    liste += (s, b, i)
    return liste
# print(compare_tri([4,6,8,1,7,5,2,3]))

def retourner(t, i):
    t[:i] = t[:i] 
    t[i:] = t[i:][::-1]
    return t
# print(retourner([4,6,8,1,7,5,2,3], 2))

def tri_pancake(t):
    liste = []
    for i in range(len(t) - 1):
        imax = i
        for j in range(i+1, len(t)):
            if t[j] > t[imax]:
                imax = j
        if imax != i:
            if imax != len(t) - 1:
                retourner(t, imax)
                liste += [imax]
            retourner(t,i)
            liste += [i]
    return liste
# print(tri_pancake([4,6,8,1,7,5,2,3]))