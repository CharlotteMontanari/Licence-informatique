def multbyalpha(b, f):
    new_f = len(bin(f)) - 3
    y = b << 1
    if (y & (1 << new_f)) != 0:
        y = y ^ f
    return y
#print(multbyalpha(8,19))

def multiplication(b, c, f):
    s = 0
    aux = b
    while c != 0:
        a = c & 1
        if a != 0:
            s = s ^ aux
        aux = multbyalpha(aux, f)
        c = c >> 1
    return s
#print(multiplication(5, 6, 13)) 

def table_log(P):
    p = len(bin(P)) - 3
    liste = [-1] * (1 << p)
    liste[1] = 0
    cpt = 1
    j = 1
    while cpt < (1 << p) - 1:
        j = multbyalpha(j, P)
        liste[j] = cpt
        cpt += 1
    return liste
#print(table_log(13))

def table_alpha(P):
    p = len(bin(P)) - 3
    liste = [1] * ((1 << p)-1)
    cpt = 1
    j = 1
    while cpt < (1 << p) - 1:
        j = multbyalpha(j, P)
        liste[cpt] = j
        cpt += 1
    return liste
#print(table_alpha(13))

def multiplie(x, y, P):
    if x == 0 or y == 0:
        return 0
    a = table_log[x]
    b = table_log[y]
    c = (1 << len(bin(P))-3) - 1
    return table_alpha[(a + b) % c]

def is_irreductible(P, p):
    flag = True
    i = 0
    while i < p and flag:
        v = P[0]
        for el in range(1, len(P)):
            v = (v * i + P[el]) % p
        flag = (v != 0)
        i += 1
    return flag
#print(is_irreductible([1, 24, 2], 29))

def decompose(x):
    liste = []
    i = 2
    while x > 1:
        if x % i == 0:
            liste += [i]
            x = x // i
        else:
            i += 1
    return liste
#print(decompose(12))

def is_primitif(P):
    degres = len(P) - 1
    nbre_elem = (1 << degres) - 1
    div = decompose(nbre_elem)
    i = 0
    while i < len(div):
        exp = nbre_elem / div[i]
        res = 2
        j = 1
        while j < exp:
            res = multiplie(res, 2, P)
            j += 1
        if res == 1:
            return False
        i += 1
    return True
#print(is_primitif(12))
