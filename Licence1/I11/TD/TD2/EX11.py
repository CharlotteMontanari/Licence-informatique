# (1)
# ce programme retourne tous les diviseurs du chiffre saisie
n = int(input("Saisir un chiffre: "))
liste = []
i = 2
while i <= n:
    if n % i == 0:
        liste = liste + [i]
    i = i + 1
print(liste)

# (2)
# ce rogramme retourne la décomposition en facteurs premiers
n = int(input("Entrez une valeur: "))
p = 2
while p <= n:
    while n % p == 0:
        print(p)
        n = n // p
    p = p + 1