def TriBulles(L) -> None:
    d = len(L)
    while d > 1:
        Propager(L, 1, d)
        d -= 1