def chiffrer(clair, clef):
    mot = ''
    for ch in clair:
        c = chr(((ord(ch) - ord('A')) + clef) % 26 + ord('A'))
        mot += c
    return mot
# print(chiffrer('COUCOU', 50))

def cribler(n):
    premier = ()
    for i in range(2, n+1):
        nbre_div = 0
        j = 1
        while j <= i:
            if i % j == 0:
                nbre_div += 1
            j += 1
        if nbre_div == 2:
            premier += (i,)
    return premier
# print(cribler(12))

def factoriser(n):
    liste = []
    while n != 1:
        for i in cribler(n):
            while n % i == 0:
                liste += [i]
                n = n // 2
    return liste
# print(factoriser(12))

def AfficheTable(T):
    for ligne in T:
        for x in ligne:
            print(str(x).rjust(3), end='')
        print()

def table(n, op):
    liste = ()
    for i in range(n):
        sous_liste = ()
        for j in range(n):
            sous_liste += ((eval(str(i) + op + str(j)) % n),)
        liste += (sous_liste,)
    return liste
# print(AfficheTable(table(10, '*')))

def mod9(n):
    while n > 9:
        c = 0
        for i in str(n):
            c += int(i)
        n = c
    if n == 9:
        return 0
    return n
# print(mod9(81))