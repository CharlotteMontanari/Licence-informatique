def TriBulle(L) -> None:
    ex = True
    d = len(L)
    while ex and d > 1:
        ex = Propager(L, 1, d)
        d -= 1