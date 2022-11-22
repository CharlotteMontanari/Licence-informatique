# (1)
def som_div_propres(n):
    somme = 0
    i = 1
    while i < n:
        if n % i == 0:
            somme = somme + i
        i = i + 1
    return somme
    
n = int(input("Saisir un nbre: "))
print(som_div_propres)


# (2)
def est_parfait(n):
    i = 1
    somme = 0
    while i < n:
        if n % i == 0:
            somme = somme + i
        i = i + 1
    if somme == n:
        return somme == n
    else:
        return somme == n

var = int(input("Saisir un nbre: "))
print(est_parfait(var))

# (3)
def affiche_parfait(k):
    for n in range(1, 2**k + 1):
        if (est_parfait(n)):
            print(n, end= ',')
    print()

kk = int(input("Saisir un nbre: "))
print(affiche_parfait(kk))