def Inserer(L, i) -> None:
    while i > 1 and L[i] < L[i - 1]:
        Echanger(L, i, i-1)
        i -= 1