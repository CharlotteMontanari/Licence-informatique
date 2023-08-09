def sym(nbre, mod):
    liste = [nbre]
    new = nbre
    while nbre != 1:
        nbre = (nbre*new) % mod
        liste += [nbre]
    return liste[-2]
#print(sym(3, 7))

def matAnneau(m, mod):
    pivot = 0
    y = 0
    det = 1
    while y < len(m) - 1:
        ligne = y + 1
        while ligne < len(m):
            x = 0
            intermediaire = m[ligne][y]
            while x < len(m):
                m[ligne][x] = (m[ligne][x] - sym(m[pivot][pivot], mod) * m[y][x] * intermediaire) % mod
                det = m[pivot][pivot] % mod
                x += 1
            ligne += 1
        pivot += 1
        y += 1
    for el in m:
        print(el)
    return det
matrice = [[3,2,5,3,4],[1,6,2,3,5],[4,3,4,3,5],[3,1,4,4,2],[2,3,4,2,2]]
print(matAnneau(matrice, 7))

def gauss(a, mod):
    i = 0
    while i < len(a) - 1:
        j = i + 1
        while j < len(a):
            for el in range(len(a[0])):
                a[j][el] = (a[i][i]*a[j][el] - a[j][i]*a[i][el]) % mod
            j += 1
        i += 1
    for i in a:
        print(i)
mat = [[3,1,2],[1,2,0],[2,3,1]]
print(gauss(mat))