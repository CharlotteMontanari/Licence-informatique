############
###GLOBAL###
from ast import operator
l = '9 - (5 + 2)'
postfix = []
############

def analex(s):
    dico = {'0':'Nbr', '1':'Nbr', '2':'Nbr', '3':'Nbr', '4':'Nbr',
            '5':'Nbr', '6':'Nbr', '7':'Nbr', '8':'Nbr', '9':'Nbr',
            '(':'PO', ')':'PF', '+':'Op', '-':'Op', '*':'Op', '/':'Op', ' ':'None'}
    i = 0
    liste = []
    while i < len(s):
        if s[i] != ' ':
            if dico[s[i]] == 'Nbr':
                aux = ''
                while i < len(s) and dico[s[i]] == "Nbr":
                    aux += s[i]
                    i += 1
                liste += [('Nbr', aux)]
            else:
                liste += [(dico[s[i]], s[i])]
                i += 1
        else:
            i += 1
    return liste
chaine = '5 - (9 + 2 * 3)'
chaine2 = '(52 + 499)'
#print(analex(chaine2))

def expr():
    return terme() and reste()

def reste():
    global postfix
    global lul 
    global pul
    if reconnaitre("Op"):
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
    if reconnaitre("Nbr"):
        postfix += [lul[pul-1][1]]
        return True
    elif reconnaitre("PO"):
        return expr() and reconnaitre("PF")
    else:
        return False

def reste1():
    global postfix
    if reconnaitre("+") or reconnaitre("-"):
        aux = lul[pul-1][1]
        if terme():
            postfix += [aux]
            return reste1()
    else:
        return True

def reste2():
    global postfix
    if reconnaitre("*") or reconnaitre("/"):
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
#print(reconnaitre("Nbr"))

def parseur(s):
    global postfix
    global lul
    lul = analex(s)
    #print(lul)
    global pul
    pul = 0
    if expr() and pul == len(lul):
        return True, postfix
    #print("Erreur", lul[pul-1])
    return False
#print(parseur(l))

def fichier(exp):
    p = parseur(exp)
    nbre = 1
    file = open("a.out", 'w')
    for i in p[1]:
        if i.isdigit():
            file.write(f"t{nbre} = {i}\n")
            nbre += 1
        elif i != ' ':
            file.write(f"t{nbre - 2} = t{nbre - 2} {i} t{nbre - 1}\n")
            nbre -= 1
    file.close()
#print(fichier(l))

