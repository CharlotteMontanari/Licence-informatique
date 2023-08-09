def TriSelection(L) -> None:
    i = 1
    n = len(L)
    while i < n:
        imin = IdxMin(L, i, n)
        Echanger(L, i, imin)
        i += 1
