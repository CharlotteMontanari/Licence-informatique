import random

def euclide_e(a, n):
    mod = n
    u = 1
    v = 0
    u1 = 0
    v1 = 1
    while n != 0:
        u, v, u1, v1 = u1, v1, u - a//n * u1, v - a//n * v1
        #print(u1, v1)
        a, n = n, a%n
        #print("a:",a)
        #print("n:",n)
    return [a, u%mod, v1]

def gen_cle(n):
    alea = random.randint(2, n)
    while euclide_e(alea, n)[0] != 1:
        alea = random.randint(2, n)
    b = random.randint(2, n)
    c = euclide_e(n, alea)[2] % n
    return [alea, b, c]
#print(gen_cle(26))

def chiffre(clair, k):
    dico = {'a':'a', 'b':'b', 'c':'c', 'd':'d', 'e':'e', 'f':'f', 'g':'g', 'h':'h',
            'i':'i', 'j':'j', 'k':'k', 'l':'l', 'm':'m', 'n':'n', 'o':'o', 'p':'p',
            'q':'q', 'r':'r', 's':'s', 't':'t', 'u':'u', 'v':'v', 'w':'w', 'x':'x',
            'y':'y', 'z':'z', 'â':'a','ä':'a', 'à':'a', 'ç':'c', 'é':'e', 'è':'e', 
            'ê':'e', 'ë':'e', 'î':'i', 'ï':'i', 'ì':'i', 'ô':'o', 'ù':'u', 'û':'u'}
    i = 0 #97
    mot = ""
    new_clair = clair.lower()
    while i < len(new_clair):
        if new_clair[i] == ' ':
            mot += ' '
        else:
            si = dico[new_clair[i]] 
            s = ord(si) - 97
            lettre = (k[0]*s + k[1]) % 26
            mot += chr(lettre+97)
        i += 1
    return mot
#print(chiffre("bonjour le", [19,1,11]))

def dechiffre(cryptogramme, k):
    mot = ""
    for strt in cryptogramme:
        if strt == ' ':
            mot += ' '
        else:
            s = ord(strt) - 97
            lettre = ((s - k[1]) * k[2]) % 26
            mot += chr(lettre+97)
    return mot
#print(dechiffre("uhoqhrm", [19,1,11]))

def analyse_freq(cryptogramme):
    dico = {'a':'a', 'b':'b', 'c':'c', 'd':'d', 'e':'e', 'f':'f', 'g':'g', 'h':'h',
            'i':'i', 'j':'j', 'k':'k', 'l':'l', 'm':'m', 'n':'n', 'o':'o', 'p':'p',
            'q':'q', 'r':'r', 's':'s', 't':'t', 'u':'u', 'v':'v', 'w':'w', 'x':'x',
            'y':'y', 'z':'z', 'â':'a','ä':'a', 'à':'a', 'ç':'c', 'é':'e', 'è':'e', 
            'ê':'e', 'ë':'e', 'î':'i', 'ï':'i', 'ì':'i', 'ô':'o', 'ù':'u', 'û':'u'}
    lettre = {}
    liste = []
    imax = 0
    mot = cryptogramme.lower()
    new_cryt = ""
    for strt in mot:
        if strt not in dico:
            new_cryt += ''
        else:
            new_cryt += dico[strt]
            if strt not in lettre:
                lettre[strt] = 1
            else:
                lettre[strt] += 1
                if lettre[strt] > imax:
                    imax = lettre[strt]
                    lettre_max = strt
    liste += [lettre_max, imax, str(round((imax/len(new_cryt))*100, 2)) + '%']
    imax2 = 0
    dico2 = {}
    strt2 = 0
    while strt2+1 < len(new_cryt):
        if new_cryt[strt2] == lettre_max:
            if new_cryt[strt2+1] not in dico2:
                dico2[new_cryt[strt2+1]] = 1
            else:
                dico2[new_cryt[strt2+1]] += 1
                if dico2[new_cryt[strt2+1]] > imax2:
                    imax2 = dico2[new_cryt[strt2+1]]
                    lettre2_max = new_cryt[strt2+1]
        strt2 += 1
    liste += [lettre2_max, imax2, str(round((imax2/imax)*100, 2)) + '%']
    return liste
#print(analyse_freq("Aa bb a aAb eabab"))

def resolution_affine(bigramme):
    dico = {' ':26, "'":27, '.':28}
    i = 0
    while i < 26:
        dico[chr(i+97)] = i
        i += 1
    x = dico[bigramme[0]] #t
    y = dico[bigramme[1]] #m
    e = (dico[bigramme[1]] - dico[bigramme[0]]) % 29
    mu = (e * euclide_e(29, 14)[2]) % 29
    lamb = (dico[bigramme[0]] - 4 * mu) % 29
    return [mu, lamb]
#print(resolution_affine('tm'))