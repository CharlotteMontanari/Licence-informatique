# (1)
Nbre = int(input("Saisir une valeur: "))
Liste = []
while Nbre != 0:
    # Liste.append(Nbre)
    Liste = Liste + [Nbre]
    Nbre = int(input("Saisir une valeur: "))
print(Liste)

# (2)
Nbre = int(input("Saisir une valeur: "))
Liste = []
somme = 0
while Nbre != 0:
    # Liste.append(Nbre)
    Liste = Liste + [Nbre]
    Nbre = int(input("Saisir une valeur: "))
for i in Liste:
    somme = somme + i
print(Liste)
print("Il y a", len(Liste), "nbre(s) dans la liste")
print("La somme de la liste est égale à", somme)


# (1)
Liste = [1,2,5,9,7,3]
max = 0
index = 0
# for i, e in enumerate(Liste):
for i in range(len(Liste)):
#     print(i, e)
    e = Liste[i]
    if e > max:
        print("nouveau max: ", e, i)
        max = e
        index = i
print(max, index)

# (2)
Liste = [1,2,5,9,7,3,8]
max1 = max2 = 0
for i in range(len(Liste)):
    print(max1, max2)
    e = Liste[i]
    if e > max1:
        print("nouveau max: ", e)
        max2 = max1
        max1 = e
    elif e > max2:
        max2 = e
print(max1, max2)

# 3
# Solution avec liste 
Liste = [1,2,5,9,7,3,8]
# max = [valeur de l'element, index de l'element]
max1 = max2 = [0, 0]
for i in range(len(Liste)):
#     print(max1, max2)
    e = Liste[i]
    if e > max1[0]:
        print("nouveau max: ", e)
        max2 = max1  # on ecrase la valeur et l'index
        max1 = [e, i]
    elif e > max2[0]:
        max2 = [e, i]
print(max1, max2)

# Solution avec tuple
Liste = [1,2,5,9,7,3,8]
max1 = max2 = (0, 0)
for i in range(len(Liste)):
#     print(max1, max2)
    e = Liste[i]
    if e > max1[0]:  # on compare l'element de la liste avec le dernier max sauvegardé
        print("nouveau max: ", e)
        max2 = max1  # on ecrase max2 avec max1
        max1 = (e, i)
    elif e > max2[0]:
        max2 = (e, i)
print(max1, max2)


# (1)
Ch = input("Saisir une chaine de caractere: ")
Ch4 = []
while Ch != "" and " " not in Ch:
    Ch4 = Ch4 + [Ch]
    Ch = input("Saisir une chaine de caractere: ")
print(Ch4)