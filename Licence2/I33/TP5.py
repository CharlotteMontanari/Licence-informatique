def comb_lineaire(c, V):
    liste = []
    i = 0
    while i < len(V[0]):
        j = 0
        somme = 0
        while j < len(c):
            somme += c[j] * V[j][i]
            j += 1
        liste += [somme]
        i += 1
    return liste
#print(comb_lineaire([2, 3], [[1, 1, 2], [2, 3, 0]]))

def combi_lineaire(c, V):
    i = len(V)-1
    res = 0
    while i >= 0:
        res = res ^ (V[i] * (c&1))
        i -= 1
        c = c >> 1
    return res

def combinaison_lineaire(c, V, p):
    i = 0
    liste = []
    while i < len(V[0]):
        j = 0
        som = 0
        while j < len(c):
            V[j][i] = (V[j][i] * c[j]) % p
            som =(som + V[j][i]) % p
            j += 1
        liste += [som]
        i += 1
    return liste

def liste_vecteurs(n):
    liste = []
    i = 0
    while i < (1 << n):
        sous_l = []
        el = i
        nbre = 0
        while nbre != n:
            sous_l = [el&1] + sous_l
            el = el >> 1
            nbre += 1
        i += 1
        liste += [sous_l]
    return liste
#print(liste_vecteurs(3))

def liste_vecteurs(p, n):
    liste = []
    for el in range(0, p**n):
        sous_l = []
        i = el
        nbre = 0
        while nbre != n:
            sous_l = [i%p] + sous_l
            i = i // p
            nbre += 1
        liste += [sous_l]
    return liste
#print(liste_vecteurs(3, 3))

def to_int(L):
    i = 0
    ans = 0
    while i < len(L):
        if L[i] == 1:
            ans += 2
        i += 1
    return ans
