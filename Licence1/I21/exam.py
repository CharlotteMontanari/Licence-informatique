def equilibre(t):
    k = len(t)//2
    n = len(t)
    sortie = n
    while 0 < k and k < n and sortie > 0:
        i = 0
        som1 = 0
        while i < k:
            som1 += t[i]
            i += 1
        j = k+1
        som2 = 0
        while j < n:
            som2 += t[j]
            j += 1
        if som1 == som2:
            return k
        if som1 > som2:
            k -= 1
        else:
            k += 1
        sortie -= 1
    return -1
print(equilibre([-2, 5, 7, 6, -1, 2,-4]))