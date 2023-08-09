def bbr(t):
    liste = []
    b = 0
    r = len(t) - 1
    w = 0
    while w <= r:
        if t[w] == 'red':
            t[w], t[r] = t[r], t[w]
            liste += [(w, r)]
            r -= 1
        elif t[w] == 'blue':
            t[w], t[b] = t[b], t[w]
            liste += [(w, b)]
            b += 1
            w += 1
        elif t[w] == 'white':
            w += 1
    # return liste
# print(bbr(['blue', 'blue', 'red', 'white', 'blue', 'red', 'red', 'white']))