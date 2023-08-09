def fusionner(t1, t2):
    liste = []
    nbre_comp = 0
    i = 0
    j = 0
    while i < len(t1) and j < len(t2):
        if t1[i] <= t2[j]:
            liste += [t1[i]]
            i += 1
            nbre_comp += 1
        else:
            liste += [t2[j]]
            j += 1
            nbre_comp += 1
    while i < len(t1):
        liste += [t1[i]]
        i += 1
    while j < len(t2):
        liste += [t2[j]]
        j += 1
    return liste, nbre_comp
# print(fusionner([2, 4] ,[5, 3, 6, 8, 5, 4]))

def tri_partiel(T, a, b):
    compt = 0
    for i in range(a+1, b):
        j = i
        while j > a and T[j] < T[j-1]:
            T[j], T[j-1] = T[j-1], T[j]
            j -= 1
            compt += 1
        compt += 1
    return compt
# print(tri_partiel([2, 4, 5, 3, 6, 8, 5, 4, 2, 7],2 ,8))

def fusion_partiel(T, a, b):
    T1 = sorted(T[:a])
    T2 = sorted(T[a:b])
    T[:b], compt = fusionner(T1, T2)[0], fusionner(T1, T2)[1]
    return compt
# print(fusion_partiel([2, 4, 5, 3, 6, 8, 5, 4, 2, 7], 3, 6))

def tri_morceau(t, m):
    j = 0
    a = tri_partiel(t, j, m)
    i = m
    while i < len(t):
        j = i
        i += m
        if i > len(t):
            i = len(t)
        a += tri_partiel(t, j, i)
        a += fusion_partiel(t, j, i)
    return a
# print(tri_morceau([4, 5, 6, 7, 8, 23, 22, 11, 5, 0, 4, 9, 7], 4))

def diff(ch1, ch2):
    for i in range(min(len(ch1), len(ch2))):
        if ch1[i] != ch2[i]:
            return i
    return -1
# print(diff('chat', 'chatte'))

def tri_alien(l, a):
    dico = {}
    i = 1
    for ch in a:
        dico[ch] = i
        i += 1
    for el in range(len(l)):
        j = el
        booll = False
        while j > 0 and booll == False:
            booll = True
            var = diff(l[j], l[j-1])
            if var == -1:
                if len(l[j]) < len(l[j-1]):
                    l[j], l[j-1] = l[j-1], l[j]
                    booll = False
            else:
                if dico[l[j][var]] < dico[l[j-1][var]]:
                    l[j-1], l[j] = l[j], l[j-1]
                    booll = False
            j -= 1
    return l
# print(tri_alien(['#!', '@!@', '!!^^!', '@#!!^', '!'], '@!#^'))