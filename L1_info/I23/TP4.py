def Lire():
    chaine = input("Permutation: ")
    return tuple([int(x)-1 for x in chaine.split()])

def Ecrire(s):
    for i in s:
        print(i + 1, end = ', ')
    print()

def EstPermutation(s):
    liste = [0] * len(s)
    for el in s:
        if el < 0 or el >= len(s):
            return False
        else:
            liste[el] = 1
    for i in liste:
        if i == 0:
            return False
    return True
# print(EstPermutation(Lire()))

def Inverser(s):
    table = [0] * len(s)
    for i in range(0, len(s)):
        table[s[i]] = i
    return tuple(table)
# print(Ecrire(Inverser(Lire())))

def Composer(s, t):
    c = ()
    for i in range(len(s)):
        c += (s[t[i]],)
    return Ecrire(c)
# print(Composer(Lire(), Lire()))

def Orbite(k, s):
    k = k - 1
    orbite = (k,)
    while s[k] not in orbite:
        k = s[k]
        orbite += (k,)
    return orbite
# print(Ecrire(Orbite(1, Lire())))

def Signature(s):
    liste = [True] * len(s)
    nbre_orbite = 0
    nbre_permutation = len(s)
    for el in s:
        if liste[el] == True:
            nbre_orbite += 1
            orbite = Orbite(el, s)
            for orb in orbite:
                liste[orb] = False
    return (-1)**(nbre_permutation - nbre_orbite)
# print(Signature(Lire()))

def suivant(b, i):
    while i < len(b):
        if b[i]:
            return i
        i += 1
    return i

def Cycles(s):
    tableau = [True] * len(s)
    orb = ()
    el = 0
    while el < len(s):
        new_orb = ()
        x = Orbite(el+1, s)
        for i in x:
            new_orb += (i+1,)
            tableau[i] = False
        orb += ((new_orb),)
        el = suivant(tableau, el)
    return orb
# print(Cycles(Lire()))

def Transpositions(s):
    transpo = ()
    for tup in Cycles(s):
        el = 0
        while el < len(tup) - 1:
            transpo += ((tup[el], tup[el+1]),)
            el += 1
    return transpo
# print(Transpositions(Lire()))