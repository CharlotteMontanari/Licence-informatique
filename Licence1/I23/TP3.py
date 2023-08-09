def factorielle(n):
    fact = []
    j = 1
    for i in range(1, n+1):
        j = j * i
        fact += [j]
    return fact
# print(factorielle(10))

def TrianglePascal(n):
    triangle = [[0] * n for p in range(n+1)]
    i, n = 0, 0
    ligne = []
    while i < len(triangle):
        while n < i:
            if n == 0:
                triangle[i][n] = 1
            else:
                triangle[i][n] = triangle[i-1][n-1] + triangle[i-1][n]
            n += 1
        i += 1
        n = 0
    # for a in triangle:
    #     for b in a:
    #         if b != 0:
    #             ligne += [b]
        # print(ligne)
        # ligne = []
    return triangle
# for ligne in TrianglePascal(6):
#     for el in ligne:
#         if el > 0:
#             print(el, end =" ")
#     print()

def TrianglePascal_r(n):
    triangle = [0] * (n+1)
    i = 0
    while i < len(triangle):
        if i == 0 or i == n:
            triangle[i] = 1
        else:
            triangle[i] = TrianglePascal_r(n-1)[i] + TrianglePascal_r(n-1)[i-1]
        i += 1
    return triangle
# print(TrianglePascal_r(6))

def TrianglePascal_r2(n):
    triangle = [0] * (n+1)
    i = 0
    while i < n:
        if i == 0 or i == n:
            triangle[i] = 1
        else:
            triangle[i] = TrianglePascal_r(n-1)[i] + TrianglePascal_r(n-1)[i-1]
        i += 1
    return triangle
# print(TrianglePascal_r2(6))

def phoque(n):
    liste = []
    if n == 1:
        liste = ['.']
    elif n == 2:
        liste = ['..', '_']
    else:
        liste = ['.' + x for x in phoque(n-1)] + ['_' + x for x in phoque(n-2)]
    return liste
# print(phoque(6))

def phoqueit(n):
    l = []
    a = ['.']
    b = ['..','-']
    if n == 1:
        return a
    elif n == 2:
        return b
    else:
        for x in range(3,n+1):
            l = ['.' + x for x in b]+['-' + x for x in a]
            a = b
            b = l
    return l
# print(phoqueit(4))

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        fibo = [0, 1]
        for el in range(n):
            fibo += [fibo[-1] + fibo[-2]]
    return fibo
# print(fibonacci(4))

def genuplet(n, m, nuplet):
    for i in range(1, m+1):
        for j in range(1, m+1):
            for c in range(1, m+1):
                nuplet += (i, j, c),
    return nuplet
x = genuplet(2, 3, ())
# for tup in x:
#     print(tup)

def genuplet_r(n, m, uplet):
    if n == 0:
        return uplet
    else:
        for i in range(1, m+1):
            r = genuplet_r(n-1, m, uplet + (i,))
    return r
# print(genuplet_r(5, 5, ()))