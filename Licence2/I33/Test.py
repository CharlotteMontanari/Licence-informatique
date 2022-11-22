def multbyalpha(b, f):
    new_f = len(bin(f)) - 3
    y = b << 1
    if (y & (1 << new_f)) != 0:
        y = y ^ f
    return y

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

def sym_mult(b, c, f):
    m = multiplication(b, c, f) == 1
    return m
#print(sym_mult(3, 3, 11))

def sym_mul(b, c, f):
    l = table_log(b)
    L = bin(l)
    a = table_alpha(c)
    return (a in l)
#rint(sym_mul(3, 4, 11))

def sym(x, P):
    p = len(bin(P)) - 3
    x1 = len(bin(x)) - 3
    return (p << 1) ^ x1
#print(sym(4, 13))