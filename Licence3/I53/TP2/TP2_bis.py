############
###GLOBAL###
from ast import operator
l = 'VRAI OU FAUX ET (FAUX ET NON VRAI)'
postfix = []
############

def analex_bool(expr):
    dico = {'VRAI':'VRAI', 'FAUX':'FAUX', 'NON':'NON', 'OU':'OU', 'ET':'ET',
            '(':'PO', ')':'PF', ' ':'None'}
    i = 0
    liste = []
    while i < len(expr):
        if expr[i] != ' ':
            if expr[i:i+4] == 'VRAI' or expr[i:i+4] == 'FAUX':
                liste += [(dico[expr[i:i+4]], expr[i:i+4])]
                i += 4
            elif expr[i:i+3] == 'NON':
                liste += [(dico[expr[i:i+3]], expr[i:i+3])]
                i += 3
            elif expr[i:i+2] == 'OU' or expr[i:i+2] == 'ET':
                liste += [(dico[expr[i:i+2]], expr[i:i+2])]
                i += 2
            else:
                liste += [(dico[expr[i]], expr[i])]
                i += 1
        else:
            i += 1
    return liste
chaine = "VRAI OU FAUX"
#print(analex_bool(chaine))

def expr():
    return terme() and reste()

def reste():
    global postfix
    global lul 
    global pul
    if reconnaitre("ET") or reconnaitre("OU") or reconnaitre("NON"):
        aux = lul[pul-1][1]
        if terme():
            postfix += [aux]
            return reste()
    else:
        return True

def facteur():
    global postfix
    global lul
    global pul
    if reconnaitre("VRAI") or reconnaitre("FAUX"):
        postfix += [lul[pul-1][1]]
        return True
    elif reconnaitre("PO"):
        return expr() and reconnaitre("PF")
    else:
        return False

def reste1():
    global postfix
    if reconnaitre("OU"):
        aux = lul[pul-1][1]
        if terme():
            postfix += [aux]
            return reste1()
    else:
        return True

def reste2():
    global postfix
    if reconnaitre("ET"):
        aux = lul[pul-1][1]
        if facteur():
            postfix += [aux]
            return reste2()
    else:
        return True

def terme():
    return facteur() and reste2()

def reconnaitre(lexeme):
    global lul
    global pul
    if pul < len(lul):
        if lexeme == lul[pul][0]:
            pul += 1
            return True
    return False

def parseur(s):
    global postfix
    global lul
    lul = analex_bool(s)
    print(lul)
    global pul
    pul = 0
    if expr() and pul == len(lul):
        return True, postfix
    print("Erreur", lul[pul-1])
    return False
print(parseur(l))