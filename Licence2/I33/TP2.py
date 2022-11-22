import random

def pgcd(a, b):
    while b != 0:
        a, b = b, a%b
    return a

def euclide_e(a, n):
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
    return u
liste = [81,45,78,15,18]
for i in liste:
    print(euclide_e(i, 89))
#print(euclide_e(6007, 2333))

def inverse(a, p):
    nbre = p
    u = 1
    v = 0
    u1 = 0
    v1 = 1
    while p != 0:
        u, v, u1, v1 = u1, v1, u - a//p * u1, v - a//p * v1
        a, p = p, a%p
    return u % nbre

def euler_phi(n):
    phi = 0
    i = 0
    while i < n:
        p = n
        a = i
        while p != 0:
            a, p = p, a%p
        if a == 1:
            phi += 1
        i += 1
    return phi

def generateurs(n):
    gene = []
    i = 0
    while i < n:
        if pgcd(n, i) == 1:
            gene += [i]
        i += 1
    return gene

def generateur(p):
    alea = random.randrange(2, p-2)
    q = (p-1)//2
    while pow(alea, q, p) == 1:
        alea = random.randrange(2, p-2)
    return alea

def decompose(n):
    i = 2
    compo = []
    while n != 1:
        if n % i == 0:
            n = n // i
            if i not in compo:
                compo += [i]
        elif i == 2:
            i += 1
        else:
            i += 1
    return compo

def generateurs(p):
    l = decompose(p-1)
    i = 2
    gene = []
    while i < p-1:
        ind = 0
        while ind < len(l) and pow(i, (p-1)//l[ind], p) != 1:
            ind += 1
        if ind == len(l):
            gene += [i]
        i += 1
    return gene

def ord1(a, n):
    x = n
    while n != 0:
        a, n = n , a%n
    return x // a

def ord(a, p):
    i = 1
    j = p
    while i <= (p-1)**0.5:
        if pow(a, i, p) == 1:
            return i
        elif pow(a, (p-1)//i, p) == 1 and (p-1)//i < j:
            j = (p-1)//i
        i += 1
    return j

