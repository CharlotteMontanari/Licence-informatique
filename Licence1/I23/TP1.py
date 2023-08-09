def ListerVariables(expression):
    liste = []
    for ch in expression:
        if ch.isalpha():
            liste += [ch]
    return sorted(set(liste))
# print(ListerVariables('!(p + q) * (!p + r) + (p * q)'))

def DicoVariables(liste):
    dico = {}
    j = 0
    for i in liste:
        dico[i] = j
        j += 1
    return dico
# print(DicoVariables(['p', 'q', 'r']))

def Int2Bin(entier, n):
    integer = bin(entier)
    newinteger = integer[2:]
    diff = n - len(str(newinteger))
    nbre = diff * '0' + newinteger
    return nbre
# print(Int2Bin(5, 5))

def Bin2Bool(bits):
    liste = ()
    for ch in bits:
        if ch == '0':
            liste += (False,)
        else:
            liste += (True,)
    return liste
# print(Bin2Bool("00101"))

def Math2Python(expression, vecteur, dicovar):
    st = ''
    for strt in expression:
        if strt == "!":
            st += " not "
        elif strt == "+":
            st += " or "
        elif strt == "*":
            st += " and "
        if strt.isalpha():
            for i in dicovar.keys():
                if strt == i:
                    st += str(vecteur[(dicovar[i])])
        elif strt == "(": 
            st += "("
        elif strt == ")": 
            st += ")"
    return st
exp = "p * q"
vec = (False, False, True)
dic = DicoVariables(ListerVariables(exp))
# print(Math2Python(exp, vec, dic))

def TabledeVerite(expression,dicovar):
    L = []
    i = 0
    liste = []
    while i < 2**(len(dicovar)):
        ligne = Int2Bin(i,len(dicovar))
        lign = Bin2Bool(ligne)
        liste += [lign]
        i += 1
    for e in liste:
        if eval(Math2Python(exp, e, dic)):
            L += [1]
        else:
            L += [0]
    return L
exp = "p * q"
dic = DicoVariables(ListerVariables(exp))
# print(TabledeVerite(exp,dic))

def Table(ex, dic):
    m = 0
    o = 0
    s = TabledeVerite(ex, dic)
    for i in dic:
        print(i, '|', end='')
    print('s', '|')
    e = 0
    while e < 2**(len(dic)):
        ligne = Int2Bin(e, len(dic))
        for l in ligne:
            print(l, '|', end="")
            o += 1
            if o == len(dic):    
                print(s[m], '|')
                m += 1
                o = 0
        e += 1
exp = "p * q"
dic = DicoVariables(ListerVariables(exp))
# print(Table(exp,dic))

def FND(TDV, listevar):
    n = len(listevar)
    debut = True
    print("FND = ", end='')
    entier = 0
    while entier < len(TDV):
        if (TDV[entier] == 1):
            bits = Int2Bin(entier,n)
            if debut:
                debut = False
            else:
                print(" + ",end='')
            i = 0
            while i < n:
                if bits[i] == "1":
                    print(listevar[i],end='')
                else:
                    print(listevar[i] + "\u0304",end='')
                i = i + 1
        entier = entier + 1
    print()

def FNC(TDV, listevar):
    n = len(listevar)
    print("FNC = ", end='')
    entier = 0
    while entier < len(TDV):
        if (TDV[entier] == 0):
            bits = Int2Bin(entier,n)
            debut = True
            i = 0
            while i < n:
                if debut:
                    print('(', end='')
                    debut = False
                else:
                    print("+", end='')
                if bits[i] == "0":
                    print(listevar[i],end='')
                else:
                    print(listevar[i] + "\u0304",end='')
                i = i + 1
            print(')',end='')
        entier = entier + 1
    print()
