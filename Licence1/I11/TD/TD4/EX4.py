# (1)
def SomCarreList(l):
    i = 0
    som = 0
    while i < len(l):
        som = som + l[i] ** 2
        i = i + 1
    return som
l1 = [51,1,4,8]
print(SomCarreList(l1))

# (2)
def MoyList(l) :
    i = 0
    som = 0
    while i < len(l):
        som = som + l[i] ** 2
        i = i + 1
    return som / i
l1 = [51,1,4,8]
print(MoyList(l1))

# (3)
def nombre_car(chaine, car):
    """
    chaine = "coucou"
    return car = 6
    """
    somme = 0
    for ch in chaine:
        if ch == car:
            somme += 1
    return somme
print(nombre_car("coucou", "c"))

# (4)
def SwapList(l, i, j):
    """
    l = [1, 2, 3, "chat"]
    i = 1
    j = "chat"
    return l = ["chat", 2, 3, 1]
    """
    car1 = l[i]
    car2 = l[j]
    l[i] = car2
    l[j] = car1
    return(l)
print(SwapList([1, 2, 3, "chat"], 1, 0))

# (5)
def EstOrdonnee(l):
    """
    return True si la liste est croissante et False si elle ne l'est pas
    """
    i = 0
    while i < len(l) - 1:
        if l[i] > l[i+1]:
            return False
        i += 1
    return True
print(EstOrdonnee([2, 4, 7]))

# (6)
def MaxNeg(l):
    Max = l[0]
    for elt in l:
        if elt > Max and elt < 0 :
            Max = elt
        elif Max >= 0 and elt < 0:
            Max = elt
    if Max<0:
        return Max
    return 0
print(MaxNeg([0, 1, -7, 5, -1]))

# (7)
def Max2(l):
    if l[0] < l[1]:
        max1, max2 = l[0], l[1]
    else:
        max1, max2 = l[1], l[0]
    for elt in l:
        if elt > max2:
            max1 = max2
            max2 = elt
        elif elt > max1 and elt < max2:
            max1 = elt
    return max1, max2
