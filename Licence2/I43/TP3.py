from operator import ne
import random

def gen_cle(n):
    liste = []
    fin = 0
    for el in range(n):
        liste += [el+1]
    while n-fin > 0:
        alea = random.randint(0, n-1)
        liste[alea], liste[fin] = liste[fin], liste[alea]
        fin += 1
    return liste
#print(gen_cle(6))

def chiffre(clair, L):
    dico = {'é':'e', 'è':'e', 'ê':'e', 'ë':'e', 'à':'a', 'ù':'u', 'ô':'o', 'ö':'o', 'ü':'u', 'û':'u',
            'ç':'c', 'î':'i', 'ï':'i', 'ì':'i', ' ':''}
    el = 0
    mot = clair.lower()
    new_clair = ""
    crypt = ""
    while el < len(mot):
        if mot[el] in dico:
            new_clair += dico[mot[el]]
        else:
            new_clair += mot[el]
        el += 1
    liste = [0]*len(new_clair)
    i = 0
    while i < len(new_clair):
        liste[L[i]-1] = new_clair[i] 
        i += 1
    for el in liste:
        crypt += el
    return crypt
#print(chiffre('Le thé est prêt', [12,11,10,9,8,7,6,5,4,3,2,1]))

def dechiffre(cryptogramme, L):
    clair = ""
    i = 0
    while i < len(cryptogramme):
        clair += cryptogramme[L[i]-1]
        i += 1
    return clair
#print(dechiffre('bcyre', [2,3,1,5,4]))

def list_to_mat(L):
    long = len(L)
    matrice = [0]*long
    el = 0
    while el < long:
        matrice[el] = [0]*long
        el += 1
    i = 0
    while i < long:
        matrice[L[i]-1][i] = 1
        i += 1
    return matrice
#print(list_to_mat([2,3,1,5,4]))

def chiffre(clair, M):
    dico = {'a':'a', 'b':'b', 'c':'c', 'd':'d', 'e':'e', 'f':'f', 'g':'g', 'h':'h',
            'i':'i', 'j':'j', 'k':'k', 'l':'l', 'm':'m', 'n':'n', 'o':'o', 'p':'p',
            'q':'q', 'r':'r', 's':'s', 't':'t', 'u':'u', 'v':'v', 'w':'w', 'x':'x',
            'y':'y', 'z':'z', 'â':'a','ä':'a', 'à':'a', 'ç':'c', 'é':'e', 'è':'e', 
            'ê':'e', 'ë':'e', 'î':'i', 'ï':'i', 'ì':'i', 'ô':'o', 'ù':'u', 'û':'u'}
    el = 0
    mot = clair.lower()
    new_clair = []
    while el < len(mot):
        if mot[el] not in dico:
            new_clair += ''
        else:
            new_clair += [ord(dico[mot[el]])]
        el += 1
    j = 0
    liste = []
    while j < len(new_clair):
        i = 0
        somme = 0
        while i < len(new_clair):
            somme += new_clair[i]*M[j][i]
            i += 1
        liste += [somme]
        j += 1
    dechiffre = ""
    nbre = 0
    while nbre < len(liste):
        dechiffre += chr(liste[nbre])
        nbre += 1
    return dechiffre
mat = [[0,0,1,0,0],[1,0,0,0,0],[0,1,0,0,0],[0,0,0,0,1],[0,0,0,1,0]]
#print(chiffre('cy bér', mat))

def mat_to_list(L):
    liste = []
    i = 0
    while i < len(L):
        j = len(L)-1
        somme = 1
        while L[i][j] != 1 and j > 0:
            j -= 1
            somme = somme << 8
        liste += [somme]
        i += 1
    return liste
la = [[0,0,0,1],[1,0,0,0],[0,1,0,0],[0,0,1,0]]
#print(mat_to_list(la))

