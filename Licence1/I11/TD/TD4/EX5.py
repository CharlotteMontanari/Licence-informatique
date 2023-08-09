# (1)
def EstPrem(n):
    if n == 1:
        return False
    i = 2
    while i < n:
        if n % i == 0:
            return False
        i += 1
    return True

# (2)
def ComptePrem(m):
    cpt = 0
    i = 0
    while i <= m:
        if EstPrem(i):
            cpt += 1
        i += 1
    return cpt

# (3)
def liste(deb, fin):
    i = deb
    l = []
    while i <= fin:
        if EstPrem(i):
            l += [i]
        i += 1
    return l