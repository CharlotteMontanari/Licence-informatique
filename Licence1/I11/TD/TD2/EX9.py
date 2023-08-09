# (1)
# ce programme retourne le chiffre a l'envers
n = 30071966
while n > 0:
    chiffre = n % 10
    print(chiffre)
    n = n // 10

# (2)
n = 30071966
somme = 0
while n > 0:
    chiffre = n % 10
    n = n // 10
    somme = somme + chiffre
print(somme)
