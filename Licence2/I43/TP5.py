import random

def gentrianginf_Zm(n, m):
    matrice = [0]*n   
    x = 0
    while x < n:
        matrice[x] = [0]*n
        diag = 0
        for diag in range(x):
            matrice[x][diag] = random.randint(1, m-1)
        ok = False
        while not ok:
            mod = m
            alea = random.randint(1, mod-1)
            sauv = alea
            while mod != 0:
                alea, mod = mod, alea%mod
            ok = (alea == 1)
        matrice[x][x] = sauv
        x += 1    
    return matrice
#print(gentrianginf_Zm(4, 26))

def transpose(M):
    liste = []
    for i in range(len(M[0])):
        liste = liste + [[0]*len(M)]
        for j in range(len(M)):
            liste[i][j] = M[j][i]
    return liste
#print(transpose([[1, 2, 3], [4, 5, 6]]))

def genmatrixinv(n, m):
    mat1 = gentrianginf_Zm(n, m)
    mat2 = transpose(gentrianginf_Zm(n, m))
    liste = [0] * len(mat1)
    el = 0
    while el < len(liste):
        liste[el] = [0] * len(mat2[0])
        j = 0
        while j < len(liste[0]):
            i = 0
            somme = 0
            while i < len(mat1[0]):
                somme += mat1[el][i]*mat2[i][j]
                i += 1
            liste[el][j] = somme % m
            j += 1
        el += 1
    return liste
#print(genmatrixinv(3, 7))

def decoupe(f_in, n):
    source = open(f_in, "r")
    dico = {'?':26, ',':27, ' ':28, "'":29, '.':30, '0':'0'}
    alphabet = 97
    while alphabet < 123:
        dico[chr(alphabet)] = alphabet - 97
        alphabet += 1
    chaine = ''
    for mot in source:
        for lettre in mot:
            if lettre in dico and lettre != '\n':
                chaine += lettre
    liste = []
    letter = 0
    chaine += '0'*(n-(len(chaine)%n))
    while letter < len(chaine):
        sous_liste = [0]*n
        cpt = 0
        while cpt < n:
            sous_liste[cpt] = dico[chaine[letter]]
            cpt += 1
            letter += 1
        liste += [sous_liste]
    return liste       
#print(decoupe("textehill.txt", 2))